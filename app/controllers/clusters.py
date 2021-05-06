from flask import Blueprint, render_template

app = Blueprint('clusters', __name__, url_prefix='/clusters')


@app.route('')
def index():
    param = {
        'title': 'AICHI-DIGGER | クラスター情報',
    }
    return render_template('clusters/index.html', **param)
