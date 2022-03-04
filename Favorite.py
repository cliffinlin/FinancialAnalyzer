# -*- coding: utf-8 -*-


stock_list = {
    # "600383",
    # # 金地集团 roi=122.55 roe=33.14 1/pe=28.89 rate=1.28 pb=1.07 dividend=6.7 yield=5.38% dividend_ratio=18.61% market_value=562.52
    # "600606",
    # # 绿地控股 roi=100.94 roe=29.17 1/pe=32.04 rate=1.08 pb=0.85 dividend=4.0 yield=7.1% dividend_ratio=22.17% market_value=685.07
    # "601668",
    # # 中国建筑 roi=89.51 roe=27.16 1/pe=30.8 rate=1.07 pb=0.77 dividend=1.85 yield=3.61% dividend_ratio=11.73% market_value=2148.61
    # "600048",
    # 保利地产 roi=83.89 roe=31.32 1/pe=21.09 rate=1.27 pb=1.25 dividend=8.2 yield=5.4% dividend_ratio=25.61% market_value=1816.97
    "000002",
    # # 万 科Ａ roi=51.44 roe=32.92 1/pe=15.47 rate=1.01 pb=1.81 dividend=10.17 yield=3.23% dividend_ratio=20.87% market_value=3658.42
    # "000921",
    # # 海信家电 roi=50.46 roe=28.9 1/pe=11.64 rate=1.5 pb=2.24 dividend=3.95 yield=2.62% dividend_ratio=22.5% market_value=205.5
    # "000951",
    # # 中国重汽 roi=48.95 roe=34.08 1/pe=8.6 rate=1.67 pb=3.29 dividend=5.5 yield=1.41% dividend_ratio=16.45% market_value=261.05
    # "000786",
    # # 北新建材 roi=39.67 roe=19.19 1/pe=3.4 rate=6.08 pb=4.82 dividend=0.82 yield=0.18% dividend_ratio=5.35% market_value=762.14
    # "600585",
    # # 海螺水泥 roi=36.07 roe=27.86 1/pe=12.33 rate=1.05 pb=1.9 dividend=20.0 yield=3.68% dividend_ratio=29.81% market_value=2883.88
    # "000581",
    # # 威孚高科 roi=26.88 roe=17.14 1/pe=11.79 rate=1.33 pb=1.35 dividend=11.0 yield=4.64% dividend_ratio=39.37% market_value=239.12
    # "000895",
    # # 双汇发展 roi=23.44 roe=41.58 1/pe=4.62 rate=1.22 pb=5.78 dividend=16.4 yield=3.98% dividend_ratio=86.18% market_value=1426.4
    # "601318",
    # # 中国平安 roi=23.4 roe=23.67 1/pe=10.19 rate=0.97 pb=2.05 dividend=14.0 yield=1.64% dividend_ratio=16.06% market_value=15638.75
    # "600612",
    # # 老凤祥 roi=19.92 roe=28.21 1/pe=6.66 rate=1.06 pb=3.75 dividend=11.5 yield=2.09% dividend_ratio=31.46% market_value=287.19
    # "601398",
    # # 工商银行 roi=16.77 roe=12.02 1/pe=15.0 rate=0.93 pb=0.75 dividend=2.63 yield=4.83% dividend_ratio=32.23% market_value=19388.5
    # "600056",
    # # 中国医药 roi=16.14 roe=16.53 1/pe=10.17 rate=0.96 pb=1.47 dividend=2.76 yield=2.02% dividend_ratio=19.92% market_value=145.63
    # "000877",
    # # 天山股份 roi=15.64 roe=17.81 1/pe=9.34 rate=0.94 pb=1.73 dividend=4.8 yield=2.74% dividend_ratio=29.3% market_value=183.95
    # "601088",
    # # 中国神华 roi=15.54 roe=13.79 1/pe=12.95 rate=0.87 pb=1.03 dividend=12.6 yield=6.79% dividend_ratio=52.4% market_value=3689.58
    # "601939",
    # # 建设银行 roi=15.35 roe=12.13 1/pe=13.61 rate=0.93 pb=0.83 dividend=3.2 yield=4.37% dividend_ratio=32.07% market_value=18325.8
    # "000049",
    # # 德赛电池 roi=15.13 roe=31.89 1/pe=4.52 rate=1.05 pb=5.75 dividend=7.0 yield=1.0% dividend_ratio=22.08% market_value=145.25
    # "601319",
    # # 中国人保 roi=13.83 roe=15.48 1/pe=10.39 rate=0.86 pb=1.35 dividend=1.52 yield=2.52% dividend_ratio=24.21% market_value=2671.13
    # "601658",
    # # 邮储银行 roi=13.7 roe=12.0 1/pe=11.53 rate=0.99 pb=0.98 dividend=2.1 yield=3.54% dividend_ratio=30.65% market_value=5166.53
    # "601607",
    # # 上海医药 roi=13.52 roe=12.57 1/pe=9.52 rate=1.13 pb=1.22 dividend=4.4 yield=2.31% dividend_ratio=24.31% market_value=540.28
    # "000028",
    # # 国药一致 roi=12.75 roe=12.67 1/pe=9.32 rate=1.08 pb=1.25 dividend=6.0 yield=1.52% dividend_ratio=16.28% market_value=169.37
    # "600298",
    # # 安琪酵母 roi=12.24 roe=27.21 1/pe=3.06 rate=1.47 pb=7.72 dividend=4.0 yield=0.77% dividend_ratio=25.24% market_value=426.71
    # "601336",
    # # 新华保险 roi=12.04 roe=15.87 1/pe=7.9 rate=0.96 pb=1.71 dividend=14.1 yield=2.74% dividend_ratio=34.74% market_value=1603.13
    # "600036",
    # # 招商银行 roi=11.61 roe=16.49 1/pe=6.9 rate=1.02 pb=2.17 dividend=12.0 yield=2.25% dividend_ratio=32.64% market_value=13447.22
    # "600511",
    # # 国药股份 roi=11.0 roe=17.37 1/pe=6.53 rate=0.97 pb=2.37 dividend=6.38 yield=1.83% dividend_ratio=28.07% market_value=262.79
    # "600104",
    # # 上汽集团 roi=10.86 roe=11.78 1/pe=12.13 rate=0.76 pb=0.93 dividend=8.8 yield=4.33% dividend_ratio=35.68% market_value=2376.42
    # "600887",
    # # 伊利股份 roi=9.62 roe=30.24 1/pe=3.06 rate=1.04 pb=8.46 dividend=8.1 yield=2.05% dividend_ratio=67.07% market_value=2401.42
    # "600900",
    # # 长江电力 roi=8.53 roe=16.04 1/pe=4.97 rate=1.07 pb=2.92 dividend=6.8 yield=3.19% dividend_ratio=64.23% market_value=4848.56
    # "601006",
    # # 大秦铁路 roi=8.27 roe=10.58 1/pe=11.49 rate=0.68 pb=0.88 dividend=4.8 yield=6.96% dividend_ratio=60.53% market_value=1025.81
    # "600519",
    # # 贵州茅台 roi=7.67 roe=37.85 1/pe=1.86 rate=1.09 pb=17.14 dividend=170.25 yield=0.84% dividend_ratio=45.11% market_value=25450.57
    # "601601",
    # # 中国太保 roi=7.59 roe=13.91 1/pe=6.27 rate=0.87 pb=1.98 dividend=12.0 yield=2.88% dividend_ratio=45.93% market_value=4008.8
    # "000001",
    # # 平安银行 roi=7.58 roe=10.6 1/pe=6.94 rate=1.03 pb=1.42 dividend=1.8 yield=0.84% dividend_ratio=12.08% market_value=4168.39
    # "600741",
    # # 华域汽车 roi=7.04 roe=12.77 1/pe=7.66 rate=0.72 pb=1.6 dividend=8.5 yield=3.34% dividend_ratio=43.62% market_value=802.37
    # "000568",
    # # 泸州老窖 roi=6.88 roe=30.26 1/pe=1.82 rate=1.25 pb=14.1 dividend=15.9 yield=0.75% dividend_ratio=41.47% market_value=3086.09
    # "000858",
    # # 五 粮 液 roi=6.84 roe=29.28 1/pe=1.98 rate=1.18 pb=12.78 dividend=22.0 yield=0.83% dividend_ratio=42.01% market_value=10264.91
    # "601628",
    # # 中国人寿 roi=6.73 roe=12.78 1/pe=5.37 rate=0.98 pb=2.17 dividend=7.3 yield=2.28% dividend_ratio=42.39% market_value=9058.84
    # "600845",
    # # 宝信软件 roi=6.47 roe=18.64 1/pe=2.17 rate=1.6 pb=8.56 dividend=4.0 yield=0.78% dividend_ratio=36.04% market_value=590.2
    # "600563",
    # # 法拉电子 roi=6.38 roe=21.35 1/pe=2.51 rate=1.19 pb=7.76 dividend=13.0 yield=1.39% dividend_ratio=55.52% market_value=209.97
    # "600332",
    # # 白云山 roi=6.31 roe=11.98 1/pe=6.2 rate=0.85 pb=1.81 dividend=5.89 yield=2.05% dividend_ratio=33.08% market_value=467.25
    # "600486",
    # # 扬农化工 roi=6.26 roe=22.41 1/pe=2.94 rate=0.95 pb=6.63 dividend=6.5 yield=0.53% dividend_ratio=17.91% market_value=382.79
    # "600132",
    # # 重庆啤酒 roi=5.95 roe=46.43 1/pe=1.35 rate=0.95 pb=38.6 dividend=14.0 yield=1.46% dividend_ratio=107.96% market_value=463.6
    # "002507",
    # # 涪陵榨菜 roi=5.79 roe=25.17 1/pe=2.15 rate=1.07 pb=10.03 dividend=3.0 yield=0.73% dividend_ratio=33.79% market_value=325.93
    # "002304",
    # # 洋河股份 roi=5.47 roe=20.46 1/pe=2.97 rate=0.9 pb=6.53 dividend=30.0 yield=1.81% dividend_ratio=60.91% market_value=2495.27
    # "000661",
    # # 长春高新 roi=5.42 roe=20.46 1/pe=1.88 rate=1.41 pb=16.12 dividend=8.0 yield=0.18% dividend_ratio=9.79% market_value=1762.56
    # "000547",
    # # 航天发展 roi=5.07 roe=11.27 1/pe=3.06 rate=1.47 pb=3.41 dividend=0.88 yield=0.52% dividend_ratio=16.83% market_value=274.21
    # "600809",
    # # 山西汾酒 roi=5.06 roe=37.47 1/pe=1.0 rate=1.35 pb=29.81 dividend=9.0 yield=0.29% dividend_ratio=28.86% market_value=2726.14
    # "002179",
    # # 中航光电 roi=4.99 roe=18.97 1/pe=2.14 rate=1.23 pb=7.19 dividend=1.5 yield=0.25% dividend_ratio=11.48% market_value=672.75
    # "000039",
    # # 中集集团 roi=4.93 roe=8.05 1/pe=5.42 rate=1.13 pb=1.44 dividend=1.2 yield=0.85% dividend_ratio=15.69% market_value=507.26
    # "603288",
    # # 海天味业 roi=4.9 roe=33.72 1/pe=1.21 rate=1.2 pb=27.61 dividend=10.8 yield=0.69% dividend_ratio=57.41% market_value=5035.65
    # "000538",
    # # 云南白药 roi=4.69 roe=13.05 1/pe=3.02 rate=1.19 pb=4.25 dividend=30.0 yield=2.37% dividend_ratio=78.46% market_value=1618.6
    # "002025",
    # # 航天电器 roi=4.61 roe=16.77 1/pe=2.52 rate=1.09 pb=5.95 dividend=1.5 yield=0.33% dividend_ratio=13.09% market_value=195.02
    # "000651",
    # # 格力电器 roi=4.55 roe=16.27 1/pe=4.66 rate=0.6 pb=3.07 dividend=22.0 yield=3.76% dividend_ratio=80.69% market_value=3519.2
    # "600271",
    # # 航天信息 roi=4.54 roe=13.05 1/pe=7.1 rate=0.49 pb=1.77 dividend=2.31 yield=2.1% dividend_ratio=29.63% market_value=203.44
    # "600597",
    # # 光明乳业 roi=4.14 roe=12.04 1/pe=3.21 rate=1.07 pb=3.44 dividend=1.3 yield=0.77% dividend_ratio=24.1% market_value=205.47
    # "000596",
    # # 古井贡酒 roi=3.72 roe=22.23 1/pe=1.97 rate=0.85 pb=9.94 dividend=15.0 yield=0.78% dividend_ratio=39.57% market_value=966.86
    # "600760",
    # # 中航沈飞 roi=3.67 roe=16.68 1/pe=1.63 rate=1.35 pb=8.83 dividend=1.5 yield=0.24% dividend_ratio=14.79% market_value=869.92
    # "600085",
    # # 同仁堂 roi=3.62 roe=13.3 1/pe=3.68 rate=0.74 pb=3.7 dividend=2.6 yield=1.01% dividend_ratio=27.38% market_value=353.84
    # "600309",
    # # 万华化学 roi=3.28 roe=19.66 1/pe=2.17 rate=0.77 pb=8.31 dividend=13.0 yield=1.12% dividend_ratio=51.45% market_value=3652.47
    # "600690",
    # # 海尔智家 roi=3.19 roe=14.17 1/pe=3.26 rate=0.69 pb=3.95 dividend=3.75 yield=1.25% dividend_ratio=38.32% market_value=2784.54
    # "600436",
    # # 片仔癀 roi=3.12 roe=25.78 1/pe=1.0 rate=1.21 pb=21.5 dividend=8.2 yield=0.31% dividend_ratio=30.56% market_value=1617.8
    # "600377",
    # # 宁沪高速 roi=2.98 roe=9.37 1/pe=5.39 rate=0.59 pb=1.74 dividend=4.6 yield=4.82% dividend_ratio=89.41% market_value=480.6
    # "600600",
    # # 青岛啤酒 roi=2.89 roe=11.51 1/pe=2.2 rate=1.14 pb=4.93 dividend=5.5 yield=0.71% dividend_ratio=32.44% market_value=1050.42
    # "600897",
    # # 厦门空港 roi=1.22 roe=6.46 1/pe=4.39 rate=0.43 pb=1.45 dividend=5.23 yield=2.93% dividend_ratio=66.68% market_value=53.25
    # "601888",
    # # 中国中免 roi=0.77 roe=18.79 1/pe=0.61 rate=0.67 pb=30.74 dividend=7.2 yield=0.23% dividend_ratio=38.41% market_value=6041.15
    # "600893",
    # # 航发动力 roi=0.6 roe=3.9 1/pe=1.02 rate=1.52 pb=3.61 dividend=1.44 yield=0.3% dividend_ratio=29.19% market_value=1285.08
    # "000768",
    # # 中航西飞 roi=0.4 roe=4.19 1/pe=0.95 rate=1.01 pb=4.32 dividend=1.2 yield=0.46% dividend_ratio=48.48% market_value=722.62
    # "600009",
    # # 上海机场 roi=0.0 roe=0.0 1/pe=0.0 rate=0.0 pb=0.0 dividend=0.0 yield=0.0% dividend_ratio=0.0% market_value=0.0
    # "600019",
    # # 宝钢股份 roi=0.0 roe=0.0 1/pe=0.0 rate=0.0 pb=0.0 dividend=0.0 yield=0.0% dividend_ratio=0.0% market_value=0.0
    # "600025",
    # # 华能水电 roi=0.0 roe=0.0 1/pe=0.0 rate=0.0 pb=0.0 dividend=0.0 yield=0.0% dividend_ratio=0.0% market_value=0.0
    # "600028",
    # # 中国石化 roi=0.0 roe=0.0 1/pe=0.0 rate=0.0 pb=0.0 dividend=0.0 yield=0.0% dividend_ratio=0.0% market_value=0.0
    # "600030",
    # # 中信证券 roi=0.0 roe=0.0 1/pe=0.0 rate=0.0 pb=0.0 dividend=0.0 yield=0.0% dividend_ratio=0.0% market_value=0.0
    # "300999",
    # # 金龙鱼 roi=0.0 roe=0.0 1/pe=1.64 rate=1.94 pb=5.91 dividend=0.0 yield=0.0% dividend_ratio=0.0% market_value=4530.82
}