from flask import Blueprint, render_template, request
import app.models.culc as culc
from datetime import datetime

app_persons = Blueprint('persons', __name__, url_prefix='/persons')


def date_to_japanese(dt):
    if type(dt) == str:
        dt = datetime.strptime(dt, r'%Y-%m-%d')
    return dt.strftime(r'%Y年%m月%d日')


@app_persons.route('')
def index():
    page = request.args.get('page', None)

    param = {
        'title': 'AICHI-DIGGER | 感染者リスト',
        'page': page
    }
    return render_template('persons/index.html', **param)


@app_persons.route('/<int:no>')
def detail(no):
    param = {
        'title': 'AICHI-DIGGER | 感染者詳細[No.{}]'.format(no),
        'no': no
    }
    return render_template('persons/detail.html', **param)


@app_persons.route('/summary')
def summary():
    persons = []

    release_date_count = sorted(
        culc.count_by_column(persons, 'release_date'), key=lambda c: c['release_date'])
    for c in release_date_count:
        c['release_date'] = date_to_japanese(c['release_date'])

    area_count = culc.count_by_column(persons, 'area')
    current_date = date_to_japanese(datetime.now())
    param = {
        'current_date': current_date,
        'release_date_count': release_date_count,
        'area_count': area_count,
    }
    return render_template('persons/summary.html', **param)
