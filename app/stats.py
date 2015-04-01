from flask import Blueprint
import ujson

mod = Blueprint('stats', __name__)

@mod.route('/stats')
def user_rating_graph():
    data = {'probability': 80, 'rating': 1200}
    return ujson.dumps(data)