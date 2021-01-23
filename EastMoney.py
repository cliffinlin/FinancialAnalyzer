# -*- coding: utf-8 -*-
import json
import random
import re
import urllib.request
from contextlib import closing
from datetime import datetime

import requests
from bs4 import BeautifulSoup  # pip3 install bs4
from requests.exceptions import RequestException

import Constants
import Utility


def get_user_agent():
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]

    user_agent = random.choice(user_agents)

    return user_agent


def get_content(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    # print(url)

    proxies = {
    }

    user_agent = get_user_agent()
    headers = {'User-Agent': user_agent}

    try:
        with closing(requests.get(url, stream=True, headers=headers, proxies=proxies)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def download_stock_list(page):
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'

    url += 'page=' + str(page)
    url += '&num=100'
    url += '&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=init'

    print(url)

    content = None

    try:
        content = urllib.request.urlopen(url).read().decode('gbk')
    except Exception:
        print("urllib.request.urlopen(url).read().decode() error")

    if Utility.is_empty(content):
        return None

    return json.loads(content)


def download_stock_information(stock):
    if stock is None:
        return None

    url = 'http://hq.sinajs.cn/list=' + stock.get_symbol() + '_i'

    print(url)

    content = None

    try:
        content = urllib.request.urlopen(url).read().decode('gbk')
    except Exception:
        print("urllib.request.urlopen(url).read().decode() error")

    if Utility.is_empty(content):
        print("content is empty, return")
        return None

    value_list = content.split(",")

    return value_list


def download_report_date_list(stock):
    report_dat_list = []

    # http: // datainterface3.eastmoney.com / EM_DataCenter_V3 / api / ZLSJBGQ / GetBGQ?tkn = eastmoney & sortDirec = 1 & pageNum = 1 & pageSize = 25 & cfg = zlsjbgq & js = jQuery112308413975235066407_1611393405908 & _ = 1611393405909

    url = 'http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/ZLSJBGQ/GetBGQ?' \
          'tkn=eastmoney' \
          '&sortDirec=1' \
          '&pageNum=1' \
          '&pageSize=25' \
          '&cfg=zlsjbgq' \
          '&js=jQuery112308413975235066407_1611393405908' \
          '&_=1611393405909'

    print(url)

    content = None

    try:
        content = urllib.request.urlopen(url).read().decode('gbk')
    except Exception:
        print("urllib.request.urlopen(url).read().decode() error")

    if Utility.is_empty(content):
        return None

    regex = '.*\[(.*?)\].*'
    matches = re.search(regex, content)
    if matches is None:
        return None

    report_date_string = matches.group(1)
    if Utility.is_empty(report_date_string) is None:
        return None

    report_date_string = report_date_string.replace("\"", "")
    if Utility.is_empty(report_date_string) is None:
        return None

    report_dat_list = report_date_string.split(",")

    return report_dat_list


def download_stock_holder_list(stock, report_date):
    stock_holder_list = []

    if stock is None:
        return None

    #http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/GGZLSJTJ/GetGGZLSJTJ?js=jQuery112308413975235066407_1611393405910&tkn=eastmoney&reportDate=2020-12-31&code=600028.sh&cfg=ggzlsjtj&_=1611393405911

    url = 'http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/GGZLSJTJ/GetGGZLSJTJ?' \
          'js=jQuery112308413975235066407_1611393405910' \
          '&tkn=eastmoney'
    url += '&reportDate=' + report_date
    url += '&code=' + stock.get_code() + "." + stock.get_se()
    url += '&cfg=ggzlsjtj' \
          '&_=1611393405911'

    print(url)

    content = None

    try:
        content = urllib.request.urlopen(url).read().decode()
    except Exception:
        print("urllib.request.urlopen(url).read().decode() error")

    if Utility.is_empty(content):
        return None

    regex = '.*\[(.*?)\].*'
    matches = re.search(regex, content)
    if matches is None:
        return None

    data_string = matches.group(1)
    if Utility.is_empty(data_string) is None:
        return None

    data_string = data_string.replace("\"", "")
    if Utility.is_empty(data_string) is None:
        return None

    data_string_list = data_string.split(",")
    if Utility.is_empty(data_string_list) is None:
        return None

    for data_string in data_string_list:
        if Utility.is_empty(data_string):
            continue

        itme_list = data_string.split('|')
        if Utility.is_empty(itme_list) or len(itme_list) < 7:
            continue

        stock_holder = dict()
        stock_holder["date"] = itme_list[0]
        stock_holder["type"] = itme_list[1]
        stock_holder["number"] = itme_list[2]
        stock_holder["hold"] = itme_list[3]
        stock_holder["ratio"] = itme_list[6]

        stock_holder_list.append(stock_holder)

    return stock_holder_list
