# -*- coding: utf-8 -*-
import re
import urllib.request

import Utility


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


def download_share_holder_list(stock, report_date):
    share_holder_list = []

    if stock is None:
        return None

    # http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/GGZLSJTJ/GetGGZLSJTJ?js=jQuery112308413975235066407_1611393405910&tkn=eastmoney&reportDate=2020-12-31&code=600028.sh&cfg=ggzlsjtj&_=1611393405911

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

        share_holder = dict()
        share_holder["date"] = itme_list[0]
        share_holder["type"] = itme_list[1]
        share_holder["number"] = itme_list[2]
        share_holder["hold"] = itme_list[3]
        share_holder["ratio"] = itme_list[6]

        if "机构汇总" in share_holder["type"]:
            share_holder_list.append(share_holder)

    return share_holder_list
