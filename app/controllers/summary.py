from flask import Blueprint, render_template, request
from datetime import datetime
import app.lib.log as log
import app.lib.util as util
import app.models.culc as culc
import urllib.parse
import urllib.request
import json
import config

app_summary = Blueprint('summary', __name__, url_prefix='/summary')
logger = log.getLogger(__name__)


@app_summary.route('/by_release_date')
def by_release_date():
    persons = []

    API_URL = 'https://delquyapi.an.r.appspot.com/api'
    param = {
        #    'user': 'tamago324_pad',    # 取得したい人のID
        #    'type': 'json'             # 取得するデータの指定
    }

    url = urllib.parse.urljoin(API_URL + '/persons/', urllib.parse.urlencode(param))
    logger.debug('U ' + url)

    req = urllib.request.Request(
        url=url,
        headers={
            'User-Agent': config.USER_AGENT
        }
    )
    with urllib.request.urlopen(req, timeout=3) as res:
        d = res.read()

    # data = json.loads(d)
    logger.debug(d)

    results = sorted(
        culc.count_by_column(persons, 'release_date'), key=lambda c: c['release_date'])

    results = [
        {'release_date': '2020-04-01', 'count': 10}
    ]

    # area_count = culc.count_by_column(persons, 'area')
    current_date = datetime.now().strftime(r'%Y-%m-%d')
    param = {
        'current_date': current_date,
        'results': results,
    }
    return render_template('summary/by_release_date.html', **param)
