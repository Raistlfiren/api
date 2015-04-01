from flask import Flask, render_template
from . import stats
from . import maps

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(stats.mod)
app.register_blueprint(maps.mod)