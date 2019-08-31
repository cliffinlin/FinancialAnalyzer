# -*- coding: utf-8 -*-


def get_stock_list():
    return stock_list


stock_list = {
    # hold
    "000895",  # 双汇发展 pe 14.684 pb 5.325 dividend 5.5 0.0%

    # draw.draw("dividend > 4 AND dividend_yield < 1", "dividend", "ASC")
    "600600",  # 青岛啤酒 pe 50.047 pb 3.757 dividend 4.8 0.91%
    "601888",  # 中国国旅 pe 60.114 pb 10.057 dividend 5.5 0.58%
    "600436",  # 片仔癀 pe 53.307 pb 11.032 dividend 6.0 0.6%
    "600009",  # 上海机场 pe 39.632 pb 5.669 dividend 6.6 0.76%
    "601318",  # 中国平安 pe 14.932 pb 2.628 dividend 7.5 0.83%
    "000661",  # 长春高新 pe 58.497 pb 9.985 dividend 8.0 0.23%
    "603288",  # 海天味业 pe 66.605 pb 20.843 dividend 9.8 0.91%
    # draw.draw("dividend > 3 AND dividend_yield >= 1 AND dividend_yield < 2", "dividend", "ASC")
    "600007",  # 中国国贸 pe 21.299 pb 2.306 dividend 3.2 1.95%
    "600030",  # 中信证券 pe 29.403 pb 1.759 dividend 3.5 1.55%
    "600298",  # 安琪酵母 pe 26.936 pb 5.053 dividend 3.5 1.25%
    "000999",  # 华润三九 pe 20.253 pb 2.379 dividend 3.9 1.32%
    "600511",  # 国药股份 pe 16.098 pb 2.327 dividend 4.0 1.36%
    "600332",  # 白云山 pe 17.958 pb 2.624 dividend 4.24 1.12%
    "600809",  # 山西汾酒 pe 42.155 pb 8.709 dividend 7.5 1.05%
    "000596",  # 古井贡酒 pe 35.006 pb 7.085 dividend 15.0 1.27%
    "000568",  # 泸州老窖 pe 37.265 pb 7.0 dividend 15.5 1.75%
    "000858",  # 五 粮 液 pe 37.45 pb 7.218 dividend 17.0 1.31%
    "600519",  # 贵州茅台 pe 40.332 pb 12.371 dividend 145.39 1.29%
    # draw.draw("dividend >= 4 AND dividend_yield >= 2 AND dividend_yield < 3", "dividend", "ASC")
    "601607",  # 上海医药 pe 13.837 pb 1.345 dividend 4.1 2.16%
    "600754",  # 锦江股份 pe 20.531 pb 1.709 dividend 6.0 2.59%
    "600887",  # 伊利股份 pe 26.981 pb 6.607 dividend 7.0 2.45%
    "600036",  # 招商银行 pe 11.588 pb 1.72 dividend 9.4 2.59%
    "601601",  # 中国太保 pe 20.111 pb 2.237 dividend 10.0 2.5%
    "000333",  # 美的集团 pe 16.964 pb 3.85 dividend 13.0396 2.5%
    "000651",  # 格力电器 pe 12.589 pb 3.532 dividend 15.0 2.73%
    "000538",  # 云南白药 pe 24.484 pb 3.909 dividend 20.0013 2.57%
    "002304",  # 洋河股份 pe 19.95 pb 4.28 dividend 32.0 2.98%
    # draw.draw("dividend >= 4 AND dividend_yield >= 3 AND dividend_yield < 4", "dividend", "ASC")
    "600056",  # 中国医药 pe 9.581 pb 1.67 dividend 4.3366 3.13%
    "600048",  # 保利地产 pe 9.101 pb 1.443 dividend 5.0 3.46%
    "600900",  # 长江电力 pe 18.389 pb 2.862 dividend 6.8 3.6%
    "600660",  # 福耀玻璃 pe 13.189 pb 2.619 dividend 7.5 3.47%
    "000423",  # 东阿阿胶 pe 10.164 pb 1.981 dividend 10.0953 3.12%
    "000002",  # 万 科Ａ pe 8.81 pb 1.892 dividend 10.451 3.88%
    # draw.draw("dividend >= 1 AND dividend_yield >= 4", "dividend", "ASC")
    "601288",  # 农业银行 pe 5.78 pb 0.722 dividend 1.739 5.1%
    "601988",  # 中国银行 pe 6.0 pb 0.667 dividend 1.84 5.2%
    "600350",  # 山东高速 pe 7.141 pb 0.755 dividend 2.21 5.06%
    "600012",  # 皖通高速 pe 8.138 pb 0.882 dividend 2.5 4.54%
    "601398",  # 工商银行 pe 6.61 pb 0.83 dividend 2.506 4.62%
    "600028",  # 中国石化 pe 9.616 pb 0.82 dividend 2.6 5.19%
    "601158",  # 重庆水务 pe 19.0 pb 1.939 dividend 2.8 4.91%
    "600606",  # 绿地控股 pe 7.301 pb 1.139 dividend 3.0 4.42%
    "601328",  # 交通银行 pe 5.698 pb 0.617 dividend 3.0 5.48%
    "000069",  # 华侨城Ａ pe 5.385 pb 0.929 dividend 3.0 4.32%
    "601939",  # 建设银行 pe 7.01 pb 0.881 dividend 3.06 4.37%
    "600873",  # 梅花生物 pe 14.063 pb 1.597 dividend 3.3 7.33%
    "002014",  # 永新股份 pe 15.378 pb 2.035 dividend 3.5 5.06%
    "600376",  # 首开股份 pe 6.987 pb 0.833 dividend 4.0 5.37%
    "600377",  # 宁沪高速 pe 11.51 pb 1.808 dividend 4.6 4.6%
    "601006",  # 大秦铁路 pe 7.929 pb 1.046 dividend 4.8 6.18%
    "600019",  # 宝钢股份 pe 6.103 pb 0.769 dividend 5.0 8.45%
    "000039",  # 中集集团 pe 9.045 pb 0.856 dividend 5.5 5.48%
    "000429",  # 粤高速Ａ pe 9.675 pb 1.614 dividend 5.62 7.26%
    "600383",  # 金地集团 pe 6.816 pb 1.152 dividend 6.0 4.92%
    "600548",  # 深高速 pe 5.859 pb 1.129 dividend 7.1 7.68%
    "601088",  # 中国神华 pe 8.517 pb 1.096 dividend 8.8 4.69%
    "601566",  # 九牧王 pe 12.473 pb 1.582 dividend 10.0 8.62%
    "600741",  # 华域汽车 pe 9.356 pb 1.639 dividend 10.5 4.41%
    "000581",  # 威孚高科 pe 7.236 pb 1.042 dividend 12.0 7.0%
    "600104",  # 上汽集团 pe 7.982 pb 1.171 dividend 12.6 5.12%
    "600897",  # 厦门空港 pe 13.428 pb 1.826 dividend 12.8 5.61%
    "600585",  # 海螺水泥 pe 7.126 pb 1.786 dividend 16.9 4.21%
    "600309",  # 万华化学 pe 11.059 pb 3.551 dividend 20.0 4.66%
    # other
    "000028",  # 国药一致 pe 16.219 pb 1.649 dividend 4.0 0.87%
    "600196",  # 复星医药 pe 25.701 pb 2.454 dividend 3.2 1.16%
    "600566",  # 济川药业 pe 13.846 pb 3.998 dividend 12.3 4.27%
    "000513",  # 丽珠集团 pe 18.987 pb 1.957 dividend 12.0 4.19%

    "000828",  # 东莞控股 pe 8.335 pb 1.304 dividend 2.7 3.21%
    "600195",  # 中牧股份 pe 22.18 pb 2.216 dividend 2.42 1.58%
    "601800",  # 中国交建 pe 8.748 pb 0.907 dividend 2.3077 2.29%
    "600276",  # 恒瑞医药 pe 69.636 pb 16.588 dividend 2.2 0.29%
    "601186",  # 中国铁建 pe 7.23 pb 0.805 dividend 2.1 2.31%
    "600068",  # 葛洲坝 pe 6.178 pb 0.916 dividend 1.8 3.28%
    "600004",  # 白云机场 pe 33.836 pb 2.429 dividend 1.7 0.91%
    "601668",  # 中国建筑 pe 6.391 pb 1.011 dividend 1.68 3.02%
    "601628",  # 中国人寿 pe 75.41 pb 2.305 dividend 1.6 0.54%
    "600018",  # 上港集团 pe 13.351 pb 1.767 dividend 1.54 2.6%
    "601390",  # 中国中铁 pe 8.357 pb 0.837 dividend 1.28 2.13%

    "600668",  # 尖峰集团 pe 6.923 pb 1.242 dividend 3.0 2.53%
    "002233",  # 塔牌集团 pe 7.014 pb 1.316 dividend 4.3 4.24%

    "600033",  # 福建高速 pe 11.597 pb 0.904 dividend 1.5 4.84%

    "600987",  # 航民股份 pe 6.385 pb 1.503 dividend 2.8 4.57%

    "600398",  # 海澜之家 pe 11.169 pb 2.864 dividend 3.8 4.42%

    "600340",  # 华夏幸福 pe 7.23 pb 2.115 dividend 12.0 4.38%
    "002146",  # 荣盛发展 pe 4.851 pb 1.056 dividend 4.5 5.33%

    "002101",  # 广东鸿图 pe 10.81 pb 0.801 dividend 3.15 4.63%

    "600563",  # 法拉电子 pe 19.881 pb 3.789 dividend 13.0 3.25%

    "600970",  # 中材国际 pe 7.641 pb 1.12 dividend 2.65 4.45%
    "600755",  # 厦门国贸 pe 9.205 pb 1.078 dividend 2.7 3.53%

    "600697",  # 欧亚集团 pe 10.674 pb 1.085 dividend 3.9 2.24%

    "600674",  # 川投能源 pe 11.874 pb 1.719 dividend 3.0 3.12%
    "600236",  # 桂冠电力 pe 12.103 pb 1.968 dividend 2.5 5.25%

    "600612",  # 老凤祥 pe 21.341 pb 3.917 dividend 11.0 2.24%
}
