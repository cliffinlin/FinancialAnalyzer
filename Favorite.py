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
            "600741",  # XD华域汽 roi 4.71 rate 0.68 roe 9.98 pe 6.94 pb 1.4 dividend 8.5 3.91%  operation 0
            "603288",  # 海天味业 roi 4.57 rate 1.18 roe 29.79 pe 1.3 pb 19.31 dividend 10.8 0.83%  operation 0
            "000999",  # 华润三九 roi 4.22 rate 0.68 roe 12.33 pe 5.03 pb 2.25 dividend 4.3 1.43%  operation 0
            "600660",  # 福耀玻璃 roi 4.01 rate 0.66 roe 13.28 pe 4.57 pb 2.76 dividend 7.5 3.12%  operation 0
            "600436",  # 片仔癀 roi 3.97 rate 1.18 roe 26.1 pe 1.29 pb 15.76 dividend 8.2 0.44%  operation 0
            "600104",  # 上汽集团 roi 3.4 rate 0.53 roe 7.52 pe 8.52 pb 0.87 dividend 8.8 4.74%  operation 0
            "600276",  # 恒瑞医药 roi 3.02 rate 1.27 roe 22.24 pe 1.07 pb 16.31 dividend 2.3 0.24%  operation 0

            "600056",  # 中国医药 roi 2.88 rate 0.55 roe 9.44 pe 5.54 pb 1.63 dividend 2.76 1.95%  operation 0
            "600009",  # 上海机场 roi 2.74 rate 0.81 roe 12.55 pe 2.7 pb 4.29 dividend 7.9 1.1%  operation 0
            "600197",  # 伊力特 roi 2.62 rate 0.67 roe 11.8 pe 3.31 pb 3.44 dividend 4.38 2.06%  operation 0
            "600030",  # 中信证券 roi 2.56 rate 1.1 roe 7.15 pe 3.26 pb 2.09 dividend 5.0 1.75%  operation 0
            "000661",  # 长春高新 roi 2.47 rate 1.68 roe 14.86 pe 0.99 pb 11.43 dividend 10.0 0.21%  operation 0
            "000429",  # 粤高速Ａ roi 2.29 rate 0.49 roe 8.32 pe 5.61 pb 1.55 dividend 4.22 5.93%  operation 0
            "601888",  # 中国中免 roi 0.37 rate 0.52 roe 11.91 pe 0.6 pb 18.5 dividend 7.2 0.38%  operation 0

            "600466",  # 蓝光发展 roi 87.26 rate 1.44 roe 27.86 pe 21.75 pb 1.0 dividend 2.87 5.45%  operation 0
            "002146",  # 荣盛发展 roi 83.37 rate 1.19 roe 26.73 pe 26.21 pb 0.84 dividend 4.8 5.93%  operation 0
            "000672",  # 上峰水泥 roi 82.55 rate 1.39 roe 60.54 pe 9.81 pb 4.08 dividend 9.0 3.11%  operation 0
            "600340",  # 华夏幸福 roi 74.63 rate 1.17 roe 29.96 pe 21.29 pb 1.1 dividend 15.0 8.6%  operation 0
            "600846",  # 同济科技 roi 69.62 rate 2.29 roe 27.0 pe 11.26 pb 1.95 dividend 3.4 3.8%  operation 0
            "600153",  # 建发股份 roi 56.08 rate 1.26 roe 20.38 pe 21.84 pb 0.8 dividend 5.0 5.43%  operation 0
            "600048",  # 保利地产 roi 52.06 rate 1.45 roe 23.73 pe 15.13 pb 1.28 dividend 8.2 5.28%  operation 0
            "000069",  # 华侨城Ａ roi 45.3 rate 1.12 roe 19.52 pe 20.72 pb 0.85 dividend 3.05 4.33%  operation 0

            "601336",  # 新华保险 roi 38.7 rate 1.82 roe 21.63 pe 9.83 pb 1.84 dividend 14.1 2.73%  operation 0
            "600383",  # 金地集团 roi 38.43 rate 1.16 roe 20.64 pe 16.05 pb 1.17 dividend 6.7 4.92%  operation 0
            "600668",  # 尖峰集团 roi 37.0 rate 1.21 roe 22.27 pe 13.73 pb 1.36 dividend 3.0 1.94%  operation 0
            "600068",  # 葛洲坝 roi 35.88 rate 1.12 roe 18.7 pe 17.13 pb 0.98 dividend 1.56 2.39%  operation 0
            "601668",  # 中国建筑 roi 35.2 rate 1.04 roe 17.6 pe 19.23 pb 0.8 dividend 1.85 3.68%  operation 0
            "000002",  # 万 科Ａ roi 34.03 rate 1.15 roe 23.52 pe 12.58 pb 1.6 dividend 10.17 3.81%  operation 0
            "600606",  # 绿地控股 roi 33.69 rate 1.14 roe 19.29 pe 15.32 pb 1.19 dividend 4.0 5.33%  operation 0
            "601601",  # 中国太保 roi 29.81 rate 1.55 roe 17.81 pe 10.8 pb 1.44 dividend 12.0 4.07%  operation 0
            "600585",  # 海螺水泥 roi 29.06 rate 1.04 roe 27.29 pe 10.24 pb 2.23 dividend 20.0 3.35%  operation 0
            "601009",  # 南京银行 roi 28.48 rate 1.12 roe 15.21 pe 16.72 pb 0.8 dividend 3.92 5.09%  operation 0
            "600352",  # 浙江龙盛 roi 26.53 rate 1.13 roe 22.95 pe 10.23 pb 1.88 dividend 2.5 1.68%  operation 0
            "600801",  # 华新水泥 roi 24.12 rate 1.0 roe 22.93 pe 10.52 pb 2.51 dividend 12.1 4.69%  operation 0
            "600036",  # 招商银行 roi 22.8 rate 1.15 roe 17.94 pe 11.05 pb 1.42 dividend 12.0 3.5%  operation 0
            "600755",  # 厦门国贸 roi 21.13 rate 0.83 roe 15.58 pe 16.34 pb 0.9 dividend 2.3 3.4%  operation 0
            "601318",  # 中国平安 roi 20.58 rate 1.02 roe 21.69 pe 9.3 pb 2.02 dividend 13.0 1.7%  operation 0
            "600486",  # 扬农化工 roi 16.35 rate 1.36 roe 25.97 pe 4.63 pb 5.04 dividend 6.5 0.72%  operation 0
            "601628",  # 中国人寿 roi 14.08 rate 2.06 roe 13.84 pe 4.94 pb 2.46 dividend 7.3 2.07%  operation 0
            "000895",  # 双汇发展 roi 14.01 rate 1.1 roe 39.18 pe 3.25 pb 9.63 dividend 10.0 1.92%  operation 0
            "601088",  # 中国神华 roi 14.0 rate 0.9 roe 11.88 pe 13.09 pb 0.85 dividend 12.6 8.11%  operation 0
            "000049",  # 德赛电池 roi 13.42 rate 1.22 roe 26.25 pe 4.19 pb 5.11 dividend 7.0 1.26%  operation 0
            "600663",  # 陆家嘴 roi 13.04 rate 1.01 roe 17.5 pe 7.38 pb 2.56 dividend 4.56 3.81%  operation 0
            "000828",  # 东莞控股 roi 13.04 rate 0.83 roe 13.57 pe 11.58 pb 1.07 dividend 3.0 3.97%  operation 0
            "000333",  # 美的集团 roi 12.59 rate 1.08 roe 24.03 pe 4.85 pb 4.44 dividend 16.0 2.38%  operation 0
            "000581",  # 威孚高科 roi 11.74 rate 0.93 roe 12.82 pe 9.85 pb 1.25 dividend 11.0 5.14%  operation 0
            "600690",  # 海尔智家 roi 10.78 rate 0.94 roe 17.2 pe 6.67 pb 2.22 dividend 3.75 2.31%  operation 0
            "600007",  # 中国国贸 roi 10.58 rate 1.14 roe 13.0 pe 7.14 pb 1.68 dividend 3.8 2.93%  operation 0
            "000651",  # 格力电器 roi 10.36 rate 0.78 roe 22.02 pe 6.03 pb 3.02 dividend 12.0 2.11%  operation 0
            "600612",  # 老凤祥 roi 10.29 rate 1.13 roe 21.42 pe 4.25 pb 4.48 dividend 11.5 1.82%  operation 0
            "000951",  # 中国重汽 roi 9.99 rate 1.15 roe 18.41 pe 4.72 pb 3.43 dividend 5.5 1.48%  operation 0
            "000568",  # 泸州老窖 roi 9.57 rate 1.28 roe 26.05 pe 2.87 pb 7.99 dividend 15.9 1.38%  operation 0
            "600511",  # 国药股份 roi 9.08 rate 1.08 roe 16.48 pe 5.1 pb 2.82 dividend 6.38 1.59%  operation 0
            "000538",  # 云南白药 roi 8.52 rate 1.38 roe 18.16 pe 3.4 pb 3.47 dividend 30.0 2.82%  operation 0
            "600062",  # 华润双鹤 roi 8.44 rate 1.0 roe 12.25 pe 6.89 pb 1.64 dividend 3.04 2.18%  operation 0
            "600519",  # 贵州茅台 roi 8.35 rate 1.14 roe 34.72 pe 2.11 pb 13.67 dividend 170.25 1.05%  operation 0
            "600309",  # 万华化学 roi 8.16 rate 0.88 roe 21.26 pe 4.36 pb 4.57 dividend 13.0 2.04%  operation 0
            "000858",  # 五 粮 液 roi 7.82 rate 1.25 roe 26.63 pe 2.35 pb 9.66 dividend 22.0 1.08%  operation 0
            "600809",  # 山西汾酒 roi 7.17 rate 1.4 roe 31.99 pe 1.6 pb 16.46 dividend 9.0 0.55%  operation 0
            "601607",  # 上海医药 roi 6.96 rate 1.0 roe 9.96 pe 6.99 pb 1.34 dividend 4.4 2.19%  operation 0
            "600900",  # 长江电力 roi 6.8 rate 0.92 roe 14.4 pe 5.13 pb 2.69 dividend 6.8 3.67%  operation 0
            "600897",  # 厦门空港 roi 6.61 rate 0.79 roe 10.83 pe 7.73 pb 1.39 dividend 5.23 2.99%  operation 0
            "000028",  # 国药一致 roi 6.43 rate 1.0 roe 10.24 pe 6.28 pb 1.49 dividend 6.0 1.32%  operation 0
            "002304",  # 洋河股份 roi 6.01 rate 0.85 roe 19.47 pe 3.63 pb 5.07 dividend 30.0 2.23%  operation 0
            "600548",  # 深高速 roi 5.73 rate 0.54 roe 10.64 pe 9.98 pb 1.04 dividend 5.2 5.96%  operation 0
            "600887",  # 伊利股份 roi 5.45 rate 0.88 roe 22.03 pe 2.81 pb 7.66 dividend 8.1 2.39%  operation 0
            "000596",  # 古井贡酒 roi 5.15 rate 1.03 roe 23.27 pe 2.15 pb 9.49 dividend 15.0 0.83%  operation 0
            "600377",  # 宁沪高速 roi 4.99 rate 0.71 roe 11.24 pe 6.25 pb 1.8 dividend 4.6 4.62%  operation 0
            "600332",  # 白云山 roi 4.95 rate 0.75 roe 12.84 pe 5.14 pb 2.28 dividend 5.89 1.66%  operation 0
            "600741",  # 华域汽车 roi 4.88 rate 0.68 roe 9.98 pe 7.19 pb 1.35 dividend 8.5 4.05%  operation 0
            "000999",  # 华润三九 roi 4.34 rate 0.68 roe 12.33 pe 5.18 pb 2.18 dividend 4.3 1.47%  operation 0
            "603288",  # 海天味业 roi 4.11 rate 1.18 roe 29.79 pe 1.17 pb 21.52 dividend 10.8 0.74%  operation 0
            "600660",  # 福耀玻璃 roi 3.97 rate 0.66 roe 13.28 pe 4.53 pb 2.78 dividend 7.5 3.1%  operation 0
            "600436",  # 片仔癀 roi 3.82 rate 1.18 roe 26.1 pe 1.24 pb 16.39 dividend 8.2 0.43%  operation 0
            "600104",  # 上汽集团 roi 3.49 rate 0.53 roe 7.52 pe 8.75 pb 0.85 dividend 8.8 4.87%  operation 0
            "600276",  # 恒瑞医药 roi 3.05 rate 1.27 roe 22.24 pe 1.08 pb 16.15 dividend 2.3 0.24%  operation 0
            "600009",  # 上海机场 roi 2.92 rate 0.81 roe 12.55 pe 2.87 pb 4.03 dividend 7.9 1.18%  operation 0
            "600197",  # 伊力特 roi 2.74 rate 0.67 roe 11.8 pe 3.46 pb 3.3 dividend 4.38 2.15%  operation 0
            "000513",  # 丽珠集团 roi 2.71 rate 1.16 roe 9.07 pe 2.58 pb 4.35 dividend 11.5 2.13%  operation 0
            "000661",  # 长春高新 roi 2.65 rate 1.68 roe 14.86 pe 1.06 pb 10.66 dividend 10.0 0.22%  operation 0
            "600030",  # 中信证券 roi 2.57 rate 1.1 roe 7.15 pe 3.27 pb 2.08 dividend 5.0 1.75%  operation 0
            "600056",  # 中国医药 roi 2.54 rate 0.55 roe 9.44 pe 4.9 pb 1.84 dividend 2.76 1.73%  operation 0
            "000429",  # 粤高速Ａ roi 2.35 rate 0.49 roe 8.32 pe 5.77 pb 1.5 dividend 4.22 6.1%  operation 0
            "601888",  # 中国中免 roi 0.35 rate 0.52 roe 11.91 pe 0.57 pb 19.64 dividend 7.2 0.36%  operation 0

            "002146",  # 荣盛发展 roi 68.96 rate 1.19 roe 26.73 pe 25.8 pb 0.86 dividend 4.8 5.84%  operation 0
            "600340",  # 华夏幸福 roi 64.11 rate 1.17 roe 29.96 pe 21.4 pb 1.1 dividend 15.0 8.65%  operation 0
            "600466",  # 蓝光发展 roi 59.68 rate 1.44 roe 27.86 pe 21.42 pb 1.02 dividend 2.87 5.36%  operation 0
            "000672",  # 上峰水泥 roi 56.85 rate 1.39 roe 60.54 pe 9.39 pb 4.26 dividend 9.0 2.98%  operation 0
            "600153",  # 建发股份 roi 43.72 rate 1.26 roe 20.38 pe 21.45 pb 0.82 dividend 5.0 5.33%  operation 0
            "000069",  # 华侨城Ａ roi 39.76 rate 1.12 roe 19.52 pe 20.37 pb 0.87 dividend 3.05 4.25%  operation 0
            "600048",  # 保利地产 roi 35.71 rate 1.45 roe 23.73 pe 15.05 pb 1.29 dividend 8.2 5.26%  operation 0
            "601668",  # 中国建筑 roi 33.84 rate 1.04 roe 17.6 pe 19.23 pb 0.8 dividend 1.85 3.68%  operation 0
            "600383",  # 金地集团 roi 32.26 rate 1.16 roe 20.64 pe 15.63 pb 1.2 dividend 6.7 4.79%  operation 0
            "600068",  # 葛洲坝 roi 31.36 rate 1.12 roe 18.7 pe 16.77 pb 1.01 dividend 1.56 2.34%  operation 0
            "600846",  # 同济科技 roi 31.05 rate 2.29 roe 27.0 pe 11.5 pb 1.91 dividend 3.4 3.89%  operation 0
            "000002",  # 万 科Ａ roi 29.42 rate 1.15 roe 23.52 pe 12.51 pb 1.61 dividend 10.17 3.79%  operation 0
            "600668",  # 尖峰集团 roi 27.5 rate 1.21 roe 22.27 pe 12.35 pb 1.51 dividend 3.0 1.75%  operation 0
            "600585",  # 海螺水泥 roi 27.18 rate 1.04 roe 27.29 pe 9.96 pb 2.29 dividend 20.0 3.26%  operation 0
            "600606",  # 绿地控股 roi 27.16 rate 1.14 roe 19.29 pe 14.08 pb 1.29 dividend 4.0 4.9%  operation 0
            "601328",  # 交通银行 roi 25.9 rate 1.04 roe 11.79 pe 21.97 pb 0.5 dividend 3.15 6.62%  operation 0
            "601009",  # 南京银行 roi 25.23 rate 1.12 roe 15.21 pe 16.59 pb 0.81 dividend 3.92 5.05%  operation 0
            "601288",  # 农业银行 roi 24.75 rate 1.05 roe 13.01 pe 19.02 pb 0.62 dividend 1.82 5.63%  operation 0
            "600755",  # 厦门国贸 roi 24.69 rate 0.83 roe 15.58 pe 15.85 pb 0.93 dividend 2.3 3.3%  operation 0
            "601939",  # 建设银行 roi 24.27 rate 1.05 roe 13.72 pe 17.69 pb 0.7 dividend 3.2 5.23%  operation 0
            "601398",  # 工商银行 roi 24.07 rate 1.05 roe 13.52 pe 17.8 pb 0.69 dividend 2.63 5.3%  operation 0
            "600352",  # 浙江龙盛 roi 23.57 rate 1.13 roe 22.95 pe 10.27 pb 1.88 dividend 2.5 1.69%  operation 0
            "601988",  # 中国银行 roi 23.31 rate 1.04 roe 12.09 pe 19.28 pb 0.57 dividend 1.91 5.74%  operation 0
            "600801",  # 华新水泥 roi 22.7 rate 1.0 roe 22.93 pe 9.9 pb 2.67 dividend 12.1 4.42%  operation 0
            "601336",  # 新华保险 roi 20.76 rate 1.82 roe 21.63 pe 9.6 pb 1.88 dividend 14.1 2.67%  operation 0
            "601318",  # 中国平安 roi 20.32 rate 1.02 roe 21.69 pe 9.37 pb 2.01 dividend 13.0 1.71%  operation 0
            "600036",  # 招商银行 roi 19.5 rate 1.15 roe 17.94 pe 10.87 pb 1.44 dividend 12.0 3.45%  operation 0
            "601601",  # 中国太保 roi 19.23 rate 1.55 roe 17.81 pe 10.8 pb 1.44 dividend 12.0 4.07%  operation 0
            "601088",  # 中国神华 roi 15.76 rate 0.9 roe 11.88 pe 13.27 pb 0.84 dividend 12.6 8.22%  operation 0
            "601006",  # 大秦铁路 roi 14.05 rate 0.85 roe 11.08 pe 12.68 pb 0.83 dividend 4.8 7.4%  operation 0
            "000651",  # 格力电器 roi 13.23 rate 0.78 roe 22.02 pe 6.01 pb 3.03 dividend 12.0 2.11%  operation 0
            "600663",  # 陆家嘴 roi 13.09 rate 0.93 roe 20.07 pe 6.52 pb 2.83 dividend 4.56 3.63%  operation 0
            "000828",  # 东莞控股 roi 12.65 rate 0.83 roe 13.57 pe 9.32 pb 1.33 dividend 3.0 3.19%  operation 0
            "000581",  # 威孚高科 roi 12.27 rate 0.93 roe 12.82 pe 9.57 pb 1.29 dividend 11.0 4.99%  operation 0
            "000895",  # 双汇发展 roi 12.15 rate 1.1 roe 39.18 pe 3.1 pb 10.1 dividend 10.0 1.83%  operation 0
            "600486",  # 扬农化工 roi 11.27 rate 1.36 roe 25.97 pe 4.34 pb 5.39 dividend 6.5 0.68%  operation 0
            "000333",  # 美的集团 roi 10.93 rate 1.08 roe 24.03 pe 4.55 pb 4.74 dividend 16.0 2.23%  operation 0
            "600690",  # 海尔智家 roi 10.37 rate 0.94 roe 17.2 pe 6.03 pb 2.46 dividend 3.75 2.08%  operation 0
            "000049",  # 德赛电池 roi 10.37 rate 1.22 roe 26.25 pe 3.95 pb 5.42 dividend 7.0 1.19%  operation 0
            "600548",  # 深高速 roi 10.33 rate 0.54 roe 10.64 pe 9.71 pb 1.07 dividend 5.2 5.8%  operation 0
            "600612",  # 老凤祥 roi 9.38 rate 1.13 roe 21.42 pe 4.38 pb 4.34 dividend 11.5 1.88%  operation 0
            "600007",  # 中国国贸 roi 9.07 rate 1.14 roe 13.0 pe 6.98 pb 1.72 dividend 3.8 2.87%  operation 0
            "000951",  # 中国重汽 roi 8.82 rate 1.15 roe 18.41 pe 4.79 pb 3.39 dividend 5.5 1.5%  operation 0
            "600309",  # 万华化学 roi 8.72 rate 0.88 roe 21.26 pe 4.1 pb 4.86 dividend 13.0 1.92%  operation 0
            "600897",  # 厦门空港 roi 8.24 rate 0.79 roe 10.83 pe 7.61 pb 1.42 dividend 5.23 2.94%  operation 0
            "600062",  # 华润双鹤 roi 8.08 rate 1.0 roe 12.25 pe 6.6 pb 1.71 dividend 3.04 2.09%  operation 0
            "600519",  # 贵州茅台 roi 7.95 rate 1.11 roe 38.22 pe 2.08 pb 15.36 dividend 170.25 1.01%  operation 0
            "600511",  # 国药股份 roi 7.7 rate 1.08 roe 16.48 pe 4.67 pb 3.08 dividend 6.38 1.45%  operation 0
            "600900",  # 长江电力 roi 7.46 rate 0.92 roe 14.4 pe 5.18 pb 2.66 dividend 6.8 3.7%  operation 0
            "000568",  # 泸州老窖 roi 7.29 rate 1.28 roe 26.05 pe 2.8 pb 8.2 dividend 15.9 1.35%  operation 0
            "600741",  # 华域汽车 roi 7.17 rate 0.68 roe 9.98 pe 7.18 pb 1.35 dividend 8.5 4.05%  operation 0
            "600377",  # 宁沪高速 roi 7.13 rate 0.71 roe 11.24 pe 6.34 pb 1.78 dividend 4.6 4.69%  operation 0
            "002304",  # 洋河股份 roi 7.05 rate 0.85 roe 19.47 pe 3.62 pb 5.09 dividend 30.0 2.22%  operation 0
            "601607",  # 上海医药 roi 6.82 rate 1.0 roe 9.96 pe 6.85 pb 1.37 dividend 4.4 2.15%  operation 0
            "601628",  # 中国人寿 roi 6.62 rate 2.06 roe 13.84 pe 4.78 pb 2.54 dividend 7.3 2.0%  operation 0
            "600104",  # 上汽集团 roi 6.54 rate 0.53 roe 7.52 pe 8.7 pb 0.85 dividend 8.8 4.84%  operation 0
            "600019",  # 宝钢股份 roi 6.44 rate 0.58 roe 6.28 pe 10.25 pb 0.61 dividend 2.8 5.69%  operation 0
            "600332",  # 白云山 roi 6.3 rate 0.75 roe 12.84 pe 4.91 pb 2.38 dividend 5.89 1.59%  operation 0
            "000999",  # 华润三九 roi 6.15 rate 0.68 roe 12.33 pe 4.99 pb 2.26 dividend 4.3 1.42%  operation 0
            "000538",  # 云南白药 roi 5.99 rate 1.38 roe 18.16 pe 3.3 pb 3.57 dividend 30.0 2.74%  operation 0
            "600660",  # 福耀玻璃 roi 5.98 rate 0.66 roe 13.28 pe 4.5 pb 2.8 dividend 7.5 3.07%  operation 0
            "000858",  # 五 粮 液 roi 5.89 rate 1.25 roe 26.63 pe 2.21 pb 10.3 dividend 22.0 1.01%  operation 0
            "000028",  # 国药一致 roi 5.87 rate 1.0 roe 10.24 pe 5.73 pb 1.63 dividend 6.0 1.21%  operation 0
            "600887",  # 伊利股份 roi 5.73 rate 0.88 roe 22.03 pe 2.6 pb 8.28 dividend 8.1 2.21%  operation 0
            "600350",  # 山东高速 roi 4.94 rate 0.69 roe 7.59 pe 6.51 pb 1.09 dividend 3.8 5.63%  operation 0
            "600809",  # 山西汾酒 roi 4.64 rate 1.4 roe 31.99 pe 1.45 pb 18.11 dividend 9.0 0.5%  operation 0
            "000429",  # 粤高速Ａ roi 4.61 rate 0.49 roe 8.32 pe 5.54 pb 1.57 dividend 4.22 5.85%  operation 0
            "600056",  # 中国医药 roi 4.54 rate 0.55 roe 9.44 pe 4.81 pb 1.88 dividend 2.76 1.7%  operation 0
            "600197",  # 伊力特 roi 4.24 rate 0.67 roe 11.8 pe 3.59 pb 3.17 dividend 4.38 2.24%  operation 0
            "000596",  # 古井贡酒 roi 4.24 rate 1.03 roe 23.27 pe 1.82 pb 11.19 dividend 15.0 0.7%  operation 0
            "600009",  # 上海机场 roi 3.56 rate 0.81 roe 12.55 pe 2.84 pb 4.08 dividend 7.9 1.16%  operation 0
            "603288",  # 海天味业 roi 3.37 rate 1.18 roe 29.79 pe 1.13 pb 22.27 dividend 10.8 0.72%  operation 0
            "600436",  # 片仔癀 roi 3.05 rate 1.18 roe 26.1 pe 1.17 pb 17.44 dividend 8.2 0.4%  operation 0
            "600276",  # 恒瑞医药 roi 2.37 rate 1.22 roe 21.35 pe 1.11 pb 18.87 dividend 2.3 0.24%  operation 0
            "000513",  # 丽珠集团 roi 2.32 rate 1.16 roe 9.07 pe 2.56 pb 4.39 dividend 11.5 2.11%  operation 0
            "600030",  # 中信证券 roi 2.22 rate 1.1 roe 7.15 pe 3.11 pb 2.18 dividend 5.0 1.67%  operation 0
            "600028",  # 中国石化 roi 1.49 rate 0.39 roe 3.12 pe 4.76 pb 0.68 dividend 1.9 4.75%  operation 0
            "000661",  # 长春高新 roi 1.44 rate 1.68 roe 14.86 pe 0.97 pb 11.66 dividend 10.0 0.2%  operation 0
            "601888",  # 中国中免 roi 0.55 rate 0.52 roe 11.91 pe 0.46 pb 23.9 dividend 7.2 0.3%  operation 0
            "000039",  # 中集集团 roi 0.2 rate 0.15 roe 1.18 pe 1.66 pb 0.86 dividend 1.2 1.44%  operation 0

            "600048",  # 保利地产 roi 51.23 rate 1.45 roe 23.73 pe 14.89 pb 1.3 dividend 8.2 5.2%  operation 0
            "000069",  # 华侨城Ａ roi 43.68 rate 1.12 roe 19.52 pe 19.98 pb 0.89 dividend 3.05 4.17%  operation 0
            "600383",  # 金地集团 roi 37.4 rate 1.16 roe 20.64 pe 15.62 pb 1.2 dividend 6.7 4.79%  operation 0
            "600068",  # XD葛洲坝 roi 36.25 rate 1.12 roe 18.7 pe 17.31 pb 0.97 dividend 1.56 2.41%  operation 0
            "601668",  # 中国建筑 roi 34.65 rate 1.04 roe 17.6 pe 18.93 pb 0.82 dividend 1.85 3.62%  operation 0
            "600668",  # 尖峰集团 roi 33.74 rate 1.21 roe 22.27 pe 12.52 pb 1.49 dividend 3.0 1.77%  operation 0
            "000002",  # 万 科Ａ roi 33.59 rate 1.15 roe 23.52 pe 12.42 pb 1.62 dividend 10.17 3.76%  operation 0
            "600606",  # 绿地控股 roi 32.26 rate 1.14 roe 19.29 pe 14.67 pb 1.24 dividend 4.0 5.1%  operation 0
            "601601",  # 中国太保 roi 29.32 rate 1.55 roe 17.81 pe 10.62 pb 1.46 dividend 12.0 4.0%  operation 0
            "600036",  # 招商银行 roi 21.31 rate 1.15 roe 17.94 pe 10.33 pb 1.52 dividend 12.0 3.28%  operation 0
            "600755",  # 厦门国贸 roi 20.73 rate 0.83 roe 15.58 pe 16.03 pb 0.92 dividend 2.3 3.34%  operation 0

            "600846",  # 同济科技 roi 432.43 rate 3.29 roe 58.21 pe 22.58 pb 2.03 dividend 3.4 3.55%  operation 0
            "002244",  # 滨江集团 roi 141.02 rate 1.64 roe 29.55 pe 29.1 pb 0.94 dividend 1.32 2.58%  operation 0
            "600153",  # 建发股份 roi 132.32 rate 1.17 roe 33.85 pe 33.41 pb 0.87 dividend 5.0 5.09%  operation 0
            "601668",  # 中国建筑 roi 86.3 rate 1.07 roe 27.5 pe 29.33 pb 0.81 dividend 1.85 3.56%  operation 0
            "002146",  # 荣盛发展 roi 84.01 rate 1.14 roe 27.61 pe 26.69 pb 0.87 dividend 4.8 5.8%  operation 0
            "600048",  # 保利地产 roi 77.61 rate 1.27 roe 31.68 pe 19.29 pb 1.38 dividend 8.2 4.98%  operation 0
            "600383",  # 金地集团 roi 75.3 rate 1.06 roe 31.84 pe 22.31 pb 1.33 dividend 6.7 4.48%  operation 0
            "600606",  # 绿地控股 roi 63.81 rate 1.07 roe 28.01 pe 21.29 pb 1.27 dividend 4.0 5.08%  operation 0
            "000069",  # 华侨城Ａ roi 57.87 rate 1.13 roe 22.52 pe 22.74 pb 0.89 dividend 3.05 4.22%  operation 0
            "000002",  # 万 科Ａ roi 55.42 rate 0.99 roe 32.91 pe 17.01 pb 1.64 dividend 10.17 3.69%  operation 0
            "600340",  # 华夏幸福 roi 44.47 rate 0.94 roe 24.98 pe 18.94 pb 1.11 dividend 15.0 8.78%  operation 0
            "600755",  # 厦门国贸 roi 43.49 rate 1.04 roe 20.97 pe 19.94 pb 0.95 dividend 2.3 3.18%  operation 0
            "600585",  # 海螺水泥 roi 34.13 rate 1.07 roe 29.7 pe 10.74 pb 2.3 dividend 20.0 3.22%  operation 0
            "600663",  # 陆家嘴 roi 29.83 rate 1.1 roe 28.88 pe 9.39 pb 2.83 dividend 4.56 3.63%  operation 0
            "600068",  # 葛洲坝 roi 26.25 rate 0.83 roe 18.02 pe 17.55 pb 0.93 dividend 1.56 2.43%  operation 0
            "000049",  # 德赛电池 roi 23.64 rate 1.15 roe 35.94 pe 5.72 pb 5.28 dividend 7.0 1.23%  operation 0
            "000951",  # 中国重汽 roi 21.52 rate 1.19 roe 26.55 pe 6.81 pb 3.4 dividend 5.5 1.48%  operation 0
            "000895",  # 双汇发展 roi 16.67 roe 46.2 pe 2.91 pb 13.69 dividend 10.0 1.53%  operation 0
            "600519",  # 贵州茅台 roi 9.58 roe 40.7 pe 2.12 pb 16.08 dividend 170.25 0.97%  operation 0

            "600846",  # 同济科技 roi 432.43 rate 3.29 roe 58.21 pe 22.58 pb 2.03 dividend 3.4 3.55%  operation 0
            "002244",  # 滨江集团 roi 141.02 rate 1.64 roe 29.55 pe 29.1 pb 0.94 dividend 1.32 2.58%  operation 0
            "600153",  # 建发股份 roi 132.32 rate 1.17 roe 33.85 pe 33.41 pb 0.87 dividend 5.0 5.09%  operation 0
            "600466",  # 蓝光发展 roi 104.4 rate 1.23 roe 33.43 pe 25.39 pb 1.04 dividend 2.87 5.31%  operation 0
            "601668",  # 中国建筑 roi 86.3 rate 1.07 roe 27.5 pe 29.33 pb 0.81 dividend 1.85 3.56%  operation 0
            "002146",  # 荣盛发展 roi 84.01 rate 1.14 roe 27.61 pe 26.69 pb 0.87 dividend 4.8 5.8%  operation 0
            "000672",  # 上峰水泥 roi 79.69 rate 1.25 roe 60.37 pe 10.56 pb 4.01 dividend 9.0 3.19%  operation 0
            "600048",  # 保利地产 roi 77.61 rate 1.27 roe 31.68 pe 19.29 pb 1.38 dividend 8.2 4.98%  operation 0
            "600383",  # 金地集团 roi 75.3 rate 1.06 roe 31.84 pe 22.31 pb 1.33 dividend 6.7 4.48%  operation 0
            "600606",  # 绿地控股 roi 63.81 rate 1.07 roe 28.01 pe 21.29 pb 1.27 dividend 4.0 5.08%  operation 0
            "000069",  # 华侨城Ａ roi 57.87 rate 1.13 roe 22.52 pe 22.74 pb 0.89 dividend 3.05 4.22%  operation 0
            "000002",  # 万 科Ａ roi 55.42 rate 0.99 roe 32.91 pe 17.01 pb 1.64 dividend 10.17 3.69%  operation 0
            "600340",  # 华夏幸福 roi 44.47 rate 0.94 roe 24.98 pe 18.94 pb 1.11 dividend 15.0 8.78%  operation 0
            "600755",  # 厦门国贸 roi 43.49 rate 1.04 roe 20.97 pe 19.94 pb 0.95 dividend 2.3 3.18%  operation 0
            "600585",  # 海螺水泥 roi 34.13 rate 1.07 roe 29.7 pe 10.74 pb 2.3 dividend 20.0 3.22%  operation 0
            "600663",  # 陆家嘴 roi 29.83 rate 1.1 roe 28.88 pe 9.39 pb 2.83 dividend 4.56 3.63%  operation 0
            "600801",  # 华新水泥 roi 29.41 rate 0.86 roe 32.98 pe 10.37 pb 2.77 dividend 12.1 4.4%  operation 0
            "601988",  # 中国银行 roi 28.33 rate 1.04 roe 13.01 pe 20.94 pb 0.57 dividend 1.91 5.79%  operation 0
            "600068",  # 葛洲坝 roi 26.25 rate 0.83 roe 18.02 pe 17.55 pb 0.93 dividend 1.56 2.43%  operation 0
            "601288",  # 农业银行 roi 26.02 rate 1.05 roe 13.02 pe 19.03 pb 0.62 dividend 1.82 5.63%  operation 0
            "600352",  # 浙江龙盛 roi 25.84 rate 1.06 roe 22.76 pe 10.71 pb 1.77 dividend 2.5 1.73%  operation 0
            "601939",  # 建设银行 roi 25.42 rate 1.05 roe 13.8 pe 17.54 pb 0.71 dividend 3.2 5.15%  operation 0
            "601398",  # 工商银行 roi 24.98 rate 1.04 roe 13.56 pe 17.71 pb 0.7 dividend 2.63 5.26%  operation 0
            "000049",  # 德赛电池 roi 23.64 rate 1.15 roe 35.94 pe 5.72 pb 5.28 dividend 7.0 1.23%  operation 0
            "601009",  # 南京银行 roi 23.45 rate 1.07 roe 15.23 pe 14.39 pb 0.98 dividend 3.92 4.38%  operation 0
            "000951",  # 中国重汽 roi 21.52 rate 1.19 roe 26.55 pe 6.81 pb 3.4 dividend 5.5 1.48%  operation 0
            "601328",  # 交通银行 roi 20.89 rate 0.94 roe 10.95 pe 20.3 pb 0.5 dividend 3.15 6.6%  operation 0
            "600668",  # 尖峰集团 roi 18.41 rate 0.8 roe 19.35 pe 11.89 pb 1.41 dividend 3.0 1.8%  operation 0
            "601088",  # 中国神华 roi 18.37 rate 0.86 roe 14.18 pe 15.06 pb 0.91 dividend 12.6 7.95%  operation 0
            "600612",  # 老凤祥 roi 18.12 rate 1.08 roe 26.26 pe 6.39 pb 3.67 dividend 11.5 2.11%  operation 0
            "600486",  # XD扬农化 roi 18.06 rate 1.4 roe 27.44 pe 4.7 pb 5.23 dividend 6.5 0.69%  operation 0
            "600036",  # 招商银行 roi 17.73 rate 1.07 roe 17.35 pe 9.55 pb 1.62 dividend 12.0 3.12%  operation 0
            "601318",  # 中国平安 roi 16.88 rate 0.83 roe 21.52 pe 9.45 pb 2.03 dividend 21.0 2.7%  operation 0
            "000895",  # 双汇发展 roi 16.67 rate 1.24 roe 46.2 pe 2.91 pb 13.69 dividend 10.0 1.53%  operation 0
            "000581",  # 威孚高科 roi 15.0 rate 1.1 roe 14.84 pe 9.19 pb 1.53 dividend 11.0 4.3%  operation 0
            "600690",  # 海尔智家 roi 14.03 rate 0.97 roe 22.78 pe 6.35 pb 3.19 dividend 3.75 1.61%  operation 0
            "601601",  # 中国太保 roi 13.34 rate 1.0 roe 15.31 pe 8.71 pb 1.53 dividend 12.0 3.81%  operation 0
            "000333",  # 美的集团 roi 12.26 rate 1.04 roe 24.71 pe 4.77 pb 4.64 dividend 16.0 2.28%  operation 0
            "601006",  # 大秦铁路 roi 11.19 rate 0.75 roe 11.67 pe 12.78 pb 0.87 dividend 4.8 7.27%  operation 0
            "000651",  # 格力电器 roi 10.8 rate 0.78 roe 22.15 pe 6.25 pb 2.93 dividend 12.0 2.18%  operation 0
            "600104",  # 上汽集团 roi 10.41 rate 0.7 roe 11.78 pe 12.63 pb 0.9 dividend 8.8 4.65%  operation 0
            "601607",  # 上海医药 roi 10.3 rate 1.04 roe 12.38 pe 8.0 pb 1.44 dividend 4.4 2.02%  operation 0
            "601336",  # 新华保险 roi 9.85 rate 0.97 roe 15.97 pe 6.36 pb 2.11 dividend 14.1 2.29%  operation 0
            "600519",  # 贵州茅台 roi 9.58 rate 1.11 roe 40.7 pe 2.12 pb 16.08 dividend 170.25 0.97%  operation 0
            "601628",  # 中国人寿 roi 9.35 rate 1.57 roe 14.46 pe 4.12 pb 3.1 dividend 7.3 1.63%  operation 0
            "000028",  # 国药一致 roi 8.73 rate 1.07 roe 12.54 pe 6.51 pb 1.77 dividend 6.0 1.1%  operation 0
            "600056",  # 中国医药 roi 8.59 rate 0.77 roe 14.82 pe 7.53 pb 1.8 dividend 2.76 1.73%  operation 0
            "600007",  # 中国国贸 roi 8.42 rate 1.04 roe 12.59 pe 6.43 pb 1.83 dividend 3.8 2.76%  operation 0
            "600511",  # 国药股份 roi 8.07 rate 0.96 roe 17.48 pe 4.81 pb 3.25 dividend 6.38 1.39%  operation 0
            "000568",  # 泸州老窖 roi 7.98 rate 1.2 roe 29.03 pe 2.29 pb 10.93 dividend 15.9 1.05%  operation 0
            "000513",  # 丽珠集团 roi 7.91 rate 1.46 roe 14.18 pe 3.82 pb 4.61 dividend 11.5 2.12%  operation 0
            "600062",  # 华润双鹤 roi 7.84 rate 0.95 roe 11.98 pe 6.89 pb 1.61 dividend 3.04 2.23%  operation 0
            "600887",  # 伊利股份 roi 7.78 rate 1.02 roe 27.25 pe 2.8 pb 9.65 dividend 8.1 2.0%  operation 0
            "000858",  # 五 粮 液 roi 7.67 rate 1.21 roe 29.89 pe 2.12 pb 12.19 dividend 22.0 0.91%  operation 0
            "600809",  # 山西汾酒 roi 6.77 rate 1.32 roe 35.87 pe 1.43 pb 20.35 dividend 9.0 0.47%  operation 0
            "000828",  # 东莞控股 roi 6.7 rate 0.73 roe 12.55 pe 7.31 pb 1.59 dividend 3.0 2.71%  operation 0
            "600197",  # 伊力特 roi 6.66 rate 0.95 roe 16.54 pe 4.24 pb 3.6 dividend 4.38 2.02%  operation 0
            "600900",  # 长江电力 roi 6.65 rate 0.92 roe 14.42 pe 5.01 pb 2.75 dividend 6.8 3.58%  operation 0
            "600741",  # 华域汽车 roi 6.14 rate 0.67 roe 12.64 pe 7.25 pb 1.66 dividend 8.5 3.36%  operation 0
            "002304",  # 洋河股份 roi 5.8 rate 0.83 roe 20.75 pe 3.37 pb 5.81 dividend 30.0 2.12%  operation 0
            "600309",  # 万华化学 roi 5.0 rate 0.74 roe 20.41 pe 3.31 pb 5.67 dividend 13.0 1.74%  operation 0
            "000661",  # 长春高新 roi 4.81 rate 1.65 roe 19.69 pe 1.48 pb 20.39 dividend 10.0 0.22%  operation 0
            "600030",  # 中信证券 roi 4.78 rate 1.42 roe 9.14 pe 3.68 pb 2.35 dividend 5.0 1.56%  operation 0
            "600332",  # 白云山 roi 4.2 rate 0.75 roe 11.25 pe 4.98 pb 2.13 dividend 5.89 1.8%  operation 0
            "603288",  # 海天味业 roi 4.19 rate 1.2 roe 34.94 pe 1.0 pb 34.65 dividend 10.8 0.6%  operation 0
            "000999",  # 华润三九 roi 4.06 rate 0.63 roe 12.17 pe 5.3 pb 2.12 dividend 4.3 1.51%  operation 0
            "600019",  # 宝钢股份 roi 3.94 rate 0.59 roe 6.57 pe 10.16 pb 0.63 dividend 2.8 5.62%  operation 0
            "000538",  # 云南白药 roi 3.34 rate 1.12 roe 9.98 pe 2.99 pb 4.03 dividend 30.0 2.62%  operation 0
            "600436",  # 片仔癀 roi 3.22 rate 1.18 roe 25.74 pe 1.06 pb 20.37 dividend 8.2 0.35%  operation 0
            "000596",  # 古井贡酒 roi 2.92 rate 0.9 roe 23.34 pe 1.39 pb 14.76 dividend 15.0 0.56%  operation 0
            "600276",  # 恒瑞医药 roi 2.88 rate 1.23 roe 21.31 pe 1.1 pb 19.07 dividend 2.3 0.24%  operation 0
            "600350",  # 山东高速 roi 2.78 rate 0.8 roe 6.26 pe 5.56 pb 1.16 dividend 3.8 5.85%  operation 0
            "600377",  # 宁沪高速 roi 2.67 rate 0.57 roe 9.2 pe 5.09 pb 1.86 dividend 4.6 4.81%  operation 0
            "600660",  # 福耀玻璃 roi 2.45 rate 0.63 roe 11.84 pe 3.28 pb 3.5 dividend 7.5 2.62%  operation 0
            "600897",  # 厦门空港 roi 2.35 rate 0.54 roe 8.25 pe 5.27 pb 1.52 dividend 5.23 2.86%  operation 0
            "600028",  # 中国石化 roi 1.3 rate 0.44 roe 4.41 pe 6.69 pb 0.68 dividend 1.9 4.71%  operation 0
            "000039",  # 中集集团 roi 1.07 rate 0.43 roe 4.86 pe 5.13 pb 0.94 dividend 1.2 1.34%  operation 0
            "000429",  # 粤高速Ａ roi 0.97 rate 0.34 roe 6.76 pe 4.21 pb 1.68 dividend 4.22 5.98%  operation 0
            "600009",  # 上海机场 roi 0.4 rate 0.41 roe 7.12 pe 1.38 pb 5.09 dividend 7.9 0.99%  operation 0
            "600548",  # 深高速 roi 0.37 rate 0.19 roe 4.68 pe 4.14 pb 1.13 dividend 5.2 5.77%  operation 0
            "601888",  # 中国中免 roi 0.29 rate 0.43 roe 12.64 pe 0.54 pb 24.37 dividend 7.2 0.33%  operation 0
            "600004",  # 白云机场
            "000089",  # 深圳机场

            "600383",  # 金地集团 roi 112.03 rate 1.28 roe 33.14 pe 26.41 pb 1.17 dividend 6.7 4.92%  operation 0
            "600606",  # 绿地控股 roi 90.92 rate 1.08 roe 29.17 pe 28.86 pb 0.94 dividend 4.0 6.4%  operation 0
            "601668",  # 中国建筑 roi 87.65 rate 1.07 roe 27.16 pe 30.16 pb 0.78 dividend 1.85 3.54%  operation 0
            "600048",  # 保利地产 roi 82.01 rate 1.27 roe 31.33 pe 20.61 pb 1.28 dividend 8.2 5.28%  operation 0
            "000002",  # 万 科Ａ roi 57.52 rate 1.01 roe 32.92 pe 17.3 pb 1.61 dividend 10.17 3.61%  operation 0
            "000951",  # 中国重汽 roi 49.17 rate 1.67 roe 34.08 pe 8.64 pb 3.28 dividend 5.5 1.42%  operation 0
            "000069",  # 华侨城Ａ roi 48.9 rate 1.02 roe 20.79 pe 23.06 pb 0.8 dividend 3.05 4.45%  operation 0
            "600755",  # 厦门国贸 roi 47.36 rate 1.09 roe 20.34 pe 21.36 pb 0.87 dividend 2.3 3.4%  operation 0
            "600585",  # 海螺水泥 roi 35.98 rate 1.05 roe 27.86 pe 12.3 pb 1.91 dividend 20.0 3.67%  operation 0
            "600663",  # 陆家嘴 roi 31.69 rate 1.05 roe 28.58 pe 10.56 pb 2.47 dividend 4.56 4.01%  operation 0
            "600068",  # 葛洲坝 roi 30.93 rate 0.89 roe 19.79 pe 17.56 pb 1.01 dividend 1.56 2.2%  operation 0
            "000581",  # 威孚高科 roi 24.12 rate 1.33 roe 17.14 pe 10.58 pb 1.5 dividend 11.0 4.17%  operation 0
            "600612",  # 老凤祥 roi 22.46 rate 1.06 roe 28.21 pe 7.51 pb 3.33 dividend 11.5 2.36%  operation 0
            "000049",  # 德赛电池 roi 21.16 rate 1.05 roe 31.89 pe 6.32 pb 4.12 dividend 7.0 1.39%  operation 0
            "000895",  # 双汇发展 roi 19.33 rate 1.22 roe 41.58 pe 3.81 pb 7.01 dividend 16.4 3.29%  operation 0
            "600352",  # 浙江龙盛 roi 18.64 rate 0.94 roe 19.16 pe 10.35 pb 1.63 dividend 2.5 1.86%  operation 0
            "601318",  # 中国平安 roi 16.23 rate 0.8 roe 21.45 pe 9.46 pb 2.05 dividend 21.0 2.64%  operation 0
            "000513",  # 丽珠集团 roi 14.56 rate 1.59 roe 19.28 pe 4.75 pb 3.84 dividend 11.5 2.44%  operation 0
            "600056",  # 中国医药 roi 14.5 rate 0.96 roe 16.53 pe 9.14 pb 1.63 dividend 2.76 1.82%  operation 0
            "600036",  # 招商银行 roi 14.4 rate 1.02 roe 16.49 pe 8.56 pb 1.75 dividend 12.0 2.8%  operation 0
            "601607",  # 上海医药 roi 13.01 rate 1.13 roe 12.57 pe 9.16 pb 1.27 dividend 4.4 2.23%  operation 0
            "601319",  # 中国人保 roi 12.82 rate 0.86 roe 15.48 pe 9.63 pb 1.46 dividend 1.52 2.33%  operation 0
            "000333",  # 美的集团 roi 10.67 rate 1.01 roe 25.33 pe 4.17 pb 5.33 dividend 16.0 1.87%  operation 0
            "000028",  # 国药一致 roi 10.33 rate 1.08 roe 12.67 pe 7.55 pb 1.54 dividend 6.0 1.23%  operation 0
            "601336",  # 新华保险 roi 10.31 rate 0.96 roe 15.87 pe 6.77 pb 1.99 dividend 14.1 2.35%  operation 0
            "000828",  # 东莞控股 roi 9.97 rate 0.77 roe 13.02 pe 9.94 pb 1.21 dividend 3.0 3.42%  operation 0
            "601601",  # 中国太保 roi 9.94 rate 0.87 roe 13.91 pe 8.21 pb 1.51 dividend 12.0 3.77%  operation 0
            "600887",  # 伊利股份 roi 9.62 rate 1.04 roe 30.23 pe 3.06 pb 8.45 dividend 8.1 2.05%  operation 0
            "600519",  # 贵州茅台 roi 9.16 rate 1.09 roe 37.85 pe 2.22 pb 14.38 dividend 170.25 1.0%  operation 0
            "600900",  # 长江电力 roi 9.11 rate 1.07 roe 16.04 pe 5.31 pb 2.74 dividend 6.8 3.41%  operation 0
            "600511",  # 国药股份 roi 9.03 rate 0.97 roe 17.37 pe 5.36 pb 2.89 dividend 6.38 1.51%  operation 0
            "600062",  # 华润双鹤 roi 8.77 rate 0.96 roe 12.02 pe 7.6 pb 1.46 dividend 3.04 2.37%  operation 0
            "600104",  # 上汽集团 roi 8.69 rate 0.76 roe 11.78 pe 9.71 pb 1.17 dividend 8.8 3.46%  operation 0
            "600486",  # 扬农化工 roi 8.3 rate 0.95 roe 22.41 pe 3.9 pb 5.0 dividend 6.5 0.7%  operation 0
            "000568",  # 泸州老窖 roi 7.91 rate 1.25 roe 30.26 pe 2.09 pb 12.28 dividend 15.9 0.87%  operation 0
            "000858",  # 五 粮 液 roi 7.15 rate 1.18 roe 29.28 pe 2.07 pb 12.23 dividend 22.0 0.87%  operation 0
            "600007",  # 中国国贸 roi 7.02 rate 0.92 roe 11.54 pe 6.61 pb 1.64 dividend 3.8 2.99%  operation 0
            "600809",  # 山西汾酒 roi 6.83 rate 1.35 roe 37.47 pe 1.35 pb 22.06 dividend 9.0 0.39%  operation 0
            "600690",  # 海尔智家 roi 6.76 rate 0.69 roe 20.0 pe 4.9 pb 3.71 dividend 3.75 1.33%  operation 0
            "000999",  # 华润三九 roi 6.75 rate 0.75 roe 13.96 pe 6.45 pb 1.96 dividend 4.3 1.57%  operation 0
            "000661",  # 长春高新 roi 6.07 rate 1.52 roe 19.96 pe 2.0 pb 15.04 dividend 10.0 0.27%  operation 0
            "600332",  # 白云山 roi 5.96 rate 0.85 roe 11.98 pe 5.85 pb 1.91 dividend 5.89 1.93%  operation 0
            "000538",  # 云南白药 roi 5.93 rate 1.19 roe 13.05 pe 3.82 pb 3.35 dividend 30.0 3.0%  operation 0
            "600741",  # 华域汽车 roi 5.32 rate 0.72 roe 12.77 pe 5.79 pb 2.12 dividend 8.5 2.53%  operation 0
            "002304",  # 洋河股份 roi 5.16 rate 0.9 roe 20.46 pe 2.8 pb 6.95 dividend 30.0 1.7%  operation 0
            "601628",  # 中国人寿 roi 4.97 rate 0.98 roe 12.78 pe 3.97 pb 2.94 dividend 7.3 1.68%  operation 0
            "603288",  # 海天味业 roi 4.69 rate 1.2 roe 33.72 pe 1.16 pb 28.81 dividend 10.8 0.67%  operation 0
            "600309",  # 万华化学 roi 4.6 rate 0.77 roe 19.66 pe 3.04 pb 5.94 dividend 13.0 1.56%  operation 0
            "600197",  # 伊力特 roi 4.49 rate 0.79 roe 14.17 pe 4.01 pb 3.31 dividend 4.38 2.15%  operation 0
            "000651",  # 格力电器 roi 4.28 rate 0.6 roe 16.27 pe 4.38 pb 3.26 dividend 22.0 3.54%  operation 0
            "600030",  # 中信证券 roi 3.99 rate 1.14 roe 8.73 pe 4.01 pb 2.07 dividend 5.0 1.74%  operation 0
            "600436",  # 片仔癀 roi 3.65 rate 1.21 roe 25.78 pe 1.17 pb 18.35 dividend 8.2 0.36%  operation 0
            "000596",  # 古井贡酒 roi 3.38 rate 0.85 roe 22.23 pe 1.79 pb 10.94 dividend 15.0 0.71%  operation 0
            "600276",  # 恒瑞医药 roi 3.06 rate 1.21 roe 20.91 pe 1.21 pb 16.94 dividend 2.3 0.26%  operation 0
            "600377",  # 宁沪高速 roi 3.05 rate 0.59 roe 9.37 pe 5.52 pb 1.7 dividend 4.6 4.94%  operation 0
            "600660",  # 福耀玻璃 roi 1.71 rate 0.71 roe 10.88 pe 2.22 pb 4.88 dividend 7.5 1.84%  operation 0
            "601888",  # 中国中免 roi 1.17 rate 0.67 roe 18.79 pe 0.93 pb 20.11 dividend 7.2 0.36%  operation 0
            "600004",  # 白云机场 roi 0.01 rate 0.19 roe 0.99 pe 0.6 pb 1.61 dividend 1.45 1.16%  operation 0
            "600009",
            "600383",  # 金地集团 roi=100.7 roe=33.14 1/pe=23.74 rate=1.28 pb=1.3 dividend=6.7 yield=4.42% delta=18.61%
            "600606",  # 绿地控股 roi=89.09 roe=29.17 1/pe=28.28 rate=1.08 pb=0.96 dividend=4.0 yield=6.27% delta=22.17%
            "601668",  # 中国建筑 roi=86.31 roe=27.16 1/pe=29.7 rate=1.07 pb=0.8 dividend=1.85 yield=3.48% delta=11.73%
            "600048",  # 保利地产 roi=76.16 roe=31.33 1/pe=19.14 rate=1.27 pb=1.38 dividend=8.2 yield=4.9% delta=25.6%
            "000002",  # 万 科Ａ roi=52.67 roe=32.92 1/pe=15.84 rate=1.01 pb=1.76 dividend=10.17 yield=3.31% delta=20.87%
            "000951",  # 中国重汽 roi=52.36 roe=34.08 1/pe=9.2 rate=1.67 pb=3.08 dividend=5.5 yield=1.51% delta=16.45%
            "000069",  # 华侨城Ａ roi=46.46 roe=20.79 1/pe=21.91 rate=1.02 pb=0.84 dividend=3.05 yield=4.23% delta=19.31%
            "600755",  # 厦门国贸 roi=42.86 roe=20.34 1/pe=19.33 rate=1.09 pb=0.96 dividend=2.3 yield=3.08% delta=15.93%
            "600585",  # 海螺水泥 roi=34.14 roe=27.86 1/pe=11.67 rate=1.05 pb=2.01 dividend=20.0 yield=3.48% delta=29.81%
            "600068",  # 葛洲坝 roi=32.02 roe=19.79 1/pe=18.18 rate=0.89 pb=0.98 dividend=1.56 yield=2.28% delta=12.53%
            "600663",  # 陆家嘴 roi=31.27 roe=28.58 1/pe=10.42 rate=1.05 pb=2.51 dividend=4.56 yield=3.96% delta=38.0%
            "000581",  # 威孚高科 roi=24.41 roe=17.14 1/pe=10.71 rate=1.33 pb=1.48 dividend=11.0 yield=4.22% delta=39.37%
            "600612",  # 老凤祥 roi=22.76 roe=28.21 1/pe=7.61 rate=1.06 pb=3.28 dividend=11.5 yield=2.4% delta=31.46%
            "000049",  # 德赛电池 roi=19.82 roe=31.89 1/pe=5.92 rate=1.05 pb=4.39 dividend=7.0 yield=1.31% delta=22.08%
            "000895",  # 双汇发展 roi=18.57 roe=41.58 1/pe=3.66 rate=1.22 pb=7.3 dividend=16.4 yield=3.16% delta=86.18%
            "000877",  # 天山股份 roi=17.96 roe=19.31 1/pe=9.03 rate=1.03 pb=1.92 dividend=5.1 yield=2.72% delta=30.12%
            "600352",  # 浙江龙盛 roi=16.73 roe=19.16 1/pe=9.29 rate=0.94 pb=1.82 dividend=2.5 yield=1.67% delta=17.97%
            "601318",  # 中国平安 roi=15.12 roe=21.45 1/pe=8.81 rate=0.8 pb=2.2 dividend=21.0 yield=2.46% delta=27.92%
            "000513",  # 丽珠集团 roi=14.89 roe=19.27 1/pe=4.86 rate=1.59 pb=3.75 dividend=11.5 yield=2.5% delta=51.36%
            "600056",  # 中国医药 roi=14.33 roe=16.53 1/pe=9.03 rate=0.96 pb=1.65 dividend=2.76 yield=1.8% delta=19.92%
            "600036",  # 招商银行 roi=13.83 roe=16.49 1/pe=8.22 rate=1.02 pb=1.82 dividend=12.0 yield=2.68% delta=32.64%
            "601319",  # 中国人保 roi=12.58 roe=15.48 1/pe=9.45 rate=0.86 pb=1.48 dividend=1.52 yield=2.29% delta=24.21%
            "601607",  # 上海医药 roi=12.37 roe=12.57 1/pe=8.71 rate=1.13 pb=1.33 dividend=4.4 yield=2.12% delta=24.31%
            "601336",  # 新华保险 roi=10.3 roe=15.87 1/pe=6.76 rate=0.96 pb=2.0 dividend=14.1 yield=2.35% delta=34.74%
            "000333",  # 美的集团 roi=10.23 roe=25.33 1/pe=4.0 rate=1.01 pb=5.56 dividend=16.0 yield=1.79% delta=44.77%
            "000028",  # 国药一致 roi=10.06 roe=12.67 1/pe=7.35 rate=1.08 pb=1.58 dividend=6.0 yield=1.2% delta=16.28%
            "600887",  # 伊利股份 roi=9.9 roe=30.23 1/pe=3.15 rate=1.04 pb=8.21 dividend=8.1 yield=2.11% delta=67.08%
            "000828",  # 东莞控股 roi=9.63 roe=13.02 1/pe=9.61 rate=0.77 pb=1.25 dividend=3.0 yield=3.3% delta=34.36%
            "601601",  # 中国太保 roi=9.56 roe=13.91 1/pe=7.9 rate=0.87 pb=1.57 dividend=12.0 yield=3.63% delta=45.93%
            "600519",  # 贵州茅台 roi=9.2 roe=37.85 1/pe=2.23 rate=1.09 pb=14.33 dividend=170.25 yield=1.01% delta=45.11%
            "600900",  # 长江电力 roi=9.18 roe=16.04 1/pe=5.35 rate=1.07 pb=2.71 dividend=6.8 yield=3.44% delta=64.23%
            "600511",  # 国药股份 roi=9.06 roe=17.37 1/pe=5.38 rate=0.97 pb=2.88 dividend=6.38 yield=1.51% delta=28.07%
            "600062",  # 华润双鹤 roi=8.76 roe=12.02 1/pe=7.59 rate=0.96 pb=1.46 dividend=3.04 yield=2.36% delta=31.15%
            "600104",  # 上汽集团 roi=8.61 roe=11.78 1/pe=9.62 rate=0.76 pb=1.18 dividend=8.8 yield=3.43% delta=35.68%
            "000568",  # 泸州老窖 roi=7.57 roe=30.26 1/pe=2.0 rate=1.25 pb=12.81 dividend=15.9 yield=0.83% delta=41.47%
            "000858",  # 五 粮 液 roi=6.88 roe=29.28 1/pe=1.99 rate=1.18 pb=12.75 dividend=22.0 yield=0.83% delta=42.01%
            "600690",  # 海尔智家 roi=6.78 roe=20.0 1/pe=4.91 rate=0.69 pb=3.7 dividend=3.75 yield=1.33% delta=27.16%
            "000999",  # 华润三九 roi=6.78 roe=13.96 1/pe=6.48 rate=0.75 pb=1.95 dividend=4.3 yield=1.57% delta=24.28%
            "600007",  # 中国国贸 roi=6.77 roe=11.54 1/pe=6.38 rate=0.92 pb=1.7 dividend=3.8 yield=2.88% delta=45.22%
            "600486",  # 扬农化工 roi=6.6 roe=22.41 1/pe=3.1 rate=0.95 pb=6.29 dividend=6.5 yield=0.56% delta=17.91%
            "000661",  # 长春高新 roi=6.58 roe=19.96 1/pe=2.17 rate=1.52 pb=13.86 dividend=10.0 yield=0.29% delta=13.29%
            "000538",  # 云南白药 roi=6.15 roe=13.05 1/pe=3.96 rate=1.19 pb=3.24 dividend=30.0 yield=3.11% delta=78.46%
            "600809",  # 山西汾酒 roi=6.07 roe=37.47 1/pe=1.2 rate=1.35 pb=24.68 dividend=9.0 yield=0.35% delta=28.86%
            "600332",  # 白云山 roi=5.81 roe=11.98 1/pe=5.71 rate=0.85 pb=1.96 dividend=5.89 yield=1.89% delta=33.08%
            "600741",  # 华域汽车 roi=5.42 roe=12.77 1/pe=5.89 rate=0.72 pb=2.08 dividend=8.5 yield=2.57% delta=43.62%
            "600019",  # 宝钢股份 roi=5.16 roe=7.21 1/pe=8.95 rate=0.8 pb=0.78 dividend=2.8 yield=4.44% delta=49.56%
            "002304",  # 洋河股份 roi=5.08 roe=20.46 1/pe=2.76 rate=0.9 pb=7.05 dividend=30.0 yield=1.68% delta=60.91%
            "601628",  # 中国人寿 roi=5.03 roe=12.78 1/pe=4.02 rate=0.98 pb=2.9 dividend=7.3 yield=1.7% delta=42.39%
            "603288",  # 海天味业 roi=4.69 roe=33.72 1/pe=1.16 rate=1.2 pb=28.7 dividend=10.8 yield=0.67% delta=57.41%
            "600309",  # 万华化学 roi=4.24 roe=19.66 1/pe=2.8 rate=0.77 pb=6.46 dividend=13.0 yield=1.44% delta=51.45%
            "600197",  # 伊力特 roi=4.16 roe=14.17 1/pe=3.72 rate=0.79 pb=3.57 dividend=4.38 yield=1.99% delta=53.63%
            "000651",  # 格力电器 roi=3.99 roe=16.27 1/pe=4.09 rate=0.6 pb=3.5 dividend=22.0 yield=3.3% delta=80.69%
            "600030",  # 中信证券 roi=3.94 roe=8.73 1/pe=3.96 rate=1.14 pb=2.1 dividend=5.0 yield=1.72% delta=43.36%
            "600436",  # 片仔癀 roi=3.84 roe=25.78 1/pe=1.23 rate=1.21 pb=17.49 dividend=8.2 yield=0.38% delta=30.56%
            "000596",  # 古井贡酒 roi=3.29 roe=22.23 1/pe=1.74 rate=0.85 pb=11.31 dividend=15.0 yield=0.69% delta=39.57%
            "600276",  # 恒瑞医药 roi=3.19 roe=20.91 1/pe=1.26 rate=1.21 pb=16.27 dividend=2.3 yield=0.27% delta=21.01%
            "600377",  # 宁沪高速 roi=2.95 roe=9.37 1/pe=5.34 rate=0.59 pb=1.76 dividend=4.6 yield=4.78% delta=89.41%
            "600660",  # 福耀玻璃 roi=1.71 roe=10.88 1/pe=2.21 rate=0.71 pb=4.9 dividend=7.5 yield=1.83% delta=82.76%
            "601888",  # 中国中免 roi=1.35 roe=18.79 1/pe=1.07 rate=0.67 pb=17.41 dividend=7.2 yield=0.41% delta=38.41%
            "600897",  # 厦门空港 roi=1.13 roe=6.46 1/pe=4.08 rate=0.43 pb=1.56 dividend=5.23 yield=2.72% delta=66.68%
            "600004",  # 白云机场 roi=0.01 roe=0.86 1/pe=0.42 rate=0.19 pb=2.03 dividend=1.45 yield=0.92% delta=219.53%

            "000672",  # 上峰水泥 roi=68.01 roe=51.01 1/pe=12.12 rate=1.1 pb=3.1 dividend=9.0 yield=3.78% delta=31.21%
            "601155",  # 新城控股 roi=113.67 roe=50.28 1/pe=18.84 rate=1.2 pb=1.97 dividend=17.0 yield=4.9% delta=26.0%
            "000789",  # 万年青 roi=106.76 roe=49.92 1/pe=17.53 rate=1.22 pb=2.27 dividend=7.0 yield=4.43% delta=25.28%

            "600846",  # 同济科技 roi=143.37 roe=44.1 1/pe=20.84 rate=1.56 pb=1.76 dividend=3.4 yield=4.0% delta=19.21%

            "600031",  # 三一重工 roi=29.24 roe=34.77 1/pe=6.05 rate=1.39 pb=4.59 dividend=4.2 yield=1.45% delta=24.02%
            "000951",  # 中国重汽 roi=50.31 roe=34.08 1/pe=8.84 rate=1.67 pb=3.2 dividend=5.5 yield=1.45% delta=16.45%
            "600153",  # 建发股份 roi=144.86 roe=33.2 1/pe=36.36 rate=1.2 pb=0.79 dividend=5.0 yield=5.55% delta=15.26%
            "600466",  # 蓝光发展 roi=109.07 roe=32.86 1/pe=28.37 rate=1.17 pb=0.93 dividend=2.87 yield=5.57% delta=19.65%
            "000876",  # 新 希 望 roi=43.36 roe=32.2 1/pe=7.05 rate=1.91 pb=3.25 dividend=1.5 yield=0.57% delta=8.16%
            "600801",  # 华新水泥 roi=29.22 roe=30.64 1/pe=11.49 rate=0.83 pb=2.4 dividend=12.1 yield=4.79% delta=41.72%
            "000656",  # 金科股份 roi=57.87 roe=29.57 1/pe=16.87 rate=1.16 pb=1.46 dividend=4.5 yield=5.58% delta=33.05%

            "600325",  # 华发股份 roi=94.7 roe=29.05 1/pe=26.72 rate=1.22 pb=0.99 dividend=4.0 yield=6.18% delta=23.14%
            "000921",  # 海信家电 roi=45.95 roe=28.9 1/pe=10.6 rate=1.5 pb=2.46 dividend=3.95 yield=2.38% delta=22.5%
            "002372",  # 伟星新材 roi=9.15 roe=28.57 1/pe=3.17 rate=1.01 pb=8.46 dividend=5.0 yield=2.42% delta=76.55%

            "600298",  # 安琪酵母 roi=13.24 roe=27.21 1/pe=3.31 rate=1.47 pb=7.14 dividend=4.0 yield=0.84% delta=25.24%
            "000963",  # 华东医药 roi=16.59 roe=26.42 1/pe=5.71 rate=1.1 pb=3.79 dividend=2.8 yield=0.91% delta=15.9%
            "600720",  # 祁连山 roi=51.8 roe=26.41 1/pe=13.91 rate=1.41 pb=1.6 dividend=5.8 yield=3.59% delta=25.8%
            "002508",  # 老板电器 roi=11.0 roe=26.01 1/pe=3.99 rate=1.06 pb=5.53 dividend=5.0 yield=1.14% delta=28.62%
            "600340",  # 华夏幸福 roi=52.67 roe=24.84 1/pe=22.8 rate=0.93 pb=1.16 dividend=15.0 yield=10.42% delta=45.7%
            "002146",  # 荣盛发展 roi=73.03 roe=24.79 1/pe=28.88 rate=1.02 pb=0.73 dividend=4.8 yield=6.63% delta=22.96%
            "600872",  # 中炬高新 roi=5.67 roe=24.34 1/pe=1.88 rate=1.24 pb=11.13 dividend=2.8 yield=0.46% delta=24.27%
            "000671",  # 阳 光 城 roi=38.79 roe=23.99 1/pe=16.01 rate=1.01 pb=1.26 dividend=1.99 yield=2.71% delta=16.96%
            "300015",  # 爱尔眼科 roi=1.82 roe=21.07 1/pe=0.68 rate=1.27 pb=27.96 dividend=1.5 yield=0.23% delta=34.22%
            "000411",  # 英特集团 roi=13.78 roe=21.58 1/pe=6.45 rate=0.99 pb=3.07 dividend=0.61 yield=0.3% delta=4.73%
            "600563",  # 法拉电子 roi=6.28 roe=21.35 1/pe=2.47 rate=1.19 pb=7.86 dividend=13.0 yield=1.37% delta=55.52%
            "601636",  # 旗滨集团 roi=14.22 roe=21.0 1/pe=4.87 rate=1.39 pb=3.84 dividend=3.0 yield=2.4% delta=49.32%

            "002415",  # 海康威视 roi=9.97 roe=32.02 1/pe=2.91 rate=1.07 pb=9.31 dividend=7.0 yield=1.47% delta=50.52%



            "600846",  # 同济科技 roi=143.23 roe=44.1 1/pe=20.82 rate=1.56 pb=1.76 dividend=3.4 yield=4.0% delta=19.21%
            "600153",  # 建发股份 roi=142.35 roe=33.2 1/pe=35.73 rate=1.2 pb=0.8 dividend=5.0 yield=5.45% delta=15.26%
            "601155",  # 新城控股 roi=113.31 roe=50.28 1/pe=18.78 rate=1.2 pb=1.97 dividend=17.0 yield=4.88% delta=26.0%
            "600466",  # 蓝光发展 roi=108.23 roe=32.86 1/pe=28.15 rate=1.17 pb=0.94 dividend=2.87 yield=5.53% delta=19.65%
            "000789",  # 万年青 roi=103.53 roe=49.92 1/pe=17.0 rate=1.22 pb=2.34 dividend=7.0 yield=4.3% delta=25.28%
            "600383",  # 金地集团 roi=101.59 roe=33.14 1/pe=23.95 rate=1.28 pb=1.29 dividend=6.7 yield=4.46% delta=18.61%
            "600325",  # 华发股份 roi=94.7 roe=29.05 1/pe=26.72 rate=1.22 pb=0.99 dividend=4.0 yield=6.18% delta=23.14%
            "600606",  # 绿地控股 roi=89.22 roe=29.17 1/pe=28.32 rate=1.08 pb=0.96 dividend=4.0 yield=6.28% delta=22.17%
            "601668",  # 中国建筑 roi=84.57 roe=27.16 1/pe=29.1 rate=1.07 pb=0.81 dividend=1.85 yield=3.41% delta=11.73%
            "600048",  # 保利地产 roi=75.12 roe=31.33 1/pe=18.88 rate=1.27 pb=1.4 dividend=8.2 yield=4.83% delta=25.6%
            "002146",  # 荣盛发展 roi=72.14 roe=24.79 1/pe=28.53 rate=1.02 pb=0.74 dividend=4.8 yield=6.55% delta=22.96%
            "000672",  # 上峰水泥 roi=66.83 roe=51.01 1/pe=11.91 rate=1.1 pb=3.16 dividend=9.0 yield=3.72% delta=31.21%
            "002244",  # 滨江集团 roi=62.8 roe=23.46 1/pe=23.48 rate=1.14 pb=0.93 dividend=1.32 yield=2.58% delta=11.0%
            "000656",  # 金科股份 roi=57.25 roe=29.57 1/pe=16.69 rate=1.16 pb=1.48 dividend=4.5 yield=5.51% delta=33.05%
            "600340",  # 华夏幸福 roi=52.25 roe=24.84 1/pe=22.62 rate=0.93 pb=1.17 dividend=15.0 yield=10.34% delta=45.7%
            "000002",  # 万 科Ａ roi=52.2 roe=32.92 1/pe=15.7 rate=1.01 pb=1.78 dividend=10.17 yield=3.28% delta=20.87%
            "600720",  # 祁连山 roi=50.27 roe=26.41 1/pe=13.5 rate=1.41 pb=1.65 dividend=5.8 yield=3.48% delta=25.8%
            "000951",  # 中国重汽 roi=49.8 roe=34.08 1/pe=8.75 rate=1.67 pb=3.23 dividend=5.5 yield=1.44% delta=16.45%
            "000069",  # 华侨城Ａ roi=45.89 roe=20.79 1/pe=21.64 rate=1.02 pb=0.85 dividend=3.05 yield=4.18% delta=19.31%
            "000921",  # 海信家电 roi=45.69 roe=28.9 1/pe=10.54 rate=1.5 pb=2.47 dividend=3.95 yield=2.37% delta=22.5%
            "000876",  # 新 希 望 roi=43.97 roe=32.2 1/pe=7.15 rate=1.91 pb=3.2 dividend=1.5 yield=0.58% delta=8.16%
            "600755",  # 厦门国贸 roi=43.92 roe=20.34 1/pe=19.81 rate=1.09 pb=0.94 dividend=2.3 yield=3.16% delta=15.93%
            "000671",  # 阳 光 城 roi=38.79 roe=23.99 1/pe=16.01 rate=1.01 pb=1.26 dividend=1.99 yield=2.71% delta=16.96%
            "600585",  # 海螺水泥 roi=34.46 roe=27.86 1/pe=11.78 rate=1.05 pb=1.99 dividend=20.0 yield=3.51% delta=29.81%
            "600068",  # 葛洲坝 roi=31.79 roe=19.79 1/pe=18.05 rate=0.89 pb=0.99 dividend=1.56 yield=2.26% delta=12.53%
            "600663",  # 陆家嘴 roi=31.15 roe=28.58 1/pe=10.38 rate=1.05 pb=2.51 dividend=4.56 yield=3.94% delta=38.0%
            "600801",  # 华新水泥 roi=28.64 roe=30.64 1/pe=11.26 rate=0.83 pb=2.45 dividend=12.1 yield=4.7% delta=41.72%

            "000581",  # 威孚高科 roi=23.98 roe=17.14 1/pe=10.52 rate=1.33 pb=1.51 dividend=11.0 yield=4.14% delta=39.37%
            "601009",  # 南京银行 roi=22.41 roe=14.49 1/pe=15.16 rate=1.02 pb=0.9 dividend=3.92 yield=4.66% delta=30.75%
            "600612",  # 老凤祥 roi=21.95 roe=28.21 1/pe=7.34 rate=1.06 pb=3.4 dividend=11.5 yield=2.31% delta=31.46%
            "601988",  # 中国银行 roi=20.81 roe=11.47 1/pe=19.51 rate=0.93 pb=0.56 dividend=1.91 yield=5.88% delta=30.13%
            "600668",  # 尖峰集团 roi=20.12 roe=18.76 1/pe=12.77 rate=0.84 pb=1.25 dividend=3.0 yield=1.93% delta=15.11%
            "601328",  # 交通银行 roi=19.81 roe=10.48 1/pe=20.55 rate=0.92 pb=0.49 dividend=3.15 yield=6.79% delta=33.04%
            "000049",  # 德赛电池 roi=19.39 roe=31.89 1/pe=5.79 rate=1.05 pb=4.49 dividend=7.0 yield=1.28% delta=22.08%
            "000895",  # 双汇发展 roi=19.38 roe=41.58 1/pe=3.82 rate=1.22 pb=6.99 dividend=16.4 yield=3.29% delta=86.18%
            "601288",  # 农业银行 roi=18.54 roe=11.47 1/pe=17.38 rate=0.93 pb=0.62 dividend=1.82 yield=5.62% delta=32.33%
            "000877",  # 天山股份 roi=18.46 roe=19.31 1/pe=9.28 rate=1.03 pb=1.86 dividend=5.1 yield=2.79% delta=30.12%
            "601398",  # 工商银行 roi=18.0 roe=12.02 1/pe=16.1 rate=0.93 pb=0.7 dividend=2.63 yield=5.19% delta=32.23%
            "000963",  # 华东医药 roi=16.86 roe=26.42 1/pe=5.8 rate=1.1 pb=3.73 dividend=2.8 yield=0.92% delta=15.9%
            "601939",  # 建设银行 roi=16.77 roe=12.13 1/pe=14.87 rate=0.93 pb=0.76 dividend=3.2 yield=4.77% delta=32.07%
            "601088",  # 中国神华 roi=15.66 roe=13.77 1/pe=13.07 rate=0.87 pb=1.02 dividend=12.6 yield=6.86% delta=52.46%
            "600352",  # 浙江龙盛 roi=15.62 roe=19.16 1/pe=8.67 rate=0.94 pb=1.94 dividend=2.5 yield=1.56% delta=17.97%
            "601318",  # 中国平安 roi=14.96 roe=21.45 1/pe=8.72 rate=0.8 pb=2.22 dividend=21.0 yield=2.44% delta=27.92%
            "000513",  # 丽珠集团 roi=14.83 roe=19.27 1/pe=4.84 rate=1.59 pb=3.76 dividend=11.5 yield=2.48% delta=51.36%
            "600056",  # 中国医药 roi=14.17 roe=16.53 1/pe=8.93 rate=0.96 pb=1.67 dividend=2.76 yield=1.78% delta=19.92%
            "600036",  # 招商银行 roi=13.62 roe=16.49 1/pe=8.1 rate=1.02 pb=1.85 dividend=12.0 yield=2.64% delta=32.64%
            "600298",  # 安琪酵母 roi=13.0 roe=27.21 1/pe=3.25 rate=1.47 pb=7.27 dividend=4.0 yield=0.82% delta=25.24%
            "601319",  # 中国人保 roi=12.53 roe=15.48 1/pe=9.41 rate=0.86 pb=1.49 dividend=1.52 yield=2.28% delta=24.21%
            "601607",  # 上海医药 roi=12.3 roe=12.57 1/pe=8.66 rate=1.13 pb=1.34 dividend=4.4 yield=2.1% delta=24.31%
            "002508",  # 老板电器 roi=11.11 roe=26.01 1/pe=4.03 rate=1.06 pb=5.48 dividend=5.0 yield=1.15% delta=28.62%
            "601336",  # 新华保险 roi=10.3 roe=15.87 1/pe=6.76 rate=0.96 pb=2.0 dividend=14.1 yield=2.35% delta=34.74%
            "000028",  # 国药一致 roi=10.02 roe=12.67 1/pe=7.32 rate=1.08 pb=1.59 dividend=6.0 yield=1.19% delta=16.28%
            "000333",  # 美的集团 roi=9.77 roe=25.33 1/pe=3.82 rate=1.01 pb=5.82 dividend=16.0 yield=1.71% delta=44.77%
            "600887",  # 伊利股份 roi=9.62 roe=30.23 1/pe=3.06 rate=1.04 pb=8.46 dividend=8.1 yield=2.05% delta=67.08%
            "000828",  # 东莞控股 roi=9.36 roe=13.02 1/pe=9.34 rate=0.77 pb=1.28 dividend=3.0 yield=3.21% delta=34.36%
            "601601",  # 中国太保 roi=9.23 roe=13.91 1/pe=7.63 rate=0.87 pb=1.63 dividend=12.0 yield=3.5% delta=45.93%
            "600900",  # 长江电力 roi=9.13 roe=16.04 1/pe=5.32 rate=1.07 pb=2.73 dividend=6.8 yield=3.42% delta=64.23%
            "600511",  # 国药股份 roi=8.93 roe=17.37 1/pe=5.3 rate=0.97 pb=2.93 dividend=6.38 yield=1.49% delta=28.07%
            "600062",  # 华润双鹤 roi=8.87 roe=12.02 1/pe=7.69 rate=0.96 pb=1.45 dividend=3.04 yield=2.4% delta=31.15%
            "600519",  # 贵州茅台 roi=8.71 roe=37.85 1/pe=2.11 rate=1.09 pb=15.15 dividend=170.25 yield=0.95% delta=45.11%
            "601006",  # 大秦铁路 roi=8.54 roe=10.58 1/pe=11.87 rate=0.68 pb=0.85 dividend=4.8 yield=7.19% delta=60.53%
            "600104",  # 上汽集团 roi=8.23 roe=11.78 1/pe=9.19 rate=0.76 pb=1.23 dividend=8.8 yield=3.28% delta=35.68%
            "002032",  # 苏 泊 尔 roi=7.84 roe=27.48 1/pe=2.94 rate=0.97 pb=9.05 dividend=13.3 yield=1.84% delta=62.42%
            "300760",  # 迈瑞医疗 roi=7.71 roe=36.21 1/pe=1.5 rate=1.42 pb=19.21 dividend=15.0 yield=0.43% delta=28.6%
            "000568",  # 泸州老窖 roi=7.34 roe=30.26 1/pe=1.94 rate=1.25 pb=13.24 dividend=15.9 yield=0.8% delta=41.47%
            "000999",  # 华润三九 roi=6.82 roe=13.96 1/pe=6.51 rate=0.75 pb=1.94 dividend=4.3 yield=1.58% delta=24.28%
            "600007",  # 中国国贸 roi=6.77 roe=11.54 1/pe=6.38 rate=0.92 pb=1.7 dividend=3.8 yield=2.88% delta=45.22%
            "000858",  # 五 粮 液 roi=6.63 roe=29.28 1/pe=1.92 rate=1.18 pb=13.18 dividend=22.0 yield=0.81% delta=42.01%
            "600486",  # 扬农化工 roi=6.45 roe=22.41 1/pe=3.03 rate=0.95 pb=6.42 dividend=6.5 yield=0.54% delta=17.91%
            "000661",  # 长春高新 roi=6.43 roe=19.96 1/pe=2.12 rate=1.52 pb=14.19 dividend=10.0 yield=0.28% delta=13.29%
            "600690",  # 海尔智家 roi=6.27 roe=20.0 1/pe=4.54 rate=0.69 pb=4.0 dividend=3.75 yield=1.23% delta=27.16%
            "000538",  # 云南白药 roi=6.06 roe=13.05 1/pe=3.9 rate=1.19 pb=3.29 dividend=30.0 yield=3.06% delta=78.46%
            "600350",  # 山东高速 roi=5.99 roe=8.37 1/pe=7.3 rate=0.98 pb=1.16 dividend=3.8 yield=5.62% delta=76.98%
            "600809",  # 山西汾酒 roi=5.92 roe=37.47 1/pe=1.17 rate=1.35 pb=25.44 dividend=9.0 yield=0.34% delta=28.86%
            "600872",  # 中炬高新 roi=5.76 roe=24.34 1/pe=1.91 rate=1.24 pb=10.95 dividend=2.8 yield=0.46% delta=24.27%
            "600332",  # 白云山 roi=5.74 roe=11.98 1/pe=5.64 rate=0.85 pb=1.98 dividend=5.89 yield=1.87% delta=33.08%
            "600741",  # 华域汽车 roi=5.43 roe=12.77 1/pe=5.91 rate=0.72 pb=2.07 dividend=8.5 yield=2.58% delta=43.62%
            "600028",  # 中国石化 roi=5.33 roe=6.71 1/pe=9.57 rate=0.83 pb=0.7 dividend=2.6 yield=6.19% delta=64.67%
            "600132",  # 重庆啤酒 roi=5.25 roe=46.43 1/pe=1.19 rate=0.95 pb=44.02 dividend=14.0 yield=1.28% delta=107.96%
            "002304",  # 洋河股份 roi=5.21 roe=20.46 1/pe=2.83 rate=0.9 pb=6.87 dividend=30.0 yield=1.72% delta=60.91%
            "600019",  # 宝钢股份 roi=5.1 roe=7.21 1/pe=8.84 rate=0.8 pb=0.79 dividend=2.8 yield=4.38% delta=49.56%
            "601628",  # 中国人寿 roi=5.06 roe=12.78 1/pe=4.04 rate=0.98 pb=2.89 dividend=7.3 yield=1.71% delta=42.39%
            "603288",  # 海天味业 roi=4.69 roe=33.72 1/pe=1.16 rate=1.2 pb=28.88 dividend=10.8 yield=0.66% delta=57.41%
            "000039",  # 中集集团 roi=4.46 roe=8.05 1/pe=4.9 rate=1.13 pb=1.6 dividend=1.2 yield=0.77% delta=15.69%
            "600309",  # 万华化学 roi=4.28 roe=19.66 1/pe=2.83 rate=0.77 pb=6.39 dividend=13.0 yield=1.45% delta=51.45%
            "000651",  # 格力电器 roi=3.9 roe=16.27 1/pe=3.99 rate=0.6 pb=3.58 dividend=22.0 yield=3.22% delta=80.69%
            "600030",  # 中信证券 roi=3.84 roe=8.73 1/pe=3.86 rate=1.14 pb=2.15 dividend=5.0 yield=1.67% delta=43.36%
            "600436",  # 片仔癀 roi=3.84 roe=25.78 1/pe=1.23 rate=1.21 pb=17.51 dividend=8.2 yield=0.38% delta=30.56%
            "600197",  # 伊力特 roi=3.4 roe=14.17 1/pe=3.04 rate=0.79 pb=4.37 dividend=4.38 yield=1.63% delta=53.63%
            "000596",  # 古井贡酒 roi=3.27 roe=22.23 1/pe=1.73 rate=0.85 pb=11.33 dividend=15.0 yield=0.69% delta=39.57%
            "600276",  # 恒瑞医药 roi=3.21 roe=20.91 1/pe=1.27 rate=1.21 pb=16.18 dividend=2.3 yield=0.27% delta=21.01%
            "600377",  # 宁沪高速 roi=2.96 roe=9.37 1/pe=5.36 rate=0.59 pb=1.75 dividend=4.6 yield=4.79% delta=89.41%
            "600763",  # 通策医疗 roi=2.16 roe=29.13 1/pe=0.74 rate=1.0 pb=31.1 dividend=0.0 yield=0.0% delta=0.0%
            "600660",  # 福耀玻璃 roi=1.67 roe=10.88 1/pe=2.16 rate=0.71 pb=5.0 dividend=7.5 yield=1.79% delta=82.76%
            "601888",  # 中国中免 roi=1.26 roe=18.79 1/pe=1.0 rate=0.67 pb=18.67 dividend=7.2 yield=0.38% delta=38.41%
            "600897",  # 厦门空港 roi=1.19 roe=6.46 1/pe=4.27 rate=0.43 pb=1.49 dividend=5.23 yield=2.85% delta=66.68%
            "000429",  # 粤高速Ａ roi=0.87 roe=6.18 1/pe=4.15 rate=0.34 pb=1.56 dividend=4.22 yield=6.17% delta=148.84%
            "600548",  # 深高速 roi=0.36 roe=4.58 1/pe=4.14 rate=0.19 pb=1.11 dividend=5.2 yield=5.7% delta=137.64%
            "600004",  # 白云机场 roi=0.01 roe=0.86 1/pe=0.45 rate=0.19 pb=1.91 dividend=1.45 yield=0.98% delta=219.53%

