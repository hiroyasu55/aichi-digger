import os
import logging

DEBUG = False
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, 'app')
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_NAME = r'aichi-digger'
LOG_FORMAT = r"%(asctime)s %(name)s [%(levelname)s] %(message)s"
LOG_TIME_FORMAT = r'%Y-%m-%d %H:%M:%S'
LOG_LEVEL = logging.INFO
USER_AGENT = \
    r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113"  # noqa: E501
WTF_CSRF_SECRET_KEY = "sefh30itgmp2fnp^ih26vb;fkga"

AICHI_PRESS_RELEASE_URL = \
    r'https://www.pref.aichi.jp/site/covid19-aichi/corona-kisya.html'
NAGOYA_PRESS_RELEASE_URL = \
    r'http://www.city.nagoya.jp/kenkofukushi/page/0000126920.html'

DEBUG = False

if os.getenv('FLASK_ENV') == 'development':
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
