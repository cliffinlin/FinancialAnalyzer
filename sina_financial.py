# -*- coding: utf-8 -*-
import random

import constant
import json
import requests
import urllib.request

from bs4 import BeautifulSoup #pip3 install bs4
from contextlib import closing
from datetime import datetime
from requests.exceptions import RequestException


class SinaFinancial:

    def get_user_agent(self):
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


    def get_content(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        # print(url)

        proxies = {
        }

        user_agent = self.get_user_agent()
        headers = {'User-Agent': user_agent}

        try:
            with closing(requests.get(url, stream=True, headers=headers, proxies=proxies)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None

        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    def is_good_response(self, resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def log_error(self, e):
        """
        It is always a good idea to log errors. 
        This function just prints them, but you can
        make it do anything.
        """
        print(e)


    # def parse_tr(self, parent):
    #     value = 0
    #     result = {}
    #
    #     if parent is None:
    #         return None
    #
    #     trs = parent.select("tr")
    #     if trs is None:
    #         return None
    #
    #     for tr in trs:
    #         if tr is None:
    #             return None
    #
    #         tds = tr.select("td")
    #         if tds is None:
    #             return None
    #
    #         if len(tds) < 2:
    #             continue
    #
    #         key_string = tds[0].text
    #         if key_string is None:
    #             continue
    #
    #         # key = datetime.strptime(key_string, constant.DATE_FORMAT)
    #
    #         value_string = tds[1].text
    #         if value_string is None:
    #             continue
    #
    #         if not value_string.strip():
    #             value_string = "0.0"
    #
    #         if ',' in value_string:
    #             value_string = value_string.replace(',', '')
    #             value = float(value_string)
    #             value = value / 100000000.0
    #         else:
    #             value = float(value_string)
    #
    #         result[key_string] = value
    #
    #     return result


    def download_stock_list(self, page):
        url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'

        url += 'page=' + str(page)
        url += '&num=100'
        url += '&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=init'

        print(url)
        #http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=100&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=init
        #symbol: "sh600000", code: "600000", name: "浦发银行", trade: "11.300", pricechange: "0.070", changepercent: "0.623", buy: "11.300", sell: "11.310", settlement: "11.230", open: "11.230", high: "11.390", low: "11.210", volume: 38949418, amount: 439706991, ticktime: "15:00:00", per: 6.108, pb: 0.691, mktcap: 33167850.84861, nmc: 31757253.20587, turnoverratio: 0.13859
        content = None

        try:
            content = urllib.request.urlopen(url).read().decode('gbk')
        except Exception:
            print("urllib.request.urlopen(url).read().decode() error")

        if content is None:
            print("content is None, return")
            return None

        content = content.replace('symbol', '"symbol"')#标记
        content = content.replace('code', '"code"')#code代码
        content = content.replace('name', '"name"')#name名称
        content = content.replace('trade', '"price"')#trade现价
        content = content.replace('pricechange', '"change"')

        content = content.replace('changepercent', '"net"')#changepercent涨跌幅
        content = content.replace('buy', '"buy"')#buy买入价
        content = content.replace('sell', '"sell"')#卖出价
        content = content.replace('settlement', '"settlement"')#settlement昨日收盘价
        content = content.replace('open', '"open"')#open开盘价
        content = content.replace('high', '"high"')#high最高价

        content = content.replace('low', '"low"')#low最低价
        content = content.replace('volume', '"volume"')#volume成交量
        content = content.replace('amount', '"value"')#amount成交金额
        content = content.replace('ticktime', '"ticktime"')
        content = content.replace('per', '"pe"')#per市盈率
        content = content.replace('pb', '"pb"')#pb市净率

        content = content.replace('mktcap', '"mktcap"')#mktcap总市值
        content = content.replace('nmc', '"nmc"')#nmc流通市值
        content = content.replace('turnoverratio', '"turnoverratio"')#turnoverratio换手率

        return json.loads(content)


    def download_stock_data(self, code, length, period=constant.MONTH):
        url = "http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?"

        se = "sh"
        if code[0] == "0" or code[0] == "3":
            se = "sz"

        symbol = "&symbol=" + se + code

        # for day 240, week 1680, month 7200
        if period == constant.DAY:
            scale = "&scale=240"
        elif period == constant.WEEK:
            scale = "&scale=1680"
        elif period == constant.MONTH:
            scale = "&scale=7200"
        else:
            return None

        ma = "&ma=" + "no"
        datalen = "&datalen=" + str(length)

        url = url + symbol + scale + ma + datalen

        print(url)

        content = None

        try:
            content = urllib.request.urlopen(url).read().decode()
        except Exception:
            print("urllib.request.urlopen(url).read().decode() error")

        if content is None:
            print("content is None, return")
            return None

        content = content.replace('day', '"date"')
        content = content.replace('open', '"open"')
        content = content.replace('high', '"high"')
        content = content.replace('low', '"low"')
        content = content.replace('close', '"close"')
        content = content.replace('volume', '"volume"')

        return json.loads(content)

    def download_stock_information(self, code):
        se = "sh"
        if code[0] == "0" or code[0] == "3":
            se = "sz"

        symbol = se + code

        url = 'http://hq.sinajs.cn/list=' + symbol + '_i'

        print(url)

        content = None

        try:
            content = urllib.request.urlopen(url).read().decode('gbk')
        except Exception:
            print("urllib.request.urlopen(url).read().decode() error")

        if content is None:
            print("content is None, return")
            return None

        value_list = content.split(",");

        return value_list

    def download_financial_data(self, stock):
        value = 0
        financial_data = dict()
        financial_data_list = []

        if stock is None:
            return None

        url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/'\
              + stock.code + '.phtml'

        print(url)

        content = self.get_content(url)

        if content is None:
            return None

        html = BeautifulSoup(content, 'html.parser')
        if html is None:
            return None

        tables = html.select('table#FundHoldSharesTable')
        if tables is None:
            return None

        for table in tables:
            if table is None:
                return None

            trs = table.select("tr")
            if trs is None:
                return None

            for tr in trs:
                if tr is None:
                    return None

                tds = tr.select("td")
                if tds is None:
                    return None

                if len(tds) < 2:
                    continue

                key_string = tds[0].text
                if key_string is None:
                    continue

                value_string = tds[1].text
                if value_string is None:
                    continue

                if '截止日期' in key_string:
                    if value_string is None:
                        continue

                    if stock.time_to_market is not None:
                        if datetime.strptime(value_string, constant.DATE_FORMAT)\
                                < datetime.strptime(stock.time_to_market, constant.DATE_FORMAT):
                            return financial_data_list[::-1]

                    financial_data = dict()

                    financial_data["date"] = value_string
                else:
                    if not value_string.strip():
                        value_string = "0.0"

                    if '元' in value_string:
                        value_string = value_string.replace('元', '')

                    if ',' in value_string:
                        value_string = value_string.replace(',', '')
                        try:
                            value = float(value_string)
                            value = value / 100000000.0
                        except:
                            value = 0
                    else:
                        try:
                            value = float(value_string)
                        except:
                            value = 0

                    if '每股净资产-摊薄/期末股数' in key_string:
                        financial_data["book_value_per_share"] = value
                    elif '每股现金流' in key_string:
                        financial_data["cash_flow_per_share"] = value
                    elif '流动资产合计' in key_string:
                        financial_data["total_current_assets"] = value
                    elif '资产总计' in key_string:
                        financial_data["total_assets"] = value
                    elif '长期负债合计' in key_string:
                        financial_data["total_long_term_liabilities"] = value
                    elif '主营业务收入' in key_string:
                        financial_data["main_business_income"] = value
                    elif '财务费用' in key_string:
                        financial_data["financial_expenses"] = value
                    elif '净利润' in key_string:
                        financial_data["net_profit"] = value

                        if stock.total_share != 0:
                            financial_data["net_profit_per_share"] = 100000000.0 * float(value) / float(stock.total_share)
                        else:
                            financial_data["net_profit_per_share"] = 0

                        financial_data_list.append(financial_data)

        return financial_data_list

    def download_share_bonus(self, code):
        share_bonus = dict()
        share_bonus_list = []

        url = 'http://money.finance.sina.com.cn/corp/go.php/vISSUE_ShareBonus/stockid/'\
              + code + '.phtml'

        print(url)

        content = self.get_content(url)

        if content is None:
            return None

        html = BeautifulSoup(content, 'html.parser')
        if html is None:
            return None

        tbodys = html.select("tbody")
        if tbodys is None:
            return None

        for tbody in tbodys:
            if tbody is None:
                return None

            trs = tbody.select("tr")
            if trs is None:
                return None

            for tr in trs:
                if tr is None:
                    return None

                tds = tr.select("td")
                if tds is None:
                    return None

                if len(tds) != 9:
                    continue

                share_bonus = dict()

                date_string = tds[0].text
                if date_string is None or "--" in date_string:
                    continue

                dividend_string = tds[3].text
                if dividend_string is None or "--" in dividend_string:
                    continue

                dividend_date_string = tds[5].text
                if dividend_date_string is None or "--" in dividend_date_string:
                    continue

                share_bonus["date"] = date_string

                if not dividend_string.strip():
                    dividend_string = "0.0"

                dividend = float(dividend_string)
                share_bonus["dividend"] = dividend

                share_bonus["dividend_date"] = dividend_date_string

                share_bonus_list.append(share_bonus)

        return share_bonus_list[::-1]
