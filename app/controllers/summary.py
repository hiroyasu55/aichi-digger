from flask import Blueprint, render_template
import app.lib.log as log

app = Blueprint('summary', __name__, url_prefix='/summary')
logger = log.getLogger(__name__)


@app.route('/')
def index():
    param = {
        'title': 'AICHI-DIGGER | 集計'
    }
    return render_template('summary/index.html', **param)


@app.route('/dailychart')
def dailychart():
    param = {
        'title': 'AICHI-DIGGER | 日別グラフ'
    }
    return render_template('summary/dailychart.html', **param)


@app.route('/varialchart')
def ratechart():
    param = {
        'title': 'AICHI-DIGGER | 各種グラフ'
    }
    return render_template('summary/varialchart.html', **param)
