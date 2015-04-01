from flask import Blueprint, render_template, request, current_app 
from werkzeug import secure_filename
import ujson, os.path

mod = Blueprint('map', __name__)

@mod.route('/map/upload', methods=['POST'])
def uppload_map():
    file = request.files['zipmap']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return 'uploaded'
    return 'error'

def allowed_file(filename):
    return os.path.splitext(filename)[1] == '.zip'