# coding: utf-8
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
import socket
import time
from bs4 import BeautifulSoup
import re
from datetime import datetime, date, timedelta
import logging
import config


logger = logging.getLogger('aichi-digger').getChild(__name__)


def excel_num_to_date(num):
    return date(1900, 1, 1) + timedelta(days=num - 2)


# Zenkaku to Hankaku
def zen_to_han(text):
    return text.translate(
        str.maketrans(
            {chr(0xFF01 + i): chr(0x21 + i) for i in range(94)}))


# Japanese date to standard date
def parse_japanese_date(text):

    gengo, jyear, month, day = re.sub(
        r'^(令和|平成)(\d+|元)年(\d+)月(\d+)日$', r'\1 \2 \3 \4', text).split()
    if jyear == r'元':
        jyear = 1
    if gengo == r'令和':
        year = int(jyear) + 2018
    elif gengo == r'平成':
        year = int(jyear) + 1988
    else:
        year = int(jyear)

    return date(year=year, month=int(month), day=int(day))


def date_to_japanese(dt):
    if type(dt) == str:
        dt = datetime.strptime(dt, r'%Y-%m-%d')
    return dt.strftime(r'%Y年%m月%d日')


def html_to_text(html, br_delimiter='\n'):
    DUMMY_STRING = r'[aynvScmp034ms5]'

    for br in html.select('br'):
        if br.string:
            br.replace_with(DUMMY_STRING + br.string)
        else:
            br.replace_with(DUMMY_STRING)

    text = html.text.strip().replace('\n', '').replace(DUMMY_STRING, br_delimiter)
    return text


def download_file(url, filepath=None):
    try:
        if not filepath:
            filename = re.sub(r'^.*\/([^\/]+)$', r'\1', url)
            filepath = config.BASE_DIR + '/data/' + filename

        urllib.request.urlretrieve(url, filepath)
        logger.info('File %s downloded.', filepath)
        return filepath

    except HTTPError as e:
        if e.code == 404:
            logger.warning('HTTP Error 404: Not Found; %s', url)
            return False

        else:
            raise e

    except Exception as e:
        raise e


def create_soup(url):
    retry_count = 4
    timeout_sec = 3

    soup = None
    for i in range(0, retry_count):
        try:
            req = urllib.request.Request(
                url=url,
                headers={
                    'User-Agent': config.USER_AGENT
                }
            )
            with urllib.request.urlopen(req, timeout=timeout_sec) as res:
                soup = BeautifulSoup(res, 'html.parser')
                break

        except socket.timeout:
            logger.info('timeout, retry url:%s', url)

        except URLError as e:
            if isinstance(e.reason, socket.timeout):
                logger.info('Timeout, retry:%s', url)
                time.sleep(0.5)
            else:
                raise e

        except Exception as e:
            raise e

    if not soup:
        raise Exception('Request timeout url:{}.'.format(url))

    time.sleep(0.5)

    return soup
