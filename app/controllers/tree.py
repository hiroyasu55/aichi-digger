from flask import Blueprint, render_template

app_tree = Blueprint('tree', __name__, url_prefix='/tree')


@app_tree.route('')
def index():
    param = {
        'title': 'AICHI-DIGGER | 感染者ツリー',
    }
    return render_template('tree/index.html', **param)