#150家持续盈利名单
            "000001",  # 平安银行
            "300015",  # 爱尔眼科
            "600643",  # 爱建集团
            "600298",  # 安琪酵母
            "600004",  # 白云机场
            "600332",  # 白云山
            "600845",  # 宝信软件
            "600048",  # 保利地产
            "000582",  # 北部湾港
            "000786",  # 北新建材
            "002244",  # 滨江集团
            "603899",  # 晨光文具
            "600874",  # 创业环保
            "002236",  # 大华股份
            "000049",  # 德赛电池
            "300244",  # 迪安诊断
            "000423",  # 东阿阿胶
            "000682",  # 东方电子
            "002271",  # 东方雨虹
            "000828",  # 东莞控股
            "000501",  # 鄂武商A
            "002262",  # 恩华药业
            "600563",  # 法拉电子
            "600498",  # 烽火通信
            "002507",  # 涪陵榨菜
            "600660",  # 福耀玻璃
            "600196",  # 复星医药
            "000651",  # 格力电器
            "600068",  # 葛洲坝
            "000596",  # 古井贡酒
            "600597",  # 光明乳业
            "000529",  # 广弘控股
            "600519",  # 贵州茅台
            "600511",  # 国药股份
            "000028",  # 国药一致
            "002311",  # 海大集团
            "600690",  # 海尔智家
            "002415",  # 海康威视
            "600585",  # 海螺水泥
            "603288",  # 海天味业
            "000921",  # 海信家电
            "600987",  # 航民股份
            "002025",  # 航天电器
            "000547",  # 航天发展
            "600271",  # 航天信息
            "600276",  # 恒瑞医药
            "300760",  # 迈瑞医疗
            "600570",  # 恒生电子
            "600461",  # 洪城水业

            "000963",  # 华东医药
            "002007",  # 华兰生物
            "000069",  # 华侨城
            "000999",  # 华润三九
            "600062",  # 华润双鹤
            "600340",  # 华夏幸福
            "600741",  # 华域汽车
            "603678",  # 火炬电子
            "600566",  # 济川药业
            "600668",  # 尖峰集团
            "600153",  # 建发股份
            "600380",  # 健康元
            "600676",  # 交运股份
            "603369",  # 今世缘
            "600383",  # 金地集团
            "002020",  # 京新药业
            "002242",  # 九阳股份
            "600998",  # 九州通
            "600557",  # 康缘药业
            "002230",  # 科大讯飞

            "002508",  # 老板电器
            "600612",  # 老凤祥
            "300003",  # 乐普医疗
            "002475",  # 立讯精密
            "000513",  # 丽珠集团
            "600363",  # 联创光电
            "600513",  # 联环药业
            "000568",  # 泸州老窖
            "600663",  # 陆家嘴
            "600606",  # 绿地控股
            "000333",  # 美的集团
            "601677",  # 明泰铝业
            "600064",  # 南京高科
            "002142",  # 宁波银行
            "600377",  # 宁沪高速
            "600436",  # 片仔癀
            "600639",  # 浦东金桥
            "000739",  # 普洛药业
            "002287",  # 奇正藏药
            "002439",  # 启明星辰
            "600600",  # 青岛啤酒
            "002146",  # 荣盛发展
            "600755",  # 厦门国贸
            "600897",  # 厦门空港
            "601009",  # 南京银行
            "000498",  # 山东路桥
            "600809",  # 山西汾酒
            "600009",  # 上海机场
            "601607",  # 上海医药
            "600104",  # 上汽集团
            "000895",  # 双汇发展

            "300284",  # 苏交科
            "600820",  # 隧道股份
            "000877",  # 天山股份
            "600763",  # 通策医疗
            "600846",  # 同济科技
            "600085",  # 同仁堂
            "000002",  # 万 科Ａ
            "600309",  # 万华化学
            "000581",  # 威孚高科
            "002372",  # 伟星新材
            "000858",  # 五 粮 液
            "000876",  # 新 希 望
            "601336",  # 新华保险
            "000756",  # 新华制药
            "000598",  # 兴蓉环境
            "600486",  # 扬农化工
            "002304",  # 洋河股份
            "600197",  # 伊力特
            "600887",  # 伊利股份
            "000411",  # 英特集团
            "002223",  # 鱼跃医疗
            "000538",  # 云南白药
            "000661",  # 长春高新
            "600900",  # 长江电力
            "600036",  # 招商银行
            "600352",  # 浙江龙盛
            "002677",  # 浙江美大
            "000733",  # 振华科技
            "601877",  # 正泰电器
            "601669",  # 中国电建
            "600007",  # 中国国贸
            "601668",  # 中国建筑
            "601800",  # 中国交建
            "601318",  # 中国平安
            "601628",  # 中国人寿
            "601601",  # 中国太保
            "601186",  # 中国铁建
            "600056",  # 中国医药
            "601888",  # 中国中免
            "601390",  # 中国中铁
            "002179",  # 中航光电
            "000777",  # 中核科技
            "600872",  # 中炬高新
            "600373",  # 中文传媒
            "600329",  # 中新药业
            "600030",  # 中信证券
            "601611",  # 中国核建
            "603444",  # 吉比特
            "601155",  # 新城控股
            "001979",  # 招商蛇口
            "002867",  # 周大生

            #ROI排名
            "600846",  # 同济科技 roi=148.26 roe=44.1 1/pe=21.55 rate=1.56 pb=1.7 dividend=3.4 yield=4.14% delta=19.21%
            "600153",  # 建发股份 roi=143.26 roe=32.87 1/pe=36.32 rate=1.2 pb=0.78 dividend=5.0 yield=5.6% delta=15.42%
            "000789",  # 万年青 roi=122.66 roe=49.92 1/pe=20.14 rate=1.22 pb=1.98 dividend=7.0 yield=5.09% delta=25.28%
            "600466",  # 蓝光发展 roi=113.45 roe=32.86 1/pe=29.51 rate=1.17 pb=0.9 dividend=2.87 yield=5.8% delta=19.65%
            "601155",  # 新城控股 roi=112.11 roe=50.31 1/pe=18.57 rate=1.2 pb=2.0 dividend=17.0 yield=4.83% delta=25.99%
            "600383",  # 金地集团 roi=108.3 roe=33.14 1/pe=25.53 rate=1.28 pb=1.21 dividend=6.7 yield=4.75% delta=18.61%
            "600325",  # 华发股份 roi=96.79 roe=29.05 1/pe=27.31 rate=1.22 pb=0.97 dividend=4.0 yield=6.32% delta=23.14%
            "600606",  # 绿地控股 roi=92.4 roe=29.17 1/pe=29.33 rate=1.08 pb=0.93 dividend=4.0 yield=6.5% delta=22.17%
            "601668",  # 中国建筑 roi=90.06 roe=27.16 1/pe=30.99 rate=1.07 pb=0.76 dividend=1.85 yield=3.63% delta=11.73%
            "600048",  # 保利地产 roi=78.62 roe=31.33 1/pe=19.76 rate=1.27 pb=1.33 dividend=8.2 yield=5.06% delta=25.6%
            "000672",  # 上峰水泥 roi=75.97 roe=51.01 1/pe=13.54 rate=1.1 pb=2.78 dividend=9.0 yield=4.23% delta=31.21%
            "002146",  # 荣盛发展 roi=75.96 roe=24.79 1/pe=30.04 rate=1.02 pb=0.71 dividend=4.8 yield=6.9% delta=22.96%
            "002244",  # 滨江集团 roi=66.17 roe=23.46 1/pe=24.74 rate=1.14 pb=0.89 dividend=1.32 yield=2.72% delta=11.0%
            "000656",  # 金科股份 roi=61.88 roe=29.57 1/pe=18.04 rate=1.16 pb=1.37 dividend=4.5 yield=5.96% delta=33.05%
            "600720",  # 祁连山 roi=58.95 roe=26.41 1/pe=15.83 rate=1.41 pb=1.41 dividend=5.8 yield=4.08% delta=25.8%
            "000951",  # 中国重汽 roi=58.85 roe=34.08 1/pe=10.34 rate=1.67 pb=2.74 dividend=5.5 yield=1.7% delta=16.45%
            "000002",  # 万 科Ａ roi=56.02 roe=32.92 1/pe=16.85 rate=1.01 pb=1.66 dividend=10.17 yield=3.52% delta=20.87%
            "600340",  # 华夏幸福 roi=54.4 roe=24.84 1/pe=23.55 rate=0.93 pb=1.12 dividend=15.0 yield=10.76% delta=45.7%
            "000921",  # 海信家电 roi=51.24 roe=28.9 1/pe=11.82 rate=1.5 pb=2.2 dividend=3.95 yield=2.66% delta=22.5%
            "000069",  # 华侨城Ａ roi=49.62 roe=20.79 1/pe=23.4 rate=1.02 pb=0.79 dividend=3.05 yield=4.52% delta=19.31%
            "000786",  # 北新建材 roi=48.19 roe=19.19 1/pe=4.13 rate=6.08 pb=3.97 dividend=0.82 yield=0.22% delta=5.35%
            "000876",  # 新 希 望 roi=48.16 roe=32.2 1/pe=7.83 rate=1.91 pb=2.92 dividend=1.5 yield=0.64% delta=8.16%
            "600064",  # 南京高科 roi=46.89 roe=19.87 1/pe=17.48 rate=1.35 pb=1.0 dividend=4.5 yield=4.28% delta=24.47%
            "600755",  # 厦门国贸 roi=46.4 roe=20.34 1/pe=20.93 rate=1.09 pb=0.89 dividend=2.3 yield=3.33% delta=15.93%
            "600998",  # 九州通 roi=45.39 roe=21.33 1/pe=10.38 rate=2.05 pb=1.72 dividend=0.0 yield=0.0% delta=0.0%
            "601390",  # 中国中铁 roi=43.43 roe=15.44 1/pe=20.99 rate=1.34 pb=0.66 dividend=1.69 yield=3.11% delta=14.8%
            "000671",  # 阳 光 城 roi=41.31 roe=23.99 1/pe=17.05 rate=1.01 pb=1.18 dividend=1.99 yield=2.89% delta=16.96%
            "001979",  # 招商蛇口 roi=40.93 roe=25.17 1/pe=15.34 rate=1.06 pb=1.5 dividend=8.3 yield=6.14% delta=40.01%
            "000529",  # 广弘控股 roi=37.95 roe=24.46 1/pe=9.46 rate=1.64 pb=2.19 dividend=1.0 yield=1.41% delta=14.92%
            "600585",  # 海螺水泥 roi=37.74 roe=27.86 1/pe=12.9 rate=1.05 pb=1.82 dividend=20.0 yield=3.84% delta=29.81%
            "600068",  # 葛洲坝 roi=33.24 roe=19.79 1/pe=18.87 rate=0.89 pb=0.94 dividend=1.56 yield=2.36% delta=12.53%
            "601186",  # 中国铁建 roi=33.18 roe=14.67 1/pe=21.14 rate=1.07 pb=0.62 dividend=2.1 yield=2.55% delta=12.07%
            "000498",  # 山东路桥 roi=32.6 roe=15.71 1/pe=14.93 rate=1.39 pb=0.94 dividend=0.8 yield=1.61% delta=10.76%
            "600663",  # 陆家嘴 roi=31.75 roe=28.58 1/pe=10.58 rate=1.05 pb=2.47 dividend=4.56 yield=4.02% delta=38.0%
            "600380",  # 健康元 roi=30.23 roe=23.91 1/pe=8.72 rate=1.45 pb=2.62 dividend=1.6 yield=1.1% delta=12.58%
            "600461",  # 洪城水业 roi=29.56 roe=16.98 1/pe=12.09 rate=1.44 pb=1.25 dividend=2.6 yield=3.9% delta=32.24%
            "002236",  # 大华股份 roi=28.64 roe=29.37 1/pe=6.68 rate=1.46 pb=3.35 dividend=1.33 yield=0.64% delta=9.61%
            "601669",  # 中国电建 roi=28.11 roe=13.69 1/pe=19.19 rate=1.07 pb=0.67 dividend=0.4 yield=1.03% delta=5.34%
            "600031",  # 三一重工 roi=27.02 roe=34.77 1/pe=5.59 rate=1.39 pb=4.97 dividend=4.2 yield=1.34% delta=24.02%
            "000581",  # 威孚高科 roi=26.51 roe=17.14 1/pe=11.63 rate=1.33 pb=1.37 dividend=11.0 yield=4.58% delta=39.37%
            "300244",  # 迪安诊断 roi=25.83 roe=28.89 1/pe=5.29 rate=1.69 pb=4.61 dividend=1.28 yield=0.36% delta=6.88%
            "601009",  # 南京银行 roi=23.62 roe=14.49 1/pe=15.98 rate=1.02 pb=0.85 dividend=3.92 yield=4.91% delta=30.75%
            "600612",  # 老凤祥 roi=22.82 roe=28.21 1/pe=7.63 rate=1.06 pb=3.27 dividend=11.5 yield=2.4% delta=31.46%
            "000877",  # 天山股份 roi=22.24 roe=19.31 1/pe=11.18 rate=1.03 pb=1.55 dividend=5.1 yield=3.37% delta=30.12%
            "601988",  # 中国银行 roi=21.13 roe=11.47 1/pe=19.81 rate=0.93 pb=0.55 dividend=1.91 yield=5.97% delta=30.13%
            "000049",  # 德赛电池 roi=20.76 roe=31.89 1/pe=6.2 rate=1.05 pb=4.19 dividend=7.0 yield=1.37% delta=22.08%
            "601328",  # 交通银行 roi=20.3 roe=10.48 1/pe=21.05 rate=0.92 pb=0.47 dividend=3.15 yield=6.95% delta=33.04%
            "000895",  # 双汇发展 roi=19.83 roe=41.58 1/pe=3.91 rate=1.22 pb=6.83 dividend=16.4 yield=3.37% delta=86.18%
            "601288",  # 农业银行 roi=18.65 roe=11.47 1/pe=17.48 rate=0.93 pb=0.61 dividend=1.82 yield=5.65% delta=32.33%
            "002677",  # 浙江美大 roi=18.43 roe=36.25 1/pe=4.5 rate=1.13 pb=7.31 dividend=5.42 yield=3.21% delta=71.35%
            "601398",  # 工商银行 roi=18.06 roe=12.02 1/pe=16.16 rate=0.93 pb=0.7 dividend=2.63 yield=5.21% delta=32.23%
            "600352",  # 浙江龙盛 roi=17.83 roe=19.16 1/pe=9.9 rate=0.94 pb=1.7 dividend=2.5 yield=1.78% delta=17.97%
            "603444",  # 吉比特 roi=17.82 roe=41.0 1/pe=4.14 rate=1.05 pb=8.19 dividend=50.0 yield=1.24% delta=29.93%
            "000963",  # 华东医药 roi=17.64 roe=26.42 1/pe=6.07 rate=1.1 pb=3.57 dividend=2.8 yield=0.96% delta=15.9%
            "601939",  # 建设银行 roi=17.24 roe=12.13 1/pe=15.28 rate=0.93 pb=0.74 dividend=3.2 yield=4.9% delta=32.07%
            "601088",  # 中国神华 roi=16.48 roe=13.77 1/pe=13.76 rate=0.87 pb=0.97 dividend=12.6 yield=7.22% delta=52.46%
            "000513",  # 丽珠集团 roi=16.09 roe=19.27 1/pe=5.25 rate=1.59 pb=3.47 dividend=11.5 yield=2.7% delta=51.36%
            "601611",  # 中国核建 roi=15.43 roe=16.62 1/pe=8.52 rate=1.09 pb=1.75 dividend=0.56 yield=0.79% delta=9.26%
            "600373",  # 中文传媒 roi=15.04 roe=12.91 1/pe=11.42 rate=1.02 pb=1.04 dividend=5.0 yield=4.47% delta=39.14%
            "601636",  # 旗滨集团 roi=14.97 roe=21.0 1/pe=5.13 rate=1.39 pb=3.65 dividend=3.0 yield=2.53% delta=49.32%
            "600056",  # 中国医药 roi=14.82 roe=16.53 1/pe=9.34 rate=0.96 pb=1.59 dividend=2.76 yield=1.86% delta=19.92%
            "601318",  # 中国平安 roi=14.72 roe=21.45 1/pe=8.58 rate=0.8 pb=2.26 dividend=21.0 yield=2.39% delta=27.92%
            "601800",  # 中国交建 roi=14.7 roe=10.17 1/pe=15.88 rate=0.91 pb=0.6 dividend=2.33 yield=3.11% delta=19.62%
            "000411",  # 英特集团 roi=14.08 roe=21.58 1/pe=6.59 rate=0.99 pb=3.01 dividend=0.61 yield=0.31% delta=4.73%
            "600036",  # 招商银行 roi=13.94 roe=16.49 1/pe=8.29 rate=1.02 pb=1.81 dividend=12.0 yield=2.7% delta=32.64%
            "601607",  # 上海医药 roi=13.38 roe=12.57 1/pe=9.42 rate=1.13 pb=1.23 dividend=4.4 yield=2.29% delta=24.31%
            "600298",  # 安琪酵母 roi=13.08 roe=27.21 1/pe=3.27 rate=1.47 pb=7.22 dividend=4.0 yield=0.83% delta=25.24%
            "601319",  # 中国人保 roi=12.69 roe=15.48 1/pe=9.53 rate=0.86 pb=1.47 dividend=1.52 yield=2.31% delta=24.21%
            "002142",  # 宁波银行 roi=12.24 roe=16.31 1/pe=6.82 rate=1.1 pb=2.1 dividend=5.0 yield=1.43% delta=20.89%
            "002508",  # 老板电器 roi=11.83 roe=26.01 1/pe=4.29 rate=1.06 pb=5.15 dividend=5.0 yield=1.23% delta=28.62%
            "600639",  # 浦东金桥 roi=11.67 roe=12.52 1/pe=7.9 rate=1.18 pb=1.44 dividend=3.1 yield=2.34% delta=29.66%
            "000582",  # 北部湾港 roi=11.17 roe=12.5 1/pe=6.98 rate=1.28 pb=1.71 dividend=1.77 yield=1.68% delta=24.12%
            "000333",  # 美的集团 roi=10.82 roe=25.33 1/pe=4.23 rate=1.01 pb=5.26 dividend=16.0 yield=1.89% delta=44.77%
            "600820",  # 隧道股份 roi=10.67 roe=9.52 1/pe=11.55 rate=0.97 pb=0.79 dividend=2.1 yield=3.74% delta=32.36%
            "000028",  # 国药一致 roi=10.54 roe=12.67 1/pe=7.7 rate=1.08 pb=1.51 dividend=6.0 yield=1.25% delta=16.28%
            "601336",  # 新华保险 roi=10.38 roe=15.87 1/pe=6.81 rate=0.96 pb=1.98 dividend=14.1 yield=2.36% delta=34.74%
            "600566",  # 济川药业 roi=10.35 roe=20.55 1/pe=6.63 rate=0.76 pb=2.62 dividend=12.3 yield=5.68% delta=85.56%
            "002415",  # 海康威视 roi=10.35 roe=32.02 1/pe=3.02 rate=1.07 pb=8.96 dividend=7.0 yield=1.53% delta=50.52%
            "000598",  # 兴蓉环境 roi=10.12 roe=10.98 1/pe=8.23 rate=1.12 pb=1.23 dividend=0.9 yield=1.81% delta=22.06%
            "002372",  # 伟星新材 roi=10.1 roe=28.57 1/pe=3.5 rate=1.01 pb=7.67 dividend=5.0 yield=2.68% delta=76.55%
            "600887",  # 伊利股份 roi=9.46 roe=30.23 1/pe=3.01 rate=1.04 pb=8.58 dividend=8.1 yield=2.02% delta=67.08%
            "600062",  # 华润双鹤 roi=9.4 roe=12.02 1/pe=8.15 rate=0.96 pb=1.36 dividend=3.04 yield=2.54% delta=31.15%
            "600900",  # 长江电力 roi=9.18 roe=16.04 1/pe=5.35 rate=1.07 pb=2.71 dividend=6.8 yield=3.44% delta=64.23%
            "600104",  # 上汽集团 roi=9.06 roe=11.78 1/pe=10.12 rate=0.76 pb=1.12 dividend=8.8 yield=3.61% delta=35.68%
            "601006",  # 大秦铁路 roi=8.65 roe=10.58 1/pe=12.02 rate=0.68 pb=0.84 dividend=4.8 yield=7.27% delta=60.53%
            "000828",  # 东莞控股 roi=8.6 roe=13.02 1/pe=8.58 rate=0.77 pb=1.4 dividend=3.0 yield=2.95% delta=34.36%
            "600519",  # 贵州茅台 roi=8.5 roe=37.85 1/pe=2.06 rate=1.09 pb=15.48 dividend=170.25 yield=0.93% delta=45.11%
            "601601",  # 中国太保 roi=8.46 roe=13.91 1/pe=6.99 rate=0.87 pb=1.77 dividend=12.0 yield=3.21% delta=45.93%
            "600197",  # 伊力特 roi=3.36 roe=14.17 1/pe=3.0 rate=0.79 pb=4.42 dividend=4.38 yield=1.61% delta=53.63%
            "600132",  # 重庆啤酒 roi=5.29 roe=46.43 1/pe=1.2 rate=0.95 pb=43.64 dividend=14.0 yield=1.29% delta=107.96%
            "002032",  # 苏 泊 尔 roi=7.94 roe=27.48 1/pe=2.98 rate=0.97 pb=8.93 dividend=13.3 yield=1.86% delta=62.42%
            "601088",  # 中国神华 roi=15.66 roe=13.77 1/pe=13.07 rate=0.87 pb=1.02 dividend=12.6 yield=6.86% delta=52.46%
            "601006",  # 大秦铁路 roi=8.54 roe=10.58 1/pe=11.87 rate=0.68 pb=0.85 dividend=4.8 yield=7.19% delta=60.53%
            "600028",  # 中国石化 roi=5.33 roe=6.71 1/pe=9.57 rate=0.83 pb=0.7 dividend=2.6 yield=6.19% delta=64.67%
            "600019",  # 宝钢股份 roi=5.1 roe=7.21 1/pe=8.84 rate=0.8 pb=0.79 dividend=2.8 yield=4.38% delta=49.56%
            "000039",  # 中集集团 roi=4.46 roe=8.05 1/pe=4.9 rate=1.13 pb=1.6 dividend=1.2 yield=0.77% delta=15.69%
            "600874",  # 创业环保 roi=7.41 roe=9.84 1/pe=6.33 rate=1.19 pb=1.46 dividend=1.07 yield=1.62% delta=25.63%
            "600690",  # 海尔智家 roi=7.36 roe=20.0 1/pe=5.33 rate=0.69 pb=3.41 dividend=3.75 yield=1.45% delta=27.16%
            "000568",  # 泸州老窖 roi=7.34 roe=30.26 1/pe=1.94 rate=1.25 pb=13.24 dividend=15.9 yield=0.8% delta=41.47%
            "600153",  # 建发股份 roi=143.26 roe=32.87 1/pe=36.32 rate=1.2 pb=0.78 dividend=5.0 yield=5.6% delta=15.42%
            "600325",  # 华发股份 roi=96.79 roe=29.05 1/pe=27.31 rate=1.22 pb=0.97 dividend=4.0 yield=6.32% delta=23.14%
            "600064",  # 南京高科 roi=46.89 roe=19.87 1/pe=17.48 rate=1.35 pb=1.0 dividend=4.5 yield=4.28% delta=24.47%
            "000999",  # 华润三九 roi=7.12 roe=13.96 1/pe=6.8 rate=0.75 pb=1.86 dividend=4.3 yield=1.65% delta=24.28%
            "000001",  # 平安银行 roi=7.11 roe=10.06 1/pe=7.36 rate=0.96 pb=1.27 dividend=2.18 yield=1.15% delta=15.68%
            "600511",  # 国药股份 roi=6.94 roe=17.37 1/pe=4.12 rate=0.97 pb=3.77 dividend=6.38 yield=1.16% delta=28.07%
            "600007",  # 中国国贸 roi=6.87 roe=11.54 1/pe=6.47 rate=0.92 pb=1.68 dividend=3.8 yield=2.93% delta=45.22%
            "600329",  # 中新药业 roi=6.78 roe=12.9 1/pe=4.82 rate=1.09 pb=2.49 dividend=3.0 yield=1.66% delta=34.37%
            "000756",  # 新华制药 roi=6.69 roe=11.58 1/pe=5.5 rate=1.05 pb=1.96 dividend=1.2 yield=1.23% delta=22.28%
            "000858",  # 五 粮 液 roi=6.63 roe=29.28 1/pe=1.92 rate=1.18 pb=13.2 dividend=22.0 yield=0.81% delta=42.01%
            "600486",  # 扬农化工 roi=6.56 roe=22.41 1/pe=3.08 rate=0.95 pb=6.32 dividend=6.5 yield=0.55% delta=17.91%
            "600513",  # 联环药业 roi=6.42 roe=11.55 1/pe=3.94 rate=1.41 pb=2.75 dividend=0.84 yield=0.84% delta=21.34%
            "600350",  # 山东高速 roi=6.37 roe=8.37 1/pe=7.77 rate=0.98 pb=1.09 dividend=3.8 yield=5.98% delta=76.98%
            "600563",  # 法拉电子 roi=6.2 roe=21.35 1/pe=2.44 rate=1.19 pb=7.98 dividend=13.0 yield=1.35% delta=55.52%
            "600741",  # 华域汽车 roi=6.18 roe=12.77 1/pe=6.72 rate=0.72 pb=1.82 dividend=8.5 yield=2.93% delta=43.62%
            "002287",  # 奇正藏药 roi=6.15 roe=19.2 1/pe=2.69 rate=1.19 pb=6.4 dividend=3.5 yield=1.21% delta=44.91%
            "000661",  # 长春高新 roi=6.04 roe=19.96 1/pe=1.99 rate=1.52 pb=15.09 dividend=10.0 yield=0.26% delta=13.29%
            "600332",  # 白云山 roi=6.02 roe=11.98 1/pe=5.91 rate=0.85 pb=1.89 dividend=5.89 yield=1.95% delta=33.08%
            "002507",  # 涪陵榨菜 roi=5.57 roe=25.17 1/pe=2.07 rate=1.07 pb=10.41 dividend=3.0 yield=0.7% delta=33.79%
            "601628",  # 中国人寿 roi=5.52 roe=12.78 1/pe=4.41 rate=0.98 pb=2.64 dividend=7.3 yield=1.87% delta=42.39%
            "600028",  # 中国石化 roi=5.51 roe=6.71 1/pe=9.9 rate=0.83 pb=0.67 dividend=2.6 yield=6.4% delta=64.67%
            "600019",  # 宝钢股份 roi=5.47 roe=7.21 1/pe=9.48 rate=0.8 pb=0.74 dividend=2.8 yield=4.7% delta=49.55%
            "600845",  # 宝信软件 roi=5.4 roe=18.64 1/pe=1.81 rate=1.6 pb=10.29 dividend=4.0 yield=0.65% delta=36.04%
            "600809",  # 山西汾酒 roi=5.31 roe=37.47 1/pe=1.05 rate=1.35 pb=28.17 dividend=9.0 yield=0.3% delta=28.86%
            "000538",  # 云南白药 roi=5.23 roe=13.05 1/pe=3.37 rate=1.19 pb=3.8 dividend=30.0 yield=2.65% delta=78.46%
            "603899",  # 晨光文具 roi=5.05 roe=29.17 1/pe=1.48 rate=1.17 pb=15.72 dividend=4.0 yield=0.48% delta=32.05%
            "603678",  # 火炬电子 roi=4.9 roe=17.4 1/pe=2.01 rate=1.4 pb=7.57 dividend=1.7 yield=0.29% delta=14.55%
            "002179",  # 中航光电 roi=4.85 roe=18.97 1/pe=2.08 rate=1.23 pb=7.39 dividend=1.5 yield=0.24% delta=11.48%
            "603369",  # 今世缘 roi=4.8 roe=21.18 1/pe=2.18 rate=1.04 pb=8.46 dividend=4.1 yield=0.76% delta=34.81%
            "600309",  # 万华化学 roi=4.77 roe=19.66 1/pe=3.15 rate=0.77 pb=5.73 dividend=13.0 yield=1.62% delta=51.45%
            "600132",  # 重庆啤酒 roi=4.68 roe=46.43 1/pe=1.06 rate=0.95 pb=49.17 dividend=14.0 yield=1.15% delta=107.96%
            "000039",  # 中集集团 roi=4.65 roe=8.05 1/pe=5.11 rate=1.13 pb=1.53 dividend=1.2 yield=0.8% delta=15.69%
            "002020",  # 京新药业 roi=4.65 roe=11.22 1/pe=5.31 rate=0.78 pb=2.16 dividend=3.5 yield=3.23% delta=60.78%
            "002304",  # 洋河股份 roi=4.51 roe=20.46 1/pe=2.45 rate=0.9 pb=7.93 dividend=30.0 yield=1.49% delta=60.91%
            "600597",  # 光明乳业 roi=4.35 roe=12.04 1/pe=3.38 rate=1.07 pb=3.28 dividend=1.3 yield=0.81% delta=24.1%
            "000651",  # 格力电器 roi=4.24 roe=16.27 1/pe=4.34 rate=0.6 pb=3.29 dividend=22.0 yield=3.51% delta=80.69%
            "600030",  # 中信证券 roi=3.98 roe=8.73 1/pe=4.0 rate=1.14 pb=2.07 dividend=5.0 yield=1.73% delta=43.36%
            "002025",  # 航天电器 roi=3.98 roe=16.77 1/pe=2.18 rate=1.09 pb=6.87 dividend=1.5 yield=0.29% delta=13.09%
            "000682",  # 东方电子 roi=3.95 roe=9.2 1/pe=4.21 rate=1.02 pb=2.06 dividend=0.38 yield=0.73% delta=17.32%
            "600271",  # 航天信息 roi=3.94 roe=13.02 1/pe=6.17 rate=0.49 pb=2.03 dividend=2.31 yield=1.83% delta=29.7%
            "603288",  # 海天味业 roi=3.93 roe=33.72 1/pe=0.97 rate=1.2 pb=34.51 dividend=10.8 yield=0.56% delta=57.41%
            "000547",  # 航天发展 roi=3.88 roe=11.27 1/pe=2.34 rate=1.47 pb=4.47 dividend=0.88 yield=0.39% delta=16.83%
            "600085",  # 同仁堂 roi=3.75 roe=13.3 1/pe=3.81 rate=0.74 pb=3.58 dividend=2.6 yield=1.04% delta=27.38%
            "600363",  # 联创光电 roi=3.69 roe=11.12 1/pe=2.72 rate=1.22 pb=3.76 dividend=0.45 yield=0.19% delta=6.96%
            "600436",  # 片仔癀 roi=3.37 roe=25.78 1/pe=1.08 rate=1.21 pb=19.88 dividend=8.2 yield=0.33% delta=30.56%
            "600197",  # 伊力特 roi=3.36 roe=14.17 1/pe=3.0 rate=0.79 pb=4.42 dividend=4.38 yield=1.61% delta=53.63%
            "002007",  # 华兰生物 roi=3.16 roe=17.69 1/pe=1.82 rate=0.98 pb=11.3 dividend=4.0 yield=0.93% delta=51.0%
            "600377",  # 宁沪高速 roi=3.04 roe=9.37 1/pe=5.5 rate=0.59 pb=1.7 dividend=4.6 yield=4.92% delta=89.41%
            "000596",  # 古井贡酒 roi=2.76 roe=22.23 1/pe=1.46 rate=0.85 pb=13.42 dividend=15.0 yield=0.58% delta=39.57%
            "000501",  # 鄂武商Ａ roi=2.42 roe=6.73 1/pe=6.41 rate=0.56 pb=0.99 dividend=2.2 yield=1.78% delta=27.78%
            "600600",  # 青岛啤酒 roi=2.07 roe=11.51 1/pe=1.58 rate=1.14 pb=6.89 dividend=5.5 yield=0.51% delta=32.44%
            "600763",  # 通策医疗 roi=1.81 roe=29.13 1/pe=0.62 rate=1.0 pb=37.28 dividend=0.0 yield=0.0% delta=0.0%
            "600498",  # 烽火通信 roi=1.4 roe=6.85 1/pe=2.56 rate=0.8 pb=2.58 dividend=3.4 yield=1.45% delta=56.72%
            "600897",  # 厦门空港 roi=1.26 roe=6.46 1/pe=4.55 rate=0.43 pb=1.4 dividend=5.23 yield=3.04% delta=66.68%
            "601888",  # 中国中免 roi=1.11 roe=18.79 1/pe=0.88 rate=0.67 pb=21.22 dividend=7.2 yield=0.34% delta=38.41%
            "000733",  # 振华科技 roi=1.07 roe=6.57 1/pe=1.57 rate=1.04 pb=3.94 dividend=0.5 yield=0.11% delta=7.29%
            "000777",  # 中核科技 roi=1.02 roe=6.91 1/pe=2.11 rate=0.7 pb=3.15 dividend=1.07 yield=0.88% delta=41.82%
            "000429",  # 粤高速Ａ roi=0.91 roe=6.18 1/pe=4.34 rate=0.34 pb=1.49 dividend=4.22 yield=6.45% delta=148.84%
            "600548",  # 深高速 roi=0.37 roe=4.58 1/pe=4.25 rate=0.19 pb=1.08 dividend=5.2 yield=5.85% delta=137.64%
            "600004",  # 白云机场 roi=0.01 roe=0.86 1/pe=0.46 rate=0.19 pb=1.84 dividend=1.45 yield=1.02% delta=219.53%
            "600009",  # 上海机场 roi=0.0 roe=1.33 1/pe=0.28 rate=0.08 pb=4.94 dividend=7.9 yield=1.04% delta=369.28%
            "000089",  # 深圳机场 roi=0.0 roe=0.53 1/pe=0.37 rate=0.11 pb=1.45 dividend=0.8 yield=0.95% delta=257.05%
            "600676",  # 交运股份 roi=-0.51 roe=-2.62 1/pe=-3.11 rate=-0.63 pb=0.87 dividend=0.4 yield=0.84% delta=0.0%
            "000423",  # 东阿阿胶 roi=-0.98 roe=-6.34 1/pe=-2.45 rate=-0.63 pb=2.85 dividend=2.03 yield=0.48% delta=0.0%

            #ROI 排序
            "600846",  # 同济科技 roi=148.26 roe=44.1 1/pe=21.55 rate=1.56 pb=1.7 dividend=3.4 yield=4.14% delta=19.21%
            "600153",  # 建发股份 roi=143.26 roe=32.87 1/pe=36.32 rate=1.2 pb=0.78 dividend=5.0 yield=5.6% delta=15.42%
            "000789",  # 万年青 roi=122.66 roe=49.92 1/pe=20.14 rate=1.22 pb=1.98 dividend=7.0 yield=5.09% delta=25.28%
            "600383",  # 金地集团 roi=108.3 roe=33.14 1/pe=25.53 rate=1.28 pb=1.21 dividend=6.7 yield=4.75% delta=18.61%
            "600325",  # 华发股份 roi=96.79 roe=29.05 1/pe=27.31 rate=1.22 pb=0.97 dividend=4.0 yield=6.32% delta=23.14%
            "600606",  # 绿地控股 roi=92.4 roe=29.17 1/pe=29.33 rate=1.08 pb=0.93 dividend=4.0 yield=6.5% delta=22.17%
            "601668",  # 中国建筑 roi=90.06 roe=27.16 1/pe=30.99 rate=1.07 pb=0.76 dividend=1.85 yield=3.63% delta=11.73%
            "600048",  # 保利地产 roi=78.62 roe=31.33 1/pe=19.76 rate=1.27 pb=1.33 dividend=8.2 yield=5.06% delta=25.6%
            "600720",  # 祁连山 roi=58.95 roe=26.41 1/pe=15.83 rate=1.41 pb=1.41 dividend=5.8 yield=4.08% delta=25.8%
            "000951",  # 中国重汽 roi=58.85 roe=34.08 1/pe=10.34 rate=1.67 pb=2.74 dividend=5.5 yield=1.7% delta=16.45%
            "000002",  # 万 科Ａ roi=56.02 roe=32.92 1/pe=16.85 rate=1.01 pb=1.66 dividend=10.17 yield=3.52% delta=20.87%
            "000921",  # 海信家电 roi=51.24 roe=28.9 1/pe=11.82 rate=1.5 pb=2.2 dividend=3.95 yield=2.66% delta=22.5%
            "000069",  # 华侨城Ａ roi=49.62 roe=20.79 1/pe=23.4 rate=1.02 pb=0.79 dividend=3.05 yield=4.52% delta=19.31%
            "000786",  # 北新建材 roi=48.19 roe=19.19 1/pe=4.13 rate=6.08 pb=3.97 dividend=0.82 yield=0.22% delta=5.35%
            "600064",  # 南京高科 roi=46.89 roe=19.87 1/pe=17.48 rate=1.35 pb=1.0 dividend=4.5 yield=4.28% delta=24.47%
            "600755",  # 厦门国贸 roi=46.4 roe=20.34 1/pe=20.93 rate=1.09 pb=0.89 dividend=2.3 yield=3.33% delta=15.93%
            "601390",  # 中国中铁 roi=43.43 roe=15.44 1/pe=20.99 rate=1.34 pb=0.66 dividend=1.69 yield=3.11% delta=14.8%
            "001979",  # 招商蛇口 roi=40.93 roe=25.17 1/pe=15.34 rate=1.06 pb=1.5 dividend=8.3 yield=6.14% delta=40.01%
            "000529",  # 广弘控股 roi=37.95 roe=24.46 1/pe=9.46 rate=1.64 pb=2.19 dividend=1.0 yield=1.41% delta=14.92%
            "600585",  # 海螺水泥 roi=37.74 roe=27.86 1/pe=12.9 rate=1.05 pb=1.82 dividend=20.0 yield=3.84% delta=29.81%
            "600068",  # 葛洲坝 roi=33.24 roe=19.79 1/pe=18.87 rate=0.89 pb=0.94 dividend=1.56 yield=2.36% delta=12.53%
            "601186",  # 中国铁建 roi=33.18 roe=14.67 1/pe=21.14 rate=1.07 pb=0.62 dividend=2.1 yield=2.55% delta=12.07%
            "000498",  # 山东路桥 roi=32.6 roe=15.71 1/pe=14.93 rate=1.39 pb=0.94 dividend=0.8 yield=1.61% delta=10.76%
            "600663",  # 陆家嘴 roi=31.75 roe=28.58 1/pe=10.58 rate=1.05 pb=2.47 dividend=4.56 yield=4.02% delta=38.0%
            "600461",  # 洪城水业 roi=29.56 roe=16.98 1/pe=12.09 rate=1.44 pb=1.25 dividend=2.6 yield=3.9% delta=32.24%
            "601669",  # 中国电建 roi=28.11 roe=13.69 1/pe=19.19 rate=1.07 pb=0.67 dividend=0.4 yield=1.03% delta=5.34%
            "000581",  # 威孚高科 roi=26.51 roe=17.14 1/pe=11.63 rate=1.33 pb=1.37 dividend=11.0 yield=4.58% delta=39.37%
            "601009",  # 南京银行 roi=23.62 roe=14.49 1/pe=15.98 rate=1.02 pb=0.85 dividend=3.92 yield=4.91% delta=30.75%
            "600612",  # 老凤祥 roi=22.82 roe=28.21 1/pe=7.63 rate=1.06 pb=3.27 dividend=11.5 yield=2.4% delta=31.46%
            "000877",  # 天山股份 roi=22.24 roe=19.31 1/pe=11.18 rate=1.03 pb=1.55 dividend=5.1 yield=3.37% delta=30.12%
            "601988",  # 中国银行 roi=21.13 roe=11.47 1/pe=19.81 rate=0.93 pb=0.55 dividend=1.91 yield=5.97% delta=30.13%
            "000049",  # 德赛电池 roi=20.76 roe=31.89 1/pe=6.2 rate=1.05 pb=4.19 dividend=7.0 yield=1.37% delta=22.08%
            "601328",  # 交通银行 roi=20.3 roe=10.48 1/pe=21.05 rate=0.92 pb=0.47 dividend=3.15 yield=6.95% delta=33.04%
            "000895",  # 双汇发展 roi=19.83 roe=41.58 1/pe=3.91 rate=1.22 pb=6.83 dividend=16.4 yield=3.37% delta=86.18%
            "601288",  # 农业银行 roi=18.65 roe=11.47 1/pe=17.48 rate=0.93 pb=0.61 dividend=1.82 yield=5.65% delta=32.33%
            "601398",  # 工商银行 roi=18.06 roe=12.02 1/pe=16.16 rate=0.93 pb=0.7 dividend=2.63 yield=5.21% delta=32.23%
            "601939",  # 建设银行 roi=17.24 roe=12.13 1/pe=15.28 rate=0.93 pb=0.74 dividend=3.2 yield=4.9% delta=32.07%
            "601088",  # 中国神华 roi=16.48 roe=13.77 1/pe=13.76 rate=0.87 pb=0.97 dividend=12.6 yield=7.22% delta=52.46%
            "601611",  # 中国核建 roi=15.43 roe=16.62 1/pe=8.52 rate=1.09 pb=1.75 dividend=0.56 yield=0.79% delta=9.26%
            "600373",  # 中文传媒 roi=15.04 roe=12.91 1/pe=11.42 rate=1.02 pb=1.04 dividend=5.0 yield=4.47% delta=39.14%
            "600056",  # 中国医药 roi=14.82 roe=16.53 1/pe=9.34 rate=0.96 pb=1.59 dividend=2.76 yield=1.86% delta=19.92%
            "601318",  # 中国平安 roi=14.72 roe=21.45 1/pe=8.58 rate=0.8 pb=2.26 dividend=21.0 yield=2.39% delta=27.92%
            "601800",  # 中国交建 roi=14.7 roe=10.17 1/pe=15.88 rate=0.91 pb=0.6 dividend=2.33 yield=3.11% delta=19.62%
            "000411",  # 英特集团 roi=14.08 roe=21.58 1/pe=6.59 rate=0.99 pb=3.01 dividend=0.61 yield=0.31% delta=4.73%
            "600036",  # 招商银行 roi=13.94 roe=16.49 1/pe=8.29 rate=1.02 pb=1.81 dividend=12.0 yield=2.7% delta=32.64%
            "601607",  # 上海医药 roi=13.38 roe=12.57 1/pe=9.42 rate=1.13 pb=1.23 dividend=4.4 yield=2.29% delta=24.31%
            "600298",  # 安琪酵母 roi=13.08 roe=27.21 1/pe=3.27 rate=1.47 pb=7.22 dividend=4.0 yield=0.83% delta=25.24%
            "601319",  # 中国人保 roi=12.69 roe=15.48 1/pe=9.53 rate=0.86 pb=1.47 dividend=1.52 yield=2.31% delta=24.21%
            "002142",  # 宁波银行 roi=12.24 roe=16.31 1/pe=6.82 rate=1.1 pb=2.1 dividend=5.0 yield=1.43% delta=20.89%
            "600639",  # 浦东金桥 roi=11.67 roe=12.52 1/pe=7.9 rate=1.18 pb=1.44 dividend=3.1 yield=2.34% delta=29.66%
            "000582",  # 北部湾港 roi=11.17 roe=12.5 1/pe=6.98 rate=1.28 pb=1.71 dividend=1.77 yield=1.68% delta=24.12%
            "600820",  # 隧道股份 roi=10.67 roe=9.52 1/pe=11.55 rate=0.97 pb=0.79 dividend=2.1 yield=3.74% delta=32.36%
            "000028",  # 国药一致 roi=10.54 roe=12.67 1/pe=7.7 rate=1.08 pb=1.51 dividend=6.0 yield=1.25% delta=16.28%
            "601336",  # 新华保险 roi=10.38 roe=15.87 1/pe=6.81 rate=0.96 pb=1.98 dividend=14.1 yield=2.36% delta=34.74%
            "002415",  # 海康威视 roi=10.35 roe=32.02 1/pe=3.02 rate=1.07 pb=8.96 dividend=7.0 yield=1.53% delta=50.52%
            "000598",  # 兴蓉环境 roi=10.12 roe=10.98 1/pe=8.23 rate=1.12 pb=1.23 dividend=0.9 yield=1.81% delta=22.06%
            "600887",  # 伊利股份 roi=9.46 roe=30.23 1/pe=3.01 rate=1.04 pb=8.58 dividend=8.1 yield=2.02% delta=67.08%
            "600062",  # 华润双鹤 roi=9.4 roe=12.02 1/pe=8.15 rate=0.96 pb=1.36 dividend=3.04 yield=2.54% delta=31.15%
            "600900",  # 长江电力 roi=9.18 roe=16.04 1/pe=5.35 rate=1.07 pb=2.71 dividend=6.8 yield=3.44% delta=64.23%
            "600104",  # 上汽集团 roi=9.06 roe=11.78 1/pe=10.12 rate=0.76 pb=1.12 dividend=8.8 yield=3.61% delta=35.68%
            "601006",  # 大秦铁路 roi=8.65 roe=10.58 1/pe=12.02 rate=0.68 pb=0.84 dividend=4.8 yield=7.27% delta=60.53%
            "000828",  # 东莞控股 roi=8.6 roe=13.02 1/pe=8.58 rate=0.77 pb=1.4 dividend=3.0 yield=2.95% delta=34.36%
            "600519",  # 贵州茅台 roi=8.5 roe=37.85 1/pe=2.06 rate=1.09 pb=15.48 dividend=170.25 yield=0.93% delta=45.11%
            "601601",  # 中国太保 roi=8.46 roe=13.91 1/pe=6.99 rate=0.87 pb=1.77 dividend=12.0 yield=3.21% delta=45.93%
            "600874",  # 创业环保 roi=7.41 roe=9.84 1/pe=6.33 rate=1.19 pb=1.46 dividend=1.07 yield=1.62% delta=25.63%
            "600690",  # 海尔智家 roi=7.36 roe=20.0 1/pe=5.33 rate=0.69 pb=3.41 dividend=3.75 yield=1.45% delta=27.16%
            "000568",  # 泸州老窖 roi=7.34 roe=30.26 1/pe=1.94 rate=1.25 pb=13.24 dividend=15.9 yield=0.8% delta=41.47%
            "000999",  # 华润三九 roi=7.12 roe=13.96 1/pe=6.8 rate=0.75 pb=1.86 dividend=4.3 yield=1.65% delta=24.28%
            "000001",  # 平安银行 roi=7.11 roe=10.06 1/pe=7.36 rate=0.96 pb=1.27 dividend=2.18 yield=1.15% delta=15.68%
            "600511",  # 国药股份 roi=6.94 roe=17.37 1/pe=4.12 rate=0.97 pb=3.77 dividend=6.38 yield=1.16% delta=28.07%
            "600007",  # 中国国贸 roi=6.87 roe=11.54 1/pe=6.47 rate=0.92 pb=1.68 dividend=3.8 yield=2.93% delta=45.22%
            "600329",  # 中新药业 roi=6.78 roe=12.9 1/pe=4.82 rate=1.09 pb=2.49 dividend=3.0 yield=1.66% delta=34.37%
            "000756",  # 新华制药 roi=6.69 roe=11.58 1/pe=5.5 rate=1.05 pb=1.96 dividend=1.2 yield=1.23% delta=22.28%
            "000858",  # 五 粮 液 roi=6.63 roe=29.28 1/pe=1.92 rate=1.18 pb=13.2 dividend=22.0 yield=0.81% delta=42.01%
            "600486",  # 扬农化工 roi=6.56 roe=22.41 1/pe=3.08 rate=0.95 pb=6.32 dividend=6.5 yield=0.55% delta=17.91%
            "600513",  # 联环药业 roi=6.42 roe=11.55 1/pe=3.94 rate=1.41 pb=2.75 dividend=0.84 yield=0.84% delta=21.34%
            "600350",  # 山东高速 roi=6.37 roe=8.37 1/pe=7.77 rate=0.98 pb=1.09 dividend=3.8 yield=5.98% delta=76.98%
            "600563",  # 法拉电子 roi=6.2 roe=21.35 1/pe=2.44 rate=1.19 pb=7.98 dividend=13.0 yield=1.35% delta=55.52%
            "600741",  # 华域汽车 roi=6.18 roe=12.77 1/pe=6.72 rate=0.72 pb=1.82 dividend=8.5 yield=2.93% delta=43.62%
            "000661",  # 长春高新 roi=6.04 roe=19.96 1/pe=1.99 rate=1.52 pb=15.09 dividend=10.0 yield=0.26% delta=13.29%
            "600332",  # 白云山 roi=6.02 roe=11.98 1/pe=5.91 rate=0.85 pb=1.89 dividend=5.89 yield=1.95% delta=33.08%
            "002507",  # 涪陵榨菜 roi=5.57 roe=25.17 1/pe=2.07 rate=1.07 pb=10.41 dividend=3.0 yield=0.7% delta=33.79%
            "601628",  # 中国人寿 roi=5.52 roe=12.78 1/pe=4.41 rate=0.98 pb=2.64 dividend=7.3 yield=1.87% delta=42.39%
            "600028",  # 中国石化 roi=5.51 roe=6.71 1/pe=9.9 rate=0.83 pb=0.67 dividend=2.6 yield=6.4% delta=64.67%
            "600019",  # 宝钢股份 roi=5.47 roe=7.21 1/pe=9.48 rate=0.8 pb=0.74 dividend=2.8 yield=4.7% delta=49.55%
            "600845",  # 宝信软件 roi=5.4 roe=18.64 1/pe=1.81 rate=1.6 pb=10.29 dividend=4.0 yield=0.65% delta=36.04%
            "600809",  # 山西汾酒 roi=5.31 roe=37.47 1/pe=1.05 rate=1.35 pb=28.17 dividend=9.0 yield=0.3% delta=28.86%
            "000538",  # 云南白药 roi=5.23 roe=13.05 1/pe=3.37 rate=1.19 pb=3.8 dividend=30.0 yield=2.65% delta=78.46%
            "002179",  # 中航光电 roi=4.85 roe=18.97 1/pe=2.08 rate=1.23 pb=7.39 dividend=1.5 yield=0.24% delta=11.48%
            "603369",  # 今世缘 roi=4.8 roe=21.18 1/pe=2.18 rate=1.04 pb=8.46 dividend=4.1 yield=0.76% delta=34.81%
            "600309",  # 万华化学 roi=4.77 roe=19.66 1/pe=3.15 rate=0.77 pb=5.73 dividend=13.0 yield=1.62% delta=51.45%
            "600132",  # 重庆啤酒 roi=4.68 roe=46.43 1/pe=1.06 rate=0.95 pb=49.17 dividend=14.0 yield=1.15% delta=107.96%
            "000039",  # 中集集团 roi=4.65 roe=8.05 1/pe=5.11 rate=1.13 pb=1.53 dividend=1.2 yield=0.8% delta=15.69%
            "002304",  # 洋河股份 roi=4.51 roe=20.46 1/pe=2.45 rate=0.9 pb=7.93 dividend=30.0 yield=1.49% delta=60.91%
            "600597",  # 光明乳业 roi=4.35 roe=12.04 1/pe=3.38 rate=1.07 pb=3.28 dividend=1.3 yield=0.81% delta=24.1%
            "000651",  # 格力电器 roi=4.24 roe=16.27 1/pe=4.34 rate=0.6 pb=3.29 dividend=22.0 yield=3.51% delta=80.69%
            "600030",  # 中信证券 roi=3.98 roe=8.73 1/pe=4.0 rate=1.14 pb=2.07 dividend=5.0 yield=1.73% delta=43.36%
            "002025",  # 航天电器 roi=3.98 roe=16.77 1/pe=2.18 rate=1.09 pb=6.87 dividend=1.5 yield=0.29% delta=13.09%
            "000682",  # 东方电子 roi=3.95 roe=9.2 1/pe=4.21 rate=1.02 pb=2.06 dividend=0.38 yield=0.73% delta=17.32%
            "600271",  # 航天信息 roi=3.94 roe=13.02 1/pe=6.17 rate=0.49 pb=2.03 dividend=2.31 yield=1.83% delta=29.7%
            "603288",  # 海天味业 roi=3.93 roe=33.72 1/pe=0.97 rate=1.2 pb=34.51 dividend=10.8 yield=0.56% delta=57.41%
            "000547",  # 航天发展 roi=3.88 roe=11.27 1/pe=2.34 rate=1.47 pb=4.47 dividend=0.88 yield=0.39% delta=16.83%
            "600085",  # 同仁堂 roi=3.75 roe=13.3 1/pe=3.81 rate=0.74 pb=3.58 dividend=2.6 yield=1.04% delta=27.38%
            "600436",  # 片仔癀 roi=3.37 roe=25.78 1/pe=1.08 rate=1.21 pb=19.88 dividend=8.2 yield=0.33% delta=30.56%
            "600197",  # 伊力特 roi=3.36 roe=14.17 1/pe=3.0 rate=0.79 pb=4.42 dividend=4.38 yield=1.61% delta=53.63%
            "600377",  # 宁沪高速 roi=3.04 roe=9.37 1/pe=5.5 rate=0.59 pb=1.7 dividend=4.6 yield=4.92% delta=89.41%
            "000596",  # 古井贡酒 roi=2.76 roe=22.23 1/pe=1.46 rate=0.85 pb=13.42 dividend=15.0 yield=0.58% delta=39.57%
            "000501",  # 鄂武商Ａ roi=2.42 roe=6.73 1/pe=6.41 rate=0.56 pb=0.99 dividend=2.2 yield=1.78% delta=27.78%
            "600600",  # 青岛啤酒 roi=2.07 roe=11.51 1/pe=1.58 rate=1.14 pb=6.89 dividend=5.5 yield=0.51% delta=32.44%
            "600498",  # 烽火通信 roi=1.4 roe=6.85 1/pe=2.56 rate=0.8 pb=2.58 dividend=3.4 yield=1.45% delta=56.72%
            "600897",  # 厦门空港 roi=1.26 roe=6.46 1/pe=4.55 rate=0.43 pb=1.4 dividend=5.23 yield=3.04% delta=66.68%
            "601888",  # 中国中免 roi=1.11 roe=18.79 1/pe=0.88 rate=0.67 pb=21.22 dividend=7.2 yield=0.34% delta=38.41%
            "000733",  # 振华科技 roi=1.07 roe=6.57 1/pe=1.57 rate=1.04 pb=3.94 dividend=0.5 yield=0.11% delta=7.29%
            "000777",  # 中核科技 roi=1.02 roe=6.91 1/pe=2.11 rate=0.7 pb=3.15 dividend=1.07 yield=0.88% delta=41.82%
            "000429",  # 粤高速Ａ roi=0.91 roe=6.18 1/pe=4.34 rate=0.34 pb=1.49 dividend=4.22 yield=6.45% delta=148.84%
            "600548",  # 深高速 roi=0.37 roe=4.58 1/pe=4.25 rate=0.19 pb=1.08 dividend=5.2 yield=5.85% delta=137.64%
            "600004",  # 白云机场 roi=0.01 roe=0.86 1/pe=0.46 rate=0.19 pb=1.84 dividend=1.45 yield=1.02% delta=219.53%
            "600009",  # 上海机场 roi=0.0 roe=1.33 1/pe=0.28 rate=0.08 pb=4.94 dividend=7.9 yield=1.04% delta=369.28%
            "000089",  # 深圳机场 roi=0.0 roe=0.53 1/pe=0.37 rate=0.11 pb=1.45 dividend=0.8 yield=0.95% delta=257.05%
            "600676",  # 交运股份 roi=-0.51 roe=-2.62 1/pe=-3.11 rate=-0.63 pb=0.87 dividend=0.4 yield=0.84% delta=0.0%
            "000423",  # 东阿阿胶 roi=-0.98 roe=-6.34 1/pe=-2.45 rate=-0.63 pb=2.85 dividend=2.03 yield=0.48% delta=0.0%

            "600846",  # 同济科技 roi=148.12 roe=44.1 1/pe=21.53 rate=1.56 pb=1.71 dividend=3.4 yield=4.14% delta=19.21%
            "600153",  # 建发股份 roi=146.38 roe=32.87 1/pe=37.11 rate=1.2 pb=0.76 dividend=5.0 yield=5.72% delta=15.42%
            "000789",  # 万年青 roi=120.28 roe=49.92 1/pe=19.75 rate=1.22 pb=2.02 dividend=7.0 yield=4.99% delta=25.28%
            "600383",  # 金地集团 roi=111.69 roe=33.14 1/pe=26.33 rate=1.28 pb=1.18 dividend=6.7 yield=4.9% delta=18.61%
            "600325",  # 华发股份 roi=98.49 roe=29.05 1/pe=27.79 rate=1.22 pb=0.95 dividend=4.0 yield=6.43% delta=23.14%
            "600606",  # 绿地控股 roi=93.16 roe=29.17 1/pe=29.57 rate=1.08 pb=0.92 dividend=4.0 yield=6.56% delta=22.17%
            "601668",  # 中国建筑 roi=89.16 roe=27.16 1/pe=30.68 rate=1.07 pb=0.77 dividend=1.85 yield=3.6% delta=11.73%
            "600048",  # 保利地产 roi=79.38 roe=31.33 1/pe=19.95 rate=1.27 pb=1.32 dividend=8.2 yield=5.11% delta=25.6%
            "000951",  # 中国重汽 roi=59.47 roe=34.08 1/pe=10.45 rate=1.67 pb=2.71 dividend=5.5 yield=1.72% delta=16.45%
            "600720",  # 祁连山 roi=57.98 roe=26.41 1/pe=15.57 rate=1.41 pb=1.43 dividend=5.8 yield=4.02% delta=25.8%
            "000002",  # 万 科Ａ roi=56.86 roe=32.92 1/pe=17.1 rate=1.01 pb=1.63 dividend=10.17 yield=3.57% delta=20.87%
            "000921",  # 海信家电 roi=51.85 roe=28.9 1/pe=11.96 rate=1.5 pb=2.18 dividend=3.95 yield=2.69% delta=22.5%
            "000786",  # 北新建材 roi=50.05 roe=19.19 1/pe=4.29 rate=6.08 pb=3.82 dividend=0.82 yield=0.23% delta=5.35%
            "000069",  # 华侨城Ａ roi=48.96 roe=20.79 1/pe=23.09 rate=1.02 pb=0.8 dividend=3.05 yield=4.46% delta=19.31%
            "600064",  # 南京高科 roi=47.8 roe=19.87 1/pe=17.82 rate=1.35 pb=0.98 dividend=4.5 yield=4.36% delta=24.47%
            "600755",  # 厦门国贸 roi=46.47 roe=20.34 1/pe=20.96 rate=1.09 pb=0.89 dividend=2.3 yield=3.34% delta=15.93%
            "601390",  # 中国中铁 roi=43.12 roe=15.44 1/pe=20.84 rate=1.34 pb=0.67 dividend=1.69 yield=3.08% delta=14.8%
            "001979",  # 招商蛇口 roi=41.09 roe=25.17 1/pe=15.4 rate=1.06 pb=1.5 dividend=8.3 yield=6.16% delta=40.01%
            "000529",  # 广弘控股 roi=38.51 roe=24.46 1/pe=9.6 rate=1.64 pb=2.16 dividend=1.0 yield=1.43% delta=14.92%
            "600585",  # 海螺水泥 roi=36.92 roe=27.86 1/pe=12.62 rate=1.05 pb=1.86 dividend=20.0 yield=3.76% delta=29.81%
            "601186",  # 中国铁建 roi=33.47 roe=14.67 1/pe=21.32 rate=1.07 pb=0.62 dividend=2.1 yield=2.57% delta=12.07%
            "600068",  # 葛洲坝 roi=33.38 roe=19.79 1/pe=18.95 rate=0.89 pb=0.94 dividend=1.56 yield=2.37% delta=12.53%
            "600801",  # 华新水泥 roi=32.81 roe=30.64 1/pe=12.9 rate=0.83 pb=2.14 dividend=12.1 yield=5.38% delta=41.72%
            "000498",  # 山东路桥 roi=32.43 roe=15.71 1/pe=14.85 rate=1.39 pb=0.95 dividend=0.8 yield=1.6% delta=10.76%
            "600663",  # 陆家嘴 roi=31.99 roe=28.58 1/pe=10.66 rate=1.05 pb=2.45 dividend=4.56 yield=4.05% delta=38.0%
            "600461",  # 洪城水业 roi=29.56 roe=16.98 1/pe=12.09 rate=1.44 pb=1.25 dividend=2.6 yield=3.9% delta=32.24%
            "601669",  # 中国电建 roi=27.41 roe=13.69 1/pe=18.71 rate=1.07 pb=0.69 dividend=0.4 yield=1.0% delta=5.34%
            "000581",  # 威孚高科 roi=26.81 roe=17.14 1/pe=11.76 rate=1.33 pb=1.35 dividend=11.0 yield=4.63% delta=39.37%
            "601009",  # 南京银行 roi=23.65 roe=14.49 1/pe=16.0 rate=1.02 pb=0.85 dividend=3.92 yield=4.92% delta=30.75%
            "600612",  # 老凤祥 roi=23.23 roe=28.21 1/pe=7.77 rate=1.06 pb=3.21 dividend=11.5 yield=2.44% delta=31.46%
            "600668",  # 尖峰集团 roi=21.62 roe=18.76 1/pe=13.72 rate=0.84 pb=1.17 dividend=3.0 yield=2.07% delta=15.11%
            "601988",  # 中国银行 roi=21.27 roe=11.47 1/pe=19.94 rate=0.93 pb=0.54 dividend=1.91 yield=6.01% delta=30.13%
            "000877",  # 天山股份 roi=21.12 roe=19.31 1/pe=10.62 rate=1.03 pb=1.63 dividend=5.1 yield=3.2% delta=30.12%
            "000049",  # 德赛电池 roi=20.49 roe=31.89 1/pe=6.12 rate=1.05 pb=4.25 dividend=7.0 yield=1.35% delta=22.08%
            "601328",  # 交通银行 roi=20.38 roe=10.48 1/pe=21.14 rate=0.92 pb=0.47 dividend=3.15 yield=6.98% delta=33.04%
            "000895",  # 双汇发展 roi=20.24 roe=41.58 1/pe=3.99 rate=1.22 pb=6.7 dividend=16.4 yield=3.44% delta=86.18%
            "601288",  # 农业银行 roi=18.94 roe=11.47 1/pe=17.76 rate=0.93 pb=0.61 dividend=1.82 yield=5.74% delta=32.33%
            "601398",  # 工商银行 roi=18.24 roe=12.02 1/pe=16.32 rate=0.93 pb=0.69 dividend=2.63 yield=5.26% delta=32.23%
            "601939",  # 建设银行 roi=17.56 roe=12.13 1/pe=15.57 rate=0.93 pb=0.73 dividend=3.2 yield=4.99% delta=32.07%
            "600373",  # 中文传媒 roi=15.51 roe=12.91 1/pe=11.78 rate=1.02 pb=1.01 dividend=5.0 yield=4.61% delta=39.14%
            "601611",  # 中国核建 roi=15.22 roe=16.62 1/pe=8.4 rate=1.09 pb=1.77 dividend=0.56 yield=0.78% delta=9.26%
            "601088",  # 中国神华 roi=15.08 roe=13.77 1/pe=12.59 rate=0.87 pb=1.06 dividend=12.6 yield=6.61% delta=52.46%
            "600056",  # 中国医药 roi=14.87 roe=16.53 1/pe=9.37 rate=0.96 pb=1.59 dividend=2.76 yield=1.87% delta=19.92%
            "601800",  # 中国交建 roi=14.84 roe=10.17 1/pe=16.03 rate=0.91 pb=0.59 dividend=2.33 yield=3.14% delta=19.62%
            "601318",  # 中国平安 roi=14.71 roe=21.45 1/pe=8.57 rate=0.8 pb=2.26 dividend=21.0 yield=2.39% delta=27.92%
            "000411",  # 英特集团 roi=14.38 roe=21.58 1/pe=6.73 rate=0.99 pb=2.94 dividend=0.61 yield=0.32% delta=4.73%
            "600036",  # 招商银行 roi=14.35 roe=16.49 1/pe=8.53 rate=1.02 pb=1.76 dividend=12.0 yield=2.78% delta=32.64%
            "601607",  # 上海医药 roi=13.35 roe=12.57 1/pe=9.4 rate=1.13 pb=1.23 dividend=4.4 yield=2.28% delta=24.31%
            "600298",  # 安琪酵母 roi=12.92 roe=27.21 1/pe=3.23 rate=1.47 pb=7.31 dividend=4.0 yield=0.82% delta=25.24%
            "601319",  # 中国人保 roi=12.75 roe=15.48 1/pe=9.58 rate=0.86 pb=1.46 dividend=1.52 yield=2.32% delta=24.21%
            "002142",  # 宁波银行 roi=12.43 roe=16.31 1/pe=6.93 rate=1.1 pb=2.06 dividend=5.0 yield=1.45% delta=20.89%
            "600639",  # 浦东金桥 roi=11.69 roe=12.52 1/pe=7.91 rate=1.18 pb=1.44 dividend=3.1 yield=2.35% delta=29.66%
            "000582",  # 北部湾港 roi=11.3 roe=12.5 1/pe=7.06 rate=1.28 pb=1.7 dividend=1.77 yield=1.7% delta=24.12%
            "000028",  # 国药一致 roi=10.7 roe=12.67 1/pe=7.82 rate=1.08 pb=1.49 dividend=6.0 yield=1.27% delta=16.28%
            "600820",  # 隧道股份 roi=10.65 roe=9.52 1/pe=11.53 rate=0.97 pb=0.79 dividend=2.1 yield=3.73% delta=32.36%
            "601336",  # 新华保险 roi=10.44 roe=15.87 1/pe=6.85 rate=0.96 pb=1.97 dividend=14.1 yield=2.38% delta=34.74%
            "002415",  # 海康威视 roi=10.35 roe=32.02 1/pe=3.02 rate=1.07 pb=8.97 dividend=7.0 yield=1.53% delta=50.51%
            "000598",  # 兴蓉环境 roi=10.22 roe=10.98 1/pe=8.31 rate=1.12 pb=1.22 dividend=0.9 yield=1.83% delta=22.06%
            "600062",  # 华润双鹤 roi=9.35 roe=12.02 1/pe=8.1 rate=0.96 pb=1.37 dividend=3.04 yield=2.52% delta=31.15%
            "600887",  # 伊利股份 roi=9.34 roe=30.24 1/pe=2.97 rate=1.04 pb=8.72 dividend=8.1 yield=1.99% delta=67.07%
            "600900",  # 长江电力 roi=9.2 roe=16.04 1/pe=5.36 rate=1.07 pb=2.71 dividend=6.8 yield=3.44% delta=64.23%
            "600104",  # 上汽集团 roi=8.95 roe=11.78 1/pe=10.0 rate=0.76 pb=1.13 dividend=8.8 yield=3.57% delta=35.68%
            "000828",  # 东莞控股 roi=8.69 roe=13.02 1/pe=8.67 rate=0.77 pb=1.38 dividend=3.0 yield=2.98% delta=34.36%
            "601006",  # 大秦铁路 roi=8.65 roe=10.58 1/pe=12.02 rate=0.68 pb=0.84 dividend=4.8 yield=7.27% delta=60.53%
            "600519",  # 贵州茅台 roi=8.46 roe=37.85 1/pe=2.05 rate=1.09 pb=15.61 dividend=170.25 yield=0.92% delta=45.11%
            "601601",  # 中国太保 roi=8.45 roe=13.91 1/pe=6.98 rate=0.87 pb=1.78 dividend=12.0 yield=3.21% delta=45.93%
            "600511",  # 国药股份 roi=8.05 roe=17.37 1/pe=4.78 rate=0.97 pb=3.24 dividend=6.38 yield=1.34% delta=28.07%
            "600874",  # 创业环保 roi=7.33 roe=9.84 1/pe=6.26 rate=1.19 pb=1.47 dividend=1.07 yield=1.6% delta=25.63%
            "000001",  # 平安银行 roi=7.31 roe=10.06 1/pe=7.57 rate=0.96 pb=1.23 dividend=2.18 yield=1.19% delta=15.68%
            "000999",  # 华润三九 roi=7.21 roe=13.96 1/pe=6.89 rate=0.75 pb=1.83 dividend=4.3 yield=1.67% delta=24.28%
            "000568",  # 泸州老窖 roi=7.07 roe=30.26 1/pe=1.87 rate=1.25 pb=13.69 dividend=15.9 yield=0.78% delta=41.47%
            "600690",  # 海尔智家 roi=6.89 roe=20.0 1/pe=4.99 rate=0.69 pb=3.64 dividend=3.75 yield=1.36% delta=27.16%
            "600007",  # 中国国贸 roi=6.84 roe=11.54 1/pe=6.44 rate=0.92 pb=1.68 dividend=3.8 yield=2.91% delta=45.22%
            "000756",  # 新华制药 roi=6.66 roe=11.58 1/pe=5.48 rate=1.05 pb=1.97 dividend=1.2 yield=1.22% delta=22.28%
            "600329",  # 中新药业 roi=6.57 roe=12.9 1/pe=4.67 rate=1.09 pb=2.57 dividend=3.0 yield=1.61% delta=34.37%
            "000858",  # 五 粮 液 roi=6.53 roe=29.28 1/pe=1.89 rate=1.18 pb=13.38 dividend=22.0 yield=0.79% delta=42.01%
            "600350",  # 山东高速 roi=6.51 roe=8.37 1/pe=7.94 rate=0.98 pb=1.07 dividend=3.8 yield=6.11% delta=76.98%
            "600563",  # 法拉电子 roi=6.45 roe=21.35 1/pe=2.54 rate=1.19 pb=7.66 dividend=13.0 yield=1.41% delta=55.52%
            "600513",  # 联环药业 roi=6.34 roe=11.55 1/pe=3.89 rate=1.41 pb=2.78 dividend=0.84 yield=0.83% delta=21.34%
            "600486",  # 扬农化工 roi=6.26 roe=22.41 1/pe=2.94 rate=0.95 pb=6.63 dividend=6.5 yield=0.53% delta=17.91%
            "600741",  # 华域汽车 roi=6.12 roe=12.77 1/pe=6.66 rate=0.72 pb=1.84 dividend=8.5 yield=2.9% delta=43.62%
            "600332",  # 白云山 roi=6.05 roe=11.98 1/pe=5.94 rate=0.85 pb=1.88 dividend=5.89 yield=1.96% delta=33.08%
            "601628",  # 中国人寿 roi=5.55 roe=12.78 1/pe=4.43 rate=0.98 pb=2.63 dividend=7.3 yield=1.88% delta=42.39%
            "002507",  # 涪陵榨菜 roi=5.55 roe=25.17 1/pe=2.06 rate=1.07 pb=10.47 dividend=3.0 yield=0.7% delta=33.79%
            "600028",  # 中国石化 roi=5.46 roe=6.71 1/pe=9.81 rate=0.83 pb=0.68 dividend=2.6 yield=6.34% delta=64.67%
            "600845",  # 宝信软件 roi=5.28 roe=18.64 1/pe=1.77 rate=1.6 pb=10.52 dividend=4.0 yield=0.64% delta=36.04%
            "600019",  # 宝钢股份 roi=5.23 roe=7.21 1/pe=9.07 rate=0.8 pb=0.77 dividend=2.8 yield=4.49% delta=49.55%
            "000538",  # 云南白药 roi=5.22 roe=13.05 1/pe=3.36 rate=1.19 pb=3.82 dividend=30.0 yield=2.63% delta=78.46%
            "000661",  # 长春高新 roi=5.1 roe=19.96 1/pe=1.68 rate=1.52 pb=17.9 dividend=10.0 yield=0.22% delta=13.29%
            "600132",  # 重庆啤酒 roi=4.9 roe=46.43 1/pe=1.11 rate=0.95 pb=47.15 dividend=14.0 yield=1.2% delta=107.96%
            "002179",  # 中航光电 roi=4.81 roe=18.97 1/pe=2.06 rate=1.23 pb=7.48 dividend=1.5 yield=0.24% delta=11.48%
            "600025",  # 华能水电
            "600809",  # 山西汾酒 roi=4.75 roe=37.47 1/pe=0.94 rate=1.35 pb=31.48 dividend=9.0 yield=0.27% delta=28.86%
            "000039",  # 中集集团 roi=4.68 roe=8.05 1/pe=5.15 rate=1.13 pb=1.52 dividend=1.2 yield=0.81% delta=15.69%
            "603369",  # 今世缘 roi=4.54 roe=21.18 1/pe=2.06 rate=1.04 pb=8.97 dividend=4.1 yield=0.72% delta=34.81%
            "600309",  # 万华化学 roi=4.39 roe=19.66 1/pe=2.9 rate=0.77 pb=6.22 dividend=13.0 yield=1.49% delta=51.45%
            "000651",  # 格力电器 roi=4.33 roe=16.27 1/pe=4.44 rate=0.6 pb=3.22 dividend=22.0 yield=3.58% delta=80.69%
            "002304",  # 洋河股份 roi=4.27 roe=20.46 1/pe=2.32 rate=0.9 pb=8.37 dividend=30.0 yield=1.41% delta=60.91%
            "600597",  # 光明乳业 roi=4.19 roe=12.04 1/pe=3.25 rate=1.07 pb=3.4 dividend=1.3 yield=0.78% delta=24.1%
            "603288",  # 海天味业 roi=4.05 roe=33.72 1/pe=1.0 rate=1.2 pb=33.59 dividend=10.8 yield=0.57% delta=57.41%
            "600030",  # 中信证券 roi=3.98 roe=8.73 1/pe=4.0 rate=1.14 pb=2.07 dividend=5.0 yield=1.74% delta=43.36%
            "600271",  # 航天信息 roi=3.97 roe=13.05 1/pe=6.21 rate=0.49 pb=2.02 dividend=2.31 yield=1.84% delta=29.63%
            "002025",  # 航天电器 roi=3.97 roe=16.77 1/pe=2.17 rate=1.09 pb=6.91 dividend=1.5 yield=0.28% delta=13.09%
            "000682",  # 东方电子 roi=3.9 roe=9.2 1/pe=4.16 rate=1.02 pb=2.08 dividend=0.38 yield=0.72% delta=17.32%
            "600085",  # 同仁堂 roi=3.72 roe=13.3 1/pe=3.78 rate=0.74 pb=3.6 dividend=2.6 yield=1.04% delta=27.38%
            "000547",  # 航天发展 roi=3.64 roe=11.27 1/pe=2.2 rate=1.47 pb=4.74 dividend=0.88 yield=0.37% delta=16.83%
            "600436",  # 片仔癀 roi=3.4 roe=25.78 1/pe=1.09 rate=1.21 pb=19.73 dividend=8.2 yield=0.33% delta=30.56%
            "600197",  # 伊力特 roi=3.2 roe=14.17 1/pe=2.86 rate=0.79 pb=4.64 dividend=4.38 yield=1.53% delta=53.63%
            "600377",  # 宁沪高速 roi=3.06 roe=9.37 1/pe=5.54 rate=0.59 pb=1.69 dividend=4.6 yield=4.96% delta=89.41%
            "000596",  # 古井贡酒 roi=2.66 roe=22.23 1/pe=1.41 rate=0.85 pb=13.89 dividend=15.0 yield=0.56% delta=39.57%
            "000501",  # 鄂武商Ａ roi=2.43 roe=6.73 1/pe=6.46 rate=0.56 pb=0.99 dividend=2.2 yield=1.8% delta=27.78%
            "600600",  # 青岛啤酒 roi=2.2 roe=11.51 1/pe=1.68 rate=1.14 pb=6.47 dividend=5.5 yield=0.54% delta=32.44%
            "600498",  # 烽火通信 roi=1.41 roe=6.85 1/pe=2.57 rate=0.8 pb=2.57 dividend=3.4 yield=1.46% delta=56.72%
            "600897",  # 厦门空港 roi=1.27 roe=6.46 1/pe=4.58 rate=0.43 pb=1.39 dividend=5.23 yield=3.05% delta=66.68%
            "601888",  # 中国中免 roi=1.08 roe=18.79 1/pe=0.86 rate=0.67 pb=21.58 dividend=7.2 yield=0.33% delta=38.41%
            "000733",  # 振华科技 roi=1.06 roe=6.57 1/pe=1.55 rate=1.04 pb=3.99 dividend=0.5 yield=0.11% delta=7.29%
            "000777",  # 中核科技 roi=1.0 roe=6.91 1/pe=2.07 rate=0.7 pb=3.21 dividend=1.07 yield=0.86% delta=41.82%
            "000429",  # 粤高速Ａ roi=0.91 roe=6.18 1/pe=4.34 rate=0.34 pb=1.49 dividend=4.22 yield=6.46% delta=148.84%
            "600548",  # 深高速 roi=0.37 roe=4.58 1/pe=4.26 rate=0.19 pb=1.08 dividend=5.2 yield=5.86% delta=137.64%
            "600004",  # 白云机场 roi=0.01 roe=0.86 1/pe=0.46 rate=0.19 pb=1.83 dividend=1.45 yield=1.02% delta=219.53%
            "600009",  # 上海机场 roi=0.0 roe=1.33 1/pe=0.28 rate=0.08 pb=4.9 dividend=7.9 yield=1.04% delta=369.28%
            "000089",  # 深圳机场 roi=0.0 roe=0.53 1/pe=0.37 rate=0.11 pb=1.44 dividend=0.8 yield=0.96% delta=257.05%
            "600676",  # 交运股份 roi=-0.5 roe=-2.62 1/pe=-3.05 rate=-0.63 pb=0.89 dividend=0.4 yield=0.82% delta=0.0%
            "000423",  # 东阿阿胶 roi=-1.01 roe=-6.34 1/pe=-2.53 rate=-0.63 pb=2.75 dividend=2.03 yield=0.5% delta=0.0%

            "600846",  # 同济科技 roi=148.12 roe=44.1 1/pe=21.53 rate=1.56 pb=1.71 dividend=3.4 yield=4.14% delta=19.21%
            "600153",  # 建发股份 roi=146.38 roe=32.87 1/pe=37.11 rate=1.2 pb=0.76 dividend=5.0 yield=5.72% delta=15.42%
            "000789",  # 万年青 roi=120.28 roe=49.92 1/pe=19.75 rate=1.22 pb=2.02 dividend=7.0 yield=4.99% delta=25.28%
            "600383",  # 金地集团 roi=111.69 roe=33.14 1/pe=26.33 rate=1.28 pb=1.18 dividend=6.7 yield=4.9% delta=18.61%
            "600325",  # 华发股份 roi=98.49 roe=29.05 1/pe=27.79 rate=1.22 pb=0.95 dividend=4.0 yield=6.43% delta=23.14%
            "600606",  # 绿地控股 roi=93.16 roe=29.17 1/pe=29.57 rate=1.08 pb=0.92 dividend=4.0 yield=6.56% delta=22.17%
            "601668",  # 中国建筑 roi=89.16 roe=27.16 1/pe=30.68 rate=1.07 pb=0.77 dividend=1.85 yield=3.6% delta=11.73%
            "600048",  # 保利地产 roi=79.38 roe=31.33 1/pe=19.95 rate=1.27 pb=1.32 dividend=8.2 yield=5.11% delta=25.6%
            "000951",  # 中国重汽 roi=59.47 roe=34.08 1/pe=10.45 rate=1.67 pb=2.71 dividend=5.5 yield=1.72% delta=16.45%
            "600720",  # 祁连山 roi=57.98 roe=26.41 1/pe=15.57 rate=1.41 pb=1.43 dividend=5.8 yield=4.02% delta=25.8%
            "000002",  # 万 科Ａ roi=56.86 roe=32.92 1/pe=17.1 rate=1.01 pb=1.63 dividend=10.17 yield=3.57% delta=20.87%
            "000921",  # 海信家电 roi=51.85 roe=28.9 1/pe=11.96 rate=1.5 pb=2.18 dividend=3.95 yield=2.69% delta=22.5%
            "000786",  # 北新建材 roi=50.05 roe=19.19 1/pe=4.29 rate=6.08 pb=3.82 dividend=0.82 yield=0.23% delta=5.35%
            "000069",  # 华侨城Ａ roi=48.96 roe=20.79 1/pe=23.09 rate=1.02 pb=0.8 dividend=3.05 yield=4.46% delta=19.31%
            "600064",  # 南京高科 roi=47.8 roe=19.87 1/pe=17.82 rate=1.35 pb=0.98 dividend=4.5 yield=4.36% delta=24.47%
            "600755",  # 厦门国贸 roi=46.47 roe=20.34 1/pe=20.96 rate=1.09 pb=0.89 dividend=2.3 yield=3.34% delta=15.93%
            "601390",  # 中国中铁 roi=43.12 roe=15.44 1/pe=20.84 rate=1.34 pb=0.67 dividend=1.69 yield=3.08% delta=14.8%
            "001979",  # 招商蛇口 roi=41.09 roe=25.17 1/pe=15.4 rate=1.06 pb=1.5 dividend=8.3 yield=6.16% delta=40.01%
            "000529",  # 广弘控股 roi=38.51 roe=24.46 1/pe=9.6 rate=1.64 pb=2.16 dividend=1.0 yield=1.43% delta=14.92%
            "600585",  # 海螺水泥 roi=36.92 roe=27.86 1/pe=12.62 rate=1.05 pb=1.86 dividend=20.0 yield=3.76% delta=29.81%
            "601186",  # 中国铁建 roi=33.47 roe=14.67 1/pe=21.32 rate=1.07 pb=0.62 dividend=2.1 yield=2.57% delta=12.07%
            "600068",  # 葛洲坝 roi=33.38 roe=19.79 1/pe=18.95 rate=0.89 pb=0.94 dividend=1.56 yield=2.37% delta=12.53%
            "000498",  # 山东路桥 roi=32.43 roe=15.71 1/pe=14.85 rate=1.39 pb=0.95 dividend=0.8 yield=1.6% delta=10.76%
            "600663",  # 陆家嘴 roi=31.99 roe=28.58 1/pe=10.66 rate=1.05 pb=2.45 dividend=4.56 yield=4.05% delta=38.0%
            "600461",  # 洪城水业 roi=29.56 roe=16.98 1/pe=12.09 rate=1.44 pb=1.25 dividend=2.6 yield=3.9% delta=32.24%
            "601669",  # 中国电建 roi=27.41 roe=13.69 1/pe=18.71 rate=1.07 pb=0.69 dividend=0.4 yield=1.0% delta=5.34%
            "000581",  # 威孚高科 roi=26.81 roe=17.14 1/pe=11.76 rate=1.33 pb=1.35 dividend=11.0 yield=4.63% delta=39.37%
            "601009",  # 南京银行 roi=23.65 roe=14.49 1/pe=16.0 rate=1.02 pb=0.85 dividend=3.92 yield=4.92% delta=30.75%
            "600612",  # 老凤祥 roi=23.23 roe=28.21 1/pe=7.77 rate=1.06 pb=3.21 dividend=11.5 yield=2.44% delta=31.46%
            "600668",  # 尖峰集团 roi=21.62 roe=18.76 1/pe=13.72 rate=0.84 pb=1.17 dividend=3.0 yield=2.07% delta=15.11%
            "601988",  # 中国银行 roi=21.27 roe=11.47 1/pe=19.94 rate=0.93 pb=0.54 dividend=1.91 yield=6.01% delta=30.13%
            "000877",  # 天山股份 roi=21.12 roe=19.31 1/pe=10.62 rate=1.03 pb=1.63 dividend=5.1 yield=3.2% delta=30.12%
            "000049",  # 德赛电池 roi=20.49 roe=31.89 1/pe=6.12 rate=1.05 pb=4.25 dividend=7.0 yield=1.35% delta=22.08%
            "601328",  # 交通银行 roi=20.38 roe=10.48 1/pe=21.14 rate=0.92 pb=0.47 dividend=3.15 yield=6.98% delta=33.04%
            "000895",  # 双汇发展 roi=20.24 roe=41.58 1/pe=3.99 rate=1.22 pb=6.7 dividend=16.4 yield=3.44% delta=86.18%
            "601288",  # 农业银行 roi=18.94 roe=11.47 1/pe=17.76 rate=0.93 pb=0.61 dividend=1.82 yield=5.74% delta=32.33%
            "601398",  # 工商银行 roi=18.24 roe=12.02 1/pe=16.32 rate=0.93 pb=0.69 dividend=2.63 yield=5.26% delta=32.23%
            "601939",  # 建设银行 roi=17.56 roe=12.13 1/pe=15.57 rate=0.93 pb=0.73 dividend=3.2 yield=4.99% delta=32.07%
            "600373",  # 中文传媒 roi=15.51 roe=12.91 1/pe=11.78 rate=1.02 pb=1.01 dividend=5.0 yield=4.61% delta=39.14%
            "601611",  # 中国核建 roi=15.22 roe=16.62 1/pe=8.4 rate=1.09 pb=1.77 dividend=0.56 yield=0.78% delta=9.26%
            "601088",  # 中国神华 roi=15.08 roe=13.77 1/pe=12.59 rate=0.87 pb=1.06 dividend=12.6 yield=6.61% delta=52.46%
            "600056",  # 中国医药 roi=14.87 roe=16.53 1/pe=9.37 rate=0.96 pb=1.59 dividend=2.76 yield=1.87% delta=19.92%
            "601800",  # 中国交建 roi=14.84 roe=10.17 1/pe=16.03 rate=0.91 pb=0.59 dividend=2.33 yield=3.14% delta=19.62%
            "601318",  # 中国平安 roi=14.71 roe=21.45 1/pe=8.57 rate=0.8 pb=2.26 dividend=21.0 yield=2.39% delta=27.92%
            "000411",  # 英特集团 roi=14.38 roe=21.58 1/pe=6.73 rate=0.99 pb=2.94 dividend=0.61 yield=0.32% delta=4.73%
            "600036",  # 招商银行 roi=14.35 roe=16.49 1/pe=8.53 rate=1.02 pb=1.76 dividend=12.0 yield=2.78% delta=32.64%
            "601607",  # 上海医药 roi=13.35 roe=12.57 1/pe=9.4 rate=1.13 pb=1.23 dividend=4.4 yield=2.28% delta=24.31%
            "600298",  # 安琪酵母 roi=12.92 roe=27.21 1/pe=3.23 rate=1.47 pb=7.31 dividend=4.0 yield=0.82% delta=25.24%
            "601319",  # 中国人保 roi=12.75 roe=15.48 1/pe=9.58 rate=0.86 pb=1.46 dividend=1.52 yield=2.32% delta=24.21%
            "002142",  # 宁波银行 roi=12.43 roe=16.31 1/pe=6.93 rate=1.1 pb=2.06 dividend=5.0 yield=1.45% delta=20.89%
            "600639",  # 浦东金桥 roi=11.69 roe=12.52 1/pe=7.91 rate=1.18 pb=1.44 dividend=3.1 yield=2.35% delta=29.66%
            "000582",  # 北部湾港 roi=11.3 roe=12.5 1/pe=7.06 rate=1.28 pb=1.7 dividend=1.77 yield=1.7% delta=24.12%
            "000028",  # 国药一致 roi=10.7 roe=12.67 1/pe=7.82 rate=1.08 pb=1.49 dividend=6.0 yield=1.27% delta=16.28%
            "600820",  # 隧道股份 roi=10.65 roe=9.52 1/pe=11.53 rate=0.97 pb=0.79 dividend=2.1 yield=3.73% delta=32.36%
            "601336",  # 新华保险 roi=10.44 roe=15.87 1/pe=6.85 rate=0.96 pb=1.97 dividend=14.1 yield=2.38% delta=34.74%
            "002415",  # 海康威视 roi=10.35 roe=32.02 1/pe=3.02 rate=1.07 pb=8.97 dividend=7.0 yield=1.53% delta=50.51%
            "000598",  # 兴蓉环境 roi=10.22 roe=10.98 1/pe=8.31 rate=1.12 pb=1.22 dividend=0.9 yield=1.83% delta=22.06%
            "600062",  # 华润双鹤 roi=9.35 roe=12.02 1/pe=8.1 rate=0.96 pb=1.37 dividend=3.04 yield=2.52% delta=31.15%
            "600887",  # 伊利股份 roi=9.34 roe=30.24 1/pe=2.97 rate=1.04 pb=8.72 dividend=8.1 yield=1.99% delta=67.07%
            "600900",  # 长江电力 roi=9.2 roe=16.04 1/pe=5.36 rate=1.07 pb=2.71 dividend=6.8 yield=3.44% delta=64.23%
            "600104",  # 上汽集团 roi=8.95 roe=11.78 1/pe=10.0 rate=0.76 pb=1.13 dividend=8.8 yield=3.57% delta=35.68%
            "000828",  # 东莞控股 roi=8.69 roe=13.02 1/pe=8.67 rate=0.77 pb=1.38 dividend=3.0 yield=2.98% delta=34.36%
            "601006",  # 大秦铁路 roi=8.65 roe=10.58 1/pe=12.02 rate=0.68 pb=0.84 dividend=4.8 yield=7.27% delta=60.53%
            "600519",  # 贵州茅台 roi=8.46 roe=37.85 1/pe=2.05 rate=1.09 pb=15.61 dividend=170.25 yield=0.92% delta=45.11%
            "601601",  # 中国太保 roi=8.45 roe=13.91 1/pe=6.98 rate=0.87 pb=1.78 dividend=12.0 yield=3.21% delta=45.93%
            "600511",  # 国药股份 roi=8.05 roe=17.37 1/pe=4.78 rate=0.97 pb=3.24 dividend=6.38 yield=1.34% delta=28.07%
            "600874",  # 创业环保 roi=7.33 roe=9.84 1/pe=6.26 rate=1.19 pb=1.47 dividend=1.07 yield=1.6% delta=25.63%
            "000001",  # 平安银行 roi=7.31 roe=10.06 1/pe=7.57 rate=0.96 pb=1.23 dividend=2.18 yield=1.19% delta=15.68%
            "000999",  # 华润三九 roi=7.21 roe=13.96 1/pe=6.89 rate=0.75 pb=1.83 dividend=4.3 yield=1.67% delta=24.28%
            "000568",  # 泸州老窖 roi=7.07 roe=30.26 1/pe=1.87 rate=1.25 pb=13.69 dividend=15.9 yield=0.78% delta=41.47%
            "600690",  # 海尔智家 roi=6.89 roe=20.0 1/pe=4.99 rate=0.69 pb=3.64 dividend=3.75 yield=1.36% delta=27.16%
            "600007",  # 中国国贸 roi=6.84 roe=11.54 1/pe=6.44 rate=0.92 pb=1.68 dividend=3.8 yield=2.91% delta=45.22%
            "000756",  # 新华制药 roi=6.66 roe=11.58 1/pe=5.48 rate=1.05 pb=1.97 dividend=1.2 yield=1.22% delta=22.28%
            "600329",  # 中新药业 roi=6.57 roe=12.9 1/pe=4.67 rate=1.09 pb=2.57 dividend=3.0 yield=1.61% delta=34.37%
            "000858",  # 五 粮 液 roi=6.53 roe=29.28 1/pe=1.89 rate=1.18 pb=13.38 dividend=22.0 yield=0.79% delta=42.01%
            "600350",  # 山东高速 roi=6.51 roe=8.37 1/pe=7.94 rate=0.98 pb=1.07 dividend=3.8 yield=6.11% delta=76.98%
            "600563",  # 法拉电子 roi=6.45 roe=21.35 1/pe=2.54 rate=1.19 pb=7.66 dividend=13.0 yield=1.41% delta=55.52%
            "600513",  # 联环药业 roi=6.34 roe=11.55 1/pe=3.89 rate=1.41 pb=2.78 dividend=0.84 yield=0.83% delta=21.34%
            "600486",  # 扬农化工 roi=6.26 roe=22.41 1/pe=2.94 rate=0.95 pb=6.63 dividend=6.5 yield=0.53% delta=17.91%
            "600741",  # 华域汽车 roi=6.12 roe=12.77 1/pe=6.66 rate=0.72 pb=1.84 dividend=8.5 yield=2.9% delta=43.62%
            "600332",  # 白云山 roi=6.05 roe=11.98 1/pe=5.94 rate=0.85 pb=1.88 dividend=5.89 yield=1.96% delta=33.08%
            "601628",  # 中国人寿 roi=5.55 roe=12.78 1/pe=4.43 rate=0.98 pb=2.63 dividend=7.3 yield=1.88% delta=42.39%
            "002507",  # 涪陵榨菜 roi=5.55 roe=25.17 1/pe=2.06 rate=1.07 pb=10.47 dividend=3.0 yield=0.7% delta=33.79%
            "600028",  # 中国石化 roi=5.46 roe=6.71 1/pe=9.81 rate=0.83 pb=0.68 dividend=2.6 yield=6.34% delta=64.67%
            "600845",  # 宝信软件 roi=5.28 roe=18.64 1/pe=1.77 rate=1.6 pb=10.52 dividend=4.0 yield=0.64% delta=36.04%
            "600019",  # 宝钢股份 roi=5.23 roe=7.21 1/pe=9.07 rate=0.8 pb=0.77 dividend=2.8 yield=4.49% delta=49.55%
            "000538",  # 云南白药 roi=5.22 roe=13.05 1/pe=3.36 rate=1.19 pb=3.82 dividend=30.0 yield=2.63% delta=78.46%
            "000661",  # 长春高新 roi=5.1 roe=19.96 1/pe=1.68 rate=1.52 pb=17.9 dividend=10.0 yield=0.22% delta=13.29%
            "600132",  # 重庆啤酒 roi=4.9 roe=46.43 1/pe=1.11 rate=0.95 pb=47.15 dividend=14.0 yield=1.2% delta=107.96%
            "002179",  # 中航光电 roi=4.81 roe=18.97 1/pe=2.06 rate=1.23 pb=7.48 dividend=1.5 yield=0.24% delta=11.48%
            "600025",  # 华能水电 roi=4.77 roe=11.61 1/pe=6.63 rate=0.62 pb=1.68 dividend=1.8 yield=3.98% delta=60.11%
            "600809",  # 山西汾酒 roi=4.75 roe=37.47 1/pe=0.94 rate=1.35 pb=31.48 dividend=9.0 yield=0.27% delta=28.86%
            "000039",  # 中集集团 roi=4.68 roe=8.05 1/pe=5.15 rate=1.13 pb=1.52 dividend=1.2 yield=0.81% delta=15.69%
            "603369",  # 今世缘 roi=4.54 roe=21.18 1/pe=2.06 rate=1.04 pb=8.97 dividend=4.1 yield=0.72% delta=34.81%
            "600309",  # 万华化学 roi=4.39 roe=19.66 1/pe=2.9 rate=0.77 pb=6.22 dividend=13.0 yield=1.49% delta=51.45%
            "000651",  # 格力电器 roi=4.33 roe=16.27 1/pe=4.44 rate=0.6 pb=3.22 dividend=22.0 yield=3.58% delta=80.69%
            "002304",  # 洋河股份 roi=4.27 roe=20.46 1/pe=2.32 rate=0.9 pb=8.37 dividend=30.0 yield=1.41% delta=60.91%
            "600597",  # 光明乳业 roi=4.19 roe=12.04 1/pe=3.25 rate=1.07 pb=3.4 dividend=1.3 yield=0.78% delta=24.1%
            "603288",  # 海天味业 roi=4.05 roe=33.72 1/pe=1.0 rate=1.2 pb=33.59 dividend=10.8 yield=0.57% delta=57.41%
            "600030",  # 中信证券 roi=3.98 roe=8.73 1/pe=4.0 rate=1.14 pb=2.07 dividend=5.0 yield=1.74% delta=43.36%
            "600271",  # 航天信息 roi=3.97 roe=13.05 1/pe=6.21 rate=0.49 pb=2.02 dividend=2.31 yield=1.84% delta=29.63%
            "002025",  # 航天电器 roi=3.97 roe=16.77 1/pe=2.17 rate=1.09 pb=6.91 dividend=1.5 yield=0.28% delta=13.09%
            "000682",  # 东方电子 roi=3.9 roe=9.2 1/pe=4.16 rate=1.02 pb=2.08 dividend=0.38 yield=0.72% delta=17.32%
            "600085",  # 同仁堂 roi=3.72 roe=13.3 1/pe=3.78 rate=0.74 pb=3.6 dividend=2.6 yield=1.04% delta=27.38%
            "000547",  # 航天发展 roi=3.64 roe=11.27 1/pe=2.2 rate=1.47 pb=4.74 dividend=0.88 yield=0.37% delta=16.83%
            "600436",  # 片仔癀 roi=3.4 roe=25.78 1/pe=1.09 rate=1.21 pb=19.73 dividend=8.2 yield=0.33% delta=30.56%
            "600197",  # 伊力特 roi=3.2 roe=14.17 1/pe=2.86 rate=0.79 pb=4.64 dividend=4.38 yield=1.53% delta=53.63%
            "600377",  # 宁沪高速 roi=3.06 roe=9.37 1/pe=5.54 rate=0.59 pb=1.69 dividend=4.6 yield=4.96% delta=89.41%
            "000596",  # 古井贡酒 roi=2.66 roe=22.23 1/pe=1.41 rate=0.85 pb=13.89 dividend=15.0 yield=0.56% delta=39.57%
            "000501",  # 鄂武商Ａ roi=2.43 roe=6.73 1/pe=6.46 rate=0.56 pb=0.99 dividend=2.2 yield=1.8% delta=27.78%
            "600600",  # 青岛啤酒 roi=2.2 roe=11.51 1/pe=1.68 rate=1.14 pb=6.47 dividend=5.5 yield=0.54% delta=32.44%
            "600498",  # 烽火通信 roi=1.41 roe=6.85 1/pe=2.57 rate=0.8 pb=2.57 dividend=3.4 yield=1.46% delta=56.72%
            "600897",  # 厦门空港 roi=1.27 roe=6.46 1/pe=4.58 rate=0.43 pb=1.39 dividend=5.23 yield=3.05% delta=66.68%
            "601888",  # 中国中免 roi=1.08 roe=18.79 1/pe=0.86 rate=0.67 pb=21.58 dividend=7.2 yield=0.33% delta=38.41%
            "000733",  # 振华科技 roi=1.06 roe=6.57 1/pe=1.55 rate=1.04 pb=3.99 dividend=0.5 yield=0.11% delta=7.29%
            "000777",  # 中核科技 roi=1.0 roe=6.91 1/pe=2.07 rate=0.7 pb=3.21 dividend=1.07 yield=0.86% delta=41.82%
            "000429",  # 粤高速Ａ roi=0.91 roe=6.18 1/pe=4.34 rate=0.34 pb=1.49 dividend=4.22 yield=6.46% delta=148.84%
            "600548",  # 深高速 roi=0.37 roe=4.58 1/pe=4.26 rate=0.19 pb=1.08 dividend=5.2 yield=5.86% delta=137.64%
            "600004",  # 白云机场 roi=0.01 roe=0.86 1/pe=0.46 rate=0.19 pb=1.83 dividend=1.45 yield=1.02% delta=219.53%
            "600009",  # 上海机场 roi=0.0 roe=1.33 1/pe=0.28 rate=0.08 pb=4.9 dividend=7.9 yield=1.04% delta=369.28%
            "000089",  # 深圳机场 roi=0.0 roe=0.53 1/pe=0.37 rate=0.11 pb=1.44 dividend=0.8 yield=0.96% delta=257.05%
            "600676",  # 交运股份 roi=-0.5 roe=-2.62 1/pe=-3.05 rate=-0.63 pb=0.89 dividend=0.4 yield=0.82% delta=0.0%
            "000423",  # 东阿阿胶 roi=-1.01 roe=-6.34 1/pe=-2.53 rate=-0.63 pb=2.75 dividend=2.03 yield=0.5% delta=0.0%
        }

    def get_stock_list(self):
        return self.stock_list
