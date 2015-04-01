from flask import Blueprint, render_template
import ujson

mod = Blueprint('stats', __name__)

@mod.route('/stats')
def user_rating_graph():
    rating = ujson.dumps({'mean': 0, 'sigma': 1})
    return render_template('stats/graph.html', rating=rating)