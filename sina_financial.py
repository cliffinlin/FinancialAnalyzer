# -*- coding: utf-8 -*-

import constant
import json
import requests
import urllib.request

from bs4 import BeautifulSoup
from contextlib import closing
from datetime import datetime
from requests.exceptions import RequestException


class SinaFinancial:

    def get_content(self, url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        # print(url)

        try:
            with closing(requests.get(url, stream=True)) as resp:
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
    #
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

    def parse_tr(self, parent):
        value = 0
        result = {}

        if parent is None:
            return None

        trs = parent.select("tr")
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

            # key = datetime.strptime(key_string, constant.DATE_FORMAT)

            value_string = tds[1].text
            if value_string is None:
                continue

            if not value_string.strip():
                value_string = "0.0"

            if ',' in value_string:
                value_string = value_string.replace(',', '')
                value = float(value_string)
                value = value / 100000000.0
            else:
                value = float(value_string)

            result[key_string] = value

        return result

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

    def download_financial_data(self, code, not_before=None):
        value = 0
        financial_data = dict()
        financial_data_list = []

        url = 'http://money.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/'\
              + code + '.phtml'

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

                    if not_before is not None:
                        if datetime.strptime(value_string, constant.DATE_FORMAT) < not_before:
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
                        value = float(value_string)
                        value = value / 100000000.0
                    else:
                        value = float(value_string)

                    if '每股净资产-摊薄/期末股数' in key_string:
                        financial_data["book_value_per_share"] = value
                    elif '每股收益-摊薄/期末股数' in key_string:
                        financial_data["earnings_per_share"] = value
                    elif '每股现金含量' in key_string:
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

                        net_assets = float(financial_data["total_assets"]) - float(
                            financial_data["total_long_term_liabilities"])
                        if net_assets == 0:
                            financial_data["roe"] = 0
                        else:
                            financial_data["roe"] = 100.0 * float(financial_data["net_profit"]) / float(net_assets)

                        financial_data["book_value_per_share_rate"] = financial_data["book_value_per_share"]

                        financial_data_list.append(financial_data)

        return financial_data_list[::-1]


    # def download_financial_data(self, code):
    #     url = 'http://money.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid='\
    #           + code + '&type=' + type
    #
    #     print(url)
    #
    #     content = self.get_content(url)
    #
    #     if content is None:
    #         return None
    #
    #     html = BeautifulSoup(content, 'html.parser')
    #     if html is None:
    #         return None
    #
    #     tables = html.select('table#Table1')
    #     if tables is None:
    #         return None
    #
    #     for table in tables:
    #         if table is None:
    #             return None
    #
    #         thead = table.select("thead")
    #         if thead is None:
    #             return None
    #
    #         tbodys = table.select("tbody")
    #         if tbodys is None:
    #             return None
    #
    #         if len(tbodys) > 0:
    #             for tbody in tbodys:
    #                 if tbody is None:
    #                     return None
    #                 return self.parse_tr(tbody)
    #         else:
    #             return self.parse_tr(table)

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

                if len(tds) < 9:
                    continue

                share_bonus = dict()

                date_string = tds[0].text
                if date_string is None:
                    continue
                share_bonus["date"] = date_string

                dividend_string = tds[3].text
                if dividend_string is None:
                    continue
                if not dividend_string.strip():
                    dividend_string = "0.0"
                dividend = float(dividend_string)
                share_bonus["dividend"] = dividend

                dividend_date_string = tds[5].text
                share_bonus["dividend_date"] = dividend_date_string

                share_bonus_list.append(share_bonus)

        return share_bonus_list[::-1]
