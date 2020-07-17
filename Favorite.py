# -*- coding: utf-8 -*-

class Favorite:
    def __init__(self):
        self.stock_list = {
            "600048",  # 保利地产 roi 50.27 rate 1.45 roe 23.73 pe 14.61 pb 1.33 dividend 8.2 5.1%  operation 0
            "000069",  # 华侨城Ａ roi 43.16 rate 1.12 roe 19.52 pe 19.74 pb 0.9 dividend 3.05 4.12%  operation 0
            "601336",  # 新华保险 roi 37.99 rate 1.82 roe 21.63 pe 9.65 pb 1.87 dividend 14.1 2.68%  operation 0
            "600383",  # 金地集团 roi 36.37 rate 1.16 roe 20.64 pe 15.19 pb 1.23 dividend 6.7 4.66%  operation 0
            "601668",  # 中国建筑 roi 35.07 rate 1.04 roe 17.6 pe 19.16 pb 0.81 dividend 1.85 3.66%  operation 0
            "600068",  # 葛洲坝 roi 34.31 rate 1.12 roe 18.7 pe 16.38 pb 1.03 dividend 1.56 2.28%  operation 0
            "000002",  # 万 科Ａ roi 33.35 rate 1.15 roe 23.52 pe 12.33 pb 1.63 dividend 10.17 3.73%  operation 0
            "600606",  # 绿地控股 roi 32.9 rate 1.14 roe 19.29 pe 14.96 pb 1.21 dividend 4.0 5.2%  operation 0
            "600585",  # 海螺水泥 roi 30.48 rate 1.04 roe 27.29 pe 10.74 pb 2.12 dividend 20.0 3.51%  operation 0
            "601601",  # 中国太保 roi 29.54 rate 1.55 roe 17.81 pe 10.7 pb 1.45 dividend 12.0 4.03%  operation 0
            "600188",  # 兖州煤业 roi 26.02 rate 0.99 roe 14.95 pe 17.58 pb 0.87 dividend 5.8 6.28%  operation 0
            "600036",  # 招商银行 roi 21.64 rate 1.15 roe 17.94 pe 10.49 pb 1.5 dividend 12.0 3.33%  operation 0
            "601318",  # 中国平安 roi 20.15 rate 1.02 roe 21.69 pe 9.11 pb 2.07 dividend 13.0 1.67%  operation 0
            "600755",  # 厦门国贸 roi 20.06 rate 0.83 roe 15.58 pe 15.51 pb 0.95 dividend 2.3 3.23%  operation 0
            "600486",  # 扬农化工 roi 17.66 rate 1.36 roe 25.97 pe 5.0 pb 4.67 dividend 6.5 0.78%  operation 0
            "000049",  # 德赛电池 roi 14.54 rate 1.22 roe 26.25 pe 4.54 pb 4.71 dividend 7.0 1.37%  operation 0
            "601628",  # 中国人寿 roi 14.43 rate 2.06 roe 13.84 pe 5.06 pb 2.4 dividend 7.3 2.11%  operation 0
            "601088",  # 中国神华 roi 13.96 rate 0.9 roe 11.88 pe 13.06 pb 0.86 dividend 12.6 8.09%  operation 0
            "000895",  # 双汇发展 roi 13.4 rate 1.1 roe 39.18 pe 3.11 pb 10.08 dividend 10.0 1.83%  operation 0
            "000333",  # 美的集团 roi 13.24 rate 1.08 roe 24.03 pe 5.1 pb 4.22 dividend 16.0 2.5%  operation 0
            "000828",  # 东莞控股 roi 12.95 rate 0.83 roe 13.57 pe 11.5 pb 1.08 dividend 3.0 3.94%  operation 0
            "600663",  # 陆家嘴 roi 12.51 rate 1.01 roe 17.5 pe 7.08 pb 2.67 dividend 4.56 3.65%  operation 0
            "000581",  # 威孚高科 roi 11.28 rate 0.93 roe 12.82 pe 9.46 pb 1.31 dividend 11.0 4.93%  operation 0
            "600612",  # 老凤祥 roi 11.26 rate 1.13 roe 21.42 pe 4.65 pb 4.09 dividend 11.5 1.99%  operation 0
            "000951",  # 中国重汽 roi 10.54 rate 1.15 roe 18.41 pe 4.98 pb 3.26 dividend 5.5 1.56%  operation 0
            "600007",  # 中国国贸 roi 10.29 rate 1.14 roe 13.0 pe 6.94 pb 1.73 dividend 3.8 2.85%  operation 0
            "000651",  # 格力电器 roi 10.27 rate 0.78 roe 22.02 pe 5.98 pb 3.05 dividend 12.0 2.1%  operation 0
            "600690",  # 海尔智家 roi 10.04 rate 0.94 roe 17.2 pe 6.21 pb 2.38 dividend 3.75 2.15%  operation 0
            "600511",  # 国药股份 roi 9.97 rate 1.08 roe 16.48 pe 5.6 pb 2.57 dividend 6.38 1.74%  operation 0
            "000568",  # 泸州老窖 roi 9.67 rate 1.28 roe 26.05 pe 2.9 pb 7.92 dividend 15.9 1.39%  operation 0
            "600062",  # XD华润双 roi 8.78 rate 1.0 roe 12.25 pe 7.17 pb 1.57 dividend 3.04 2.27%  operation 0
            "000538",  # 云南白药 roi 8.55 rate 1.38 roe 18.16 pe 3.41 pb 3.46 dividend 30.0 2.83%  operation 0
            "600309",  # 万华化学 roi 8.36 rate 0.88 roe 21.26 pe 4.47 pb 4.46 dividend 13.0 2.09%  operation 0
            "600519",  # 贵州茅台 roi 8.23 rate 1.14 roe 34.72 pe 2.08 pb 13.88 dividend 170.25 1.03%  operation 0
            "000858",  # 五 粮 液 roi 7.79 rate 1.25 roe 26.63 pe 2.34 pb 9.72 dividend 22.0 1.07%  operation 0
            "600809",  # 山西汾酒 roi 7.52 rate 1.4 roe 31.99 pe 1.68 pb 15.72 dividend 9.0 0.57%  operation 0
            "601607",  # 上海医药 roi 7.25 rate 1.0 roe 9.96 pe 7.28 pb 1.29 dividend 4.4 2.28%  operation 0
            "600900",  # XD长江电 roi 6.77 rate 0.92 roe 14.4 pe 5.11 pb 2.7 dividend 6.8 3.65%  operation 0
            "600897",  # 厦门空港 roi 6.37 rate 0.79 roe 10.83 pe 7.45 pb 1.45 dividend 5.23 2.88%  operation 0
            "000028",  # 国药一致 roi 6.29 rate 1.0 roe 10.24 pe 6.14 pb 1.52 dividend 6.0 1.29%  operation 0
            "002304",  # 洋河股份 roi 6.29 rate 0.85 roe 19.47 pe 3.8 pb 4.84 dividend 30.0 2.34%  operation 0
            "600548",  # 深高速 roi 5.6 rate 0.54 roe 10.64 pe 9.75 pb 1.07 dividend 5.2 5.82%  operation 0
            "600887",  # 伊利股份 roi 5.39 rate 0.88 roe 22.03 pe 2.78 pb 7.76 dividend 8.1 2.36%  operation 0
            "600332",  # 白云山 roi 5.21 rate 0.75 roe 12.84 pe 5.41 pb 2.16 dividend 5.89 1.75%  operation 0
            "600377",  # 宁沪高速 roi 4.92 rate 0.71 roe 11.24 pe 6.16 pb 1.83 dividend 4.6 4.55%  operation 0
            "000596",  # 古井贡酒 roi 4.79 rate 1.03 roe 23.27 pe 2.0 pb 10.2 dividend 15.0 0.77%  operation 0
            "600999",  # 招商证券 roi 4.73 rate 1.27 roe 10.25 pe 3.63 pb 2.64 dividend 0.0 0.0%  operation 0
            "600741",  # XD华域汽 roi 4.71 rate 0.68 roe 9.98 pe 6.94 pb 1.4 dividend 8.5 3.91%  operation 0
            "603288",  # 海天味业 roi 4.57 rate 1.18 roe 29.79 pe 1.3 pb 19.31 dividend 10.8 0.83%  operation 0
            "000999",  # 华润三九 roi 4.22 rate 0.68 roe 12.33 pe 5.03 pb 2.25 dividend 4.3 1.43%  operation 0
            "600660",  # 福耀玻璃 roi 4.01 rate 0.66 roe 13.28 pe 4.57 pb 2.76 dividend 7.5 3.12%  operation 0
            "600436",  # 片仔癀 roi 3.97 rate 1.18 roe 26.1 pe 1.29 pb 15.76 dividend 8.2 0.44%  operation 0
            "600104",  # 上汽集团 roi 3.4 rate 0.53 roe 7.52 pe 8.52 pb 0.87 dividend 8.8 4.74%  operation 0
            "600276",  # 恒瑞医药 roi 3.02 rate 1.27 roe 22.24 pe 1.07 pb 16.31 dividend 2.3 0.24%  operation 0
            "000513",  # 丽珠集团 roi 2.91 rate 1.16 roe 9.07 pe 2.77 pb 4.05 dividend 11.5 2.29%  operation 0
            "600056",  # 中国医药 roi 2.88 rate 0.55 roe 9.44 pe 5.54 pb 1.63 dividend 2.76 1.95%  operation 0
            "600009",  # 上海机场 roi 2.74 rate 0.81 roe 12.55 pe 2.7 pb 4.29 dividend 7.9 1.1%  operation 0
            "600197",  # 伊力特 roi 2.62 rate 0.67 roe 11.8 pe 3.31 pb 3.44 dividend 4.38 2.06%  operation 0
            "600030",  # 中信证券 roi 2.56 rate 1.1 roe 7.15 pe 3.26 pb 2.09 dividend 5.0 1.75%  operation 0
            "000661",  # 长春高新 roi 2.47 rate 1.68 roe 14.86 pe 0.99 pb 11.43 dividend 10.0 0.21%  operation 0
            "000429",  # 粤高速Ａ roi 2.29 rate 0.49 roe 8.32 pe 5.61 pb 1.55 dividend 4.22 5.93%  operation 0
            "601888",  # 中国中免 roi 0.37 rate 0.52 roe 11.91 pe 0.6 pb 18.5 dividend 7.2 0.38%  operation 0
        }

    def get_stock_list(self):
        return self.stock_list
