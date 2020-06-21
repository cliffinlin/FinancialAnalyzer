# -*- coding: utf-8 -*-

class Favorite:
    def __init__(self):
        self.stock_list = {
            "000672",  # 上峰水泥 roe 33.5 pe 9.15 pb 3.66 dividend 4.0 1.93%  operation 6 discount 1.09
            "600779",  # 水井坊 roe 33.11 pe 2.91 pb 11.39 dividend 11.42 2.54%  operation 6 discount 3.44
            "000895",  # 双汇发展 roe 25.96 pe 3.27 pb 7.93 dividend 5.5 1.52%  operation 2 discount 3.05
            "603288",  # 海天味业 roe 25.46 pe 1.39 pb 18.27 dividend 9.8 0.96%  operation 6 discount 7.17
            "600801",  # 华新水泥 roe 24.41 pe 9.51 pb 2.57 dividend 11.5 4.73%  operation 6 discount 1.05
            "600519",  # 贵州茅台 roe 24.31 pe 2.18 pb 11.17 dividend 145.39 1.31%  operation 6 discount 4.6
            "600809",  # 山西汾酒 roe 23.38 pe 2.16 pb 10.81 dividend 7.5 0.83%  operation 6 discount 4.63
            "600887",  # 伊利股份 roe 23.12 pe 3.18 pb 7.27 dividend 7.0 2.41%  operation 6 discount 3.14
            "600763",  # 通策医疗 roe 23.09 pe 1.13 pb 20.51 dividend 0.3 0.03%  operation 6 discount 8.88
            "600566",  # 济川药业 roe 22.9 pe 6.82 pb 3.36 dividend 12.3 5.24%  operation 2 discount 1.47
            "601318",  # 中国平安 roe 22.19 pe 10.46 pb 2.12 dividend 18.5 2.37%  operation 6 discount 0.96
            "000651",  # 格力电器 roe 21.94 pe 6.21 pb 3.54 dividend 21.0 3.55%  operation 6 discount 1.61
            "600031",  # 三一重工 roe 21.61 pe 6.2 pb 3.49 dividend 2.6 1.48%  operation 6 discount 1.61
            "000333",  # 美的集团 roe 21.61 pe 5.66 pb 3.82 dividend 13.0396 2.42%  operation 6 discount 1.77
            "601888",  # 中国国旅 roe 21.54 pe 2.72 pb 7.93 dividend 5.5 0.7%  operation 6 discount 3.68
            "600486",  # 扬农化工 roe 21.31 pe 4.76 pb 4.48 dividend 8.7 1.2%  operation 2 discount 2.1
            "600398",  # 海澜之家 roe 20.7 pe 8.62 pb 2.4 dividend 3.8 5.53%  operation 6 discount 1.16
            "000568",  # 泸州老窖 roe 20.45 pe 3.33 pb 6.14 dividend 15.5 1.99%  operation 6 discount 3.0
            "000596",  # 古井贡酒 roe 20.28 pe 2.79 pb 7.27 dividend 15.0 1.21%  operation 6 discount 3.58
            "600368",  # 五洲交通 roe 19.9 pe 18.22 pb 1.09 dividend 1.14 2.73%  operation 0 discount 0.55
            "002304",  # 洋河股份 roe 19.7 pe 4.98 pb 3.96 dividend 32.0 3.36%  operation 6 discount 2.01
            "002032",  # 苏 泊 尔 roe 19.6 pe 2.15 pb 9.14 dividend 12.78 1.8%  operation 6 discount 4.66
            "600309",  # 万华化学 roe 19.58 pe 5.19 pb 3.78 dividend 20.0 4.12%  operation 2 discount 1.93
            "600585",  # 海螺水泥 roe 18.66 pe 8.07 pb 2.31 dividend 16.9 3.03%  operation 6 discount 1.24
            "002035",  # 华帝股份 roe 18.62 pe 4.91 pb 3.79 dividend 3.0 2.48%  operation 2 discount 2.04
            "600452",  # 涪陵电力 roe 18.12 pe 5.37 pb 3.38 dividend 2.2 1.18%  operation 6 discount 1.86
            "000858",  # 五 粮 液 roe 18.07 pe 2.56 pb 7.06 dividend 17.0 1.35%  operation 6 discount 3.91
            "002271",  # 东方雨虹 roe 17.84 pe 3.32 pb 5.37 dividend 3.0 0.95%  operation 6 discount 3.01
            "600436",  # 片仔癀 roe 17.66 pe 1.48 pb 11.91 dividend 6.0 0.48%  operation 6 discount 6.74
            "002242",  # 九阳股份 roe 17.5 pe 2.83 pb 6.18 dividend 13.0 4.57%  operation 2 discount 3.53
            "600612",  # 老凤祥 roe 17.2 pe 5.09 pb 3.38 dividend 11.0 2.51%  operation 6 discount 1.97
            "600690",  # 海尔智家 roe 17.11 pe 6.72 pb 2.55 dividend 3.51 2.0%  operation 6 discount 1.49
            "600995",  # 文山电力 roe 17.09 pe 10.63 pb 1.61 dividend 2.0 2.66%  operation 2 discount 0.94
            "002508",  # 老板电器 roe 17.03 pe 3.72 pb 4.58 dividend 8.0 2.6%  operation 6 discount 2.69
            "600668",  # 尖峰集团 roe 16.88 pe 12.15 pb 1.39 dividend 3.0 2.04%  operation 2 discount 0.82
            "000049",  # 德赛电池 roe 16.46 pe 3.75 pb 4.39 dividend 2.5 0.57%  operation 2 discount 2.67
            "600352",  # 浙江龙盛 roe 16.44 pe 8.46 pb 1.94 dividend 2.5 1.77%  operation 6 discount 1.18
            "601336",  # 新华保险 roe 16.3 pe 9.43 pb 1.73 dividend 7.7 1.74%  operation 2 discount 1.06
            "000661",  # 长春高新 roe 16.26 pe 1.2 pb 13.56 dividend 8.0 0.16%  operation 6 discount 8.34
            "600276",  # 恒瑞医药 roe 16.13 pe 0.95 pb 16.98 dividend 2.2 0.25%  operation 6 discount 10.53
            "300014",  # 亿纬锂能 roe 16.12 pe 1.77 pb 9.1 dividend 1.00104 0.15%  operation 6 discount 5.65
            "601225",  # 陕西煤业 roe 16.11 pe 11.63 pb 1.38 dividend 3.3 4.23%  operation 2 discount 0.86
            "000999",  # 华润三九 roe 15.86 pe 5.94 pb 2.67 dividend 3.9 1.15%  operation 6 discount 1.68
            "600606",  # 绿地控股 roe 15.7 pe 16.23 pb 0.97 dividend 3.0 5.02%  operation 6 discount 0.62
            "601628",  # 中国人寿 roe 15.15 pe 7.0 pb 2.16 dividend 1.6 0.55%  operation 2 discount 1.43
            "600663",  # 陆家嘴 roe 14.73 pe 5.27 pb 2.8 dividend 4.99 4.25%  operation 0 discount 1.9
            "002014",  # 永新股份 roe 14.48 pe 5.39 pb 2.69 dividend 3.5 3.53%  operation 6 discount 1.85
            "600872",  # 中炬高新 roe 14.45 pe 1.6 pb 9.03 dividend 2.3 0.54%  operation 6 discount 6.25
            "600755",  # 厦门国贸 roe 14.4 pe 15.03 pb 0.96 dividend 2.7 3.97%  operation 6 discount 0.67
            "600426",  # 华鲁恒升 roe 13.98 pe 7.01 pb 1.99 dividend 2.0 1.19%  operation 2 discount 1.43
            "600298",  # 安琪酵母 roe 13.87 pe 2.58 pb 5.38 dividend 3.5 1.12%  operation 2 discount 3.88
            "600036",  # 招商银行 roe 13.73 pe 8.96 pb 1.53 dividend 9.4 2.75%  operation 6 discount 1.12
            "600273",  # 嘉化能源 roe 13.64 pe 6.6 pb 2.07 dividend 2.9 2.91%  operation 6 discount 1.51
            "601601",  # 中国太保 roe 13.46 pe 8.17 pb 1.65 dividend 10.0 3.23%  operation 6 discount 1.22
            "002146",  # 荣盛发展 roe 13.32 pe 13.15 pb 1.01 dividend 4.5 5.26%  operation 2 discount 0.76
            "600332",  # 白云山 roe 13.08 pe 5.65 pb 2.31 dividend 4.24 1.23%  operation 6 discount 1.77
            "600600",  # 青岛啤酒 roe 12.99 pe 4.38 pb 2.96 dividend 4.8 1.1%  operation 6 discount 2.28
            "600064",  # 南京高科 roe 12.92 pe 12.68 pb 1.02 dividend 2.5 2.63%  operation 0 discount 0.79
            "600009",  # 上海机场 roe 12.9 pe 2.94 pb 4.38 dividend 6.6 0.94%  operation 6 discount 3.4
            "600846",  # 同济科技 roe 12.87 pe 5.73 pb 2.25 dividend 1.5 1.66%  operation 2 discount 1.75
            "600377",  # 宁沪高速 roe 12.86 pe 6.79 pb 1.89 dividend 4.6 4.42%  operation 0 discount 1.47
            "002543",  # 万和电气 roe 12.81 pe 6.89 pb 1.86 dividend 4.3 4.94%  operation 2 discount 1.45
            "002287",  # 奇正藏药 roe 12.79 pe 2.38 pb 5.38 dividend 4.07724 1.87%  operation 6 discount 4.21
            "000876",  # 新 希 望 roe 12.76 pe 2.5 pb 5.11 dividend 0.3 0.1%  operation 2 discount 4.01
            "600593",  # 大连圣亚 roe 12.56 pe 1.45 pb 8.66 dividend 0.0 0.0%  operation 0 discount 6.89
            "600326",  # 西藏天路 roe 12.54 pe 7.17 pb 1.75 dividend 0.8 1.16%  operation 2 discount 1.39
            "600183",  # 生益科技 roe 12.53 pe 1.53 pb 8.21 dividend 3.5 1.17%  operation 2 discount 6.55
            "002128",  # 露天煤业 roe 12.41 pe 13.23 pb 0.94 dividend 4.0 5.19%  operation 6 discount 0.76
            "600188",  # 兖州煤业 roe 12.4 pe 15.59 pb 0.8 dividend 15.4 16.89%  operation 2 discount 0.64
            "600563",  # 法拉电子 roe 12.33 pe 2.68 pb 4.6 dividend 13.0 2.58%  operation 2 discount 3.73
            "000029",  # 深深房Ａ roe 12.32 pe 0.0 pb 0.0 dividend 2.0 0.0%  operation 2 discount 0.0
            "601668",  # 中国建筑 roe 12.3 pe 13.03 pb 0.94 dividend 1.68 3.07%  operation 6 discount 0.77
            "600900",  # 长江电力 roe 12.28 pe 4.65 pb 2.64 dividend 6.8 3.9%  operation 4 discount 2.15
            "601877",  # 正泰电器 roe 12.28 pe 5.06 pb 2.43 dividend 6.0 2.28%  operation 2 discount 1.97
            "600197",  # 伊力特 roe 12.08 pe 5.09 pb 2.37 dividend 3.5 2.56%  operation 6 discount 1.97
            "002081",  # 金 螳 螂 roe 12.01 pe 7.28 pb 1.65 dividend 2.0 2.23%  operation 6 discount 1.37
            "002275",  # 桂林三金 roe 12.01 pe 4.04 pb 2.97 dividend 3.5 2.52%  operation 2 discount 2.48
            "600548",  # 深高速 roe 11.95 pe 10.2 pb 1.17 dividend 7.1 7.34%  operation 0 discount 0.98
            "000828",  # 东莞控股 roe 11.95 pe 10.44 pb 1.15 dividend 2.7 3.52%  operation 4 discount 0.96
            "600970",  # 中材国际 roe 11.82 pe 10.59 pb 1.12 dividend 2.65 4.23%  operation 6 discount 0.94
            "600885",  # 宏发股份 roe 11.64 pe 2.2 pb 5.3 dividend 2.9 0.85%  operation 2 discount 4.56
            "002088",  # 鲁阳节能 roe 11.6 pe 6.4 pb 1.81 dividend 6.5 6.25%  operation 6 discount 1.56
            "002557",  # 洽洽食品 roe 11.6 pe 1.91 pb 6.06 dividend 5.0 1.21%  operation 2 discount 5.22
            "601166",  # 兴业银行 roe 11.57 pe 15.22 pb 0.76 dividend 6.9 3.97%  operation 2 discount 0.66
            "000429",  # 粤高速Ａ roe 11.55 pe 7.14 pb 1.62 dividend 5.62 7.57%  operation 0 discount 1.4
            "600323",  # 瀚蓝环境 roe 11.48 pe 4.61 pb 2.49 dividend 2.0 0.96%  operation 0 discount 2.17
            "601799",  # 星宇股份 roe 11.48 pe 1.98 pb 5.8 dividend 9.9 1.02%  operation 6 discount 5.05
            "600660",  # 福耀玻璃 roe 11.23 pe 4.07 pb 2.76 dividend 7.5 3.26%  operation 2 discount 2.46
            "600449",  # 宁夏建材 roe 11.21 pe 11.67 pb 0.96 dividend 3.0 2.75%  operation 2 discount 0.86
            "600383",  # 金地集团 roe 11.07 pe 8.18 pb 1.35 dividend 6.0 4.08%  operation 0 discount 1.22
            "600068",  # 葛洲坝 roe 11.04 pe 10.59 pb 1.04 dividend 1.8 2.74%  operation 2 discount 0.94
            "600897",  # 厦门空港 roe 10.99 pe 6.83 pb 1.61 dividend 12.8 6.55%  operation 6 discount 1.46
            "601939",  # 建设银行 roe 10.96 pe 13.91 pb 0.79 dividend 3.06 4.72%  operation 6 discount 0.72
            "000002",  # 万 科Ａ roe 10.9 pe 5.28 pb 2.06 dividend 10.451 3.42%  operation 6 discount 1.89
            "600987",  # 航民股份 roe 10.86 pe 7.24 pb 1.5 dividend 2.8 4.4%  operation 6 discount 1.38
            "600062",  # 华润双鹤 roe 10.85 pe 6.53 pb 1.66 dividend 2.79 2.07%  operation 6 discount 1.53
            "600511",  # 国药股份 roe 10.85 pe 5.34 pb 2.03 dividend 4.0 1.5%  operation 6 discount 1.87
            "600750",  # 江中药业 roe 10.85 pe 5.65 pb 1.92 dividend 3.5 2.72%  operation 6 discount 1.77
            "601006",  # 大秦铁路 roe 10.85 pe 11.4 pb 0.95 dividend 4.8 6.73%  operation 2 discount 0.88
            "600056",  # 中国医药 roe 10.82 pe 6.08 pb 1.78 dividend 4.3366 2.91%  operation 2 discount 1.64
            "601088",  # 中国神华 roe 10.69 pe 11.45 pb 0.93 dividend 8.8 5.41%  operation 2 discount 0.87
            "600048",  # 保利地产 roe 10.52 pe 6.65 pb 1.58 dividend 5.0 3.09%  operation 0 discount 1.5
            "601288",  # 农业银行 roe 10.52 pe 15.05 pb 0.7 dividend 1.739 5.07%  operation 6 discount 0.66
            "000581",  # 威孚高科 roe 10.5 pe 8.61 pb 1.22 dividend 12.0 6.04%  operation 2 discount 1.16
            "601398",  # 工商银行 roe 10.41 pe 13.3 pb 0.78 dividend 2.506 4.72%  operation 6 discount 0.75
            "002083",  # 孚日股份 roe 10.34 pe 5.42 pb 1.91 dividend 1.0 1.32%  operation 2 discount 1.84
            "000001",  # 平安银行 roe 10.33 pe 10.05 pb 1.03 dividend 1.45 1.0%  operation 6 discount 0.99
            "600016",  # 民生银行 roe 10.31 pe 17.96 pb 0.57 dividend 3.45 5.96%  operation 2 discount 0.56
            "600741",  # 华域汽车 roe 10.24 pe 6.08 pb 1.68 dividend 10.5 4.09%  operation 2 discount 1.64
            "002025",  # 航天电器 roe 10.12 pe 2.85 pb 3.55 dividend 1.5 0.62%  operation 2 discount 3.5
            "600007",  # 中国国贸 roe 10.07 pe 5.28 pb 1.91 dividend 3.2 2.3%  operation 4 discount 1.89
            "601677",  # 明泰铝业 roe 9.96 pe 10.13 pb 0.98 dividend 2.0 1.78%  operation 6 discount 0.99
            "600376",  # 首开股份 roe 9.89 pe 13.05 pb 0.76 dividend 4.0 5.67%  operation 4 discount 0.77
            "000601",  # 韶能股份 roe 9.89 pe 6.22 pb 1.59 dividend 1.5 2.11%  operation 0 discount 1.61
            "000910",  # 大亚圣象 roe 9.88 pe 6.27 pb 1.58 dividend 1.3 0.96%  operation 6 discount 1.6
            "601988",  # 中国银行 roe 9.81 pe 15.18 pb 0.65 dividend 1.84 5.15%  operation 2 discount 0.66
            "600557",  # 康缘药业 roe 9.8 pe 4.59 pb 2.13 dividend 0.8 0.58%  operation 6 discount 2.18
            "000732",  # 泰禾集团 roe 9.64 pe 14.4 pb 0.67 dividend 2.2 3.72%  operation 4 discount 0.69
            "000069",  # 华侨城Ａ roe 9.62 pe 11.03 pb 0.87 dividend 3.0 4.52%  operation 4 discount 0.91
            "000513",  # 丽珠集团 roe 9.57 pe 2.94 pb 3.25 dividend 12.0 3.17%  operation 2 discount 3.4
            "600373",  # 中文传媒 roe 9.49 pe 6.97 pb 1.36 dividend 5.0 3.71%  operation 2 discount 1.43
            "000538",  # 云南白药 roe 9.47 pe 3.5 pb 2.7 dividend 20.0013 2.53%  operation 6 discount 2.85
            "601186",  # 中国铁建 roe 9.12 pe 10.67 pb 0.86 dividend 2.1 2.07%  operation 6 discount 0.94
            "000860",  # 顺鑫农业 roe 9.12 pe 1.51 pb 6.04 dividend 1.5 0.25%  operation 6 discount 6.62
            "600529",  # 山东药玻 roe 9.1 pe 1.67 pb 5.45 dividend 3.0 0.87%  operation 6 discount 5.98
            "000501",  # 鄂武商Ａ roe 9.04 pe 9.41 pb 0.96 dividend 2.0 1.77%  operation 2 discount 1.06
            "600757",  # 长江传媒 roe 8.98 pe 9.62 pb 0.93 dividend 1.5 2.73%  operation 2 discount 1.04
            "601328",  # 交通银行 roe 8.9 pe 15.34 pb 0.58 dividend 3.0 5.68%  operation 2 discount 0.65
            "601566",  # 九牧王 roe 8.87 pe 6.11 pb 1.45 dividend 10.0 9.22%  operation 6 discount 1.64
            "600085",  # 同仁堂 roe 8.68 pe 2.36 pb 3.68 dividend 7.6 2.89%  operation 2 discount 4.24
            "601390",  # 中国中铁 roe 8.52 pe 11.29 pb 0.75 dividend 1.28 2.29%  operation 6 discount 0.89
            "600104",  # 上汽集团 roe 8.5 pe 7.99 pb 1.06 dividend 12.6 5.66%  operation 2 discount 1.25
            "600018",  # 上港集团 roe 8.41 pe 6.24 pb 1.35 dividend 1.54 3.29%  operation 0 discount 1.6
            "600138",  # 中青旅 roe 8.3 pe 7.18 pb 1.16 dividend 1.4 1.33%  operation 2 discount 1.39
            "601607",  # 上海医药 roe 8.3 pe 6.31 pb 1.32 dividend 4.1 2.16%  operation 6 discount 1.59
            "601928",  # 凤凰传媒 roe 8.3 pe 6.52 pb 1.27 dividend 3.0 4.37%  operation 2 discount 1.53
            "600012",  # 皖通高速 roe 8.05 pe 8.84 pb 0.91 dividend 2.5 4.33%  operation 6 discount 1.13
            "000726",  # 鲁 泰Ａ roe 8.0 pe 7.24 pb 1.1 dividend 5.0 5.29%  operation 2 discount 1.38
            "600054",  # 黄山旅游 roe 7.75 pe 5.43 pb 1.43 dividend 1.32 1.56%  operation 2 discount 1.84
            "000028",  # 国药一致 roe 7.73 pe 5.0 pb 1.55 dividend 4.0 0.89%  operation 2 discount 2.0
            "600835",  # 上海机电 roe 7.68 pe 5.45 pb 1.41 dividend 4.4 2.85%  operation 2 discount 1.83
            "600697",  # 欧亚集团 roe 7.64 pe 7.83 pb 0.98 dividend 3.9 2.44%  operation 2 discount 1.28
            "600350",  # 山东高速 roe 7.48 pe 10.26 pb 0.73 dividend 2.21 5.14%  operation 0 discount 0.97
            "000498",  # 山东路桥 roe 7.09 pe 5.68 pb 1.25 dividend 0.75 1.27%  operation 6 discount 1.76
            "601800",  # 中国交建 roe 7.06 pe 8.69 pb 0.81 dividend 2.3077 2.43%  operation 2 discount 1.15
            "600033",  # 福建高速 roe 6.94 pe 8.32 pb 0.83 dividend 1.5 5.15%  operation 0 discount 1.2
            "600196",  # 复星医药 roe 6.74 pe 2.83 pb 2.38 dividend 3.2 1.12%  operation 0 discount 3.53
            "600754",  # 锦江酒店 roe 6.71 pe 3.1 pb 2.16 dividend 6.0 2.04%  operation 4 discount 3.23
            "000719",  # 中原传媒 roe 6.65 pe 6.97 pb 0.96 dividend 2.5 3.36%  operation 2 discount 1.44
            "600030",  # 中信证券 roe 6.57 pe 3.46 pb 1.9 dividend 3.5 1.39%  operation 2 discount 2.89
            "600195",  # 中牧股份 roe 6.57 pe 2.21 pb 2.98 dividend 2.42 1.65%  operation 2 discount 4.53
            "600153",  # 建发股份 roe 6.52 pe 7.95 pb 0.82 dividend 5.0 6.17%  operation 2 discount 1.26
            "603019",  # 中科曙光 roe 6.52 pe 0.59 pb 11.0 dividend 1.4 0.3%  operation 6 discount 16.86
            "002589",  # 瑞康医药 roe 6.52 pe 5.97 pb 1.09 dividend 0.52 0.81%  operation 2 discount 1.67
            "300212",  # 易华录 roe 6.51 pe 0.74 pb 8.76 dividend 1.6 0.32%  operation 0 discount 13.46
            "300145",  # 中金环境 roe 6.5 pe 4.13 pb 1.57 dividend 0.5 1.19%  operation 2 discount 2.42
            "600213",  # 亚星客车 roe 6.49 pe 0.71 pb 9.14 dividend 0.6 0.72%  operation 2 discount 14.07
            "002074",  # 国轩高科 roe 6.49 pe 2.23 pb 2.91 dividend 1.0 0.44%  operation 2 discount 4.48
            "600820",  # 隧道股份 roe 6.48 pe 7.4 pb 0.88 dividend 1.9 3.18%  operation 6 discount 1.35
            "600269",  # 赣粤高速 roe 6.45 pe 11.39 pb 0.57 dividend 1.0 2.64%  operation 0 discount 0.88
            "600874",  # 创业环保 roe 6.4 pe 3.75 pb 1.71 dividend 1.06 1.46%  operation 0 discount 2.67
            "600823",  # 世茂股份 roe 6.37 pe 9.6 pb 0.66 dividend 2.6 6.06%  operation 4 discount 1.04
            "600639",  # 浦东金桥 roe 6.33 pe 4.02 pb 1.57 dividend 3.0 2.28%  operation 0 discount 2.49
            "600028",  # 中国石化 roe 5.96 pe 7.46 pb 0.8 dividend 3.8 7.93%  operation 2 discount 1.34
            "600019",  # 宝钢股份 roe 5.08 pe 7.39 pb 0.69 dividend 5.0 9.28%  operation 2 discount 1.35
            "000544",  # 中原环保 roe 4.44 pe 4.01 pb 1.11 dividend 2.5 3.81%  operation 0 discount 2.49
            "000402",  # 金 融 街 roe 4.24 pe 6.36 pb 0.67 dividend 3.0 4.15%  operation 0 discount 1.57

            "000789",  # 万年青 roe 27.03 pe 12.93 pb 2.09 dividend 8.0 6.02%  operation 2 discount 0.77
            "002016",  # 世荣兆业 roe 24.67 pe 12.93 pb 1.91 dividend 5.0 6.98%  operation 2 discount 0.77
            "600325",  # 华发股份 roe 20.81 pe 19.81 pb 1.05 dividend 3.5 5.27%  operation 0 discount 0.5
            "000736",  # 中交地产 roe 19.84 pe 13.33 pb 1.49 dividend 1.9 2.5%  operation 2 discount 0.75


        }

    def get_stock_list(self):
        return self.stock_list
