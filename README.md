# FaForever API
This is an API for the FaForever ressources.

* Authentification over OAuth 2.0
* JSON oriented

# Installation - Automatic

To setup the development environment automatic we use Vagrant and a VM.

1. Install Vagrant: http://www.vagrantup.com/downloads
2. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
3. Clone this repository
4. Open the command console and navigate to folder of this repository (check with `ls` or `dir` that `Vagrantfile` is present)
5. Run `vagrant up`

To login the vm use `vagrant ssh`.
To shutdown the vm use `vagrant halt`.
You find the data under `/vagrant` in the VM.
This folder is autmatically synced from host to guest and back.

## Installation - Manual

Install Python 3.4 or later. Pre-requisites are listed in `requirements.txt`,
install using `pip install -r requirements.txt`.

Take a look at the `Vagrantfile` if something is unclear.

## Database 

A mysql database is automatically installed over Vagrant in a docker container
and connected to port 5001 to your host system.
You must only run the initial database script `db-structure.sql`.

## Development

To start the development server in the vagrant enviorment execute

   python3 /vagrant/run.py

You can access the api over

   http://127.0.0.1:5000