# -*- coding: utf-8 -*-


class BlackList:
    def __init__(self):
        self.stock_list = {
            # "300362",  # 天翔环境 roe 8519.97 pe 0.0 pb 0.0 dividend 0.0 0.0%  operation 0
            # "600556",  # 天下秀 roe 222.38 pe 1.0 pb 31.59 dividend 0.15 0.08%  operation 0
            # "600768",  # 宁波富邦 roe 115.83 pe 8.82 pb 5.67 dividend 0.0 0.0%  operation 0
            # "002234",  # 民和股份 roe 91.0 pe 20.92 pb 2.27 dividend 6.0 2.77%  operation 0
            # "000048",  # 京基智农 roe 90.41 pe 10.59 pb 4.41 dividend 7.5 3.05%  operation 0
            # "002714",  # 牧原股份 roe 64.61 pe 3.84 pb 6.58 dividend 5.5 0.73%  operation 0
            # "002458",  # 益生股份 roe 60.55 pe 12.96 pb 4.75 dividend 10.0 6.42%  operation 0
            # "002607",  # 中公教育 roe 59.04 pe 1.01 pb 85.98 dividend 2.4 0.83%  operation 0
            # "002611",  # 东方精工 roe 55.71 pe 26.68 pb 1.59 dividend 0.0 0.0%  operation 0
            # "600678",  # 四川金顶 roe 52.51 pe 1.82 pb 17.12 dividend 0.0 0.0%  operation 0
            # "002605",  # 姚记科技 roe 51.39 pe 6.76 pb 7.04 dividend 4.02 1.14%  operation 0
            # "300122",  # 智飞生物 roe 50.84 pe 1.55 pb 24.49 dividend 5.0 0.52%  operation 0
            # "002299",  # 圣农发展 roe 49.36 pe 12.51 pb 3.52 dividend 15.0 5.64%  operation 0
            # "600132",  # 重庆啤酒 roe 49.19 pe 2.04 pb 20.45 dividend 14.0 2.28%  operation 0
            # "600052",  # 浙江广厦 roe 48.62 pe 37.18 pb 0.9 dividend 0.95 2.61%  operation 0
            # "002182",  # 云海金属 roe 48.07 pe 15.8 pb 2.1 dividend 1.5 1.7%  operation 0
            # "600802",  # 福建水泥 roe 46.49 pe 11.14 pb 3.06 dividend 1.6 1.45%  operation 0
            # "002157",  # 正邦科技 roe 46.11 pe 6.96 pb 4.13 dividend 0.7 0.41%  operation 0
            # "002124",  # 天邦股份 roe 44.6 pe 6.95 pb 3.91 dividend 0.0 0.0%  operation 0
            # "300216",  # 千山药机 roe 42.41 pe 0.0 pb 0.0 dividend 0.0 0.0%  operation 0
            # "600685",  # 中船防务 roe 41.81 pe 16.57 pb 1.87 dividend 0.0 0.0%  operation 0
            # "603111",  # 康尼机电 roe 39.52 pe 10.87 pb 2.42 dividend 0.0 0.0%  operation 0
            # "002161",  # 远 望 谷 roe 38.94 pe 10.13 pb 2.96 dividend 0.0 0.0%  operation 0
            # "600779",  # 水井坊 roe 38.48 pe 2.9 pb 11.97 dividend 14.5 2.57%  operation 0
            # "002555",  # 三七互娱 roe 37.46 pe 2.75 pb 11.14 dividend 3.0 0.73%  operation 0
            # "002190",  # 成飞集成 roe 37.43 pe 8.19 pb 3.15 dividend 0.6 0.27%  operation 0
            # "002248",  # 华东数控 roe 36.8 pe 1.34 pb 19.88 dividend 0.0 0.0%  operation 0
            # "002015",  # 协鑫能科 roe 36.32 pe 8.75 pb 1.51 dividend 0.0 0.0%  operation 0
            # "002459",  # 晶澳科技 roe 34.75 pe 7.44 pb 2.47 dividend 0.0 0.0%  operation 0
            # "300462",  # 华铭智能 roe 34.66 pe 7.36 pb 2.55 dividend 1.5 0.68%  operation 0
            # "002755",  # 奥赛康 roe 34.44 pe 4.23 pb 6.31 dividend 2.2 1.23%  operation 0
            # "300417",  # 南华仪器 roe 33.31 pe 8.61 pb 2.85 dividend 8.0 4.34%  operation 0
            # "002415",  # 海康威视 roe 31.56 pe 4.39 pb 6.08 dividend 7.0 2.32%  operation 0
            # "002127",  # 南极电商 roe 31.42 pe 2.34 pb 10.4 dividend 1.24 0.59%  operation 0
            # "603609",  # 禾丰牧业 roe 31.19 pe 10.02 pb 2.27 dividend 2.2 1.49%  operation 0
            # "600764",  # 中国海防 roe 31.14 pe 3.32 pb 2.91 dividend 2.73 1.07%  operation 0
            # "600546",  # 山煤国际 roe 31.08 pe 5.14 pb 3.35 dividend 0.6 0.53%  operation 0
            # "600346",  # 恒力石化 roe 30.35 pe 12.09 pb 2.51 dividend 4.0 2.92%  operation 0
            # "002463",  # 沪电股份 roe 30.04 pe 2.98 pb 7.87 dividend 2.0 0.82%  operation 0
            # "300132",  # 青松股份 roe 29.52 pe 3.8 pb 3.85 dividend 1.35 0.58%  operation 0
            # "601012",  # 隆基股份 roe 29.43 pe 5.1 pb 4.34 dividend 2.0 0.59%  operation 0
            # "300033",  # 同花顺 roe 29.12 pe 1.37 pb 18.35 dividend 8.5 0.68%  operation 0
            # "600745",  # 闻泰科技 roe 28.79 pe 1.41 pb 6.03 dividend 1.5 0.13%  operation 0
            # "600466",  # 蓝光发展 roe 28.03 pe 21.39 pb 1.02 dividend 2.87 5.32%  operation 0
            # "002016",  # 世荣兆业 roe 28.0 pe 15.22 pb 1.61 dividend 0.0 0.0%  operation 0
            # "603899",  # 晨光文具 roe 27.89 pe 2.11 pb 10.93 dividend 4.0 0.76%  operation 0
            # "002677",  # 浙江美大 roe 27.84 pe 5.66 pb 4.65 dividend 5.42 4.89%  operation 0
            # "002653",  # 海思科 roe 27.77 pe 2.03 pb 11.31 dividend 0.92 0.35%  operation 0
            # "603988",  # 中电电机 roe 27.6 pe 6.6 pb 3.65 dividend 2.52 2.05%  operation 0
            # "000537",  # 广宇发展 roe 27.57 pe 22.19 pb 0.98 dividend 3.0 3.99%  operation 0
            # "000876",  # 新 希 望 roe 27.48 pe 4.89 pb 4.43 dividend 1.5 0.52%  operation 0
            # "000717",  # 韶钢松山 roe 27.19 pe 18.63 pb 1.15 dividend 1.5 3.78%  operation 0
            # "601100",  # 恒立液压 roe 27.05 pe 2.02 pb 11.01 dividend 6.0 0.81%  operation 0
            # "000987",  # 越秀金控 roe 26.9 pe 14.05 pb 1.4 dividend 1.7 1.48%  operation 0
            # "002100",  # 天康生物 roe 26.9 pe 5.88 pb 3.27 dividend 2.0 1.32%  operation 0
            # "000656",  # 金科股份 roe 26.78 pe 13.76 pb 1.48 dividend 4.5 5.68%  operation 0
            # "600031",  # 三一重工 roe 26.08 pe 6.28 pb 3.49 dividend 4.2 2.19%  operation 0
            # "000011",  # 深物业A roe 26.08 pe 9.46 pb 2.86 dividend 3.6 2.28%  operation 0
            # "300016",  # 北陆药业 roe 26.07 pe 5.97 pb 3.72 dividend 0.7 0.63%  operation 0
            # "002271",  # 东方雨虹 roe 25.76 pe 3.16 pb 5.75 dividend 3.0 0.72%  operation 0
            # "002746",  # 仙坛股份 roe 25.76 pe 16.2 pb 1.8 dividend 4.0 2.99%  operation 0
            # "600053",  # 九鼎投资 roe 25.5 pe 5.2 pb 4.34 dividend 0.0 0.0%  operation 0
            # "000789",  # 万年青 roe 25.41 pe 13.17 pb 2.0 dividend 7.0 5.24%  operation 0
            # "000897",  # 津滨发展 roe 24.36 pe 6.95 pb 2.82 dividend 0.0 0.0%  operation 0
            # "000517",  # 荣安地产 roe 24.33 pe 16.68 pb 1.16 dividend 1.0 4.02%  operation 0
            # "600051",  # 宁波联合 roe 24.17 pe 22.69 pb 0.87 dividend 2.0 2.42%  operation 0
            # "000403",  # 双林生物 roe 24.17 pe 0.84 pb 23.08 dividend 1.21 0.17%  operation 0
            # "000961",  # 中南建设 roe 23.7 pe 13.42 pb 1.45 dividend 2.8 3.29%  operation 0
            # "300418",  # 昆仑万维 roe 23.58 pe 5.62 pb 4.59 dividend 0.26 0.12%  operation 0
            # "600217",  # 中再资环 roe 23.53 pe 4.89 pb 3.92 dividend 0.0 0.0%  operation 0
            # "000090",  # 天健集团 roe 23.5 pe 16.64 pb 1.49 dividend 3.8 5.48%  operation 0
            # "300347",  # 泰格医药 roe 23.07 pe 1.41 pb 14.94 dividend 2.78 0.31%  operation 0
            # "600325",  # 华发股份 roe 22.93 pe 19.22 pb 1.04 dividend 4.0 5.76%  operation 0
            # "002214",  # 大立科技 roe 22.75 pe 2.2 pb 8.94 dividend 0.8 0.34%  operation 0
            # "300432",  # 富临精工 roe 22.57 pe 8.97 pb 2.02 dividend 0.0 0.0%  operation 0
            # "600183",  # 生益科技 roe 22.54 pe 2.31 pb 7.25 dividend 4.0 1.36%  operation 0
            # "000671",  # 阳 光 城 roe 22.44 pe 15.34 pb 1.21 dividend 1.99 3.02%  operation 0
            # "300003",  # 乐普医疗 roe 22.29 pe 2.34 pb 8.36 dividend 2.0 0.55%  operation 0
            # "002601",  # 龙蟒佰利 roe 22.15 pe 7.83 pb 2.48 dividend 9.0 4.99%  operation 0
            # "002690",  # 美亚光电 roe 22.02 pe 1.46 pb 14.79 dividend 8.0 1.51%  operation 0
            # "601919",  # 中远海控 roe 21.85 pe 14.55 pb 1.22 dividend 0.0 0.0%  operation 0
            # "300136",  # 信维通信 roe 21.67 pe 1.79 pb 9.83 dividend 0.5 0.1%  operation 0
            # "000933",  # 神火股份 roe 21.65 pe 16.66 pb 1.02 dividend 1.0 2.38%  operation 0
            # "002572",  # 索菲亚 roe 21.55 pe 4.64 pb 3.79 dividend 5.5 2.44%  operation 0
            # "002697",  # 红旗连锁 roe 21.55 pe 3.84 pb 4.72 dividend 0.87 0.78%  operation 0
            # "000401",  # 冀东水泥 roe 21.43 pe 10.52 pb 1.88 dividend 5.0 2.99%  operation 0
            # "002045",  # 国光电器 roe 21.38 pe 7.88 pb 2.37 dividend 0.8 0.83%  operation 0
            # "601225",  # 陕西煤业 roe 21.34 pe 15.4 pb 1.19 dividend 3.6 4.94%  operation 0
            # "603808",  # 歌力思 roe 21.34 pe 12.1 pb 2.0 dividend 2.5 1.97%  operation 0
            # "600720",  # 祁连山 roe 21.3 pe 9.34 pb 1.94 dividend 5.8 3.41%  operation 0
            # "002216",  # 三全食品 roe 21.29 pe 2.38 pb 7.4 dividend 0.6 0.26%  operation 0
            # "600507",  # 方大特钢 roe 21.28 pe 12.98 pb 1.13 dividend 0.0 0.0%  operation 0
            # "603606",  # 东方电缆 roe 20.89 pe 5.36 pb 4.16 dividend 1.3 0.94%  operation 0
            # "603369",  # 今世缘 roe 20.74 pe 2.99 pb 6.01 dividend 4.1 1.1%  operation 0
            # "002372",  # 伟星新材 roe 20.67 pe 4.95 pb 4.78 dividend 5.0 4.14%  operation 0
            # "603568",  # 伟明环保 roe 21.21 pe 3.31 pb 6.17 dividend 3.1 1.06%  operation 0
            # "600985",  # 淮北矿业 roe 20.4 pe 20.03 pb 0.89 dividend 6.0 7.36%  operation 0
            # "600766",  # 园城黄金 roe 20.38 pe 0.65 pb 25.86 dividend 0.0 0.0%  operation 0
            # "000338",  # 潍柴动力 roe 20.36 pe 7.89 pb 2.29 dividend 1.36 0.99%  operation 0
            # "002379",  # 宏创控股 roe 20.32 pe 10.0 pb 1.69 dividend 0.0 0.0%  operation 0
            # "300198",  # 纳川股份 roe 20.14 pe 5.89 pb 2.84 dividend 0.0 0.0%  operation 0
            # "601058",  # 赛轮轮胎 roe 20.07 pe 13.2 pb 1.32 dividend 1.0 2.78%  operation 0
            #
            # #民企
            # "000672",  # 上峰水泥 roe 60.54 pe 12.23 pb 3.27 dividend 9.0 3.88%  operation 0
            # "600340",  # 华夏幸福 roe 38.95 pe 21.14 pb 1.44 dividend 15.0 6.57%  operation 0
            # "002146",  # 荣盛发展 roe 26.73 pe 26.34 pb 0.84 dividend 4.8 5.96%  operation 0
            # "600153",  # 建发股份 roe 20.38 pe 22.06 pb 0.79 dividend 5.0 5.48%  operation 0
            # "600352",  # 浙江龙盛 roe 22.95 pe 11.86 pb 1.62 dividend 2.5 1.95%  operation 0
            # "002236",  # 大华股份 roe 24.5 pe 5.61 pb 3.56 dividend 1.33 0.7%  operation 0
            # "000963",  # 华东医药 roe 23.54 pe 7.44 pb 3.04 dividend 2.8 1.19%  operation 0
            # "002311",  # 海大集团 roe 23.15 pe 2.41 pb 8.08 dividend 3.5 0.73%  operation 0
            # "600763",  # 通策医疗 roe 24.81 pe 0.72 pb 27.51 dividend 0.0 0.0%  operation 0
            # "600276",  # 恒瑞医药 roe 22.24 pe 1.1 pb 15.75 dividend 2.3 0.25%  operation 0
            # "603288",  # 海天味业 roe 29.79 pe 1.42 pb 17.72 dividend 10.8 0.9%  operation 0
            # "002242",  # 九阳股份 roe 20.02 pe 2.98 pb 6.95 dividend 5.8 1.64%  operation 0
            # "002508",  # 老板电器 roe 23.79 pe 4.95 pb 4.3 dividend 5.0 1.55%  operation 0
            # "002035",  # 华帝股份 roe 25.31 pe 7.15 pb 3.07 dividend 3.0 2.82%  operation 0
            #
            # #外资
            # "600801",  # 华新水泥 roe 22.93 pe 11.15 pb 2.37 dividend 12.1 4.97%  operation 0
            # "002032",  # 苏 泊 尔 roe 26.63 pe 3.05 pb 8.12 dividend 13.3 1.95%  operation 0
            #
            # #水泥+医药
            # "600668",  # 尖峰集团 roe 22.27 pe 14.32 pb 1.3 dividend 3.0 2.02%  operation 0
            #
            # #农药
            # "600486",  # 扬农化工 roe 25.97 pe 5.04 pb 4.64 dividend 6.5 0.79%  operation 0
            #
            # #
            # # "600507",  # 方大特钢 roe 26.15 pe 13.22 pb 1.98 dividend 17.0 19.02%  operation 2 discount 0.76
            # # "000717",  # 韶钢松山 roe 17.27 pe 12.25 pb 1.41 dividend 0.5 1.15%  operation 2 discount 0.82
            # # "002110",  # 三钢闽光 roe 15.81 pe 13.54 pb 1.17 dividend 20.0 23.5%  operation 2 discount 0.74
            # # "600282",  # 南钢股份 roe 14.38 pe 16.7 pb 0.86 dividend 3.0 9.35%  operation 2 discount 0.6
            # # "601003",  # 柳钢股份 roe 14.16 pe 11.29 pb 1.25 dividend 6.0 11.7%  operation 2 discount 0.89
            # # "600307",  # 酒钢宏兴 roe 10.59 pe 10.81 pb 0.98 dividend 0.3 1.62%  operation 2 discount 0.92
            # #
            # # "000537",  # 广宇发展 roe 19.07 pe 18.42 pb 1.04 dividend 1.3 1.81%  operation 0 discount 0.54
            # # "000885",  # 城发环境 roe 19.01 pe 10.34 pb 1.84 dividend 2.3 2.12%  operation 0 discount 0.97
            # #
            # # "000835",  # 长城动漫 roe 208.47 pe -2.97 pb -70.21 dividend 0.4 0.99%  operation 0 discount -3.37
            # # "600198",  # 大唐电信 roe 156.96 pe -5.84 pb -26.86 dividend 2.0 1.86%  operation 0 discount -1.71
            # # "600898",  # 国美通讯 roe 155.94 pe -11.64 pb -13.4 dividend 0.5 0.71%  operation 2 discount -0.86
            # # "600306",  # 商业城 roe 138.58 pe -8.27 pb -16.75 dividend 0.2 0.38%  operation 2 discount -1.21
            # # "300090",  # 盛运环保 roe 138.55 pe -31.95 pb -4.34 dividend 0.5 3.82%  operation 0 discount -0.31
            # # "300362",  # 天翔环境 roe 115.46 pe -102.59 pb -1.13 dividend 0.2 0.96%  operation 0 discount -0.1
            # # "000927",  # 一汽夏利 roe 115.44 pe -10.63 pb -10.86 dividend 0.1 0.24%  operation 2 discount -0.94
            # # "300116",  # 坚瑞沃能 roe 107.76 pe -60.55 pb -1.78 dividend 0.1 0.56%  operation 0 discount -0.17
            # # "600651",  # 飞乐音响 roe 102.51 pe -17.8 pb -5.76 dividend 0.17 0.45%  operation 0 discount -0.56
            # # "300104",  # 乐视网 roe 76.99 pe 0.0 pb 0.0 dividend 0.28 0.0%  operation 0 discount 0.0
            # # "002607",  # 中公教育 roe 71.19 pe 1.37 pb 52.07 dividend 6.199999999999999 2.9%  operation 2 discount 7.31
            # # "600083",  # 博信股份 roe 70.58 pe 0.49 pb 144.13 dividend 0.0 0.0%  operation 2 discount 20.42
            # # "002458",  # 益生股份 roe 60.43 pe 11.78 pb 5.13 dividend 5.0 1.56%  operation 6 discount 0.85
            # # "002234",  # 民和股份 roe 52.64 pe 13.97 pb 3.77 dividend 10.0 3.37%  operation 2 discount 0.72
            # # "600768",  # 宁波富邦 roe 49.36 pe 7.89 pb 6.26 dividend 0.2 0.19%  operation 2 discount 1.27
            # # "000526",  # 紫光学大 roe 44.26 pe 1.64 pb 26.95 dividend 0.0 0.0%  operation 2 discount 6.09
            # # "600132",  # 重庆啤酒 roe 43.93 pe 2.56 pb 17.16 dividend 8.0 1.67%  operation 2 discount 3.91
            # # "002161",  # 远 望 谷 roe 37.66 pe 9.3 pb 4.05 dividend 0.1 0.09%  operation 2 discount 1.08
            # # "300122",  # 智飞生物 roe 34.27 pe 1.7 pb 20.15 dividend 5.0 0.77%  operation 6 discount 5.88
            # # "300417",  # 南华仪器 roe 34.03 pe 4.66 pb 7.31 dividend 7.5 1.86%  operation 2 discount 2.15
            # # "600052",  # 浙江广厦 roe 33.56 pe 29.66 pb 1.13 dividend 0.77 1.66%  operation 2 discount 0.34
            # # "002714",  # 牧原股份 roe 29.61 pe 2.08 pb 14.25 dividend 0.5 0.04%  operation 2 discount 4.81
            # # "000933",  # 神火股份 roe 29.58 pe 29.12 pb 1.02 dividend 0.15 0.33%  operation 2 discount 0.34
            # # "002299",  # 圣农发展 roe 29.39 pe 9.41 pb 3.12 dividend 15.0 6.49%  operation 2 discount 1.06
            # # "600732",  # 爱旭股份 roe 28.19 pe 3.44 pb 8.21 dividend 1.0 1.07%  operation 2 discount 2.91
            # # "600678",  # 四川金顶 roe 27.88 pe 1.03 pb 27.19 dividend 0.333 0.41%  operation 0 discount 9.75
            # # "601918",  # 新集能源 roe 26.37 pe 25.42 pb 1.04 dividend 0.1 0.34%  operation 0 discount 0.39
            # # "002555",  # 三七互娱 roe 23.85 pe 2.31 pb 10.31 dividend 3.0 0.94%  operation 2 discount 4.32
            # # "300198",  # 纳川股份 roe 23.81 pe 9.3 pb 2.56 dividend 0.1 0.26%  operation 2 discount 1.08
            # # "002182",  # 云海金属 roe 22.7 pe 7.19 pb 3.16 dividend 1.0 0.9%  operation 2 discount 1.39
            # # "300033",  # 同花顺 roe 22.5 pe 1.38 pb 16.25 dividend 4.8 0.4%  operation 2 discount 7.22
            # # "002677",  # 浙江美大 roe 22.49 pe 3.75 pb 5.99 dividend 4.65 3.7%  operation 6 discount 2.66
            # # "600802",  # 福建水泥 roe 22.14 pe 6.06 pb 3.65 dividend 0.33 0.3%  operation 2 discount 1.65
            # # "002746",  # 仙坛股份 roe 21.99 pe 9.31 pb 2.36 dividend 5.0 3.34%  operation 2 discount 1.07
            # # "000048",  # 康达尔 roe 21.82 pe 3.29 pb 6.63 dividend 0.0 0.0%  operation 6 discount 3.04
            # # "300003",  # 乐普医疗 roe 21.61 pe 2.29 pb 9.43 dividend 1.65 0.42%  operation 6 discount 4.36
            # # "000708",  # 中信特钢 roe 21.34 pe 6.54 pb 3.26 dividend 8.0 2.88%  operation 2 discount 1.53
            # # "300418",  # 昆仑万维 roe 21.15 pe 3.82 pb 5.53 dividend 0.87 0.41%  operation 2 discount 2.62
            # # "600346",  # 恒力石化 roe 21.12 pe 6.8 pb 3.11 dividend 3.0 2.11%  operation 2 discount 1.47
            # # "600570",  # 恒生电子 roe 21.09 pe 1.1 pb 19.21 dividend 3.2 0.35%  operation 6 discount 9.11
            # # "300117",  # 嘉寓股份 roe 20.98 pe 13.41 pb 1.56 dividend 0.08 0.21%  operation 2 discount 0.75
            # # "300216",  # 千山药机 roe 20.87 pe 0.0 pb 0.0 dividend 0.6 0.0%  operation 0 discount 0.0
            # # "002512",  # 达华智能 roe 20.43 pe 4.52 pb 4.52 dividend 0.45 0.75%  operation 2 discount 2.21
            # # "603899",  # 晨光文具 roe 20.37 pe 1.97 pb 10.35 dividend 3.0 0.68%  operation 2 discount 5.08
            # # "300357",  # 我武生物 roe 20.23 pe 1.02 pb 19.79 dividend 2.5 0.54%  operation 6 discount 9.78
            # # "002379",  # 宏创控股 roe 20.22 pe 8.79 pb 2.3 dividend 0.1 0.26%  operation 2 discount 1.14
            # # "002415",  # 海康威视 roe 19.85 pe 2.57 pb 7.74 dividend 6.0 1.79%  operation 2 discount 3.9
            # # "300401",  # 花园生物 roe 19.72 pe 5.41 pb 3.65 dividend 1.3 0.98%  operation 6 discount 1.85
            # # "600338",  # 西藏珠峰 roe 19.42 pe 5.67 pb 3.42 dividend 0.4 0.4%  operation 2 discount 1.76
            # # "600587",  # 新华医疗 roe 19.34 pe 10.13 pb 1.91 dividend 0.45 0.23%  operation 2 discount 0.99
            # # "000509",  # 华塑控股 roe 19.32 pe 0.44 pb 44.25 dividend 1.0 4.33%  operation 2 discount 22.91
            # # "000401",  # 冀东水泥 roe 19.29 pe 9.55 pb 2.02 dividend 4.0 2.08%  operation 2 discount 1.05
            # # "002372",  # 伟星新材 roe 19.25 pe 3.52 pb 5.47 dividend 6.0 4.8%  operation 6 discount 2.84
            # # "000848",  # 承德露露 roe 19.16 pe 5.42 pb 3.53 dividend 4.0 5.85%  operation 2 discount 1.84
            # # "300080",  # 易成新能 roe 19.15 pe 7.58 pb 2.53 dividend 0.1 0.16%  operation 2 discount 1.32
            # # "300015",  # 爱尔眼科 roe 19.1 pe 0.9 pb 21.14 dividend 2.0 0.45%  operation 6 discount 11.07
            # # "000963",  # 华东医药 roe 18.98 pe 6.32 pb 3.0 dividend 3.3 1.65%  operation 6 discount 1.58
            # # "002597",  # 金禾实业 roe 18.69 pe 6.68 pb 2.8 dividend 3.6 1.66%  operation 2 discount 1.5
            # # "002507",  # 涪陵榨菜 roe 18.61 pe 2.22 pb 8.4 dividend 2.6 0.88%  operation 6 discount 4.51
            # # "600217",  # 中再资环 roe 18.58 pe 3.95 pb 4.7 dividend 0.5 0.85%  operation 6 discount 2.53
            # # "603369",  # 今世缘 roe 18.55 pe 3.35 pb 5.54 dividend 3.3 1.07%  operation 6 discount 2.99
            # # "002011",  # 盾安环境 roe 18.52 pe 11.33 pb 1.64 dividend 1.0 2.04%  operation 2 discount 0.88
            # # "300136",  # 信维通信 roe 18.38 pe 1.93 pb 9.53 dividend 0.8 0.18%  operation 6 discount 5.19
            # # "002605",  # 姚记科技 roe 18.35 pe 2.22 pb 8.27 dividend 1.00011 0.34%  operation 2 discount 4.51
            # # "002690",  # 美亚光电 roe 17.92 pe 1.53 pb 11.73 dividend 7.0 1.8%  operation 6 discount 6.55
            # # "002463",  # 沪电股份 roe 17.84 pe 1.84 pb 9.7 dividend 1.0 0.37%  operation 6 discount 5.44
            # # "601100",  # 恒立液压 roe 17.66 pe 1.87 pb 9.46 dividend 3.0 0.54%  operation 6 discount 5.36
            # # "002600",  # 领益智造 roe 17.49 pe 2.78 pb 6.28 dividend 1.0 0.9%  operation 2 discount 3.59
            # # "002626",  # 金达威 roe 17.47 pe 3.89 pb 4.49 dividend 8.0 3.63%  operation 2 discount 2.57
            # # "002653",  # 海思科 roe 17.32 pe 1.64 pb 10.57 dividend 1.9 0.87%  operation 2 discount 6.1
            # # "600267",  # 海正药业 roe 16.87 pe 8.45 pb 2.0 dividend 0.5 0.33%  operation 2 discount 1.18
            # # "000906",  # 浙商中拓 roe 16.8 pe 10.54 pb 1.59 dividend 1.50195 2.7%  operation 6 discount 0.95
            # # "000403",  # 双林生物 roe 16.64 pe 1.32 pb 12.57 dividend 1.0 0.28%  operation 2 discount 7.55
            # # "300107",  # 建新股份 roe 16.49 pe 7.08 pb 2.33 dividend 2.99665 4.13%  operation 2 discount 1.41
            # # "000338",  # 潍柴动力 roe 16.46 pe 6.26 pb 2.63 dividend 4.3 3.03%  operation 6 discount 1.6
            # # "000921",  # 海信家电 roe 16.29 pe 9.62 pb 1.69 dividend 3.03 2.94%  operation 2 discount 1.04
            # # "000656",  # 金科股份 roe 16.19 pe 9.52 pb 1.7 dividend 3.6 4.6%  operation 4 discount 1.05
            # # "300146",  # 汤臣倍健 roe 16.13 pe 4.53 pb 3.56 dividend 5.0 3.01%  operation 6 discount 2.21
            # # "002045",  # 国光电器 roe 16.08 pe 5.98 pb 2.69 dividend 0.8 0.72%  operation 2 discount 1.67
            # # "002311",  # 海大集团 roe 15.94 pe 2.51 pb 6.36 dividend 3.0 0.84%  operation 6 discount 3.99
            # # "000603",  # 盛达资源 roe 15.78 pe 4.02 pb 3.92 dividend 5.0 4.08%  operation 6 discount 2.49
            # # "002475",  # 立讯精密 roe 15.73 pe 1.27 pb 12.41 dividend 0.5 0.12%  operation 6 discount 7.89
            # # "002007",  # 华兰生物 roe 15.49 pe 1.59 pb 9.77 dividend 4.0 0.92%  operation 2 discount 6.31
            # # "600985",  # 淮北矿业 roe 15.47 pe 15.25 pb 1.01 dividend 5.0 5.85%  operation 2 discount 0.66
            # # "002624",  # 完美世界 roe 15.46 pe 2.55 pb 6.05 dividend 1.8 0.4%  operation 2 discount 3.91
            # # "000720",  # 新能泰山 roe 15.4 pe 5.66 pb 2.72 dividend 0.5 0.99%  operation 2 discount 1.77
            # # "002120",  # 韵达股份 roe 15.32 pe 3.03 pb 5.07 dividend 4.76 1.64%  operation 6 discount 3.31
            # # "603606",  # 东方电缆 roe 15.27 pe 3.6 pb 4.24 dividend 1.05 0.82%  operation 2 discount 2.78
            # # "600387",  # 海越能源 roe 15.26 pe 12.8 pb 1.19 dividend 0.6 0.78%  operation 2 discount 0.78
            # # "002601",  # 龙蟒佰利 roe 15.18 pe 6.07 pb 2.5 dividend 8.5 5.07%  operation 2 discount 1.65
            # # "600260",  # 凯乐科技 roe 15.13 pe 7.26 pb 2.09 dividend 1.6 1.2%  operation 6 discount 1.38
            # # "002043",  # 兔 宝 宝 roe 15.12 pe 4.09 pb 3.7 dividend 2.5 3.12%  operation 2 discount 2.45
            # # "300422",  # 博世科 roe 15.03 pe 5.38 pb 2.79 dividend 0.679965 0.53%  operation 6 discount 1.86
            # # "002262",  # 恩华药业 roe 15.0 pe 4.17 pb 3.6 dividend 0.6 0.49%  operation 6 discount 2.4
        }

    def get_stock_list(self):
        return self.stock_list
