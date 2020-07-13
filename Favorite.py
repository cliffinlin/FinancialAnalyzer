# -*- coding: utf-8 -*-

class Favorite:
    def __init__(self):
        self.stock_list = {
            "600048",  # 保利地产 roi 46.66 roe 23.73 pe 13.56 pb 1.43 dividend 8.2 4.74%  operation 0
            "000069",  # 华侨城Ａ roi 39.33 roe 19.52 pe 17.99 pb 0.98 dividend 3.05 3.76%  operation 0
            "601336",  # 新华保险 roi 35.71 roe 21.63 pe 9.07 pb 1.99 dividend 14.1 2.52%  operation 0
            "600383",  # 金地集团 roi 34.41 roe 20.64 pe 14.37 pb 1.3 dividend 6.7 4.4%  operation 0
            "601668",  # 中国建筑 roi 33.17 roe 17.6 pe 18.12 pb 0.85 dividend 1.85 3.46%  operation 0
            "000002",  # 万 科Ａ roi 31.11 roe 23.52 pe 11.5 pb 1.75 dividend 10.17 3.48%  operation 0
            "600068",  # 葛洲坝 roi 30.98 roe 18.7 pe 14.79 pb 1.14 dividend 1.56 2.06%  operation 0
            "600585",  # 海螺水泥 roi 29.69 roe 27.29 pe 10.46 pb 2.18 dividend 20.0 3.42%  operation 0
            "600606",  # 绿地控股 roi 28.65 roe 19.29 pe 13.03 pb 1.39 dividend 4.0 4.53%  operation 0
            "601601",  # 中国太保 roi 27.44 roe 17.81 pe 9.94 pb 1.56 dividend 12.0 3.74%  operation 0
            "600970",  # 中材国际 roi 25.88 roe 16.66 pe 14.52 pb 1.02 dividend 3.01 4.98%  operation 0
            "600188",  # 兖州煤业 roi 23.78 roe 14.95 pe 16.07 pb 0.95 dividend 5.8 5.74%  operation 0
            "600036",  # 招商银行 roi 20.92 roe 17.94 pe 10.14 pb 1.55 dividend 12.0 3.22%  operation 0
            "601318",  # 中国平安 roi 19.09 roe 21.69 pe 8.63 pb 2.18 dividend 13.0 1.58%  operation 0
            "600755",  # 厦门国贸 roi 18.57 roe 15.58 pe 14.36 pb 1.03 dividend 2.3 2.99%  operation 0
            "600486",  # 扬农化工 roi 16.78 roe 25.97 pe 4.75 pb 4.91 dividend 6.5 0.74%  operation 0
            "000895",  # 双汇发展 roi 14.74 roe 39.18 pe 3.42 pb 9.17 dividend 10.0 2.02%  operation 0
            "000049",  # 德赛电池 roi 13.48 roe 26.25 pe 4.21 pb 5.08 dividend 7.0 1.27%  operation 0
            "000333",  # 美的集团 roi 13.41 roe 24.07 pe 5.16 pb 4.18 dividend 16.0 2.53%  operation 0
            "601088",  # 中国神华 roi 13.1 roe 11.88 pe 12.25 pb 0.91 dividend 12.6 7.59%  operation 0
            "601628",  # 中国人寿 roi 12.35 roe 13.84 pe 4.33 pb 2.8 dividend 7.3 1.81%  operation 0
            "000828",  # 东莞控股 roi 12.16 roe 13.57 pe 10.8 pb 1.15 dividend 3.0 3.7%  operation 0
            "600663",  # 陆家嘴 roi 11.17 roe 17.5 pe 6.32 pb 2.99 dividend 4.56 3.26%  operation 0
            "600612",  # 老凤祥 roi 11.04 roe 21.42 pe 4.56 pb 4.18 dividend 11.5 1.95%  operation 0
            "000951",  # 中国重汽 roi 10.95 roe 18.41 pe 5.17 pb 3.14 dividend 5.5 1.62%  operation 0
            "000581",  # 威孚高科 roi 10.71 roe 12.82 pe 8.98 pb 1.38 dividend 11.0 4.68%  operation 0
            "000651",  # 格力电器 roi 9.89 roe 22.02 pe 5.76 pb 3.17 dividend 12.0 2.02%  operation 0
            "600690",  # 海尔智家 roi 9.59 roe 17.2 pe 5.93 pb 2.5 dividend 3.75 2.05%  operation 0
            "600309",  # 万华化学 roi 9.41 roe 21.26 pe 5.03 pb 3.97 dividend 13.0 2.36%  operation 0
            "600007",  # 中国国贸 roi 9.34 roe 13.0 pe 6.3 pb 1.9 dividend 3.8 2.59%  operation 0
            "000568",  # 泸州老窖 roi 8.8 roe 26.05 pe 2.64 pb 8.68 dividend 15.9 1.27%  operation 0
            "000538",  # 云南白药 roi 8.3 roe 18.16 pe 3.31 pb 3.56 dividend 30.0 2.75%  operation 0
            "600511",  # 国药股份 roi 8.28 roe 16.48 pe 4.65 pb 3.09 dividend 6.38 1.44%  operation 0
            "600062",  # 华润双鹤 roi 8.21 roe 12.25 pe 6.7 pb 1.68 dividend 3.04 2.12%  operation 0
            "600519",  # 贵州茅台 roi 7.6 roe 34.72 pe 1.92 pb 15.01 dividend 170.25 0.96%  operation 0
            "000858",  # 五 粮 液 roi 7.32 roe 26.63 pe 2.2 pb 10.33 dividend 22.0 1.01%  operation 0
            "600809",  # 山西汾酒 roi 7.17 roe 31.99 pe 1.6 pb 16.47 dividend 9.0 0.55%  operation 0
            "601607",  # 上海医药 roi 6.92 roe 9.96 pe 6.95 pb 1.35 dividend 4.4 2.18%  operation 0
            "600900",  # 长江电力 roi 6.57 roe 14.4 pe 4.96 pb 2.78 dividend 6.8 3.55%  operation 0
            "600897",  # 厦门空港 roi 6.05 roe 10.83 pe 7.07 pb 1.52 dividend 5.23 2.74%  operation 0
            "000028",  # 国药一致 roi 5.94 roe 10.24 pe 5.8 pb 1.61 dividend 6.0 1.22%  operation 0
            "002304",  # 洋河股份 roi 5.86 roe 19.47 pe 3.54 pb 5.2 dividend 30.0 2.17%  operation 0
            "600548",  # 深高速 roi 5.22 roe 10.64 pe 9.08 pb 1.15 dividend 5.2 5.42%  operation 0
            "600887",  # 伊利股份 roi 5.21 roe 22.03 pe 2.69 pb 8.01 dividend 8.1 2.28%  operation 0
            "600332",  # XD白云山 roi 4.98 roe 12.84 pe 5.17 pb 2.26 dividend 5.89 1.67%  operation 0
            "600377",  # 宁沪高速 roi 4.84 roe 11.24 pe 6.06 pb 1.86 dividend 4.6 4.48%  operation 0
            "600999",  # 招商证券 roi 4.73 roe 10.25 pe 3.63 pb 2.64 dividend 0.0 0.0%  operation 0
            "000596",  # 古井贡酒 roi 4.67 roe 23.27 pe 1.95 pb 10.45 dividend 15.0 0.75%  operation 0
            "603288",  # 海天味业 roi 4.53 roe 29.79 pe 1.29 pb 19.5 dividend 10.8 0.82%  operation 0
            "600741",  # 华域汽车 roi 4.28 roe 9.98 pe 6.31 pb 1.54 dividend 8.5 3.56%  operation 0
            "600660",  # 福耀玻璃 roi 4.17 roe 13.28 pe 4.76 pb 2.64 dividend 7.5 3.25%  operation 0
            "000999",  # 华润三九 roi 4.0 roe 12.33 pe 4.77 pb 2.37 dividend 4.3 1.36%  operation 0
            "600436",  # 片仔癀 roi 3.7 roe 26.1 pe 1.2 pb 16.92 dividend 8.2 0.41%  operation 0
            "600104",  # 上汽集团 roi 3.28 roe 7.52 pe 8.22 pb 0.9 dividend 8.8 4.57%  operation 0
            "600276",  # 恒瑞医药 roi 2.91 roe 22.24 pe 1.03 pb 16.91 dividend 2.3 0.23%  operation 0
            "000513",  # 丽珠集团 roi 2.84 roe 9.07 pe 2.7 pb 4.16 dividend 11.5 2.23%  operation 0
            "600009",  # 上海机场 roi 2.65 roe 12.55 pe 2.61 pb 4.44 dividend 7.9 1.07%  operation 0
            "600056",  # 中国医药 roi 2.62 roe 9.44 pe 5.05 pb 1.79 dividend 2.76 1.78%  operation 0
            "000661",  # 长春高新 roi 2.55 roe 14.86 pe 1.02 pb 11.1 dividend 10.0 0.21%  operation 0
            "600197",  # 伊力特 roi 2.4 roe 11.8 pe 3.04 pb 3.76 dividend 4.38 1.89%  operation 0
            "600030",  # 中信证券 roi 2.26 roe 7.15 pe 2.87 pb 2.37 dividend 5.0 1.54%  operation 0
            "000429",  # 粤高速Ａ roi 2.18 roe 8.32 pe 5.35 pb 1.62 dividend 4.22 5.66%  operation 0
            "601888",  # 中国中免 roi 0.36 roe 11.91 pe 0.58 pb 19.15 dividend 7.2 0.37%  operation 0
        }

    def get_stock_list(self):
        return self.stock_list
