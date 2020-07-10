# -*- coding: utf-8 -*-

class Favorite:
    def __init__(self):
        self.stock_list = {
            "600340",  # DR华夏幸 roi 928.96 roe 38.95 pe 23.85 pb 1.28 dividend 15.0 7.41%  operation 0
            "002146",  # 荣盛发展 roi 606.77 roe 26.73 pe 22.7 pb 0.98 dividend 4.8 5.14%  operation 0
            "600466",  # 蓝光发展 roi 549.4 roe 27.86 pe 19.72 pb 1.1 dividend 2.87 4.94%  operation 0
            "600153",  # 建发股份 roi 422.68 roe 20.38 pe 20.74 pb 0.85 dividend 5.0 5.15%  operation 0
            "000069",  # 华侨城Ａ roi 351.56 roe 19.52 pe 18.01 pb 0.98 dividend 3.05 3.76%  operation 0
            "601668",  # 中国建筑 roi 323.14 roe 17.6 pe 18.36 pb 0.84 dividend 1.85 3.51%  operation 0
            "600048",  # 保利地产 roi 319.41 roe 23.73 pe 13.46 pb 1.44 dividend 8.2 4.7%  operation 0
            "000656",  # 金科股份 roi 314.93 roe 26.78 pe 11.76 pb 1.73 dividend 4.5 4.85%  operation 0
            "000671",  # 阳 光 城 roi 306.39 roe 22.43 pe 13.66 pb 1.36 dividend 1.99 2.69%  operation 0
            "600668",  # 尖峰集团 roi 296.86 roe 22.27 pe 13.33 pb 1.4 dividend 3.0 1.88%  operation 0
            "600383",  # XD金地集 roi 295.77 roe 20.64 pe 14.33 pb 1.31 dividend 6.7 4.39%  operation 0
            "600846",  # 同济科技 roi 294.3 roe 27.0 pe 10.9 pb 2.01 dividend 3.4 3.68%  operation 0
            "600585",  # 海螺水泥 roi 292.0 roe 27.29 pe 10.7 pb 2.13 dividend 20.0 3.5%  operation 0
            "600068",  # 葛洲坝 roi 288.54 roe 18.7 pe 15.43 pb 1.09 dividend 1.56 2.15%  operation 0
            "601166",  # 兴业银行 roi 270.74 roe 14.73 pe 18.38 pb 0.72 dividend 7.62 4.33%  operation 0
            "000002",  # 万 科Ａ roi 270.72 roe 23.52 pe 11.51 pb 1.75 dividend 10.17 3.49%  operation 0
            "600016",  # 民生银行 roi 254.98 roe 12.8 pe 19.92 pb 0.59 dividend 3.7 5.9%  operation 0
            "600352",  # XD浙江龙 roi 252.22 roe 22.95 pe 10.99 pb 1.75 dividend 2.5 1.81%  operation 0
            "600188",  # 兖州煤业 roi 252.21 roe 14.95 pe 16.87 pb 0.91 dividend 5.8 6.03%  operation 0
            "600970",  # 中材国际 roi 248.4 roe 16.66 pe 14.91 pb 0.99 dividend 3.01 5.12%  operation 0
            "600606",  # XD绿地控 roi 244.98 roe 19.29 pe 12.7 pb 1.43 dividend 4.0 4.42%  operation 0
            "601009",  # 南京银行 roi 241.69 roe 15.21 pe 15.89 pb 0.85 dividend 3.92 4.84%  operation 0
            "601288",  # XD农业银 roi 237.95 roe 13.01 pe 18.29 pb 0.65 dividend 1.82 5.42%  operation 0
            "601398",  # 工商银行 roi 228.76 roe 13.52 pe 16.92 pb 0.73 dividend 2.63 5.04%  operation 0
            "601818",  # 光大银行 roi 228.23 roe 12.96 pe 17.61 pb 0.67 dividend 2.14 5.14%  operation 0
            "601328",  # 交通银行 roi 227.43 roe 11.79 pe 19.29 pb 0.57 dividend 3.15 5.81%  operation 0
            "601939",  # XD建设银 roi 226.79 roe 13.72 pe 16.53 pb 0.75 dividend 3.2 4.89%  operation 0
            "600755",  # 厦门国贸 roi 226.69 roe 15.58 pe 14.55 pb 1.01 dividend 2.3 3.03%  operation 0
            "601390",  # 中国中铁 roi 219.32 roe 13.3 pe 16.49 pb 0.73 dividend 1.69 2.92%  operation 0
            "601988",  # 中国银行 roi 211.57 roe 12.09 pe 17.5 pb 0.63 dividend 1.91 5.2%  operation 0
            "601998",  # 中信银行 roi 207.15 roe 11.77 pe 17.6 pb 0.61 dividend 2.39 4.18%  operation 0
            "601336",  # 新华保险 roi 196.4 roe 21.63 pe 9.08 pb 1.99 dividend 14.1 2.52%  operation 0
            "600566",  # 济川药业 roi 192.32 roe 26.86 pe 7.16 pb 3.41 dividend 12.3 4.55%  operation 0
            "601186",  # 中国铁建 roi 189.86 roe 12.54 pe 15.14 pb 0.74 dividend 2.1 2.24%  operation 0
            "601318",  # 中国平安 roi 187.18 roe 21.69 pe 8.63 pb 2.18 dividend 13.0 1.58%  operation 0
            "600036",  # XD招商银 roi 182.27 roe 17.94 pe 10.16 pb 1.55 dividend 12.0 3.22%  operation 0
            "600376",  # 首开股份 roi 180.25 roe 11.75 pe 15.34 pb 0.71 dividend 4.0 5.84%  operation 0
            "601601",  # 中国太保 roi 178.99 roe 17.81 pe 10.05 pb 1.55 dividend 12.0 3.79%  operation 0
            "600064",  # 南京高科 roi 160.38 roe 14.13 pe 11.35 pb 1.12 dividend 4.5 3.99%  operation 0
            "000828",  # 东莞控股 roi 148.46 roe 13.57 pe 10.94 pb 1.13 dividend 3.0 3.75%  operation 0
            "601088",  # 中国神华 roi 146.84 roe 11.88 pe 12.36 pb 0.9 dividend 12.6 7.65%  operation 0
            "000963",  # 华东医药 roi 142.65 roe 23.54 pe 6.06 pb 3.74 dividend 2.8 0.97%  operation 0
            "601800",  # 中国交建 roi 140.04 roe 10.32 pe 13.57 pb 0.68 dividend 2.33 2.76%  operation 0
            "002142",  # 宁波银行 roi 137.92 roe 17.75 pe 7.77 pb 1.89 dividend 5.0 1.63%  operation 0
            "000895",  # 双汇发展 roi 135.17 roe 39.18 pe 3.45 pb 9.09 dividend 10.0 2.03%  operation 0
            "601006",  # 大秦铁路 roi 132.96 roe 11.08 pe 12.0 pb 0.88 dividend 4.8 7.0%  operation 0
            "002589",  # 瑞康医药 roi 129.4 roe -11.85 pe -10.92 pb 1.29 dividend 0.0 0.0%  operation 0
            "000651",  # 格力电器 roi 127.72 roe 22.02 pe 5.8 pb 3.14 dividend 12.0 2.03%  operation 0
            "600486",  # 扬农化工 roi 127.25 roe 25.97 pe 4.9 pb 4.77 dividend 6.5 0.77%  operation 0
            "600823",  # 世茂股份 roi 125.29 roe 9.92 pe 12.63 pb 0.74 dividend 2.6 5.17%  operation 0
            "000333",  # 美的集团 roi 123.96 roe 24.07 pe 5.15 pb 4.19 dividend 16.0 2.52%  operation 0
            "000581",  # 威孚高科 roi 119.48 roe 12.82 pe 9.32 pb 1.33 dividend 11.0 4.86%  operation 0
            "600987",  # 航民股份 roi 117.81 roe 10.7 pe 11.01 pb 1.27 dividend 2.2 3.82%  operation 0
            "000001",  # 平安银行 roi 115.93 roe 11.41 pe 10.16 pb 1.02 dividend 2.18 1.47%  operation 0
            "000049",  # 德赛电池 roi 113.4 roe 26.25 pe 4.32 pb 4.96 dividend 7.0 1.3%  operation 0
            "600663",  # 陆家嘴 roi 111.48 roe 17.5 pe 6.37 pb 2.97 dividend 4.56 3.29%  operation 0
            "600309",  # 万华化学 roi 109.7 roe 21.26 pe 5.16 pb 3.86 dividend 13.0 2.42%  operation 0
            "600690",  # 海尔智家 roi 103.89 roe 17.2 pe 6.04 pb 2.45 dividend 3.75 2.09%  operation 0
            "600612",  # 老凤祥 roi 98.96 roe 21.42 pe 4.62 pb 4.12 dividend 11.5 1.98%  operation 0
            "600639",  # 浦东金桥 roi 98.3 roe 14.33 pe 6.86 pb 1.86 dividend 3.1 1.83%  operation 0
            "600548",  # XD深高速 roi 97.57 roe 10.64 pe 9.17 pb 1.14 dividend 5.2 5.47%  operation 0
            "600820",  # 隧道股份 roi 95.7 roe 9.41 pe 10.17 pb 0.88 dividend 2.1 3.39%  operation 0
            "600018",  # 上港集团 roi 87.44 roe 11.04 pe 7.92 pb 1.33 dividend 1.45 3.02%  operation 0
            "600062",  # 华润双鹤 roi 84.77 roe 12.25 pe 6.92 pb 1.63 dividend 3.04 2.19%  operation 0
            "600007",  # XD中国国 roi 82.81 roe 13.0 pe 6.37 pb 1.88 dividend 3.8 2.62%  operation 0
            "600511",  # 国药股份 roi 81.58 roe 16.48 pe 4.95 pb 2.9 dividend 6.38 1.54%  operation 0
            "600897",  # 厦门空港 roi 77.33 roe 10.83 pe 7.14 pb 1.51 dividend 5.23 2.76%  operation 0
            "600900",  # 长江电力 roi 72.43 roe 14.4 pe 5.03 pb 2.74 dividend 6.8 3.6%  operation 0
            "002032",  # 苏 泊 尔 roi 72.43 roe 26.63 pe 2.72 pb 9.11 dividend 13.3 1.73%  operation 0
            "600557",  # 康缘药业 roi 71.86 roe 13.21 pe 5.44 pb 2.18 dividend 0.8 0.54%  operation 0
            "601607",  # 上海医药 roi 71.31 roe 9.96 pe 7.16 pb 1.31 dividend 4.4 2.24%  operation 0
            "002304",  # 洋河股份 roi 71.07 roe 19.47 pe 3.65 pb 5.05 dividend 30.0 2.24%  operation 0
            "000568",  # 泸州老窖 roi 70.86 roe 26.05 pe 2.72 pb 8.44 dividend 15.9 1.31%  operation 0
            "002271",  # 东方雨虹 roi 70.84 roe 25.76 pe 2.75 pb 6.61 dividend 3.0 0.63%  operation 0
            "600519",  # 贵州茅台 roi 69.44 roe 34.72 pe 2.0 pb 14.44 dividend 170.25 0.99%  operation 0
            "600377",  # 宁沪高速 roi 68.34 roe 11.24 pe 6.08 pb 1.85 dividend 4.6 4.5%  operation 0
            "600660",  # 福耀玻璃 roi 66.53 roe 13.28 pe 5.01 pb 2.51 dividend 7.5 3.42%  operation 0
            "600332",  # 白云山 roi 66.38 roe 12.84 pe 5.17 pb 2.26 dividend 5.89 1.67%  operation 0
            "600323",  # 瀚蓝环境 roi 65.93 roe 14.24 pe 4.63 pb 2.77 dividend 2.2 0.91%  operation 0
            "600741",  # 华域汽车 roi 64.97 roe 9.98 pe 6.51 pb 1.49 dividend 8.5 3.67%  operation 0
            "600012",  # 皖通高速 roi 64.17 roe 7.55 pe 8.5 pb 0.86 dividend 2.3 4.14%  operation 0
            "600104",  # 上汽集团 roi 62.79 roe 7.52 pe 8.35 pb 0.89 dividend 8.8 4.65%  operation 0
            "000858",  # 五 粮 液 roi 61.78 roe 26.63 pe 2.32 pb 9.8 dividend 22.0 1.06%  operation 0
            "000538",  # 云南白药 roi 61.2 roe 18.16 pe 3.37 pb 3.5 dividend 30.0 2.8%  operation 0
            "000028",  # 国药一致 roi 60.93 roe 10.24 pe 5.95 pb 1.57 dividend 6.0 1.25%  operation 0
            "600887",  # 伊利股份 roi 60.8 roe 22.03 pe 2.76 pb 7.81 dividend 8.1 2.34%  operation 0
            "600019",  # 宝钢股份 roi 60.35 roe 6.28 pe 9.61 pb 0.65 dividend 2.8 5.33%  operation 0
            "000999",  # 华润三九 roi 60.05 roe 12.33 pe 4.87 pb 2.32 dividend 4.3 1.39%  operation 0
            "601628",  # 中国人寿 roi 59.1 roe 13.84 pe 4.27 pb 2.85 dividend 7.3 1.78%  operation 0
            "600563",  # 法拉电子 roi 55.15 roe 17.62 pe 3.13 pb 5.28 dividend 13.0 2.03%  operation 0
            "600809",  # 山西汾酒 roi 54.38 roe 31.99 pe 1.7 pb 15.51 dividend 9.0 0.58%  operation 0
            "600350",  # XD山东高 roi 53.66 roe 7.59 pe 7.07 pb 1.0 dividend 3.8 6.11%  operation 0
            "600874",  # XD创业环 roi 50.69 roe 9.44 pe 5.37 pb 1.61 dividend 1.07 1.51%  operation 0
            "000596",  # 古井贡酒 roi 49.8 roe 23.27 pe 2.14 pb 9.5 dividend 15.0 0.83%  operation 0
            "600056",  # 中国医药 roi 49.09 roe 9.44 pe 5.2 pb 1.74 dividend 2.76 1.83%  operation 0
            "600033",  # 福建高速 roi 48.4 roe 6.31 pe 7.67 pb 0.82 dividend 0.5 1.77%  operation 0
            "002507",  # 涪陵榨菜 roi 45.22 roe 23.43 pe 1.93 pb 10.51 dividend 3.0 0.74%  operation 0
            "600298",  # 安琪酵母 roi 45.09 roe 21.17 pe 2.13 pb 8.77 dividend 4.0 0.73%  operation 0
            "000429",  # 粤高速Ａ roi 44.93 roe 8.32 pe 5.4 pb 1.61 dividend 4.22 5.71%  operation 0
            "600197",  # 伊力特 roi 39.41 roe 11.8 pe 3.34 pb 3.42 dividend 4.38 2.08%  operation 0
            "600196",  # 复星医药 roi 38.85 roe 11.1 pe 3.5 pb 2.78 dividend 3.9 1.1%  operation 0
            "603288",  # 海天味业 roi 38.73 roe 29.79 pe 1.3 pb 19.33 dividend 10.8 0.83%  operation 0
            "600436",  # 片仔癀 roi 34.19 roe 26.1 pe 1.31 pb 15.58 dividend 8.2 0.45%  operation 0
            "002025",  # 航天电器 roi 33.87 roe 14.35 pe 2.36 pb 5.43 dividend 1.5 0.38%  operation 0
            "600009",  # 上海机场 roi 32.0 roe 12.55 pe 2.55 pb 4.54 dividend 7.9 1.05%  operation 0
            "600872",  # 中炬高新 roi 29.77 roe 20.39 pe 1.46 pb 12.08 dividend 2.8 0.44%  operation 0
            "000513",  # 丽珠集团 roi 26.03 roe 9.07 pe 2.87 pb 3.91 dividend 11.5 2.37%  operation 0
            "600276",  # 恒瑞医药 roi 22.91 roe 22.24 pe 1.03 pb 16.83 dividend 2.3 0.23%  operation 0
            "600030",  # 中信证券 roi 20.95 roe 7.15 pe 2.93 pb 2.32 dividend 5.0 1.57%  operation 0
            "600085",  # 同仁堂 roi 20.63 roe 9.13 pe 2.26 pb 4.07 dividend 2.6 0.92%  operation 0
            "600763",  # 通策医疗 roi 16.87 roe 24.81 pe 0.68 pb 28.96 dividend 0.0 0.0%  operation 0
            "000661",  # 长春高新 roi 15.75 roe 14.86 pe 1.06 pb 10.67 dividend 10.0 0.22%  operation 0
            "600028",  # 中国石化 roi 14.38 roe 3.12 pe 4.61 pb 0.7 dividend 1.9 4.6%  operation 0
            "600529",  # 山东药玻 roi 12.26 roe 9.5 pe 1.29 pb 9.33 dividend 3.0 0.48%  operation 0
            "601566",  # 九牧王 roi 10.32 roe 3.45 pe 2.99 pb 1.26 dividend 6.5 6.87%  operation 0
            "601888",  # 中国中免 roi 6.55 roe 11.91 pe 0.55 pb 20.01 dividend 7.2 0.35%  operation 0
            "600269",  # 赣粤高速 roi 0.53 roe 0.55 pe 0.96 pb 0.58 dividend 1.5 3.92%  operation 0

            "600340",  # 华夏幸福 roi 689.03 roe 38.95 pe 17.69 pb 1.72 dividend 15.0 5.5%  operation 0
            "002146",  # 荣盛发展 roi 587.26 roe 26.73 pe 21.97 pb 1.01 dividend 4.8 4.97%  operation 0
            "600466",  # 蓝光发展 roi 536.58 roe 27.86 pe 19.26 pb 1.13 dividend 2.87 4.82%  operation 0
            "600153",  # 建发股份 roi 417.18 roe 20.38 pe 20.47 pb 0.86 dividend 5.0 5.09%  operation 0
            "000069",  # 华侨城Ａ roi 333.79 roe 19.52 pe 17.1 pb 1.03 dividend 3.05 3.57%  operation 0
            "600048",  # 保利地产 roi 315.37 roe 23.73 pe 13.29 pb 1.46 dividend 8.2 4.64%  operation 0
            "601668",  # 中国建筑 roi 315.22 roe 17.6 pe 17.91 pb 0.86 dividend 1.85 3.43%  operation 0
            "000656",  # 金科股份 roi 309.31 roe 26.78 pe 11.55 pb 1.76 dividend 4.5 4.77%  operation 0
            "600668",  # 尖峰集团 roi 301.76 roe 22.27 pe 13.55 pb 1.38 dividend 3.0 1.91%  operation 0
            "600068",  # 葛洲坝 roi 299.57 roe 18.7 pe 16.02 pb 1.05 dividend 1.56 2.23%  operation 0
            "000671",  # 阳 光 城 roi 298.9 roe 22.44 pe 13.32 pb 1.39 dividend 1.99 2.62%  operation 0
            "600846",  # 同济科技 roi 297.0 roe 27.0 pe 11.0 pb 2.0 dividend 3.4 3.72%  operation 0
            "600585",  # 海螺水泥 roi 287.91 roe 27.29 pe 10.55 pb 2.16 dividend 20.0 3.45%  operation 0
            "600383",  # 金地集团 roi 266.88 roe 20.64 pe 12.93 pb 1.45 dividend 6.7 3.96%  operation 0
            "000002",  # 万 科Ａ roi 260.6 roe 23.52 pe 11.08 pb 1.82 dividend 10.17 3.36%  operation 0
            "601166",  # 兴业银行 roi 259.69 roe 14.73 pe 17.63 pb 0.75 dividend 7.62 4.15%  operation 0
            "600606",  # 绿地控股 roi 256.17 roe 19.29 pe 13.28 pb 1.37 dividend 4.0 4.62%  operation 0
            "600188",  # XD兖州煤 roi 252.51 roe 14.95 pe 16.89 pb 0.91 dividend 5.8 6.04%  operation 0
            "600970",  # 中材国际 roi 250.57 roe 16.66 pe 15.04 pb 0.98 dividend 3.01 5.16%  operation 0
            "600352",  # 浙江龙盛 roi 249.24 roe 22.95 pe 10.86 pb 1.77 dividend 2.5 1.79%  operation 0
            "600016",  # 民生银行 roi 245.12 roe 12.8 pe 19.15 pb 0.61 dividend 3.7 5.67%  operation 0
            "600755",  # 厦门国贸 roi 238.37 roe 15.58 pe 15.3 pb 0.96 dividend 2.3 3.19%  operation 0
            "601009",  # 南京银行 roi 234.23 roe 15.21 pe 15.4 pb 0.87 dividend 3.92 4.69%  operation 0
            "601328",  # 交通银行 roi 218.23 roe 11.79 pe 18.51 pb 0.59 dividend 3.15 5.58%  operation 0
            "601398",  # 工商银行 roi 214.7 roe 13.52 pe 15.88 pb 0.77 dividend 2.63 4.73%  operation 0
            "601288",  # 农业银行 roi 214.27 roe 13.01 pe 16.47 pb 0.72 dividend 1.82 4.88%  operation 0
            "601939",  # 建设银行 roi 204.84 roe 13.72 pe 14.93 pb 0.83 dividend 3.2 4.41%  operation 0
            "601988",  # 中国银行 roi 203.23 roe 12.09 pe 16.81 pb 0.66 dividend 1.91 5.0%  operation 0
            "601818",  # 光大银行 roi 213.84 roe 12.96 pe 16.5 pb 0.71 dividend 2.14 4.82%  operation 0
            "600566",  # 济川药业 roi 195.81 roe 26.86 pe 7.29 pb 3.35 dividend 12.3 4.63%  operation 0
            "601318",  # 中国平安 roi 185.23 roe 21.69 pe 8.54 pb 2.2 dividend 13.0 1.56%  operation 0
            "601390",  # 中国中铁 roi 220.12 roe 13.3 pe 16.55 pb 0.73 dividend 1.69 2.93%  operation 0
            "601998",  # 中信银行 roi 200.8 roe 11.77 pe 17.06 pb 0.63 dividend 2.39 4.05%  operation 0
            "601186",  # 中国铁建 roi 187.47 roe 12.54 pe 14.95 pb 0.75 dividend 2.1 2.21%  operation 0
            "600376",  # 首开股份 roi 181.3 roe 11.75 pe 15.43 pb 0.71 dividend 4.0 5.87%  operation 0
            "601601",  # 中国太保 roi 175.14 roe 17.89 pe 9.79 pb 1.59 dividend 12.0 3.67%  operation 0
            "601336",  # 新华保险 roi 193.59 roe 21.63 pe 8.95 pb 2.02 dividend 14.1 2.49%  operation 0
            "600036",  # 招商银行 roi 165.23 roe 17.94 pe 9.21 pb 1.7 dividend 12.0 2.92%  operation 0
            "600064",  # XD南京高 roi 164.47 roe 14.13 pe 11.64 pb 1.09 dividend 4.5 4.09%  operation 0
            "000963",  # 华东医药 roi 154.89 roe 23.54 pe 6.58 pb 3.44 dividend 2.8 1.06%  operation 0
            "000828",  # 东莞控股 roi 152.39 roe 13.57 pe 11.23 pb 1.1 dividend 3.0 3.85%  operation 0
            "601088",  # 中国神华 roi 142.68 roe 11.88 pe 12.01 pb 0.93 dividend 12.6 7.44%  operation 0
            "000895",  # 双汇发展 roi 140.26 roe 39.18 pe 3.58 pb 8.74 dividend 10.0 2.12%  operation 0
            "601800",  # 中国交建 roi 137.88 roe 10.32 pe 13.36 pb 0.69 dividend 2.33 2.72%  operation 0
            "002142",  # 宁波银行 roi 134.19 roe 17.75 pe 7.56 pb 1.95 dividend 5.0 1.58%  operation 0
            "601006",  # 大秦铁路 roi 130.85 roe 11.08 pe 11.81 pb 0.89 dividend 4.8 6.89%  operation 0
            "600486",  # 扬农化工 roi 128.81 roe 25.97 pe 4.96 pb 4.71 dividend 6.5 0.78%  operation 0
            "000651",  # 格力电器 roi 125.29 roe 22.02 pe 5.69 pb 3.2 dividend 12.0 2.0%  operation 0
            "000333",  # 美的集团 roi 122.03 roe 24.07 pe 5.07 pb 4.25 dividend 16.0 2.49%  operation 0
            "000581",  # 威孚高科 roi 119.74 roe 12.82 pe 9.34 pb 1.32 dividend 11.0 4.87%  operation 0
            "600987",  # 航民股份 roi 119.52 roe 10.7 pe 11.17 pb 1.25 dividend 2.2 3.87%  operation 0
            "600663",  # 陆家嘴 roi 113.75 roe 17.5 pe 6.5 pb 2.91 dividend 4.56 3.35%  operation 0
            "000049",  # 德赛电池 roi 111.3 roe 26.25 pe 4.24 pb 5.05 dividend 7.0 1.28%  operation 0
            "000001",  # 平安银行 roi 111.25 roe 11.41 pe 9.75 pb 1.06 dividend 2.18 1.41%  operation 0
            "600309",  # 万华化学 roi 106.94 roe 21.26 pe 5.03 pb 3.96 dividend 13.0 2.36%  operation 0
            "600612",  # 老凤祥 roi 104.74 roe 21.42 pe 4.89 pb 3.89 dividend 11.5 2.09%  operation 0
            "600690",  # 海尔智家 roi 100.45 roe 17.2 pe 5.84 pb 2.54 dividend 3.75 2.02%  operation 0
            "600639",  # 浦东金桥 roi 98.02 roe 14.33 pe 6.84 pb 1.87 dividend 3.1 1.83%  operation 0
            "600820",  # 隧道股份 roi 97.11 roe 9.41 pe 10.32 pb 0.87 dividend 2.1 3.44%  operation 0
            "600548",  # 深高速 roi 93.42 roe 10.64 pe 8.78 pb 1.19 dividend 5.2 5.24%  operation 0
            "600018",  # 上港集团 roi 89.87 roe 11.04 pe 8.14 pb 1.29 dividend 1.45 3.1%  operation 0
            "600062",  # 华润双鹤 roi 85.87 roe 12.25 pe 7.01 pb 1.61 dividend 3.04 2.22%  operation 0
            "600511",  # 国药股份 roi 84.71 roe 16.48 pe 5.14 pb 2.79 dividend 6.38 1.6%  operation 0
            "600007",  # 中国国贸 roi 83.07 roe 13.0 pe 6.39 pb 1.87 dividend 3.8 2.63%  operation 0
            "600897",  # 厦门空港 roi 78.08 roe 10.83 pe 7.21 pb 1.49 dividend 5.23 2.79%  operation 0
            "000568",  # 泸州老窖 roi 74.76 roe 26.05 pe 2.87 pb 7.98 dividend 15.9 1.38%  operation 0
            "601607",  # 上海医药 roi 72.31 roe 9.96 pe 7.26 pb 1.29 dividend 4.4 2.27%  operation 0
            "600900",  # 长江电力 roi 70.85 roe 14.4 pe 4.92 pb 2.8 dividend 6.8 3.52%  operation 0
            "002032",  # 苏 泊 尔 roi 70.57 roe 26.63 pe 2.65 pb 9.35 dividend 13.3 1.69%  operation 0
            "600519",  # 贵州茅台 roi 70.48 roe 34.72 pe 2.03 pb 14.22 dividend 170.25 1.01%  operation 0
            "002304",  # 洋河股份 roi 70.48 roe 19.47 pe 3.62 pb 5.08 dividend 30.0 2.22%  operation 0
            "600323",  # 瀚蓝环境 roi 69.06 roe 14.24 pe 4.85 pb 2.64 dividend 2.2 0.95%  operation 0
            "600377",  # 宁沪高速 roi 68.68 roe 11.24 pe 6.11 pb 1.84 dividend 4.6 4.52%  operation 0
            "600332",  # 白云山 roi 68.05 roe 12.84 pe 5.3 pb 2.2 dividend 5.89 1.71%  operation 0
            "601628",  # 中国人寿 roi 64.77 roe 13.84 pe 4.68 pb 2.6 dividend 7.3 1.96%  operation 0
            "600660",  # 福耀玻璃 roi 64.41 roe 13.28 pe 4.85 pb 2.59 dividend 7.5 3.32%  operation 0
            "600012",  # 皖通高速 roi 63.8 roe 7.55 pe 8.45 pb 0.86 dividend 2.3 4.12%  operation 0
            "000858",  # 五 粮 液 roi 63.38 roe 26.63 pe 2.38 pb 9.56 dividend 22.0 1.09%  operation 0
            "600741",  # 华域汽车 roi 63.07 roe 9.98 pe 6.32 pb 1.53 dividend 8.5 3.56%  operation 0
            "600887",  # 伊利股份 roi 62.96 roe 22.09 pe 2.85 pb 7.59 dividend 8.1 2.41%  operation 0
            "600104",  # 上汽集团 roi 61.96 roe 7.52 pe 8.24 pb 0.9 dividend 8.8 4.58%  operation 0
            "000028",  # 国药一致 roi 61.13 roe 10.24 pe 5.97 pb 1.57 dividend 6.0 1.26%  operation 0
            "600019",  # 宝钢股份 roi 60.79 roe 6.28 pe 9.68 pb 0.65 dividend 2.8 5.37%  operation 0
            "000999",  # 华润三九 roi 60.66 roe 12.33 pe 4.92 pb 2.3 dividend 4.3 1.4%  operation 0
            "000538",  # 云南白药 roi 60.47 roe 18.16 pe 3.33 pb 3.55 dividend 30.0 2.76%  operation 0
            "600563",  # 法拉电子 roi 56.74 roe 17.62 pe 3.22 pb 5.12 dividend 13.0 2.1%  operation 0
            "600809",  # 山西汾酒 roi 55.02 roe 31.99 pe 1.72 pb 15.27 dividend 9.0 0.59%  operation 0
            "000596",  # 古井贡酒 roi 52.82 roe 23.27 pe 2.27 pb 8.98 dividend 15.0 0.88%  operation 0
            "600056",  # 中国医药 roi 49.94 roe 9.44 pe 5.29 pb 1.71 dividend 2.76 1.86%  operation 0
            "600298",  # 安琪酵母 roi 49.75 roe 21.17 pe 2.35 pb 7.95 dividend 4.0 0.8%  operation 0
            "600350",  # 山东高速 roi 49.41 roe 7.59 pe 6.51 pb 1.09 dividend 3.8 5.63%  operation 0
            "600033",  # 福建高速 roi 48.78 roe 6.31 pe 7.73 pb 0.81 dividend 0.5 1.79%  operation 0
            "000429",  # 粤高速Ａ roi 44.84 roe 8.32 pe 5.39 pb 1.61 dividend 4.22 5.7%  operation 0
            "600197",  # 伊力特 roi 43.66 roe 11.8 pe 3.7 pb 3.08 dividend 4.38 2.3%  operation 0
            "600196",  # 复星医药 roi 38.85 roe 11.1 pe 3.5 pb 2.78 dividend 3.9 1.1%  operation 0
            "600436",  # 片仔癀 roi 34.71 roe 26.1 pe 1.33 pb 15.24 dividend 8.2 0.46%  operation 0
            "600872",  # 中炬高新 roi 33.44 roe 20.39 pe 1.64 pb 10.79 dividend 2.8 0.5%  operation 0
            "600276",  # 恒瑞医药 roi 23.57 roe 22.24 pe 1.06 pb 16.48 dividend 2.3 0.24%  operation 0

            "600809",  # XD山西汾 roe 31.99 pe 1.9 pb 13.84 dividend 9.0 0.65%  operation 0
            "600585",  # 海螺水泥 roe 27.29 pe 11.21 pb 2.03 dividend 20.0 3.66%  operation 0
            "600846",  # 同济科技 roe 27.0 pe 11.69 pb 1.88 dividend 3.4 3.95%  operation 0
            "600566",  # 济川药业 roe 26.86 pe 7.84 pb 3.11 dividend 12.3 4.98%  operation 0
            "000858",  # 五 粮 液 roe 26.63 pe 2.9 pb 7.84 dividend 22.0 1.33%  operation 0
            "000049",  # 德赛电池 roe 26.25 pe 4.64 pb 4.61 dividend 7.0 1.4%  operation 0
            "600436",  # 片仔癀 roe 26.1 pe 1.5 pb 13.53 dividend 8.2 0.52%  operation 0
            "000568",  # 泸州老窖 roe 26.05 pe 3.59 pb 6.39 dividend 15.9 1.73%  operation 0
            "000333",  # 美的集团 roe 24.09 pe 5.47 pb 3.95 dividend 16.0 2.68%  operation 0
            "600048",  # 保利地产 roe 23.74 pe 16.13 pb 1.2 dividend 8.2 5.63%  operation 0
            "000002",  # 万 科Ａ roe 23.52 pe 12.94 pb 1.55 dividend 10.17 3.92%  operation 0
            "002507",  # 涪陵榨菜 roe 23.43 pe 2.23 pb 9.1 dividend 3.0 0.86%  operation 0
            "000596",  # 古井贡酒 roe 23.27 pe 2.63 pb 7.73 dividend 15.0 1.02%  operation 0
            "600887",  # 伊利股份 roe 22.09 pe 3.2 pb 6.76 dividend 8.1 2.71%  operation 0
            "000651",  # 格力电器 roe 22.02 pe 5.81 pb 3.13 dividend 12.0 2.04%  operation 0
            "601318",  # 中国平安 roe 21.69 pe 9.68 pb 1.94 dividend 13.0 1.77%  operation 0
            "601336",  # 新华保险 roe 21.63 pe 11.21 pb 1.61 dividend 14.1 3.12%  operation 0
            "600612",  # 老凤祥 roe 21.42 pe 5.55 pb 3.43 dividend 11.5 2.37%  operation 0
            "600309",  # 万华化学 roe 21.26 pe 5.67 pb 3.52 dividend 13.0 2.66%  operation 0
            "600298",  # 安琪酵母 roe 21.17 pe 2.58 pb 7.26 dividend 4.0 0.88%  operation 0
            "600383",  # 金地集团 roe 20.64 pe 16.4 pb 1.14 dividend 6.7 5.03%  operation 0
            "600872",  # 中炬高新 roe 20.39 pe 1.66 pb 10.65 dividend 2.8 0.5%  operation 0



            "000895",  # 双汇发展 roe 25.96 pe 3.27 pb 7.93 dividend 5.5 1.52%  operation 2 discount 3.05
            "603288",  # 海天味业 roe 25.46 pe 1.39 pb 18.27 dividend 9.8 0.96%  operation 6 discount 7.17
            "600519",  # 贵州茅台 roe 24.31 pe 2.18 pb 11.17 dividend 145.39 1.31%  operation 6 discount 4.6
            "600809",  # 山西汾酒 roe 23.38 pe 2.16 pb 10.81 dividend 7.5 0.83%  operation 6 discount 4.63
            "600887",  # 伊利股份 roe 23.12 pe 3.18 pb 7.27 dividend 7.0 2.41%  operation 6 discount 3.14
            "600763",  # 通策医疗 roe 23.09 pe 1.13 pb 20.51 dividend 0.3 0.03%  operation 6 discount 8.88
            "600566",  # 济川药业 roe 22.9 pe 6.82 pb 3.36 dividend 12.3 5.24%  operation 2 discount 1.47
            "601318",  # 中国平安 roe 22.19 pe 10.46 pb 2.12 dividend 18.5 2.37%  operation 6 discount 0.96
            "000651",  # 格力电器 roe 21.94 pe 6.21 pb 3.54 dividend 21.0 3.55%  operation 6 discount 1.61
            "000333",  # 美的集团 roe 21.61 pe 5.66 pb 3.82 dividend 13.0396 2.42%  operation 6 discount 1.77
            "601888",  # 中国国旅 roe 21.54 pe 2.72 pb 7.93 dividend 5.5 0.7%  operation 6 discount 3.68
            "600486",  # 扬农化工 roe 21.31 pe 4.76 pb 4.48 dividend 8.7 1.2%  operation 2 discount 2.1
            "000568",  # 泸州老窖 roe 20.45 pe 3.33 pb 6.14 dividend 15.5 1.99%  operation 6 discount 3.0
            "000596",  # 古井贡酒 roe 20.28 pe 2.79 pb 7.27 dividend 15.0 1.21%  operation 6 discount 3.58
            "002304",  # 洋河股份 roe 19.7 pe 4.98 pb 3.96 dividend 32.0 3.36%  operation 6 discount 2.01
            "002032",  # 苏 泊 尔 roe 19.6 pe 2.15 pb 9.14 dividend 12.78 1.8%  operation 6 discount 4.66
            "600309",  # 万华化学 roe 19.58 pe 5.19 pb 3.78 dividend 20.0 4.12%  operation 2 discount 1.93
            "600585",  # 海螺水泥 roe 18.66 pe 8.07 pb 2.31 dividend 16.9 3.03%  operation 6 discount 1.24
            "000858",  # 五 粮 液 roe 18.07 pe 2.56 pb 7.06 dividend 17.0 1.35%  operation 6 discount 3.91
            "002271",  # 东方雨虹 roe 17.84 pe 3.32 pb 5.37 dividend 3.0 0.95%  operation 6 discount 3.01
            "600436",  # 片仔癀 roe 17.66 pe 1.48 pb 11.91 dividend 6.0 0.48%  operation 6 discount 6.74
            "600612",  # 老凤祥 roe 17.2 pe 5.09 pb 3.38 dividend 11.0 2.51%  operation 6 discount 1.97
            "600690",  # 海尔智家 roe 17.11 pe 6.72 pb 2.55 dividend 3.51 2.0%  operation 6 discount 1.49
            "600668",  # 尖峰集团 roe 16.88 pe 12.15 pb 1.39 dividend 3.0 2.04%  operation 2 discount 0.82
            "000049",  # 德赛电池 roe 16.46 pe 3.75 pb 4.39 dividend 2.5 0.57%  operation 2 discount 2.67
            "600352",  # 浙江龙盛 roe 16.44 pe 8.46 pb 1.94 dividend 2.5 1.77%  operation 6 discount 1.18
            "601336",  # 新华保险 roe 16.3 pe 9.43 pb 1.73 dividend 7.7 1.74%  operation 2 discount 1.06
            "000661",  # 长春高新 roe 16.26 pe 1.2 pb 13.56 dividend 8.0 0.16%  operation 6 discount 8.34
            "600276",  # 恒瑞医药 roe 16.13 pe 0.95 pb 16.98 dividend 2.2 0.25%  operation 6 discount 10.53
            "000999",  # 华润三九 roe 15.86 pe 5.94 pb 2.67 dividend 3.9 1.15%  operation 6 discount 1.68
            "600606",  # 绿地控股 roe 15.7 pe 16.23 pb 0.97 dividend 3.0 5.02%  operation 6 discount 0.62
            "600663",  # 陆家嘴 roe 14.73 pe 5.27 pb 2.8 dividend 4.99 4.25%  operation 0 discount 1.9
            "600872",  # 中炬高新 roe 14.45 pe 1.6 pb 9.03 dividend 2.3 0.54%  operation 6 discount 6.25
            "600755",  # 厦门国贸 roe 14.4 pe 15.03 pb 0.96 dividend 2.7 3.97%  operation 6 discount 0.67
            "600298",  # 安琪酵母 roe 13.87 pe 2.58 pb 5.38 dividend 3.5 1.12%  operation 2 discount 3.88
            "600036",  # 招商银行 roe 13.73 pe 8.96 pb 1.53 dividend 9.4 2.75%  operation 6 discount 1.12
            "601601",  # 中国太保 roe 13.46 pe 8.17 pb 1.65 dividend 10.0 3.23%  operation 6 discount 1.22
            "002146",  # 荣盛发展 roe 13.32 pe 13.15 pb 1.01 dividend 4.5 5.26%  operation 2 discount 0.76
            "600332",  # 白云山 roe 13.08 pe 5.65 pb 2.31 dividend 4.24 1.23%  operation 6 discount 1.77
            "600064",  # 南京高科 roe 12.92 pe 12.68 pb 1.02 dividend 2.5 2.63%  operation 0 discount 0.79
            "600009",  # 上海机场 roe 12.9 pe 2.94 pb 4.38 dividend 6.6 0.94%  operation 6 discount 3.4
            "600846",  # 同济科技 roe 12.87 pe 5.73 pb 2.25 dividend 1.5 1.66%  operation 2 discount 1.75
            "600377",  # 宁沪高速 roe 12.86 pe 6.79 pb 1.89 dividend 4.6 4.42%  operation 0 discount 1.47
            "600188",  # 兖州煤业 roe 12.4 pe 15.59 pb 0.8 dividend 15.4 16.89%  operation 2 discount 0.64
            "600563",  # 法拉电子 roe 12.33 pe 2.68 pb 4.6 dividend 13.0 2.58%  operation 2 discount 3.73
            "601668",  # 中国建筑 roe 12.3 pe 13.03 pb 0.94 dividend 1.68 3.07%  operation 6 discount 0.77
            "600900",  # 长江电力 roe 12.28 pe 4.65 pb 2.64 dividend 6.8 3.9%  operation 4 discount 2.15
            "600197",  # 伊力特 roe 12.08 pe 5.09 pb 2.37 dividend 3.5 2.56%  operation 6 discount 1.97
            "600548",  # 深高速 roe 11.95 pe 10.2 pb 1.17 dividend 7.1 7.34%  operation 0 discount 0.98
            "000828",  # 东莞控股 roe 11.95 pe 10.44 pb 1.15 dividend 2.7 3.52%  operation 4 discount 0.96
            "600970",  # 中材国际 roe 11.82 pe 10.59 pb 1.12 dividend 2.65 4.23%  operation 6 discount 0.94
            "601166",  # 兴业银行 roe 11.57 pe 15.22 pb 0.76 dividend 6.9 3.97%  operation 2 discount 0.66
            "000429",  # 粤高速Ａ roe 11.55 pe 7.14 pb 1.62 dividend 5.62 7.57%  operation 0 discount 1.4
            "600323",  # 瀚蓝环境 roe 11.48 pe 4.61 pb 2.49 dividend 2.0 0.96%  operation 0 discount 2.17
            "600660",  # 福耀玻璃 roe 11.23 pe 4.07 pb 2.76 dividend 7.5 3.26%  operation 2 discount 2.46
            "600383",  # 金地集团 roe 11.07 pe 8.18 pb 1.35 dividend 6.0 4.08%  operation 0 discount 1.22
            "600068",  # 葛洲坝 roe 11.04 pe 10.59 pb 1.04 dividend 1.8 2.74%  operation 2 discount 0.94
            "600897",  # 厦门空港 roe 10.99 pe 6.83 pb 1.61 dividend 12.8 6.55%  operation 6 discount 1.46
            "601939",  # 建设银行 roe 10.96 pe 13.91 pb 0.79 dividend 3.06 4.72%  operation 6 discount 0.72
            "000002",  # 万 科Ａ roe 10.9 pe 5.28 pb 2.06 dividend 10.451 3.42%  operation 6 discount 1.89
            "600987",  # 航民股份 roe 10.86 pe 7.24 pb 1.5 dividend 2.8 4.4%  operation 6 discount 1.38
            "600062",  # 华润双鹤 roe 10.85 pe 6.53 pb 1.66 dividend 2.79 2.07%  operation 6 discount 1.53
            "600511",  # 国药股份 roe 10.85 pe 5.34 pb 2.03 dividend 4.0 1.5%  operation 6 discount 1.87
            "601006",  # 大秦铁路 roe 10.85 pe 11.4 pb 0.95 dividend 4.8 6.73%  operation 2 discount 0.88
            "600056",  # 中国医药 roe 10.82 pe 6.08 pb 1.78 dividend 4.3366 2.91%  operation 2 discount 1.64
            "601088",  # 中国神华 roe 10.69 pe 11.45 pb 0.93 dividend 8.8 5.41%  operation 2 discount 0.87
            "600048",  # 保利地产 roe 10.52 pe 6.65 pb 1.58 dividend 5.0 3.09%  operation 0 discount 1.5
            "601288",  # 农业银行 roe 10.52 pe 15.05 pb 0.7 dividend 1.739 5.07%  operation 6 discount 0.66
            "000581",  # 威孚高科 roe 10.5 pe 8.61 pb 1.22 dividend 12.0 6.04%  operation 2 discount 1.16
            "601398",  # 工商银行 roe 10.41 pe 13.3 pb 0.78 dividend 2.506 4.72%  operation 6 discount 0.75
            "000001",  # 平安银行 roe 10.33 pe 10.05 pb 1.03 dividend 1.45 1.0%  operation 6 discount 0.99
            "600016",  # 民生银行 roe 10.31 pe 17.96 pb 0.57 dividend 3.45 5.96%  operation 2 discount 0.56
            "600741",  # 华域汽车 roe 10.24 pe 6.08 pb 1.68 dividend 10.5 4.09%  operation 2 discount 1.64
            "002025",  # 航天电器 roe 10.12 pe 2.85 pb 3.55 dividend 1.5 0.62%  operation 2 discount 3.5
            "600007",  # 中国国贸 roe 10.07 pe 5.28 pb 1.91 dividend 3.2 2.3%  operation 4 discount 1.89
            "600376",  # 首开股份 roe 9.89 pe 13.05 pb 0.76 dividend 4.0 5.67%  operation 4 discount 0.77
            "601988",  # 中国银行 roe 9.81 pe 15.18 pb 0.65 dividend 1.84 5.15%  operation 2 discount 0.66
            "600557",  # 康缘药业 roe 9.8 pe 4.59 pb 2.13 dividend 0.8 0.58%  operation 6 discount 2.18

            "000513",  # 丽珠集团 roe 9.57 pe 2.94 pb 3.25 dividend 12.0 3.17%  operation 2 discount 3.4
            "000538",  # 云南白药 roe 9.47 pe 3.5 pb 2.7 dividend 20.0013 2.53%  operation 6 discount 2.85
            "601186",  # 中国铁建 roe 9.12 pe 10.67 pb 0.86 dividend 2.1 2.07%  operation 6 discount 0.94
            "600529",  # 山东药玻 roe 9.1 pe 1.67 pb 5.45 dividend 3.0 0.87%  operation 6 discount 5.98
            "601328",  # 交通银行 roe 8.9 pe 15.34 pb 0.58 dividend 3.0 5.68%  operation 2 discount 0.65
            "601566",  # 九牧王 roe 8.87 pe 6.11 pb 1.45 dividend 10.0 9.22%  operation 6 discount 1.64
            "600085",  # 同仁堂 roe 8.68 pe 2.36 pb 3.68 dividend 7.6 2.89%  operation 2 discount 4.24
            "601390",  # 中国中铁 roe 8.52 pe 11.29 pb 0.75 dividend 1.28 2.29%  operation 6 discount 0.89
            "600104",  # 上汽集团 roe 8.5 pe 7.99 pb 1.06 dividend 12.6 5.66%  operation 2 discount 1.25
            "600018",  # 上港集团 roe 8.41 pe 6.24 pb 1.35 dividend 1.54 3.29%  operation 0 discount 1.6
            "601607",  # 上海医药 roe 8.3 pe 6.31 pb 1.32 dividend 4.1 2.16%  operation 6 discount 1.59
            "600012",  # 皖通高速 roe 8.05 pe 8.84 pb 0.91 dividend 2.5 4.33%  operation 6 discount 1.13
            "000028",  # 国药一致 roe 7.73 pe 5.0 pb 1.55 dividend 4.0 0.89%  operation 2 discount 2.0
            "600350",  # 山东高速 roe 7.48 pe 10.26 pb 0.73 dividend 2.21 5.14%  operation 0 discount 0.97
            "601800",  # 中国交建 roe 7.06 pe 8.69 pb 0.81 dividend 2.3077 2.43%  operation 2 discount 1.15
            "600033",  # 福建高速 roe 6.94 pe 8.32 pb 0.83 dividend 1.5 5.15%  operation 0 discount 1.2
            "600196",  # 复星医药 roe 6.74 pe 2.83 pb 2.38 dividend 3.2 1.12%  operation 0 discount 3.53
            "600030",  # 中信证券 roe 6.57 pe 3.46 pb 1.9 dividend 3.5 1.39%  operation 2 discount 2.89
            "600153",  # 建发股份 roe 6.52 pe 7.95 pb 0.82 dividend 5.0 6.17%  operation 2 discount 1.26
            "002589",  # 瑞康医药 roe 6.52 pe 5.97 pb 1.09 dividend 0.52 0.81%  operation 2 discount 1.67
            "600820",  # 隧道股份 roe 6.48 pe 7.4 pb 0.88 dividend 1.9 3.18%  operation 6 discount 1.35
            "600269",  # 赣粤高速 roe 6.45 pe 11.39 pb 0.57 dividend 1.0 2.64%  operation 0 discount 0.88
            "600874",  # 创业环保 roe 6.4 pe 3.75 pb 1.71 dividend 1.06 1.46%  operation 0 discount 2.67
            "600823",  # 世茂股份 roe 6.37 pe 9.6 pb 0.66 dividend 2.6 6.06%  operation 4 discount 1.04
            "600639",  # 浦东金桥 roe 6.33 pe 4.02 pb 1.57 dividend 3.0 2.28%  operation 0 discount 2.49
            "600028",  # 中国石化 roe 5.96 pe 7.46 pb 0.8 dividend 3.8 7.93%  operation 2 discount 1.34
            "600019",  # 宝钢股份 roe 5.08 pe 7.39 pb 0.69 dividend 5.0 9.28%  operation 2 discount 1.35
        }

    def get_stock_list(self):
        return self.stock_list
