"""
Holds routes for deployment based off of github events
"""
import json
import re

from flask import request, redirect, render_template
from requests.auth import HTTPBasicAuth

from api import *
from api.oauth import *

import hmac
import subprocess
import requests
import uritemplate
import os

GITHUB_DEPLOYMENTS_URI = "https://api.github.com/repos/{owner}/{repo}/deployments"

def validate_github_request(body, signature):
    digest = hmac.new(app.config['GITHUB_SECRET'],
                   body, 'sha1').hexdigest()
    return hmac.compare_digest(digest, signature)

@app.route('/github', methods=['POST'])
def github_hook():
    body = request.get_json()
    if not validate_github_request(request.data,
                                   request.headers['X-Hub-Signature'].split("sha1=")[1]):
        return "Invalid request", 400
    event = request.headers['X-Github-Event']
    if event == 'push':
        if body['repository']['name'] == 'api':
            head_commit = body['head_commit']
            match = re.search('Deploy: ([\w\W]+)', head_commit['message'])
            if match:
                repo_url = uritemplate.expand(GITHUB_DEPLOYMENTS_URI, owner='FAForever', repo=body['repository']['name'])
                deployment_response = requests.post(repo_url,
                                                    data=json.dumps({
                                                        "ref": body['ref'],
                                                        "environment": match.group(1),
                                                        "description": head_commit['message']
                                                    }),
                                                    auth=HTTPBasicAuth(app.config['GITHUB_USER'],
                                                                       app.config['GITHUB_TOKEN']))
                if not deployment_response.status_code == 201:
                    raise Exception(deployment_response.content)
        return "OK", 200
    elif event == 'deployment':
        deployment = body['deployment']
        repo = body['repository']
        repo_url = uritemplate.expand(GITHUB_DEPLOYMENTS_URI, owner='FAForever', repo=repo['name'])
        if deployment['environment'] == app.config['ENVIRONMENT']:
            status, description = deploy(body['repository']['name'], body['repository']['clone_url'], deployment['ref'], deployment['sha'])
            status_response = requests.post(repo_url+'/{}/statuses'.format(deployment['id']),
                                            data=json.dumps({
                                                "state": status,
                                                "description": description
                                            }),
                                            auth=HTTPBasicAuth(app.config['GITHUB_USER'],
                                                               app.config['GITHUB_TOKEN']))
            return "Success", status_response.status_code
        else:
            return "Unknown error", 400
    else:
        return "Noop", 200

def deploy(repository, clone_url, ref, sha):
    """
    Perform deployment on this machine
    :param repository:
    :param ref:
    :param sha:
    :return:
    """
    if repository not in ['api']:
        return "error", "invalid repository"
    repo_path = app.config.get('{}_PATH'.format(repository.upper()))
    git_path = app.config.get('GIT_PATH', '/usr/bin/git')
    if not subprocess.call('{} -C {} fetch {}'.format(
                git_path,
                repo_path,
                clone_url)) == 0:
        return "error", "git fetch returned nonzero access code"
    if not subprocess.call('{} -C {} checkout -f {}'.format(
        git_path,
        repo_path,
        sha
    )):
        return "error", "git checkout returned nonzero access code"
    restart_file = repo_path+'/tmp/restart.txt'
    with open(restart_file):
        os.utime(restart_file, None)
    return "success", "Deployed successfully"
