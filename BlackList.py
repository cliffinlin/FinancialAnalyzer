# -*- coding: utf-8 -*-


class BlackList:
    def __init__(self):
        self.stock_list = {
            "300362",  # 天翔环境 roe 8519.97 pe 0.0 pb 0.0 dividend 0.0 0.0%  operation 0
            "600556",  # 天下秀 roe 222.38 pe 1.0 pb 31.59 dividend 0.15 0.08%  operation 0
            "600768",  # 宁波富邦 roe 115.83 pe 8.82 pb 5.67 dividend 0.0 0.0%  operation 0
            "002234",  # 民和股份 roe 91.0 pe 20.92 pb 2.27 dividend 6.0 2.77%  operation 0
            "000048",  # 京基智农 roe 90.41 pe 10.59 pb 4.41 dividend 7.5 3.05%  operation 0
            "002714",  # 牧原股份 roe 64.61 pe 3.84 pb 6.58 dividend 5.5 0.73%  operation 0
            "002458",  # 益生股份 roe 60.55 pe 12.96 pb 4.75 dividend 10.0 6.42%  operation 0
            "002607",  # 中公教育 roe 59.04 pe 1.01 pb 85.98 dividend 2.4 0.83%  operation 0
            "002611",  # 东方精工 roe 55.71 pe 26.68 pb 1.59 dividend 0.0 0.0%  operation 0
            "600678",  # 四川金顶 roe 52.51 pe 1.82 pb 17.12 dividend 0.0 0.0%  operation 0
            "002605",  # 姚记科技 roe 51.39 pe 6.76 pb 7.04 dividend 4.02 1.14%  operation 0
            "300122",  # 智飞生物 roe 50.84 pe 1.55 pb 24.49 dividend 5.0 0.52%  operation 0
            "002299",  # 圣农发展 roe 49.36 pe 12.51 pb 3.52 dividend 15.0 5.64%  operation 0
            "600132",  # 重庆啤酒 roe 49.19 pe 2.04 pb 20.45 dividend 14.0 2.28%  operation 0
            "600052",  # 浙江广厦 roe 48.62 pe 37.18 pb 0.9 dividend 0.95 2.61%  operation 0
            "002182",  # 云海金属 roe 48.07 pe 15.8 pb 2.1 dividend 1.5 1.7%  operation 0
            "600802",  # 福建水泥 roe 46.49 pe 11.14 pb 3.06 dividend 1.6 1.45%  operation 0
            "002157",  # 正邦科技 roe 46.11 pe 6.96 pb 4.13 dividend 0.7 0.41%  operation 0
            "002124",  # 天邦股份 roe 44.6 pe 6.95 pb 3.91 dividend 0.0 0.0%  operation 0
            "300216",  # 千山药机 roe 42.41 pe 0.0 pb 0.0 dividend 0.0 0.0%  operation 0
            "600685",  # 中船防务 roe 41.81 pe 16.57 pb 1.87 dividend 0.0 0.0%  operation 0
            "603111",  # 康尼机电 roe 39.52 pe 10.87 pb 2.42 dividend 0.0 0.0%  operation 0
            "002161",  # 远 望 谷 roe 38.94 pe 10.13 pb 2.96 dividend 0.0 0.0%  operation 0
            "600779",  # 水井坊 roe 38.48 pe 2.9 pb 11.97 dividend 14.5 2.57%  operation 0
            "002555",  # 三七互娱 roe 37.46 pe 2.75 pb 11.14 dividend 3.0 0.73%  operation 0
            "002190",  # 成飞集成 roe 37.43 pe 8.19 pb 3.15 dividend 0.6 0.27%  operation 0
            "002248",  # 华东数控 roe 36.8 pe 1.34 pb 19.88 dividend 0.0 0.0%  operation 0
            "002015",  # 协鑫能科 roe 36.32 pe 8.75 pb 1.51 dividend 0.0 0.0%  operation 0
            "002459",  # 晶澳科技 roe 34.75 pe 7.44 pb 2.47 dividend 0.0 0.0%  operation 0
            "300462",  # 华铭智能 roe 34.66 pe 7.36 pb 2.55 dividend 1.5 0.68%  operation 0
            "002755",  # 奥赛康 roe 34.44 pe 4.23 pb 6.31 dividend 2.2 1.23%  operation 0
            "300417",  # 南华仪器 roe 33.31 pe 8.61 pb 2.85 dividend 8.0 4.34%  operation 0
            "002415",  # 海康威视 roe 31.56 pe 4.39 pb 6.08 dividend 7.0 2.32%  operation 0
            "002127",  # 南极电商 roe 31.42 pe 2.34 pb 10.4 dividend 1.24 0.59%  operation 0
            "603609",  # 禾丰牧业 roe 31.19 pe 10.02 pb 2.27 dividend 2.2 1.49%  operation 0
            "600764",  # 中国海防 roe 31.14 pe 3.32 pb 2.91 dividend 2.73 1.07%  operation 0
            "600546",  # 山煤国际 roe 31.08 pe 5.14 pb 3.35 dividend 0.6 0.53%  operation 0
            "600346",  # 恒力石化 roe 30.35 pe 12.09 pb 2.51 dividend 4.0 2.92%  operation 0
            "002463",  # 沪电股份 roe 30.04 pe 2.98 pb 7.87 dividend 2.0 0.82%  operation 0
            "300132",  # 青松股份 roe 29.52 pe 3.8 pb 3.85 dividend 1.35 0.58%  operation 0
            "601012",  # 隆基股份 roe 29.43 pe 5.1 pb 4.34 dividend 2.0 0.59%  operation 0
            "300033",  # 同花顺 roe 29.12 pe 1.37 pb 18.35 dividend 8.5 0.68%  operation 0
            "600745",  # 闻泰科技 roe 28.79 pe 1.41 pb 6.03 dividend 1.5 0.13%  operation 0
            "600466",  # 蓝光发展 roe 28.03 pe 21.39 pb 1.02 dividend 2.87 5.32%  operation 0
            "002016",  # 世荣兆业 roe 28.0 pe 15.22 pb 1.61 dividend 0.0 0.0%  operation 0
            "603899",  # 晨光文具 roe 27.89 pe 2.11 pb 10.93 dividend 4.0 0.76%  operation 0
            "002677",  # 浙江美大 roe 27.84 pe 5.66 pb 4.65 dividend 5.42 4.89%  operation 0
            "002653",  # 海思科 roe 27.77 pe 2.03 pb 11.31 dividend 0.92 0.35%  operation 0
            "603988",  # 中电电机 roe 27.6 pe 6.6 pb 3.65 dividend 2.52 2.05%  operation 0
            "000537",  # 广宇发展 roe 27.57 pe 22.19 pb 0.98 dividend 3.0 3.99%  operation 0
            "000876",  # 新 希 望 roe 27.48 pe 4.89 pb 4.43 dividend 1.5 0.52%  operation 0
            "000717",  # 韶钢松山 roe 27.19 pe 18.63 pb 1.15 dividend 1.5 3.78%  operation 0
            "601100",  # 恒立液压 roe 27.05 pe 2.02 pb 11.01 dividend 6.0 0.81%  operation 0
            "000987",  # 越秀金控 roe 26.9 pe 14.05 pb 1.4 dividend 1.7 1.48%  operation 0
            "002100",  # 天康生物 roe 26.9 pe 5.88 pb 3.27 dividend 2.0 1.32%  operation 0
            "000656",  # 金科股份 roe 26.78 pe 13.76 pb 1.48 dividend 4.5 5.68%  operation 0
            "600031",  # 三一重工 roe 26.08 pe 6.28 pb 3.49 dividend 4.2 2.19%  operation 0
            "000011",  # 深物业A roe 26.08 pe 9.46 pb 2.86 dividend 3.6 2.28%  operation 0
            "300016",  # 北陆药业 roe 26.07 pe 5.97 pb 3.72 dividend 0.7 0.63%  operation 0
            "002271",  # 东方雨虹 roe 25.76 pe 3.16 pb 5.75 dividend 3.0 0.72%  operation 0
            "002746",  # 仙坛股份 roe 25.76 pe 16.2 pb 1.8 dividend 4.0 2.99%  operation 0
            "600053",  # 九鼎投资 roe 25.5 pe 5.2 pb 4.34 dividend 0.0 0.0%  operation 0
            "000789",  # 万年青 roe 25.41 pe 13.17 pb 2.0 dividend 7.0 5.24%  operation 0
            "000897",  # 津滨发展 roe 24.36 pe 6.95 pb 2.82 dividend 0.0 0.0%  operation 0
            "000517",  # 荣安地产 roe 24.33 pe 16.68 pb 1.16 dividend 1.0 4.02%  operation 0
            "600051",  # 宁波联合 roe 24.17 pe 22.69 pb 0.87 dividend 2.0 2.42%  operation 0
            "000403",  # 双林生物 roe 24.17 pe 0.84 pb 23.08 dividend 1.21 0.17%  operation 0
            "000961",  # 中南建设 roe 23.7 pe 13.42 pb 1.45 dividend 2.8 3.29%  operation 0
            "300418",  # 昆仑万维 roe 23.58 pe 5.62 pb 4.59 dividend 0.26 0.12%  operation 0
            "600217",  # 中再资环 roe 23.53 pe 4.89 pb 3.92 dividend 0.0 0.0%  operation 0
            "000090",  # 天健集团 roe 23.5 pe 16.64 pb 1.49 dividend 3.8 5.48%  operation 0
            "300347",  # 泰格医药 roe 23.07 pe 1.41 pb 14.94 dividend 2.78 0.31%  operation 0
            "600325",  # 华发股份 roe 22.93 pe 19.22 pb 1.04 dividend 4.0 5.76%  operation 0
            "002214",  # 大立科技 roe 22.75 pe 2.2 pb 8.94 dividend 0.8 0.34%  operation 0
            "300432",  # 富临精工 roe 22.57 pe 8.97 pb 2.02 dividend 0.0 0.0%  operation 0
            "600183",  # 生益科技 roe 22.54 pe 2.31 pb 7.25 dividend 4.0 1.36%  operation 0
            "000671",  # 阳 光 城 roe 22.44 pe 15.34 pb 1.21 dividend 1.99 3.02%  operation 0
            "300003",  # 乐普医疗 roe 22.29 pe 2.34 pb 8.36 dividend 2.0 0.55%  operation 0
            "002601",  # 龙蟒佰利 roe 22.15 pe 7.83 pb 2.48 dividend 9.0 4.99%  operation 0
            "002690",  # 美亚光电 roe 22.02 pe 1.46 pb 14.79 dividend 8.0 1.51%  operation 0
            "601919",  # 中远海控 roe 21.85 pe 14.55 pb 1.22 dividend 0.0 0.0%  operation 0
            "300136",  # 信维通信 roe 21.67 pe 1.79 pb 9.83 dividend 0.5 0.1%  operation 0
            "000933",  # 神火股份 roe 21.65 pe 16.66 pb 1.02 dividend 1.0 2.38%  operation 0
            "002572",  # 索菲亚 roe 21.55 pe 4.64 pb 3.79 dividend 5.5 2.44%  operation 0
            "002697",  # 红旗连锁 roe 21.55 pe 3.84 pb 4.72 dividend 0.87 0.78%  operation 0
            "000401",  # 冀东水泥 roe 21.43 pe 10.52 pb 1.88 dividend 5.0 2.99%  operation 0
            "002045",  # 国光电器 roe 21.38 pe 7.88 pb 2.37 dividend 0.8 0.83%  operation 0
            "601225",  # 陕西煤业 roe 21.34 pe 15.4 pb 1.19 dividend 3.6 4.94%  operation 0
            "603808",  # 歌力思 roe 21.34 pe 12.1 pb 2.0 dividend 2.5 1.97%  operation 0
            "600720",  # 祁连山 roe 21.3 pe 9.34 pb 1.94 dividend 5.8 3.41%  operation 0
            "002216",  # 三全食品 roe 21.29 pe 2.38 pb 7.4 dividend 0.6 0.26%  operation 0
            "600507",  # 方大特钢 roe 21.28 pe 12.98 pb 1.13 dividend 0.0 0.0%  operation 0
            "603606",  # 东方电缆 roe 20.89 pe 5.36 pb 4.16 dividend 1.3 0.94%  operation 0
            "603369",  # 今世缘 roe 20.74 pe 2.99 pb 6.01 dividend 4.1 1.1%  operation 0
            "002372",  # 伟星新材 roe 20.67 pe 4.95 pb 4.78 dividend 5.0 4.14%  operation 0
            "603568",  # 伟明环保 roe 21.21 pe 3.31 pb 6.17 dividend 3.1 1.06%  operation 0
            "600985",  # 淮北矿业 roe 20.4 pe 20.03 pb 0.89 dividend 6.0 7.36%  operation 0
            "600766",  # 园城黄金 roe 20.38 pe 0.65 pb 25.86 dividend 0.0 0.0%  operation 0
            "000338",  # 潍柴动力 roe 20.36 pe 7.89 pb 2.29 dividend 1.36 0.99%  operation 0
            "002379",  # 宏创控股 roe 20.32 pe 10.0 pb 1.69 dividend 0.0 0.0%  operation 0
            "300198",  # 纳川股份 roe 20.14 pe 5.89 pb 2.84 dividend 0.0 0.0%  operation 0
            "601058",  # 赛轮轮胎 roe 20.07 pe 13.2 pb 1.32 dividend 1.0 2.78%  operation 0

            "600507",  # 方大特钢 roe 26.15 pe 13.22 pb 1.98 dividend 17.0 19.02%  operation 2 discount 0.76
            "000717",  # 韶钢松山 roe 17.27 pe 12.25 pb 1.41 dividend 0.5 1.15%  operation 2 discount 0.82
            "002110",  # 三钢闽光 roe 15.81 pe 13.54 pb 1.17 dividend 20.0 23.5%  operation 2 discount 0.74
            "600282",  # 南钢股份 roe 14.38 pe 16.7 pb 0.86 dividend 3.0 9.35%  operation 2 discount 0.6
            "601003",  # 柳钢股份 roe 14.16 pe 11.29 pb 1.25 dividend 6.0 11.7%  operation 2 discount 0.89
            "600307",  # 酒钢宏兴 roe 10.59 pe 10.81 pb 0.98 dividend 0.3 1.62%  operation 2 discount 0.92

            "000537",  # 广宇发展 roe 19.07 pe 18.42 pb 1.04 dividend 1.3 1.81%  operation 0 discount 0.54
            "000885",  # 城发环境 roe 19.01 pe 10.34 pb 1.84 dividend 2.3 2.12%  operation 0 discount 0.97

            "000835",  # 长城动漫 roe 208.47 pe -2.97 pb -70.21 dividend 0.4 0.99%  operation 0 discount -3.37
            "600198",  # 大唐电信 roe 156.96 pe -5.84 pb -26.86 dividend 2.0 1.86%  operation 0 discount -1.71
            "600898",  # 国美通讯 roe 155.94 pe -11.64 pb -13.4 dividend 0.5 0.71%  operation 2 discount -0.86
            "600306",  # 商业城 roe 138.58 pe -8.27 pb -16.75 dividend 0.2 0.38%  operation 2 discount -1.21
            "300090",  # 盛运环保 roe 138.55 pe -31.95 pb -4.34 dividend 0.5 3.82%  operation 0 discount -0.31
            "300362",  # 天翔环境 roe 115.46 pe -102.59 pb -1.13 dividend 0.2 0.96%  operation 0 discount -0.1
            "000927",  # 一汽夏利 roe 115.44 pe -10.63 pb -10.86 dividend 0.1 0.24%  operation 2 discount -0.94
            "300116",  # 坚瑞沃能 roe 107.76 pe -60.55 pb -1.78 dividend 0.1 0.56%  operation 0 discount -0.17
            "600651",  # 飞乐音响 roe 102.51 pe -17.8 pb -5.76 dividend 0.17 0.45%  operation 0 discount -0.56
            "300104",  # 乐视网 roe 76.99 pe 0.0 pb 0.0 dividend 0.28 0.0%  operation 0 discount 0.0
            "002607",  # 中公教育 roe 71.19 pe 1.37 pb 52.07 dividend 6.199999999999999 2.9%  operation 2 discount 7.31
            "600083",  # 博信股份 roe 70.58 pe 0.49 pb 144.13 dividend 0.0 0.0%  operation 2 discount 20.42
            "002458",  # 益生股份 roe 60.43 pe 11.78 pb 5.13 dividend 5.0 1.56%  operation 6 discount 0.85
            "002234",  # 民和股份 roe 52.64 pe 13.97 pb 3.77 dividend 10.0 3.37%  operation 2 discount 0.72
            "600768",  # 宁波富邦 roe 49.36 pe 7.89 pb 6.26 dividend 0.2 0.19%  operation 2 discount 1.27
            "000526",  # 紫光学大 roe 44.26 pe 1.64 pb 26.95 dividend 0.0 0.0%  operation 2 discount 6.09
            "600132",  # 重庆啤酒 roe 43.93 pe 2.56 pb 17.16 dividend 8.0 1.67%  operation 2 discount 3.91
            "002161",  # 远 望 谷 roe 37.66 pe 9.3 pb 4.05 dividend 0.1 0.09%  operation 2 discount 1.08
            "300122",  # 智飞生物 roe 34.27 pe 1.7 pb 20.15 dividend 5.0 0.77%  operation 6 discount 5.88
            "300417",  # 南华仪器 roe 34.03 pe 4.66 pb 7.31 dividend 7.5 1.86%  operation 2 discount 2.15
            "600052",  # 浙江广厦 roe 33.56 pe 29.66 pb 1.13 dividend 0.77 1.66%  operation 2 discount 0.34
            "002714",  # 牧原股份 roe 29.61 pe 2.08 pb 14.25 dividend 0.5 0.04%  operation 2 discount 4.81
            "000933",  # 神火股份 roe 29.58 pe 29.12 pb 1.02 dividend 0.15 0.33%  operation 2 discount 0.34
            "002299",  # 圣农发展 roe 29.39 pe 9.41 pb 3.12 dividend 15.0 6.49%  operation 2 discount 1.06
            "600732",  # 爱旭股份 roe 28.19 pe 3.44 pb 8.21 dividend 1.0 1.07%  operation 2 discount 2.91
            "600678",  # 四川金顶 roe 27.88 pe 1.03 pb 27.19 dividend 0.333 0.41%  operation 0 discount 9.75
            "601918",  # 新集能源 roe 26.37 pe 25.42 pb 1.04 dividend 0.1 0.34%  operation 0 discount 0.39
            "002555",  # 三七互娱 roe 23.85 pe 2.31 pb 10.31 dividend 3.0 0.94%  operation 2 discount 4.32
            "300198",  # 纳川股份 roe 23.81 pe 9.3 pb 2.56 dividend 0.1 0.26%  operation 2 discount 1.08
            "002182",  # 云海金属 roe 22.7 pe 7.19 pb 3.16 dividend 1.0 0.9%  operation 2 discount 1.39
            "300033",  # 同花顺 roe 22.5 pe 1.38 pb 16.25 dividend 4.8 0.4%  operation 2 discount 7.22
            "002677",  # 浙江美大 roe 22.49 pe 3.75 pb 5.99 dividend 4.65 3.7%  operation 6 discount 2.66
            "600802",  # 福建水泥 roe 22.14 pe 6.06 pb 3.65 dividend 0.33 0.3%  operation 2 discount 1.65
            "002746",  # 仙坛股份 roe 21.99 pe 9.31 pb 2.36 dividend 5.0 3.34%  operation 2 discount 1.07
            "000048",  # 康达尔 roe 21.82 pe 3.29 pb 6.63 dividend 0.0 0.0%  operation 6 discount 3.04
            "300003",  # 乐普医疗 roe 21.61 pe 2.29 pb 9.43 dividend 1.65 0.42%  operation 6 discount 4.36
            "000708",  # 中信特钢 roe 21.34 pe 6.54 pb 3.26 dividend 8.0 2.88%  operation 2 discount 1.53
            "300418",  # 昆仑万维 roe 21.15 pe 3.82 pb 5.53 dividend 0.87 0.41%  operation 2 discount 2.62
            "600346",  # 恒力石化 roe 21.12 pe 6.8 pb 3.11 dividend 3.0 2.11%  operation 2 discount 1.47
            "600570",  # 恒生电子 roe 21.09 pe 1.1 pb 19.21 dividend 3.2 0.35%  operation 6 discount 9.11
            "300117",  # 嘉寓股份 roe 20.98 pe 13.41 pb 1.56 dividend 0.08 0.21%  operation 2 discount 0.75
            "300216",  # 千山药机 roe 20.87 pe 0.0 pb 0.0 dividend 0.6 0.0%  operation 0 discount 0.0
            "002512",  # 达华智能 roe 20.43 pe 4.52 pb 4.52 dividend 0.45 0.75%  operation 2 discount 2.21
            "603899",  # 晨光文具 roe 20.37 pe 1.97 pb 10.35 dividend 3.0 0.68%  operation 2 discount 5.08
            "300357",  # 我武生物 roe 20.23 pe 1.02 pb 19.79 dividend 2.5 0.54%  operation 6 discount 9.78
            "002379",  # 宏创控股 roe 20.22 pe 8.79 pb 2.3 dividend 0.1 0.26%  operation 2 discount 1.14
            "002415",  # 海康威视 roe 19.85 pe 2.57 pb 7.74 dividend 6.0 1.79%  operation 2 discount 3.9
            "300401",  # 花园生物 roe 19.72 pe 5.41 pb 3.65 dividend 1.3 0.98%  operation 6 discount 1.85
            "600338",  # 西藏珠峰 roe 19.42 pe 5.67 pb 3.42 dividend 0.4 0.4%  operation 2 discount 1.76
            "600587",  # 新华医疗 roe 19.34 pe 10.13 pb 1.91 dividend 0.45 0.23%  operation 2 discount 0.99
            "000509",  # 华塑控股 roe 19.32 pe 0.44 pb 44.25 dividend 1.0 4.33%  operation 2 discount 22.91
            "000401",  # 冀东水泥 roe 19.29 pe 9.55 pb 2.02 dividend 4.0 2.08%  operation 2 discount 1.05
            "002372",  # 伟星新材 roe 19.25 pe 3.52 pb 5.47 dividend 6.0 4.8%  operation 6 discount 2.84
            "000848",  # 承德露露 roe 19.16 pe 5.42 pb 3.53 dividend 4.0 5.85%  operation 2 discount 1.84
            "300080",  # 易成新能 roe 19.15 pe 7.58 pb 2.53 dividend 0.1 0.16%  operation 2 discount 1.32
            "300015",  # 爱尔眼科 roe 19.1 pe 0.9 pb 21.14 dividend 2.0 0.45%  operation 6 discount 11.07
            "000963",  # 华东医药 roe 18.98 pe 6.32 pb 3.0 dividend 3.3 1.65%  operation 6 discount 1.58
            "002597",  # 金禾实业 roe 18.69 pe 6.68 pb 2.8 dividend 3.6 1.66%  operation 2 discount 1.5
            "002507",  # 涪陵榨菜 roe 18.61 pe 2.22 pb 8.4 dividend 2.6 0.88%  operation 6 discount 4.51
            "600217",  # 中再资环 roe 18.58 pe 3.95 pb 4.7 dividend 0.5 0.85%  operation 6 discount 2.53
            "603369",  # 今世缘 roe 18.55 pe 3.35 pb 5.54 dividend 3.3 1.07%  operation 6 discount 2.99
            "002011",  # 盾安环境 roe 18.52 pe 11.33 pb 1.64 dividend 1.0 2.04%  operation 2 discount 0.88
            "300136",  # 信维通信 roe 18.38 pe 1.93 pb 9.53 dividend 0.8 0.18%  operation 6 discount 5.19
            "002605",  # 姚记科技 roe 18.35 pe 2.22 pb 8.27 dividend 1.00011 0.34%  operation 2 discount 4.51
            "002690",  # 美亚光电 roe 17.92 pe 1.53 pb 11.73 dividend 7.0 1.8%  operation 6 discount 6.55
            "002463",  # 沪电股份 roe 17.84 pe 1.84 pb 9.7 dividend 1.0 0.37%  operation 6 discount 5.44
            "601100",  # 恒立液压 roe 17.66 pe 1.87 pb 9.46 dividend 3.0 0.54%  operation 6 discount 5.36
            "002600",  # 领益智造 roe 17.49 pe 2.78 pb 6.28 dividend 1.0 0.9%  operation 2 discount 3.59
            "002626",  # 金达威 roe 17.47 pe 3.89 pb 4.49 dividend 8.0 3.63%  operation 2 discount 2.57
            "002653",  # 海思科 roe 17.32 pe 1.64 pb 10.57 dividend 1.9 0.87%  operation 2 discount 6.1
            "600267",  # 海正药业 roe 16.87 pe 8.45 pb 2.0 dividend 0.5 0.33%  operation 2 discount 1.18
            "000906",  # 浙商中拓 roe 16.8 pe 10.54 pb 1.59 dividend 1.50195 2.7%  operation 6 discount 0.95
            "000403",  # 双林生物 roe 16.64 pe 1.32 pb 12.57 dividend 1.0 0.28%  operation 2 discount 7.55
            "300107",  # 建新股份 roe 16.49 pe 7.08 pb 2.33 dividend 2.99665 4.13%  operation 2 discount 1.41
            "000338",  # 潍柴动力 roe 16.46 pe 6.26 pb 2.63 dividend 4.3 3.03%  operation 6 discount 1.6
            "000921",  # 海信家电 roe 16.29 pe 9.62 pb 1.69 dividend 3.03 2.94%  operation 2 discount 1.04
            "000656",  # 金科股份 roe 16.19 pe 9.52 pb 1.7 dividend 3.6 4.6%  operation 4 discount 1.05
            "300146",  # 汤臣倍健 roe 16.13 pe 4.53 pb 3.56 dividend 5.0 3.01%  operation 6 discount 2.21
            "002045",  # 国光电器 roe 16.08 pe 5.98 pb 2.69 dividend 0.8 0.72%  operation 2 discount 1.67
            "002311",  # 海大集团 roe 15.94 pe 2.51 pb 6.36 dividend 3.0 0.84%  operation 6 discount 3.99
            "000603",  # 盛达资源 roe 15.78 pe 4.02 pb 3.92 dividend 5.0 4.08%  operation 6 discount 2.49
            "002475",  # 立讯精密 roe 15.73 pe 1.27 pb 12.41 dividend 0.5 0.12%  operation 6 discount 7.89
            "002007",  # 华兰生物 roe 15.49 pe 1.59 pb 9.77 dividend 4.0 0.92%  operation 2 discount 6.31
            "600985",  # 淮北矿业 roe 15.47 pe 15.25 pb 1.01 dividend 5.0 5.85%  operation 2 discount 0.66
            "002624",  # 完美世界 roe 15.46 pe 2.55 pb 6.05 dividend 1.8 0.4%  operation 2 discount 3.91
            "000720",  # 新能泰山 roe 15.4 pe 5.66 pb 2.72 dividend 0.5 0.99%  operation 2 discount 1.77
            "002120",  # 韵达股份 roe 15.32 pe 3.03 pb 5.07 dividend 4.76 1.64%  operation 6 discount 3.31
            "603606",  # 东方电缆 roe 15.27 pe 3.6 pb 4.24 dividend 1.05 0.82%  operation 2 discount 2.78
            "600387",  # 海越能源 roe 15.26 pe 12.8 pb 1.19 dividend 0.6 0.78%  operation 2 discount 0.78
            "002601",  # 龙蟒佰利 roe 15.18 pe 6.07 pb 2.5 dividend 8.5 5.07%  operation 2 discount 1.65
            "600260",  # 凯乐科技 roe 15.13 pe 7.26 pb 2.09 dividend 1.6 1.2%  operation 6 discount 1.38
            "002043",  # 兔 宝 宝 roe 15.12 pe 4.09 pb 3.7 dividend 2.5 3.12%  operation 2 discount 2.45
            "300422",  # 博世科 roe 15.03 pe 5.38 pb 2.79 dividend 0.679965 0.53%  operation 6 discount 1.86
            "002262",  # 恩华药业 roe 15.0 pe 4.17 pb 3.6 dividend 0.6 0.49%  operation 6 discount 2.4
            "000629",  # 攀钢钒钛 roe 14.92 pe 6.76 pb 2.21 dividend 0.1 0.41%  operation 2 discount 1.48
            "600681",  # 百川能源 roe 14.67 pe 8.01 pb 1.83 dividend 5.0 8.79%  operation 6 discount 1.25
            "300327",  # 中颖电子 roe 14.65 pe 1.61 pb 9.12 dividend 4.5 1.41%  operation 2 discount 6.23
            "603699",  # 纽威股份 roe 14.63 pe 3.59 pb 4.08 dividend 6.7 4.87%  operation 2 discount 2.79
            "600778",  # 友好集团 roe 14.62 pe 8.54 pb 1.71 dividend 0.9 1.83%  operation 2 discount 1.17
            "600729",  # 重庆百货 roe 14.58 pe 8.39 pb 1.74 dividend 6.5 2.45%  operation 2 discount 1.19
            "000810",  # 创维数字 roe 14.52 pe 3.76 pb 3.86 dividend 0.8 0.64%  operation 2 discount 2.66
            "600598",  # 北大荒 roe 14.36 pe 4.3 pb 3.34 dividend 4.0 3.14%  operation 2 discount 2.33
            "300232",  # 洲明科技 roe 14.35 pe 4.09 pb 3.51 dividend 0.600239 0.59%  operation 6 discount 2.45
            "000710",  # 贝瑞基因 roe 14.31 pe 1.96 pb 7.29 dividend 1.5 0.33%  operation 6 discount 5.09
            "002706",  # 良信电器 roe 14.18 pe 3.06 pb 4.64 dividend 2.5 2.37%  operation 6 discount 3.27
            "002734",  # 利民股份 roe 14.17 pe 6.54 pb 2.17 dividend 3.5 2.29%  operation 6 discount 1.53
            "002127",  # 南极电商 roe 14.16 pe 2.16 pb 6.54 dividend 0.62 0.55%  operation 6 discount 4.62
            "002572",  # 索菲亚 roe 14.16 pe 4.05 pb 3.5 dividend 5.0 2.57%  operation 2 discount 2.47
            "300322",  # 硕贝德 roe 14.14 pe 1.12 pb 12.64 dividend 0.3 0.15%  operation 2 discount 8.93
            "300415",  # 伊之密 roe 14.1 pe 4.7 pb 3.0 dividend 1.0 1.14%  operation 2 discount 2.13
            "600618",  # 氯碱化工 roe 14.05 pe 6.38 pb 2.2 dividend 1.2 1.41%  operation 2 discount 1.57
            "000935",  # 四川双马 roe 13.87 pe 4.91 pb 2.82 dividend 1.75 1.17%  operation 2 discount 2.04
            "600724",  # 宁波富达 roe 13.79 pe 6.43 pb 2.14 dividend 0.2 0.48%  operation 2 discount 1.56
            "002697",  # 红旗连锁 roe 13.78 pe 3.17 pb 4.35 dividend 0.53 0.56%  operation 6 discount 3.15
            "000779",  # 甘咨询 roe 13.76 pe 6.07 pb 2.27 dividend 0.0 0.0%  operation 6 discount 1.65
            "002595",  # 豪迈科技 roe 13.76 pe 3.87 pb 3.55 dividend 3.75 1.79%  operation 2 discount 2.58
            "600867",  # 通化东宝 roe 13.75 pe 2.81 pb 4.9 dividend 2.0 1.66%  operation 2 discount 3.56
            "600438",  # 通威股份 roe 13.72 pe 3.8 pb 3.61 dividend 1.6 1.05%  operation 6 discount 2.63
            "601233",  # 桐昆股份 roe 13.71 pe 9.66 pb 1.42 dividend 1.2 0.87%  operation 6 discount 1.04
            "603609",  # 禾丰牧业 roe 13.7 pe 6.52 pb 2.1 dividend 1.8 1.52%  operation 6 discount 1.53
            "600261",  # 阳光照明 roe 13.69 pe 8.83 pb 1.55 dividend 1.5 3.69%  operation 2 discount 1.13
            "601058",  # 赛轮轮胎 roe 13.67 pe 7.97 pb 1.72 dividend 0.5 1.13%  operation 2 discount 1.26
            "300347",  # 泰格医药 roe 13.67 pe 0.91 pb 15.02 dividend 3.5 0.45%  operation 6 discount 10.99
            "600167",  # 联美控股 roe 13.63 pe 3.19 pb 4.28 dividend 1.5 1.19%  operation 6 discount 3.14
            "000063",  # 中兴通讯 roe 13.63 pe 1.76 pb 7.76 dividend 2.5 0.49%  operation 2 discount 5.7
            "600236",  # 桂冠电力 roe 13.54 pe 5.63 pb 2.4 dividend 2.5 5.64%  operation 0 discount 1.77
            "600828",  # 茂业商业 roe 13.54 pe 12.32 pb 1.1 dividend 1.0 2.45%  operation 6 discount 0.81
            "601012",  # 隆基股份 roe 13.51 pe 3.22 pb 4.2 dividend 1.0 0.35%  operation 2 discount 3.11
            "002099",  # 海翔药业 roe 13.46 pe 6.81 pb 1.98 dividend 3.0 4.29%  operation 2 discount 1.47
            "600477",  # 杭萧钢构 roe 13.42 pe 5.06 pb 2.65 dividend 1.0 2.33%  operation 2 discount 1.97
            "600136",  # 当代明诚 roe 13.4 pe 10.44 pb 1.28 dividend 0.23 0.22%  operation 4 discount 0.96
            "002174",  # 游族网络 roe 13.3 pe 3.82 pb 3.48 dividend 0.766418 0.37%  operation 2 discount 2.62
            "002236",  # 大华股份 roe 13.24 pe 3.32 pb 3.99 dividend 1.00001 0.53%  operation 6 discount 3.01
            "300423",  # 鲁亿通 roe 13.19 pe 6.29 pb 2.1 dividend 2.28 1.65%  operation 6 discount 1.59
            "600070",  # 浙江富润 roe 13.17 pe 6.16 pb 2.14 dividend 0.8 0.72%  operation 2 discount 1.62
            "002020",  # 京新药业 roe 13.14 pe 6.11 pb 2.15 dividend 3.0 2.72%  operation 6 discount 1.64
            "002024",  # 苏宁易购 roe 13.09 pe 13.4 pb 0.98 dividend 1.2 1.26%  operation 6 discount 0.75
            "002117",  # 东港股份 roe 13.05 pe 2.88 pb 4.53 dividend 7.0 5.34%  operation 2 discount 3.47
            "002164",  # 宁波东力 roe 13.05 pe 3.25 pb 4.01 dividend 0.5 1.32%  operation 2 discount 3.07
            "603368",  # 柳药股份 roe 13.02 pe 6.37 pb 2.05 dividend 6.2 1.87%  operation 6 discount 1.57
            "300226",  # 上海钢联 roe 13.02 pe 1.04 pb 12.47 dividend 0.5 0.06%  operation 6 discount 9.58
            "600516",  # 方大炭素 roe 12.98 pe 6.91 pb 1.88 dividend 0.0 0.0%  operation 2 discount 1.45
            "002142",  # 宁波银行 roe 12.98 pe 6.99 pb 1.86 dividend 4.0 1.47%  operation 6 discount 1.43
            "300016",  # 北陆药业 roe 12.98 pe 3.13 pb 4.15 dividend 1.0 0.93%  operation 6 discount 3.19
            "600609",  # 金杯汽车 roe 12.95 pe 1.28 pb 10.15 dividend 0.0 0.0%  operation 2 discount 7.83
            "000031",  # 大悦城 roe 12.93 pe 9.9 pb 1.31 dividend 1.1 1.92%  operation 0 discount 1.01
            "002524",  # 光正集团 roe 12.89 pe 2.65 pb 4.87 dividend 0.25 0.28%  operation 2 discount 3.78
            "000877",  # 天山股份 roe 12.85 pe 9.64 pb 1.33 dividend 3.8 3.25%  operation 6 discount 1.04
            "300179",  # 四方达 roe 12.85 pe 3.26 pb 3.94 dividend 1.5 2.07%  operation 2 discount 3.07
            "600389",  # 江山股份 roe 12.84 pe 4.08 pb 3.15 dividend 4.0 1.92%  operation 2 discount 2.45
            "000036",  # 华联控股 roe 12.84 pe 11.11 pb 1.16 dividend 6.0 16.26%  operation 2 discount 0.9
            "300144",  # 宋城演艺 roe 12.8 pe 3.26 pb 3.93 dividend 1.2 0.45%  operation 6 discount 3.07
            "300396",  # 迪瑞医疗 roe 12.78 pe 3.33 pb 3.84 dividend 2.8 1.36%  operation 6 discount 3.01
            "000922",  # 佳电股份 roe 12.75 pe 6.92 pb 1.84 dividend 0.33 0.42%  operation 6 discount 1.45
            "300205",  # 天喻信息 roe 12.74 pe 3.09 pb 4.12 dividend 1.0 0.74%  operation 2 discount 3.23
            "600675",  # 中华企业 roe 12.7 pe 6.79 pb 1.87 dividend 1.8 3.99%  operation 0 discount 1.47
            "002440",  # 闰土股份 roe 12.7 pe 8.39 pb 1.51 dividend 5.0 4.48%  operation 2 discount 1.19
            "300113",  # 顺网科技 roe 12.68 pe 2.08 pb 6.09 dividend 1.99927 0.83%  operation 2 discount 4.8
            "600173",  # 卧龙地产 roe 12.67 pe 9.38 pb 1.35 dividend 1.0 2.01%  operation 2 discount 1.07
            "600395",  # 盘江股份 roe 12.65 pe 9.29 pb 1.36 dividend 4.0 6.86%  operation 6 discount 1.08
            "603328",  # 依顿电子 roe 12.65 pe 3.89 pb 3.25 dividend 14.5 12.75%  operation 2 discount 2.57
            "300088",  # 长信科技 roe 12.65 pe 2.88 pb 4.39 dividend 1.3 1.28%  operation 2 discount 3.47
            "600782",  # 新钢股份 roe 12.61 pe 18.82 pb 0.67 dividend 2.0 4.54%  operation 2 discount 0.53
            "002180",  # 纳思达 roe 12.6 pe 1.74 pb 7.23 dividend 0.8 0.21%  operation 2 discount 5.74
            "002728",  # 特一药业 roe 12.6 pe 3.85 pb 3.28 dividend 6.5 3.78%  operation 6 discount 2.6
            "002705",  # 新宝股份 roe 12.56 pe 2.98 pb 4.22 dividend 3.5 1.61%  operation 2 discount 3.36
            "002468",  # 申通快递 roe 12.52 pe 3.76 pb 3.33 dividend 5.0 2.6%  operation 6 discount 2.66
            "002318",  # 久立特材 roe 12.49 pe 5.32 pb 2.35 dividend 3.0 3.46%  operation 2 discount 1.88
            "000951",  # 中国重汽 roe 12.46 pe 6.23 pb 2.0 dividend 4.6 2.35%  operation 6 discount 1.6
            "600546",  # 山煤国际 roe 12.45 pe 3.92 pb 3.18 dividend 0.5 0.49%  operation 2 discount 2.55
            "000966",  # 长源电力 roe 12.45 pe 10.84 pb 1.15 dividend 0.6 1.46%  operation 2 discount 0.92
            "600848",  # 上海临港 roe 12.44 pe 2.75 pb 4.52 dividend 1.2 0.58%  operation 0 discount 3.64
            "600728",  # 佳都科技 roe 12.41 pe 3.53 pb 3.52 dividend 0.57 0.57%  operation 6 discount 2.84
            "002402",  # 和而泰 roe 12.4 pe 1.77 pb 7.0 dividend 0.4 0.27%  operation 6 discount 5.65
            "600161",  # 天坛生物 roe 12.3 pe 1.32 pb 9.31 dividend 0.5 0.15%  operation 2 discount 7.57
            "300130",  # 新国都 roe 12.3 pe 3.85 pb 3.2 dividend 3.49988 2.16%  operation 2 discount 2.6
            "300236",  # 上海新阳 roe 12.26 pe 1.91 pb 6.41 dividend 0.5 0.1%  operation 2 discount 5.23
            "600533",  # 栖霞建设 roe 12.23 pe 13.21 pb 0.93 dividend 1.0 2.81%  operation 0 discount 0.76
            "600285",  # 羚锐制药 roe 12.19 pe 5.02 pb 2.43 dividend 1.5 1.63%  operation 2 discount 1.99
            "002737",  # 葵花药业 roe 12.19 pe 4.35 pb 2.8 dividend 10.0 6.81%  operation 6 discount 2.3
            "000042",  # 中洲控股 roe 12.17 pe 14.03 pb 0.87 dividend 1.0 1.01%  operation 0 discount 0.71
            "000034",  # 神州数码 roe 12.16 pe 2.98 pb 4.08 dividend 2.53 0.97%  operation 2 discount 3.35
            "600455",  # 博通股份 roe 12.14 pe 1.1 pb 11.07 dividend 0.0 0.0%  operation 2 discount 9.12
            "600580",  # 卧龙电驱 roe 12.07 pe 4.59 pb 2.63 dividend 1.5 1.1%  operation 2 discount 2.18
            "601515",  # 东风股份 roe 12.07 pe 4.96 pb 2.43 dividend 5.0 6.69%  operation 6 discount 2.02
            "603600",  # 永艺股份 roe 12.04 pe 3.79 pb 3.18 dividend 4.2 3.36%  operation 2 discount 2.64
            "002360",  # 同德化工 roe 12.04 pe 6.03 pb 2.0 dividend 1.0 1.86%  operation 2 discount 1.66
            "600886",  # 国投电力 roe 12.01 pe 8.36 pb 1.44 dividend 2.25 2.95%  operation 0 discount 1.2
            "300303",  # 聚飞光电 roe 11.96 pe 3.35 pb 3.57 dividend 0.45 0.76%  operation 2 discount 2.99
            "601636",  # 旗滨集团 roe 11.91 pe 6.33 pb 1.88 dividend 3.0 5.5%  operation 2 discount 1.58
            "300012",  # 华测检测 roe 11.9 pe 1.38 pb 8.61 dividend 0.35 0.22%  operation 2 discount 7.24
            "000650",  # 仁和药业 roe 11.86 pe 4.55 pb 2.61 dividend 1.0 1.28%  operation 6 discount 2.2
            "300403",  # 汉宇集团 roe 11.86 pe 5.31 pb 2.23 dividend 2.0 3.93%  operation 2 discount 1.88
            "002568",  # 百润股份 roe 11.85 pe 1.3 pb 9.1 dividend 4.0 1.18%  operation 2 discount 7.68
            "300251",  # 光线传媒 roe 11.85 pe 3.76 pb 3.15 dividend 0.5 0.5%  operation 2 discount 2.66
            "000739",  # 普洛药业 roe 11.84 pe 2.05 pb 5.77 dividend 1.1 0.62%  operation 2 discount 4.87
            "000517",  # 荣安地产 roe 11.83 pe 7.12 pb 1.66 dividend 0.2 0.7%  operation 0 discount 1.41
            "300286",  # 安科瑞 roe 11.82 pe 3.6 pb 3.28 dividend 2.0 1.67%  operation 2 discount 2.78
            "002701",  # 奥瑞金 roe 11.8 pe 6.53 pb 1.81 dividend 1.08 2.42%  operation 2 discount 1.53
            "000915",  # 山大华特 roe 11.79 pe 3.24 pb 3.64 dividend 3.0 1.12%  operation 2 discount 3.09
            "002050",  # 三花智控 roe 11.77 pe 1.81 pb 6.5 dividend 2.5 1.19%  operation 6 discount 5.52
            "002223",  # 鱼跃医疗 roe 11.76 pe 2.15 pb 5.47 dividend 1.5 0.45%  operation 6 discount 4.65
            "600993",  # 马应龙 roe 11.75 pe 4.3 pb 2.74 dividend 1.5 0.95%  operation 2 discount 2.33
            "300114",  # 中航电测 roe 11.75 pe 2.85 pb 4.13 dividend 0.45 0.41%  operation 6 discount 3.51
            "300406",  # 九强生物 roe 11.75 pe 2.19 pb 5.37 dividend 1.5 0.76%  operation 6 discount 4.57
            "002396",  # 星网锐捷 roe 11.73 pe 1.96 pb 5.99 dividend 1.1 0.26%  operation 2 discount 5.11
            "002478",  # 常宝股份 roe 11.71 pe 9.58 pb 1.22 dividend 1.2 2.15%  operation 6 discount 1.04
            "600829",  # 人民同泰 roe 11.7 pe 4.33 pb 2.7 dividend 5.0 6.0%  operation 2 discount 2.31
            "002222",  # 福晶科技 roe 11.69 pe 2.18 pb 5.37 dividend 1.0 0.84%  operation 2 discount 4.6
            "600673",  # 东阳光 roe 11.67 pe 3.36 pb 3.47 dividend 0.7 0.89%  operation 6 discount 2.97
            "002139",  # 拓邦股份 roe 11.66 pe 4.24 pb 2.75 dividend 1.00603 1.58%  operation 6 discount 2.36
            "000968",  # 蓝焰控股 roe 11.64 pe 5.9 pb 1.97 dividend 0.5 0.56%  operation 0 discount 1.69
            "002003",  # 伟星股份 roe 11.63 pe 5.64 pb 2.06 dividend 3.5 5.34%  operation 2 discount 1.77
            "300152",  # 科融环境 roe 11.6 pe 3.99 pb 2.91 dividend 0.06 0.19%  operation 2 discount 2.51
            "601021",  # 春秋航空 roe 11.57 pe 4.94 pb 2.34 dividend 2.0 0.53%  operation 2 discount 2.03
            "600803",  # 新奥股份 roe 11.56 pe 8.68 pb 1.33 dividend 2.1 2.08%  operation 6 discount 1.15
            "002233",  # 塔牌集团 roe 11.53 pe 7.35 pb 1.57 dividend 7.3 6.07%  operation 6 discount 1.36
            "603611",  # 诺力股份 roe 11.52 pe 3.71 pb 3.1 dividend 5.0 2.64%  operation 2 discount 2.69
            "300132",  # 青松股份 roe 11.52 pe 4.64 pb 2.48 dividend 1.0 0.71%  operation 6 discount 2.16
            "603010",  # 万盛股份 roe 11.51 pe 2.62 pb 4.39 dividend 1.5 0.97%  operation 2 discount 3.81
            "600233",  # 圆通速递 roe 11.5 pe 3.57 pb 3.22 dividend 1.5 1.11%  operation 6 discount 2.8
            "000961",  # 中南建设 roe 11.48 pe 7.15 pb 1.61 dividend 1.2 1.41%  operation 0 discount 1.4
            "002215",  # 诺 普 信 roe 11.47 pe 4.15 pb 2.76 dividend 1.5 2.16%  operation 2 discount 2.41
            "002511",  # 中顺洁柔 roe 11.46 pe 2.07 pb 5.52 dividend 0.23 0.14%  operation 6 discount 4.82
            "600305",  # 恒顺醋业 roe 11.44 pe 1.71 pb 6.68 dividend 1.2 0.64%  operation 6 discount 5.84
            "600810",  # 神马股份 roe 11.43 pe 6.42 pb 1.78 dividend 4.5 4.33%  operation 2 discount 1.56
            "600177",  # 雅戈尔 roe 11.41 pe 9.33 pb 1.22 dividend 5.0 7.6%  operation 0 discount 1.07
            "000023",  # 深天地Ａ roe 11.35 pe 2.9 pb 3.92 dividend 0.6 0.44%  operation 2 discount 3.45
            "002398",  # 垒知集团 roe 11.32 pe 5.69 pb 1.99 dividend 0.7 0.89%  operation 6 discount 1.76
            "600738",  # 兰州民百 roe 11.31 pe 4.7 pb 2.41 dividend 19.0233 34.09%  operation 6 discount 2.13
            "002563",  # 森马服饰 roe 11.31 pe 6.06 pb 1.87 dividend 3.5 4.38%  operation 2 discount 1.65
            "002668",  # 奥马电器 roe 11.3 pe 5.41 pb 2.09 dividend 0.62 1.22%  operation 2 discount 1.85
            "000671",  # 阳 光 城 roe 11.29 pe 7.35 pb 1.54 dividend 0.56338 0.75%  operation 4 discount 1.36
            "002698",  # 博实股份 roe 11.25 pe 2.42 pb 4.64 dividend 1.4 1.39%  operation 6 discount 4.13
            "000932",  # 华菱钢铁 roe 11.24 pe 13.47 pb 0.83 dividend 0.0 0.0%  operation 2 discount 0.74
            "300394",  # 天孚通信 roe 11.17 pe 1.37 pb 8.16 dividend 3.6 0.78%  operation 2 discount 7.31
            "603111",  # 康尼机电 roe 11.16 pe 3.06 pb 3.65 dividend 1.2 1.7%  operation 2 discount 3.27
            "002732",  # 燕塘乳业 roe 11.15 pe 3.57 pb 3.13 dividend 1.0 0.51%  operation 2 discount 2.8
            "600512",  # 腾达建设 roe 11.13 pe 9.25 pb 1.2 dividend 0.2 0.56%  operation 2 discount 1.08
            "603008",  # 喜临门 roe 11.13 pe 5.72 pb 1.95 dividend 0.5 0.39%  operation 2 discount 1.75
            "002727",  # 一心堂 roe 11.09 pe 3.93 pb 2.83 dividend 3.0 1.38%  operation 6 discount 2.55
            "002587",  # 奥拓电子 roe 11.06 pe 3.25 pb 3.41 dividend 1.00251 1.36%  operation 2 discount 3.08
            "300341",  # 麦克奥迪 roe 11.06 pe 2.11 pb 5.25 dividend 0.58 0.59%  operation 2 discount 4.75
            "603018",  # 中设集团 roe 11.04 pe 5.83 pb 1.89 dividend 3.8 3.53%  operation 6 discount 1.72
            "300121",  # 阳谷华泰 roe 11.02 pe 5.5 pb 2.01 dividend 6.5 7.53%  operation 2 discount 1.82
            "300043",  # 星辉娱乐 roe 11.01 pe 5.63 pb 1.95 dividend 0.3 0.62%  operation 2 discount 1.78
            "000997",  # 新 大 陆 roe 10.97 pe 3.33 pb 3.3 dividend 3.0 1.67%  operation 2 discount 3.01
            "002221",  # 东华能源 roe 10.97 pe 4.93 pb 2.22 dividend 0.37 0.3%  operation 6 discount 2.03
            "002179",  # 中航光电 roe 10.96 pe 2.01 pb 5.44 dividend 1.3 0.35%  operation 2 discount 4.97
            "002294",  # 信立泰 roe 10.96 pe 3.71 pb 2.95 dividend 8.0 4.33%  operation 2 discount 2.69
            "600053",  # 九鼎投资 roe 10.94 pe 1.7 pb 6.43 dividend 7.4 2.42%  operation 2 discount 5.87
            "002381",  # 双箭股份 roe 10.9 pe 5.3 pb 2.06 dividend 4.0 4.67%  operation 6 discount 1.89
            "300231",  # 银信科技 roe 10.9 pe 3.52 pb 3.09 dividend 1.5 1.73%  operation 2 discount 2.84
            "000046",  # 泛海控股 roe 10.89 pe 10.88 pb 1.0 dividend 1.5 3.4%  operation 0 discount 0.92
            "002116",  # 中国海诚 roe 10.88 pe 4.69 pb 2.32 dividend 2.5 3.02%  operation 2 discount 2.13
            "002352",  # 顺丰控股 roe 10.85 pe 2.08 pb 5.22 dividend 2.1 0.45%  operation 2 discount 4.81
            "000425",  # 徐工机械 roe 10.84 pe 7.18 pb 1.51 dividend 0.6 1.12%  operation 6 discount 1.39
            "002078",  # 太阳纸业 roe 10.83 pe 5.7 pb 1.9 dividend 1.0 0.99%  operation 2 discount 1.76
            "600644",  # 乐山电力 roe 10.8 pe 5.92 pb 1.82 dividend 0.5 0.97%  operation 2 discount 1.69
            "603898",  # 好莱客 roe 10.79 pe 5.54 pb 1.95 dividend 3.71 2.44%  operation 2 discount 1.8
            "300316",  # 晶盛机电 roe 10.77 pe 1.71 pb 6.31 dividend 1.0 0.46%  operation 2 discount 5.86
            "600702",  # 舍得酒业 roe 10.75 pe 3.63 pb 2.96 dividend 1.03 0.42%  operation 6 discount 2.76
            "002611",  # 东方精工 roe 10.75 pe 5.1 pb 2.11 dividend 0.45 0.9%  operation 2 discount 1.96
            "000065",  # 北方国际 roe 10.74 pe 7.89 pb 1.36 dividend 0.8 0.98%  operation 2 discount 1.27
            "603588",  # 高能环境 roe 10.71 pe 3.75 pb 2.86 dividend 0.5 0.4%  operation 4 discount 2.67
            "000913",  # 钱江摩托 roe 10.71 pe 6.03 pb 1.78 dividend 1.0 0.91%  operation 2 discount 1.66
            "002489",  # 浙江永强 roe 10.67 pe 2.93 pb 3.64 dividend 0.6 1.07%  operation 2 discount 3.41
            "000952",  # 广济药业 roe 10.66 pe 3.92 pb 2.72 dividend 1.1 1.04%  operation 2 discount 2.55
            "300160",  # 秀强股份 roe 10.6 pe 1.63 pb 6.5 dividend 2.2 2.04%  operation 2 discount 6.13
            "002098",  # 浔兴股份 roe 10.55 pe 2.75 pb 3.83 dividend 0.2 0.3%  operation 2 discount 3.63
            "601001",  # 大同煤业 roe 10.53 pe 10.62 pb 0.99 dividend 0.27 0.71%  operation 2 discount 0.94
            "002038",  # 双鹭药业 roe 10.51 pe 3.66 pb 2.87 dividend 3.0 2.24%  operation 6 discount 2.73
            "600170",  # 上海建工 roe 10.5 pe 8.91 pb 1.18 dividend 1.35 3.94%  operation 6 discount 1.12
            "600704",  # 物产中大 roe 10.5 pe 9.7 pb 1.08 dividend 2.5 5.18%  operation 2 discount 1.03
            "601216",  # 君正集团 roe 10.49 pe 8.36 pb 1.25 dividend 1.9000000000000001 6.91%  operation 2 discount 1.2
            "600850",  # 华东电脑 roe 10.45 pe 2.45 pb 4.26 dividend 3.6 1.45%  operation 2 discount 4.08
            "600871",  # 石化油服 roe 10.45 pe 1.63 pb 6.39 dividend 0.0 0.0%  operation 6 discount 6.12
            "002001",  # 新 和 成 roe 10.41 pe 2.85 pb 3.65 dividend 7.0 2.51%  operation 2 discount 3.51
            "603167",  # 渤海轮渡 roe 10.38 pe 8.24 pb 1.26 dividend 6.0 6.79%  operation 6 discount 1.21
            "002648",  # 卫星石化 roe 10.36 pe 4.8 pb 2.16 dividend 0.9 0.5%  operation 2 discount 2.09
            "000718",  # 苏宁环球 roe 10.35 pe 8.22 pb 1.26 dividend 3.0 9.29%  operation 2 discount 1.22
            "000628",  # 高新发展 roe 10.33 pe 3.63 pb 2.85 dividend 0.0 0.0%  operation 2 discount 2.76
            "002615",  # 哈尔斯 roe 10.31 pe 4.27 pb 2.41 dividend 0.8 1.54%  operation 2 discount 2.34
            "000723",  # 美锦能源 roe 10.3 pe 2.54 pb 4.05 dividend 2.0 2.53%  operation 6 discount 3.93
            "300234",  # 开尔新材 roe 10.3 pe 3.11 pb 3.31 dividend 0.1 0.09%  operation 2 discount 3.21
            "300246",  # 宝莱特 roe 10.3 pe 1.98 pb 5.21 dividend 1.0 0.52%  operation 2 discount 5.06
            "600271",  # 航天信息 roe 10.29 pe 2.76 pb 3.73 dividend 4.4 1.97%  operation 2 discount 3.63
            "002332",  # 仙琚制药 roe 10.29 pe 2.81 pb 3.67 dividend 0.65 0.57%  operation 6 discount 3.56
            "601567",  # 三星医疗 roe 10.28 pe 6.7 pb 1.53 dividend 3.0 3.48%  operation 2 discount 1.49
            "600176",  # 中国巨石 roe 10.25 pe 4.81 pb 2.13 dividend 2.25 2.45%  operation 2 discount 2.08
            "002641",  # 永高股份 roe 10.22 pe 4.49 pb 2.28 dividend 0.33 0.51%  operation 2 discount 2.23
            "300285",  # 国瓷材料 roe 10.22 pe 1.52 pb 6.74 dividend 1.0 0.41%  operation 6 discount 6.6
            "300233",  # 金城医药 roe 10.2 pe 5.47 pb 1.86 dividend 2.5 1.24%  operation 2 discount 1.83
            "600727",  # 鲁北化工 roe 10.19 pe 5.35 pb 1.9 dividend 1.0 1.32%  operation 2 discount 1.87
            "600535",  # 天士力 roe 10.18 pe 4.94 pb 2.06 dividend 3.0 1.98%  operation 6 discount 2.02
            "600984",  # 建设机械 roe 10.18 pe 3.66 pb 2.78 dividend 0.0 0.0%  operation 2 discount 2.73
            "600211",  # 西藏药业 roe 10.17 pe 3.76 pb 2.7 dividend 3.7 1.03%  operation 2 discount 2.66
            "002695",  # 煌上煌 roe 10.17 pe 2.33 pb 4.37 dividend 0.82 0.46%  operation 6 discount 4.3
            "600388",  # 龙净环保 roe 10.15 pe 4.69 pb 2.17 dividend 1.7 1.53%  operation 6 discount 2.13
            "601818",  # 光大银行 roe 10.15 pe 15.66 pb 0.65 dividend 1.61 4.21%  operation 2 discount 0.64
            "002019",  # 亿帆医药 roe 10.14 pe 3.36 pb 3.02 dividend 1.0 0.56%  operation 2 discount 2.98
            "002027",  # 分众传媒 roe 10.1 pe 1.76 pb 5.73 dividend 1.0 1.9%  operation 2 discount 5.68
            "002039",  # 黔源电力 roe 10.1 pe 6.87 pb 1.47 dividend 3.0 2.2%  operation 0 discount 1.46
            "600000",  # 浦发银行 roe 10.07 pe 15.28 pb 0.66 dividend 3.5 3.25%  operation 6 discount 0.65
            "600761",  # 安徽合力 roe 10.07 pe 6.94 pb 1.45 dividend 3.5 3.72%  operation 6 discount 1.44
            "600626",  # 申达股份 roe 10.06 pe 6.59 pb 1.53 dividend 0.5 0.76%  operation 2 discount 1.52
            "600674",  # 川投能源 roe 10.06 pe 6.61 pb 1.52 dividend 3.0 3.32%  operation 0 discount 1.51
            "000993",  # 闽东电力 roe 10.06 pe 6.75 pb 1.49 dividend 0.25 0.36%  operation 0 discount 1.48
            "002191",  # 劲嘉股份 roe 10.03 pe 4.6 pb 2.18 dividend 3.0 3.0%  operation 6 discount 2.17
            "600693",  # 东百集团 roe 10.0 pe 5.36 pb 1.87 dividend 1.0 2.0%  operation 0 discount 1.87
            "002036",  # 联创电子 roe 9.97 pe 1.96 pb 5.09 dividend 0.45 0.28%  operation 2 discount 5.1
            "603806",  # 福斯特 roe 9.96 pe 2.43 pb 4.11 dividend 4.5 0.96%  operation 2 discount 4.12
            "300309",  # 吉艾科技 roe 9.96 pe 6.31 pb 1.58 dividend 0.0 0.0%  operation 0 discount 1.59
            "000703",  # 恒逸石化 roe 9.94 pe 5.74 pb 1.73 dividend 3.0 2.21%  operation 2 discount 1.74
            "000546",  # 金圆股份 roe 9.93 pe 6.24 pb 1.59 dividend 0.5 0.55%  operation 2 discount 1.6
            "000637",  # 茂化实华 roe 9.93 pe 3.16 pb 3.14 dividend 0.6 1.08%  operation 2 discount 3.16
            "002085",  # 万丰奥威 roe 9.92 pe 3.89 pb 2.55 dividend 3.03462 4.29%  operation 2 discount 2.57
            "002080",  # 中材科技 roe 9.9 pe 4.48 pb 2.21 dividend 2.43 1.79%  operation 6 discount 2.23
            "002326",  # 永太科技 roe 9.9 pe 2.57 pb 3.84 dividend 1.5 1.07%  operation 2 discount 3.88
            "600093",  # 易见股份 roe 9.89 pe 5.17 pb 1.91 dividend 3.63 2.71%  operation 2 discount 1.94
            "300019",  # 硅宝科技 roe 9.87 pe 2.26 pb 4.37 dividend 1.0 0.9%  operation 2 discount 4.43
            "603601",  # 再升科技 roe 9.86 pe 1.04 pb 9.44 dividend 1.5 0.82%  operation 2 discount 9.57
            "002444",  # 巨星科技 roe 9.83 pe 5.31 pb 1.85 dividend 1.9 1.49%  operation 2 discount 1.88
            "002399",  # 海普瑞 roe 9.82 pe 2.27 pb 4.32 dividend 1.0 0.42%  operation 2 discount 4.4
            "000902",  # 新洋丰 roe 9.8 pe 5.7 pb 1.72 dividend 2.0 2.31%  operation 6 discount 1.75
            "601158",  # 重庆水务 roe 9.78 pe 5.56 pb 1.76 dividend 2.8 5.19%  operation 2 discount 1.8
            "002353",  # 杰瑞股份 roe 9.75 pe 2.91 pb 3.35 dividend 1.2 0.37%  operation 2 discount 3.43
            "002384",  # 东山精密 roe 9.75 pe 1.97 pb 4.95 dividend 0.55 0.2%  operation 6 discount 5.08
            "300118",  # 东方日升 roe 9.75 pe 5.94 pb 1.64 dividend 0.600509 0.41%  operation 2 discount 1.68
            "600143",  # 金发科技 roe 9.74 pe 3.19 pb 3.05 dividend 1.0 0.87%  operation 2 discount 3.13
            "600229",  # 城市传媒 roe 9.74 pe 4.99 pb 1.95 dividend 2.0 2.68%  operation 6 discount 2.0
            "601169",  # 北京银行 roe 9.74 pe 16.51 pb 0.59 dividend 2.86 5.52%  operation 6 discount 0.61
            "600643",  # 爱建集团 roe 9.73 pe 7.22 pb 1.35 dividend 1.2 1.38%  operation 4 discount 1.38
            "002056",  # 横店东磁 roe 9.73 pe 2.56 pb 3.81 dividend 1.49189 1.26%  operation 2 discount 3.91
            "002145",  # 中核钛白 roe 9.71 pe 4.65 pb 2.09 dividend 0.2 0.45%  operation 2 discount 2.15
            "000062",  # 深圳华强 roe 9.7 pe 3.57 pb 2.71 dividend 2.5 1.91%  operation 2 discount 2.8
            "002203",  # 海亮股份 roe 9.68 pe 4.57 pb 2.12 dividend 0.713397 0.78%  operation 2 discount 2.19
            "002419",  # 天虹股份 roe 9.67 pe 5.96 pb 1.62 dividend 4.0 4.39%  operation 2 discount 1.68
            "002531",  # 天顺风能 roe 9.66 pe 4.98 pb 1.94 dividend 0.601314 0.98%  operation 6 discount 2.01
            "002550",  # 千红制药 roe 9.66 pe 3.64 pb 2.65 dividend 1.2 2.53%  operation 2 discount 2.74
            "000030",  # 富奥股份 roe 9.65 pe 5.28 pb 1.83 dividend 1.5 2.33%  operation 2 discount 1.89
            "600873",  # 梅花生物 roe 9.62 pe 5.77 pb 1.67 dividend 3.3 6.92%  operation 2 discount 1.73
            "002632",  # 道明光学 roe 9.62 pe 3.65 pb 2.63 dividend 3.5 4.26%  operation 6 discount 2.74
            "300296",  # 利亚德 roe 9.61 pe 3.91 pb 2.46 dividend 0.8 0.99%  operation 6 discount 2.55
            "600661",  # 昂立教育 roe 9.59 pe 1.97 pb 4.86 dividend 2.0 1.1%  operation 2 discount 5.07
            "603678",  # 火炬电子 roe 9.56 pe 2.46 pb 3.89 dividend 1.0 0.38%  operation 2 discount 4.07
            "600567",  # 山鹰纸业 roe 9.55 pe 8.5 pb 1.12 dividend 1.33 3.91%  operation 2 discount 1.18
            "300371",  # 汇中股份 roe 9.54 pe 2.96 pb 3.22 dividend 2.0 1.54%  operation 6 discount 3.38
            "002111",  # 威海广泰 roe 9.49 pe 4.39 pb 2.16 dividend 3.55771 2.21%  operation 2 discount 2.28
            "300320",  # 海达股份 roe 9.49 pe 4.02 pb 2.36 dividend 0.56 0.88%  operation 6 discount 2.49
            "000755",  # 山西路桥 roe 9.47 pe 6.09 pb 1.56 dividend 1.5 3.85%  operation 0 discount 1.64
            "603939",  # 益丰药房 roe 9.43 pe 1.27 pb 7.46 dividend 3.0 0.34%  operation 2 discount 7.9
            "000936",  # 华西股份 roe 9.43 pe 5.28 pb 1.78 dividend 0.5 0.49%  operation 0 discount 1.89
            "601998",  # 中信银行 roe 9.42 pe 15.22 pb 0.62 dividend 2.3 4.2%  operation 6 discount 0.66
            "002094",  # 青岛金王 roe 9.42 pe 10.09 pb 0.93 dividend 1.2 2.8%  operation 2 discount 0.99
            "600694",  # 大商股份 roe 9.38 pe 11.7 pb 0.8 dividend 9.0 3.7%  operation 2 discount 0.85
            "000818",  # 航锦科技 roe 9.36 pe 1.39 pb 6.76 dividend 1.5 0.6%  operation 2 discount 7.22
            "002430",  # 杭氧股份 roe 9.36 pe 4.38 pb 2.14 dividend 1.8 1.43%  operation 6 discount 2.28
            "300284",  # 苏交科 roe 9.36 pe 4.66 pb 2.01 dividend 1.4 1.5%  operation 2 discount 2.15
            "300427",  # 红相股份 roe 9.31 pe 3.01 pb 3.09 dividend 1.29 0.7%  operation 6 discount 3.32
            "600371",  # 万向德农 roe 9.29 pe 1.61 pb 5.75 dividend 2.0 1.65%  operation 2 discount 6.19
            "300009",  # 安科生物 roe 9.29 pe 1.59 pb 5.85 dividend 1.5 0.97%  operation 2 discount 6.29
            "000985",  # 大庆华科 roe 9.28 pe 2.71 pb 3.43 dividend 1.85 1.2%  operation 2 discount 3.7
            "002549",  # 凯美特气 roe 9.28 pe 2.16 pb 4.29 dividend 1.0 1.49%  operation 2 discount 4.63
            "002664",  # 长鹰信质 roe 9.28 pe 3.73 pb 2.49 dividend 0.7 0.48%  operation 2 discount 2.68
            "600530",  # 交大昂立 roe 9.27 pe 3.05 pb 3.04 dividend 0.65 1.66%  operation 0 discount 3.28
            "002091",  # 江苏国泰 roe 9.27 pe 6.98 pb 1.33 dividend 2.0 2.84%  operation 2 discount 1.43
            "002293",  # 罗莱生活 roe 9.26 pe 4.74 pb 1.95 dividend 4.0 4.4%  operation 2 discount 2.11
            "300389",  # 艾比森 roe 9.25 pe 3.67 pb 2.52 dividend 1.55 1.45%  operation 2 discount 2.72
            "600252",  # 中恒集团 roe 9.24 pe 4.52 pb 2.04 dividend 0.6 1.63%  operation 2 discount 2.21
            "600641",  # 万业企业 roe 9.24 pe 3.48 pb 2.65 dividend 1.96 0.95%  operation 2 discount 2.87
            "600521",  # 华海药业 roe 9.21 pe 1.76 pb 5.24 dividend 2.0 0.91%  operation 2 discount 5.68
            "002137",  # 麦达数字 roe 9.21 pe 2.83 pb 3.25 dividend 0.2 0.24%  operation 2 discount 3.53
            "002579",  # 中京电子 roe 9.2 pe 1.9 pb 4.85 dividend 1.0 0.7%  operation 2 discount 5.27
            "300124",  # 汇川技术 roe 9.19 pe 1.3 pb 7.07 dividend 2.0 0.7%  operation 2 discount 7.69
            "002637",  # 赞宇科技 roe 9.18 pe 4.64 pb 1.98 dividend 1.0 0.83%  operation 6 discount 2.16
            "600706",  # 曲江文旅 roe 9.16 pe 6.22 pb 1.47 dividend 0.45 0.59%  operation 6 discount 1.61
            "000157",  # 中联重科 roe 9.16 pe 7.15 pb 1.28 dividend 2.5 4.05%  operation 6 discount 1.4
            "300031",  # 宝通科技 roe 9.16 pe 3.09 pb 2.97 dividend 1.15 0.61%  operation 6 discount 3.24
            "002015",  # 协鑫能科 roe 9.15 pe 4.29 pb 2.14 dividend 0.0 0.0%  operation 0 discount 2.33
            "300196",  # 长海股份 roe 9.14 pe 4.8 pb 1.91 dividend 2.0 1.7%  operation 2 discount 2.08
            "300408",  # 三环集团 roe 9.14 pe 1.66 pb 5.52 dividend 2.5 1.08%  operation 2 discount 6.04
            "300345",  # 红宇新材 roe 9.13 pe 1.42 pb 6.44 dividend 0.3 0.42%  operation 2 discount 7.05
            "600794",  # 保税科技 roe 9.12 pe 4.01 pb 2.27 dividend 0.12 0.32%  operation 2 discount 2.49
            "600348",  # 阳泉煤业 roe 9.08 pe 13.78 pb 0.66 dividend 2.8 5.81%  operation 6 discount 0.73
            "002518",  # 科士达 roe 9.08 pe 2.76 pb 3.29 dividend 2.0 1.4%  operation 2 discount 3.62
            "600487",  # 亨通光电 roe 9.06 pe 3.51 pb 2.58 dividend 1.5 0.84%  operation 2 discount 2.85
            "002300",  # 太阳电缆 roe 9.06 pe 3.04 pb 2.98 dividend 1.2 1.71%  operation 2 discount 3.29
            "601588",  # 北辰实业 roe 9.05 pe 13.45 pb 0.67 dividend 1.2 4.17%  operation 0 discount 0.74
            "300127",  # 银河磁体 roe 9.04 pe 2.16 pb 4.19 dividend 3.5 2.21%  operation 2 discount 4.64
            "600419",  # 天润乳业 roe 9.03 pe 3.8 pb 2.38 dividend 1.66 1.44%  operation 6 discount 2.63
            "600589",  # 广东榕泰 roe 9.03 pe 7.52 pb 1.2 dividend 0.2 0.34%  operation 2 discount 1.33
            "600997",  # 开滦股份 roe 9.03 pe 12.69 pb 0.71 dividend 2.6 5.18%  operation 6 discount 0.79
            "601137",  # 博威合金 roe 9.01 pe 3.65 pb 2.47 dividend 0.8 0.61%  operation 2 discount 2.74
            "600577",  # 精达股份 roe 9.0 pe 5.4 pb 1.67 dividend 0.4 1.35%  operation 2 discount 1.85
            "000524",  # 岭南控股 roe 9.0 pe 5.57 pb 1.61 dividend 2.25 3.53%  operation 6 discount 1.79
            "002119",  # 康强电子 roe 9.0 pe 1.55 pb 5.79 dividend 0.25 0.18%  operation 2 discount 6.43
            "002317",  # 众生药业 roe 9.0 pe 3.32 pb 2.71 dividend 2.0 1.47%  operation 6 discount 3.02
            "000529",  # 广弘控股 roe 8.99 pe 3.45 pb 2.6 dividend 0.7 0.98%  operation 2 discount 2.9
            "002150",  # 通润装备 roe 8.98 pe 5.06 pb 1.78 dividend 1.5 2.38%  operation 2 discount 1.98
            "300207",  # 欣旺达 roe 8.98 pe 1.7 pb 5.3 dividend 1.30048 0.69%  operation 6 discount 5.9
            "002274",  # 华昌化工 roe 8.96 pe 4.1 pb 2.19 dividend 1.5 2.33%  operation 2 discount 2.44
            "600845",  # 宝信软件 roe 8.95 pe 1.16 pb 7.72 dividend 3.82 0.83%  operation 6 discount 8.63
            "300306",  # 远方信息 roe 8.95 pe 3.65 pb 2.45 dividend 2.0 1.57%  operation 2 discount 2.74
            "300137",  # 先河环保 roe 8.93 pe 3.99 pb 2.24 dividend 0.5 0.62%  operation 6 discount 2.51
            "002022",  # 科华生物 roe 8.92 pe 2.77 pb 3.22 dividend 0.65 0.45%  operation 2 discount 3.61
            "300382",  # 斯莱克 roe 8.92 pe 2.24 pb 3.98 dividend 2.0 2.84%  operation 6 discount 4.47
            "002206",  # 海 利 得 roe 8.91 pe 4.88 pb 1.83 dividend 2.0 4.9%  operation 6 discount 2.05
            "000796",  # 凯撒旅业 roe 8.89 pe 3.55 pb 2.5 dividend 1.0 1.32%  operation 2 discount 2.82
            "600682",  # 南京新百 roe 8.87 pe 9.76 pb 0.91 dividend 0.9 0.87%  operation 2 discount 1.03
            "300193",  # 佳士科技 roe 8.87 pe 4.59 pb 1.93 dividend 2.0 2.24%  operation 2 discount 2.18
            "600315",  # 上海家化 roe 8.86 pe 3.12 pb 2.84 dividend 2.5 0.94%  operation 6 discount 3.21
            "002105",  # 信隆健康 roe 8.86 pe 2.23 pb 3.97 dividend 0.6 0.99%  operation 2 discount 4.48
            "002462",  # 嘉事堂 roe 8.85 pe 6.43 pb 1.38 dividend 1.5 0.95%  operation 6 discount 1.56
            "300041",  # 回天新材 roe 8.84 pe 3.01 pb 2.93 dividend 1.52547 1.33%  operation 2 discount 3.32
            "300206",  # 理邦仪器 roe 8.84 pe 1.38 pb 6.39 dividend 1.03 0.73%  operation 6 discount 7.23
            "000301",  # 东方盛虹 roe 8.83 pe 5.98 pb 1.47 dividend 1.0 2.03%  operation 2 discount 1.67
            "002049",  # 紫光国微 roe 8.8 pe 1.12 pb 7.83 dividend 0.58 0.11%  operation 2 discount 8.91
            "002558",  # 巨人网络 roe 8.8 pe 1.97 pb 4.47 dividend 1.7 0.94%  operation 2 discount 5.08
            "300067",  # 安诺其 roe 8.8 pe 3.78 pb 2.33 dividend 1.0 2.42%  operation 2 discount 2.64
            "300244",  # 迪安诊断 roe 8.8 pe 2.19 pb 4.01 dividend 0.25 0.1%  operation 6 discount 4.56
            "600422",  # 昆药集团 roe 8.79 pe 4.44 pb 1.98 dividend 1.0 0.94%  operation 2 discount 2.25
            "300243",  # 瑞丰高材 roe 8.79 pe 3.4 pb 2.59 dividend 1.0 1.37%  operation 6 discount 2.94
            "002357",  # 富临运业 roe 8.78 pe 5.92 pb 1.48 dividend 1.0 1.8%  operation 2 discount 1.69
            "600710",  # 苏美达 roe 8.77 pe 5.03 pb 1.74 dividend 1.05 1.69%  operation 6 discount 1.99
            "600971",  # 恒源煤电 roe 8.77 pe 11.88 pb 0.74 dividend 4.1 8.13%  operation 2 discount 0.84
            "601231",  # 环旭电子 roe 8.77 pe 1.97 pb 4.44 dividend 1.64 0.82%  operation 2 discount 5.07
            "603766",  # 隆鑫通用 roe 8.77 pe 8.36 pb 1.05 dividend 4.0 11.17%  operation 2 discount 1.2
            "000688",  # 国城矿业 roe 8.77 pe 1.12 pb 7.86 dividend 1.0 0.66%  operation 2 discount 8.96
            "600210",  # 紫江企业 roe 8.74 pe 5.82 pb 1.5 dividend 1.5 3.26%  operation 2 discount 1.72
            "600572",  # 康恩贝 roe 8.74 pe 2.98 pb 2.93 dividend 1.5 2.51%  operation 2 discount 3.36
            "002449",  # 国星光电 roe 8.74 pe 3.85 pb 2.27 dividend 3.0 2.28%  operation 6 discount 2.6
            "002640",  # 跨境通 roe 8.74 pe 6.44 pb 1.36 dividend 0.45 0.64%  operation 2 discount 1.55
            "002158",  # 汉钟精机 roe 8.72 pe 1.97 pb 4.42 dividend 1.5 0.93%  operation 2 discount 5.07
            "600863",  # 内蒙华电 roe 8.71 pe 6.37 pb 1.37 dividend 0.96 3.52%  operation 4 discount 1.57
            "600469",  # 风神股份 roe 8.7 pe 5.99 pb 1.45 dividend 0.2 0.35%  operation 2 discount 1.67
            "000528",  # 柳 工 roe 8.7 pe 8.88 pb 0.98 dividend 1.5 2.23%  operation 6 discount 1.13
            "300200",  # 高盟新材 roe 8.7 pe 4.21 pb 2.07 dividend 2.1 1.69%  operation 2 discount 2.37
            "300411",  # 金盾股份 roe 8.67 pe 2.7 pb 3.21 dividend 0.5 0.44%  operation 2 discount 3.71
            "601717",  # 郑煤机 roe 8.65 pe 9.87 pb 0.88 dividend 1.45 2.34%  operation 6 discount 1.01
            "600266",  # 城建发展 roe 8.64 pe 12.86 pb 0.67 dividend 2.4 3.23%  operation 0 discount 0.78
            "600327",  # 大东方 roe 8.64 pe 6.78 pb 1.27 dividend 2.0 4.94%  operation 2 discount 1.47
            "600559",  # 老白干酒 roe 8.6 pe 3.18 pb 2.7 dividend 2.0 2.11%  operation 6 discount 3.14
            "002302",  # 西部建设 roe 8.6 pe 4.43 pb 1.94 dividend 0.7 0.64%  operation 2 discount 2.26
            "002688",  # 金河生物 roe 8.59 pe 2.78 pb 3.08 dividend 2.5 3.09%  operation 2 discount 3.59
            "000531",  # 穗恒运Ａ roe 8.58 pe 7.61 pb 1.13 dividend 2.1 3.17%  operation 2 discount 1.31
            "002436",  # 兴森科技 roe 8.58 pe 1.04 pb 8.21 dividend 0.6 0.4%  operation 2 discount 9.58
            "300131",  # 英唐智控 roe 8.58 pe 2.22 pb 3.87 dividend 0.2 0.3%  operation 2 discount 4.51
            "300393",  # 中来股份 roe 8.58 pe 4.18 pb 2.05 dividend 4.09261 2.7%  operation 2 discount 2.39
            "000983",  # 西山煤电 roe 8.54 pe 11.11 pb 0.77 dividend 3.0 5.81%  operation 6 discount 0.9
            "600076",  # 康欣新材 roe 8.52 pe 8.43 pb 1.01 dividend 0.2 0.5%  operation 2 discount 1.19
            "600329",  # 中新药业 roe 8.51 pe 4.31 pb 1.97 dividend 2.2 1.65%  operation 2 discount 2.32
            "600740",  # 山西焦化 roe 8.51 pe 9.94 pb 0.86 dividend 2.0 3.35%  operation 2 discount 1.01
            "600857",  # 宁波中百 roe 8.51 pe 1.92 pb 4.44 dividend 0.6 0.62%  operation 2 discount 5.22
            "600862",  # 中航高科 roe 8.51 pe 1.98 pb 4.3 dividend 1.1 0.9%  operation 2 discount 5.06
            "000100",  # TCL科技 roe 8.49 pe 3.2 pb 2.65 dividend 1.0 1.68%  operation 6 discount 3.12
            "600310",  # 桂东电力 roe 8.48 pe 4.86 pb 1.74 dividend 0.25 0.58%  operation 2 discount 2.06
            "603988",  # 中电电机 roe 8.48 pe 2.39 pb 3.55 dividend 3.85 4.01%  operation 2 discount 4.19
            "002534",  # 杭锅股份 roe 8.47 pe 4.79 pb 1.77 dividend 2.0 2.58%  operation 2 discount 2.09
            "002552",  # 宝鼎科技 roe 8.45 pe 0.91 pb 9.25 dividend 0.1 0.05%  operation 6 discount 10.94
            "300039",  # 上海凯宝 roe 8.43 pe 3.32 pb 2.54 dividend 1.0 1.67%  operation 2 discount 3.01
            "300326",  # 凯利泰 roe 8.43 pe 1.36 pb 6.2 dividend 0.708202 0.31%  operation 6 discount 7.35
            "300192",  # 科斯伍德 roe 8.42 pe 1.96 pb 4.3 dividend 0.2 0.14%  operation 2 discount 5.1
            "000598",  # 兴蓉环境 roe 8.41 pe 6.87 pb 1.22 dividend 0.66 1.45%  operation 4 discount 1.46
            "002660",  # 茂硕电源 roe 8.41 pe 2.03 pb 4.15 dividend 0.16 0.17%  operation 2 discount 4.94
            "002602",  # 世纪华通 roe 8.4 pe 2.56 pb 3.28 dividend 1.0 0.76%  operation 2 discount 3.9
            "600073",  # 上海梅林 roe 8.39 pe 4.41 pb 1.9 dividend 1.0 1.24%  operation 2 discount 2.27
            "002616",  # 长青集团 roe 8.39 pe 3.16 pb 2.65 dividend 2.0 2.43%  operation 0 discount 3.16
            "300258",  # 精锻科技 roe 8.37 pe 3.35 pb 2.5 dividend 1.5 1.22%  operation 2 discount 2.98
            "300294",  # 博雅生物 roe 8.37 pe 1.99 pb 4.21 dividend 1.52601 0.41%  operation 6 discount 5.03
            "002028",  # 思源电气 roe 8.35 pe 3.14 pb 2.66 dividend 1.0 0.58%  operation 2 discount 3.18
            "002392",  # 北京利尔 roe 8.35 pe 6.64 pb 1.26 dividend 0.28 0.72%  operation 6 discount 1.51
            "000830",  # 鲁西化工 roe 8.34 pe 6.47 pb 1.29 dividend 5.0 5.48%  operation 2 discount 1.55
            "600066",  # 宇通客车 roe 8.33 pe 4.07 pb 2.05 dividend 5.0 3.4%  operation 2 discount 2.46
            "000631",  # 顺发恒业 roe 8.33 pe 8.17 pb 1.02 dividend 2.0 7.41%  operation 2 discount 1.22
            "002273",  # 水晶光电 roe 8.33 pe 1.93 pb 4.31 dividend 1.0 0.65%  operation 2 discount 5.17
            "300384",  # 三联虹普 roe 8.32 pe 2.48 pb 3.35 dividend 0.4 0.21%  operation 6 discount 4.03
            "002493",  # 荣盛石化 roe 8.31 pe 2.55 pb 3.26 dividend 1.0 0.87%  operation 2 discount 3.92
            "601139",  # 深圳燃气 roe 8.3 pe 4.91 pb 1.69 dividend 1.5 2.31%  operation 2 discount 2.04
            "601168",  # 西部矿业 roe 8.3 pe 5.5 pb 1.51 dividend 1.0 1.62%  operation 2 discount 1.82
            "000540",  # 中天金融 roe 8.3 pe 5.9 pb 1.41 dividend 0.501871 1.38%  operation 0 discount 1.69
            "000900",  # 现代投资 roe 8.29 pe 13.24 pb 0.63 dividend 1.5 3.67%  operation 2 discount 0.76
            "000411",  # 英特集团 roe 8.28 pe 3.95 pb 2.09 dividend 1.3 1.04%  operation 2 discount 2.53
            "300349",  # 金卡智能 roe 8.28 pe 4.33 pb 1.91 dividend 5.0 3.13%  operation 6 discount 2.31
            "002107",  # 沃华医药 roe 8.27 pe 1.2 pb 6.91 dividend 0.5 0.42%  operation 2 discount 8.36
            "600483",  # 福能股份 roe 8.26 pe 7.21 pb 1.15 dividend 2.1 2.39%  operation 0 discount 1.39
            "000756",  # 新华制药 roe 8.25 pe 3.96 pb 2.08 dividend 1.0 1.03%  operation 6 discount 2.53
            "300017",  # 网宿科技 roe 8.23 pe 3.42 pb 2.4 dividend 0.301004 0.32%  operation 2 discount 2.92
            "000811",  # 冰轮环境 roe 8.22 pe 5.06 pb 1.62 dividend 0.5 0.64%  operation 2 discount 1.98
            "002097",  # 山河智能 roe 8.21 pe 5.69 pb 1.44 dividend 1.0 1.45%  operation 6 discount 1.76
            "002598",  # 山东章鼓 roe 8.21 pe 3.49 pb 2.35 dividend 2.0 3.13%  operation 6 discount 2.86
            "600113",  # 浙江东日 roe 8.2 pe 4.37 pb 1.87 dividend 0.4 0.61%  operation 2 discount 2.29
            "600258",  # 首旅酒店 roe 8.2 pe 4.47 pb 1.83 dividend 1.1 0.68%  operation 2 discount 2.24
            "603686",  # 龙马环卫 roe 8.2 pe 3.16 pb 2.6 dividend 2.65 1.75%  operation 2 discount 3.17
            "002214",  # 大立科技 roe 8.2 pe 0.81 pb 10.08 dividend 0.3 0.12%  operation 2 discount 12.29
            "000559",  # 万向钱潮 roe 8.18 pe 2.68 pb 3.05 dividend 2.0 3.55%  operation 2 discount 3.73
            "000715",  # 中兴商业 roe 8.18 pe 4.94 pb 1.66 dividend 0.8 1.39%  operation 2 discount 2.03
            "600866",  # 星湖科技 roe 8.17 pe 2.74 pb 2.99 dividend 1.5 2.49%  operation 2 discount 3.66
            "601992",  # 金隅集团 roe 8.15 pe 9.86 pb 0.83 dividend 0.55 1.56%  operation 0 discount 1.01
            "600415",  # 小商品城 roe 8.12 pe 5.33 pb 1.52 dividend 0.6 1.7%  operation 0 discount 1.87
            "600420",  # 现代制药 roe 8.12 pe 5.7 pb 1.43 dividend 1.0 1.02%  operation 2 discount 1.75
            "001696",  # 宗申动力 roe 8.11 pe 5.25 pb 1.54 dividend 2.3 4.09%  operation 2 discount 1.9
            "600597",  # 光明乳业 roe 8.09 pe 3.31 pb 2.44 dividend 1.0 0.91%  operation 2 discount 3.02
            "300052",  # 中青宝 roe 8.08 pe 1.79 pb 4.52 dividend 0.2 0.14%  operation 2 discount 5.6
            "601699",  # 潞安环能 roe 8.07 pe 11.43 pb 0.71 dividend 2.68 4.34%  operation 2 discount 0.88
            "300046",  # 台基股份 roe 8.05 pe 1.76 pb 4.57 dividend 3.0 1.55%  operation 2 discount 5.68
            "600287",  # 江苏舜天 roe 8.03 pe 6.28 pb 1.28 dividend 0.8 1.27%  operation 2 discount 1.59
            "000950",  # 重药控股 roe 8.03 pe 6.3 pb 1.28 dividend 1.5 2.53%  operation 2 discount 1.59
            "300259",  # 新天科技 roe 8.03 pe 2.38 pb 3.37 dividend 0.1 0.17%  operation 2 discount 4.2
            "600057",  # 厦门象屿 roe 8.01 pe 8.07 pb 0.99 dividend 2.4 5.05%  operation 6 discount 1.24
            "300138",  # 晨光生物 roe 8.01 pe 3.53 pb 2.27 dividend 0.8 0.98%  operation 6 discount 2.83
            "300298",  # 三诺生物 roe 8.01 pe 2.51 pb 3.19 dividend 3.0 2.0%  operation 2 discount 3.98
            "002391",  # 长青股份 roe 8.0 pe 4.66 pb 1.72 dividend 3.0 2.9%  operation 6 discount 2.15
            "601238",  # 广汽集团 roe 7.99 pe 5.31 pb 1.5 dividend 3.3 2.83%  operation 2 discount 1.88
            "002248",  # 华东数控 roe 7.99 pe 0.35 pb 23.01 dividend 0.5 0.59%  operation 2 discount 28.8
            "000919",  # 金陵药业 roe 7.97 pe 6.07 pb 1.31 dividend 1.7 2.2%  operation 2 discount 1.65
            "000799",  # 酒鬼酒 roe 7.95 pe 1.64 pb 4.85 dividend 1.5 0.43%  operation 6 discount 6.1
            "300203",  # 聚光科技 roe 7.95 pe 4.85 pb 1.64 dividend 5.0 3.28%  operation 6 discount 2.06
            "603688",  # 石英股份 roe 7.93 pe 1.24 pb 6.42 dividend 1.3 0.48%  operation 2 discount 8.09
            "300398",  # 飞凯材料 roe 7.93 pe 1.72 pb 4.61 dividend 1.0 0.48%  operation 6 discount 5.81
            "600965",  # 福成股份 roe 7.92 pe 2.52 pb 3.15 dividend 1.5 1.93%  operation 2 discount 3.97
            "600295",  # 鄂尔多斯 roe 7.88 pe 8.25 pb 0.95 dividend 1.5 1.81%  operation 6 discount 1.21
            "002452",  # 长高集团 roe 7.87 pe 2.88 pb 2.74 dividend 0.3 0.48%  operation 2 discount 3.48
            "300037",  # 新宙邦 roe 7.87 pe 1.6 pb 4.91 dividend 1.7 0.43%  operation 2 discount 6.24
            "600479",  # 千金药业 roe 7.86 pe 4.18 pb 1.88 dividend 4.0 4.35%  operation 6 discount 2.39
            "600337",  # 美克家居 roe 7.84 pe 4.56 pb 1.72 dividend 2.0 4.56%  operation 6 discount 2.19
            "600629",  # 华建集团 roe 7.84 pe 4.98 pb 1.58 dividend 1.8 2.13%  operation 6 discount 2.01
            "002065",  # 东华软件 roe 7.84 pe 1.51 pb 5.19 dividend 1.0 0.62%  operation 2 discount 6.62
            "300063",  # 天龙集团 roe 7.84 pe 1.92 pb 4.09 dividend 0.5 0.85%  operation 2 discount 5.22
            "600182",  # S佳通 roe 7.83 pe 1.51 pb 5.17 dividend 0.8 0.55%  operation 2 discount 6.61
            "603788",  # 宁波高发 roe 7.83 pe 3.4 pb 2.31 dividend 6.0 3.25%  operation 2 discount 2.94
            "300174",  # 元力股份 roe 7.82 pe 1.39 pb 5.61 dividend 0.5 0.32%  operation 2 discount 7.17
            "002672",  # 东江环保 roe 7.81 pe 3.52 pb 2.22 dividend 1.4 1.31%  operation 2 discount 2.84
            "600081",  # 东风科技 roe 7.8 pe 2.8 pb 2.79 dividend 1.42 1.18%  operation 2 discount 3.58
            "600351",  # 亚宝药业 roe 7.8 pe 5.18 pb 1.51 dividend 2.5 4.4%  operation 6 discount 1.93
            "002643",  # 万润股份 roe 7.8 pe 2.25 pb 3.46 dividend 1.76 0.98%  operation 2 discount 4.44
            "300082",  # 奥克股份 roe 7.8 pe 4.85 pb 1.61 dividend 3.35 4.56%  operation 6 discount 2.06
            "300342",  # 天银机电 roe 7.8 pe 1.12 pb 6.95 dividend 1.5 0.68%  operation 2 discount 8.9
            "600461",  # 洪城水业 roe 7.79 pe 5.82 pb 1.34 dividend 1.7 2.67%  operation 6 discount 1.72
            "002645",  # 华宏科技 roe 7.77 pe 2.97 pb 2.62 dividend 1.2 1.1%  operation 6 discount 3.37
            "600510",  # 黑牡丹 roe 7.76 pe 7.54 pb 1.03 dividend 1.95 2.4%  operation 2 discount 1.33
            "300253",  # 卫宁健康 roe 7.75 pe 0.66 pb 11.81 dividend 0.199806 0.08%  operation 2 discount 15.24
            "002649",  # 博彦科技 roe 7.74 pe 3.52 pb 2.2 dividend 0.86 0.78%  operation 6 discount 2.84
            "601117",  # 中国化学 roe 7.73 pe 6.75 pb 1.15 dividend 1.18 1.61%  operation 2 discount 1.48
            "002034",  # 旺能环境 roe 7.73 pe 4.68 pb 1.65 dividend 1.0 0.63%  operation 0 discount 2.14
            "600390",  # 五矿资本 roe 7.72 pe 7.25 pb 1.06 dividend 1.81 2.22%  operation 0 discount 1.38
            "002327",  # 富安娜 roe 7.72 pe 4.11 pb 1.88 dividend 5.0 7.1%  operation 2 discount 2.43
            "002401",  # 中远海科 roe 7.72 pe 2.0 pb 3.85 dividend 0.5 0.42%  operation 6 discount 4.99
            "002532",  # 新界泵业 roe 7.72 pe 3.28 pb 2.35 dividend 2.0 3.1%  operation 2 discount 3.04
            "300376",  # 易事特 roe 7.72 pe 3.03 pb 2.55 dividend 0.25 0.44%  operation 2 discount 3.3
            "601866",  # 中远海发 roe 7.71 pe 4.99 pb 1.55 dividend 0.33 1.48%  operation 0 discount 2.0
            "002075",  # 沙钢股份 roe 7.71 pe 1.77 pb 4.34 dividend 0.3 0.32%  operation 2 discount 5.64
            "300007",  # 汉威科技 roe 7.7 pe 2.32 pb 3.33 dividend 0.15 0.08%  operation 0 discount 4.32
            "000576",  # 广东甘化 roe 7.68 pe 2.69 pb 2.86 dividend 0.0 0.0%  operation 0 discount 3.72
            "300388",  # 国祯环保 roe 7.68 pe 2.99 pb 2.57 dividend 1.17785 0.93%  operation 4 discount 3.34
            "600256",  # 广汇能源 roe 7.67 pe 5.88 pb 1.3 dividend 1.0 3.34%  operation 0 discount 1.7
            "300395",  # 菲利华 roe 7.67 pe 1.69 pb 4.53 dividend 2.0 0.82%  operation 6 discount 5.9
            "000573",  # 粤宏远Ａ roe 7.66 pe 6.98 pb 1.1 dividend 0.6 1.97%  operation 2 discount 1.43
            "600545",  # 卓郎智能 roe 7.65 pe 2.87 pb 2.67 dividend 1.293 1.91%  operation 2 discount 3.49
            "002514",  # 宝馨科技 roe 7.65 pe 2.67 pb 2.87 dividend 0.0 0.0%  operation 6 discount 3.75
            "600079",  # 人福医药 roe 7.64 pe 3.79 pb 2.01 dividend 1.6 1.1%  operation 2 discount 2.64
            "002258",  # 利尔化学 roe 7.61 pe 2.99 pb 2.55 dividend 2.0 1.34%  operation 2 discount 3.35
            "000988",  # 华工科技 roe 7.6 pe 1.94 pb 3.93 dividend 0.3 0.13%  operation 2 discount 5.17
            "002315",  # 焦点科技 roe 7.6 pe 2.36 pb 3.22 dividend 7.5 2.76%  operation 2 discount 4.24
            "600611",  # 大众交通 roe 7.59 pe 7.67 pb 0.99 dividend 1.2 3.14%  operation 2 discount 1.3
            "600406",  # 国电南瑞 roe 7.58 pe 2.18 pb 3.49 dividend 3.7 1.73%  operation 2 discount 4.6
            "600015",  # 华夏银行 roe 7.57 pe 13.84 pb 0.55 dividend 1.74 2.43%  operation 6 discount 0.72
            "600248",  # 延长化建 roe 7.57 pe 5.26 pb 1.44 dividend 1.0 2.22%  operation 6 discount 1.9
            "600713",  # 南京医药 roe 7.57 pe 5.85 pb 1.29 dividend 1.0 2.07%  operation 6 discount 1.71
            "002100",  # 天康生物 roe 7.57 pe 1.99 pb 3.8 dividend 1.0 0.7%  operation 2 discount 5.02
            "600528",  # 中铁工业 roe 7.56 pe 5.42 pb 1.39 dividend 1.15 1.09%  operation 2 discount 1.84
            "600202",  # 哈空调 roe 7.55 pe 2.78 pb 2.71 dividend 0.18 0.38%  operation 6 discount 3.59
            "000791",  # 甘肃电投 roe 7.55 pe 10.41 pb 0.73 dividend 1.5 4.35%  operation 4 discount 0.96
            "002048",  # 宁波华翔 roe 7.55 pe 4.41 pb 1.71 dividend 1.5 0.62%  operation 2 discount 2.27
            "600917",  # 重庆燃气 roe 7.54 pe 2.94 pb 2.57 dividend 0.8 1.18%  operation 2 discount 3.4
            "601000",  # 唐山港 roe 7.54 pe 8.7 pb 0.87 dividend 0.7 2.88%  operation 6 discount 1.15
            "603099",  # 长白山 roe 7.54 pe 3.56 pb 2.12 dividend 0.26 0.3%  operation 2 discount 2.81
            "603558",  # 健盛集团 roe 7.54 pe 4.96 pb 1.52 dividend 0.5 0.45%  operation 2 discount 2.02
            "600380",  # 健康元 roe 7.52 pe 3.28 pb 2.29 dividend 1.6 1.31%  operation 2 discount 3.05
            "000582",  # 北部湾港 roe 7.52 pe 5.12 pb 1.47 dividend 1.1421 1.32%  operation 6 discount 1.95
            "300383",  # 光环新网 roe 7.52 pe 1.44 pb 5.24 dividend 0.2 0.07%  operation 6 discount 6.97
            "600859",  # 王府井 roe 7.51 pe 8.4 pb 0.89 dividend 4.7 3.62%  operation 2 discount 1.19
            "000019",  # 深粮控股 roe 7.51 pe 4.46 pb 1.68 dividend 1.0 1.56%  operation 2 discount 2.24
            "601933",  # 永辉超市 roe 7.5 pe 1.63 pb 4.62 dividend 1.1 1.11%  operation 2 discount 6.15
            "000975",  # 银泰黄金 roe 7.48 pe 2.17 pb 3.44 dividend 2.0 1.31%  operation 6 discount 4.6
            "002736",  # 国信证券 roe 7.48 pe 3.61 pb 2.08 dividend 1.2 0.95%  operation 2 discount 2.77
            "300026",  # 红日药业 roe 7.48 pe 3.69 pb 2.03 dividend 0.2 0.43%  operation 2 discount 2.71
            "000888",  # 峨眉山Ａ roe 7.47 pe 5.7 pb 1.31 dividend 1.0 1.61%  operation 2 discount 1.75
            "002057",  # 中钢天源 roe 7.47 pe 2.25 pb 3.33 dividend 1.0 1.24%  operation 2 discount 4.45
            "002062",  # 宏润建设 roe 7.47 pe 2.89 pb 2.58 dividend 0.5 0.68%  operation 2 discount 3.46
            "000534",  # 万泽股份 roe 7.46 pe 1.45 pb 5.14 dividend 0.5 0.51%  operation 2 discount 6.89
            "300035",  # 中科电气 roe 7.45 pe 2.2 pb 3.39 dividend 0.3 0.35%  operation 6 discount 4.54
            "601899",  # 紫金矿业 roe 7.44 pe 2.7 pb 2.75 dividend 1.0 2.28%  operation 2 discount 3.7
            "002394",  # 联发股份 roe 7.44 pe 7.24 pb 1.03 dividend 6.0 6.02%  operation 2 discount 1.38
            "002424",  # 贵州百灵 roe 7.44 pe 2.29 pb 3.25 dividend 0.8 0.85%  operation 6 discount 4.38
            "600785",  # 新华百货 roe 7.43 pe 5.07 pb 1.46 dividend 1.75 1.17%  operation 2 discount 1.97
            "002002",  # 鸿达兴业 roe 7.43 pe 4.06 pb 1.83 dividend 0.6 1.3%  operation 2 discount 2.46
            "000622",  # 恒立实业 roe 7.42 pe 0.73 pb 10.24 dividend 0.3 0.6%  operation 2 discount 13.79
            "002608",  # 江苏国信 roe 7.42 pe 7.55 pb 0.98 dividend 1.0 1.45%  operation 2 discount 1.32
            "300360",  # 炬华科技 roe 7.42 pe 2.96 pb 2.5 dividend 1.0 0.76%  operation 2 discount 3.37
            "600502",  # 安徽建工 roe 7.41 pe 7.09 pb 1.05 dividend 1.5 3.47%  operation 2 discount 1.41
            "600822",  # 上海物贸 roe 7.4 pe 0.99 pb 7.45 dividend 1.0 1.02%  operation 2 discount 10.07
            "002406",  # 远东传动 roe 7.4 pe 5.67 pb 1.3 dividend 0.5 0.83%  operation 6 discount 1.76
            "600737",  # 中粮糖业 roe 7.39 pe 3.09 pb 2.39 dividend 1.7 1.91%  operation 2 discount 3.23
            "000878",  # 云南铜业 roe 7.39 pe 3.16 pb 2.34 dividend 2.0 1.74%  operation 2 discount 3.17
            "002090",  # 金智科技 roe 7.39 pe 2.26 pb 3.27 dividend 0.8 0.76%  operation 2 discount 4.42
            "300230",  # 永利股份 roe 7.39 pe 4.45 pb 1.66 dividend 2.45 3.82%  operation 2 discount 2.25
            "603017",  # 中衡设计 roe 7.37 pe 4.45 pb 1.66 dividend 3.0 2.77%  operation 6 discount 2.25
            "002498",  # 汉缆股份 roe 7.37 pe 3.11 pb 2.37 dividend 0.36 1.03%  operation 2 discount 3.21
            "000869",  # 张 裕Ａ roe 7.36 pe 4.19 pb 1.76 dividend 6.0 2.36%  operation 2 discount 2.39
            "002687",  # 乔治白 roe 7.36 pe 3.71 pb 1.98 dividend 1.5 2.48%  operation 6 discount 2.69
            "000617",  # 中油资本 roe 7.34 pe 6.1 pb 1.2 dividend 2.41 2.2%  operation 0 discount 1.64
            "002008",  # 大族激光 roe 7.34 pe 1.48 pb 4.97 dividend 2.0 0.52%  operation 2 discount 6.77
            "300420",  # 五洋停车 roe 7.34 pe 2.31 pb 3.17 dividend 0.37 0.51%  operation 6 discount 4.32
            "601018",  # 宁波港 roe 7.33 pe 6.41 pb 1.14 dividend 0.93 2.67%  operation 6 discount 1.56
            "603088",  # 宁波精达 roe 7.32 pe 2.61 pb 2.8 dividend 3.2 3.42%  operation 6 discount 3.83
            "002195",  # 二三四五 roe 7.32 pe 3.89 pb 1.88 dividend 0.3 0.92%  operation 6 discount 2.57
            "600745",  # 闻泰科技 roe 7.31 pe 0.36 pb 20.28 dividend 0.2 0.02%  operation 2 discount 27.73
            "600705",  # 中航资本 roe 7.3 pe 5.17 pb 1.41 dividend 0.36 0.79%  operation 0 discount 1.93
            "601107",  # 四川成渝 roe 7.3 pe 9.77 pb 0.75 dividend 1.0 2.67%  operation 0 discount 1.02
            "601369",  # 陕鼓动力 roe 7.3 pe 4.64 pb 1.57 dividend 2.0 3.19%  operation 6 discount 2.16
            "002051",  # 中工国际 roe 7.3 pe 6.54 pb 1.12 dividend 3.0 3.21%  operation 2 discount 1.53
            "002225",  # 濮耐股份 roe 7.3 pe 4.66 pb 1.57 dividend 0.7 1.66%  operation 6 discount 2.15
            "600735",  # 新华锦 roe 7.29 pe 2.91 pb 2.51 dividend 0.61 0.97%  operation 2 discount 3.44
            "600760",  # 中航沈飞 roe 7.29 pe 1.53 pb 4.76 dividend 0.5 0.17%  operation 2 discount 6.53
            "002033",  # 丽江旅游 roe 7.28 pe 5.88 pb 1.24 dividend 1.5 2.62%  operation 2 discount 1.7
            "002603",  # 以岭药业 roe 7.28 pe 3.0 pb 2.43 dividend 1.0 0.63%  operation 2 discount 3.34
            "600117",  # 西宁特钢 roe 7.27 pe 2.44 pb 2.97 dividend 0.13 0.38%  operation 2 discount 4.09
            "000520",  # 长航凤凰 roe 7.27 pe 0.74 pb 9.84 dividend 0.28 0.71%  operation 2 discount 13.53
            "600742",  # 一汽富维 roe 7.25 pe 4.92 pb 1.48 dividend 6.0 4.2%  operation 2 discount 2.03
            "300255",  # 常山药业 roe 7.24 pe 3.46 pb 2.09 dividend 0.28 0.47%  operation 2 discount 2.89
            "603969",  # 银龙股份 roe 7.23 pe 3.68 pb 1.96 dividend 1.0 2.41%  operation 2 discount 2.72
            "002617",  # 露笑科技 roe 7.23 pe 2.38 pb 3.04 dividend 0.2 0.32%  operation 0 discount 4.21
            "300119",  # 瑞普生物 roe 7.23 pe 2.18 pb 3.32 dividend 1.53061 0.93%  operation 2 discount 4.59
            "600251",  # 冠农股份 roe 7.22 pe 3.18 pb 2.27 dividend 0.13 0.21%  operation 2 discount 3.14
            "601111",  # 中国国航 roe 7.21 pe 6.04 pb 1.19 dividend 1.0328 1.34%  operation 4 discount 1.66
            "300058",  # 蓝色光标 roe 7.2 pe 3.41 pb 2.11 dividend 0.326884 0.44%  operation 2 discount 2.94
            "002429",  # 兆驰股份 roe 7.19 pe 2.7 pb 2.66 dividend 0.25 0.46%  operation 2 discount 3.7
            "600223",  # 鲁商发展 roe 7.18 pe 2.07 pb 3.46 dividend 0.5 0.56%  operation 2 discount 4.82
            "002541",  # 鸿路钢构 roe 7.17 pe 4.27 pb 1.68 dividend 0.85 0.56%  operation 6 discount 2.34
            "600771",  # 广誉远 roe 7.15 pe 2.38 pb 3.01 dividend 0.0 0.0%  operation 2 discount 4.2
            "000027",  # 深圳能源 roe 7.15 pe 7.63 pb 0.94 dividend 0.5 0.88%  operation 0 discount 1.31
            "600723",  # 首商股份 roe 7.14 pe 7.97 pb 0.9 dividend 1.7 3.0%  operation 2 discount 1.25
            "600522",  # 中天科技 roe 7.12 pe 5.04 pb 1.41 dividend 1.0 1.08%  operation 6 discount 1.99
            "600588",  # 用友网络 roe 7.12 pe 0.38 pb 18.55 dividend 2.5 0.54%  operation 6 discount 26.07
            "600596",  # 新安股份 roe 7.12 pe 5.96 pb 1.19 dividend 5.3 5.46%  operation 2 discount 1.68
            "000822",  # 山东海化 roe 7.11 pe 6.51 pb 1.09 dividend 2.0 4.76%  operation 2 discount 1.54
            "601222",  # 林洋能源 roe 7.1 pe 6.52 pb 1.09 dividend 1.75 2.92%  operation 0 discount 1.53
            "300172",  # 中电环保 roe 7.1 pe 3.59 pb 1.98 dividend 0.5 0.92%  operation 6 discount 2.79
            "000006",  # 深振业Ａ roe 7.08 pe 6.76 pb 1.05 dividend 1.95 3.94%  operation 0 discount 1.48
            "600753",  # 东方银星 roe 7.06 pe 0.59 pb 11.92 dividend 0.5 0.27%  operation 2 discount 16.88
            "601101",  # 昊华能源 roe 7.06 pe 11.29 pb 0.62 dividend 1.9 4.28%  operation 0 discount 0.89
            "600999",  # 招商证券 roe 7.05 pe 3.8 pb 1.85 dividend 2.64 1.39%  operation 2 discount 2.63
            "000639",  # 西王食品 roe 7.03 pe 5.55 pb 1.27 dividend 0.8 1.44%  operation 2 discount 1.8
            "002412",  # 汉森制药 roe 7.02 pe 2.38 pb 2.95 dividend 0.0 0.0%  operation 2 discount 4.2
            "600647",  # 同达创业 roe 7.01 pe 1.08 pb 6.5 dividend 0.5 0.37%  operation 2 discount 9.28
            "002654",  # 万润科技 roe 7.01 pe 3.28 pb 2.13 dividend 0.5 0.98%  operation 2 discount 3.05
            "300416",  # 苏试试验 roe 7.01 pe 1.13 pb 6.19 dividend 1.0 0.28%  operation 6 discount 8.83
            "600665",  # 天地源 roe 7.0 pe 8.1 pb 0.86 dividend 1.46 4.16%  operation 0 discount 1.23
            "300066",  # 三川智慧 roe 7.0 pe 2.07 pb 3.39 dividend 0.2 0.36%  operation 2 discount 4.84
            "000887",  # 中鼎股份 roe 6.99 pe 5.08 pb 1.38 dividend 2.0 2.07%  operation 2 discount 1.97
            "600565",  # 迪马股份 roe 6.97 pe 7.28 pb 0.96 dividend 2.8 8.72%  operation 0 discount 1.37
            "000681",  # 视觉中国 roe 6.97 pe 1.73 pb 4.03 dividend 0.46 0.26%  operation 6 discount 5.79
            "600011",  # 华能国际 roe 6.96 pe 7.02 pb 0.99 dividend 1.0 2.04%  operation 4 discount 1.42
            "600208",  # 新湖中宝 roe 6.95 pe 8.23 pb 0.84 dividend 0.59 1.7%  operation 0 discount 1.21
            "601669",  # 中国电建 roe 6.95 pe 8.84 pb 0.79 dividend 0.9782 2.27%  operation 4 discount 1.13
            "600648",  # 外高桥 roe 6.94 pe 4.1 pb 1.69 dividend 2.2 1.38%  operation 2 discount 2.44
            "002130",  # 沃尔核材 roe 6.94 pe 2.84 pb 2.44 dividend 0.2 0.36%  operation 2 discount 3.52
            "002126",  # 银轮股份 roe 6.93 pe 2.85 pb 2.44 dividend 0.5 0.44%  operation 6 discount 3.51
            "000987",  # 越秀金控 roe 6.92 pe 4.75 pb 1.46 dividend 0.9 1.0%  operation 2 discount 2.11
            "002443",  # 金洲管道 roe 6.92 pe 4.85 pb 1.43 dividend 2.0 3.13%  operation 6 discount 2.06
            "002373",  # 千方科技 roe 6.91 pe 1.55 pb 4.46 dividend 0.55 0.21%  operation 6 discount 6.47
            "300214",  # 日科化学 roe 6.91 pe 3.19 pb 2.17 dividend 0.5 0.58%  operation 2 discount 3.13
            "600865",  # 百大集团 roe 6.9 pe 5.33 pb 1.29 dividend 2.0 3.19%  operation 2 discount 1.87
            "601098",  # 中南传媒 roe 6.9 pe 4.48 pb 1.54 dividend 6.1 5.35%  operation 2 discount 2.23
            "002745",  # 木林森 roe 6.9 pe 4.23 pb 1.63 dividend 1.3 1.02%  operation 6 discount 2.36
            "002084",  # 海鸥住工 roe 6.89 pe 3.44 pb 2.0 dividend 1.0 1.61%  operation 2 discount 2.91
            "002367",  # 康力电梯 roe 6.89 pe 2.86 pb 2.4 dividend 5.3 6.01%  operation 2 discount 3.49
            "002408",  # 齐翔腾达 roe 6.89 pe 4.36 pb 1.58 dividend 0.90028 1.33%  operation 2 discount 2.29
            "600123",  # 兰花科创 roe 6.88 pe 10.88 pb 0.63 dividend 3.0 5.04%  operation 2 discount 0.92
            "002138",  # 顺络电子 roe 6.88 pe 1.44 pb 4.79 dividend 2.0 0.78%  operation 2 discount 6.96
            "600317",  # 营口港 roe 6.87 pe 5.6 pb 1.23 dividend 0.47 2.03%  operation 6 discount 1.79
            "601919",  # 中远海控 roe 6.87 pe 4.04 pb 1.7 dividend 0.9 2.11%  operation 0 discount 2.47
            "600160",  # 巨化股份 roe 6.86 pe 3.93 pb 1.74 dividend 1.5 1.82%  operation 2 discount 2.54
            "002683",  # 宏大爆破 roe 6.85 pe 0.99 pb 6.91 dividend 1.5 0.48%  operation 2 discount 10.09
            "002561",  # 徐家汇 roe 6.84 pe 4.74 pb 1.44 dividend 3.6 4.65%  operation 2 discount 2.11
            "603306",  # 华懋科技 roe 6.83 pe 3.04 pb 2.25 dividend 5.0 2.96%  operation 2 discount 3.29
            "002194",  # 武汉凡谷 roe 6.83 pe 0.78 pb 8.77 dividend 0.5 0.19%  operation 2 discount 12.84
            "002404",  # 嘉欣丝绸 roe 6.83 pe 3.05 pb 2.24 dividend 2.0 2.98%  operation 6 discount 3.28
            "002422",  # 科伦药业 roe 6.82 pe 2.67 pb 2.56 dividend 2.096 0.88%  operation 2 discount 3.75
            "300385",  # 雪浪环境 roe 6.81 pe 2.72 pb 2.5 dividend 0.7 0.48%  operation 2 discount 3.68
            "000026",  # 飞亚达 roe 6.8 pe 4.1 pb 1.66 dividend 2.00813 2.04%  operation 6 discount 2.44
            "002047",  # 宝鹰股份 roe 6.8 pe 4.17 pb 1.63 dividend 0.25 0.49%  operation 2 discount 2.4
            "600107",  # 美尔雅 roe 6.79 pe 1.83 pb 3.72 dividend 1.0 1.59%  operation 2 discount 5.47
            "600667",  # 太极实业 roe 6.79 pe 1.67 pb 4.05 dividend 1.37 1.07%  operation 6 discount 5.97
            "000668",  # 荣丰控股 roe 6.79 pe 3.58 pb 1.89 dividend 0.4 0.32%  operation 2 discount 2.79
            "002438",  # 江苏神通 roe 6.79 pe 3.21 pb 2.11 dividend 0.25 0.3%  operation 6 discount 3.11
            "600731",  # 湖南海利 roe 6.78 pe 3.01 pb 2.25 dividend 0.2 0.27%  operation 2 discount 3.32
            "000655",  # 金岭矿业 roe 6.77 pe 5.05 pb 1.34 dividend 1.0 1.73%  operation 2 discount 1.98
            "002228",  # 合兴包装 roe 6.77 pe 4.26 pb 1.59 dividend 0.5 1.28%  operation 6 discount 2.35
            "600475",  # 华光股份 roe 6.76 pe 5.99 pb 1.13 dividend 2.3 2.29%  operation 6 discount 1.67
            "601311",  # 骆驼股份 roe 6.75 pe 4.83 pb 1.4 dividend 1.5 1.49%  operation 2 discount 2.07
            "000059",  # 华锦股份 roe 6.73 pe 9.16 pb 0.73 dividend 2.5 3.97%  operation 2 discount 1.09
            "002437",  # 誉衡药业 roe 6.72 pe 5.01 pb 1.34 dividend 0.12 0.43%  operation 2 discount 2.0
            "300059",  # 东方财富 roe 6.71 pe 1.08 pb 6.2 dividend 0.2 0.1%  operation 2 discount 9.23
            "600508",  # 上海能源 roe 6.7 pe 10.54 pb 0.64 dividend 2.8 3.19%  operation 2 discount 0.95
            "300274",  # 阳光电源 roe 6.69 pe 3.11 pb 2.15 dividend 0.600294 0.49%  operation 2 discount 3.21
            "002376",  # 新北洋 roe 6.68 pe 2.66 pb 2.51 dividend 2.0 1.62%  operation 2 discount 3.76
            "300365",  # 恒华科技 roe 6.68 pe 1.4 pb 4.77 dividend 0.7 0.46%  operation 2 discount 7.14
            "000757",  # 浩物股份 roe 6.66 pe 3.53 pb 1.88 dividend 0.0 0.0%  operation 2 discount 2.83
            "300413",  # 芒果超媒 roe 6.66 pe 1.17 pb 5.72 dividend 0.0 0.0%  operation 2 discount 8.58
            "002254",  # 泰和新材 roe 6.63 pe 1.74 pb 3.81 dividend 0.5 0.35%  operation 2 discount 5.75
            "300092",  # 科新机电 roe 6.63 pe 2.28 pb 2.91 dividend 0.15 0.2%  operation 2 discount 4.39
            "300335",  # 迪森股份 roe 6.63 pe 4.63 pb 1.43 dividend 2.0 3.7%  operation 2 discount 2.16
            "002414",  # 高德红外 roe 6.62 pe 0.53 pb 12.58 dividend 0.3 0.06%  operation 2 discount 19.0
            "002573",  # 清新环境 roe 6.62 pe 4.65 pb 1.43 dividend 1.0 1.56%  operation 2 discount 2.15
            "600127",  # 金健米业 roe 6.61 pe 1.59 pb 4.16 dividend 0.0 0.0%  operation 2 discount 6.29
            "300292",  # 吴通控股 roe 6.6 pe 1.44 pb 4.6 dividend 0.5 0.86%  operation 2 discount 6.97
            "600379",  # 宝光股份 roe 6.59 pe 1.85 pb 3.57 dividend 0.65 1.11%  operation 2 discount 5.42
            "000676",  # 智度股份 roe 6.59 pe 3.14 pb 2.1 dividend 0.3 0.29%  operation 2 discount 3.18
            "002717",  # 岭南股份 roe 6.59 pe 3.6 pb 1.83 dividend 0.8 1.45%  operation 2 discount 2.77
            "600125",  # 铁龙物流 roe 6.58 pe 5.48 pb 1.2 dividend 1.2 2.21%  operation 2 discount 1.82
            "002591",  # 恒大高新 roe 6.55 pe 2.86 pb 2.29 dividend 3.00263 3.16%  operation 6 discount 3.5
            "600439",  # 瑞贝卡 roe 6.53 pe 4.94 pb 1.32 dividend 0.5 1.52%  operation 2 discount 2.03
            "600998",  # 九州通 roe 6.48 pe 3.04 pb 2.13 dividend 1.0 0.56%  operation 2 discount 3.29
            "000560",  # 我爱我家 roe 6.48 pe 7.16 pb 0.91 dividend 0.7 1.84%  operation 2 discount 1.4
            "002621",  # 美吉姆 roe 6.47 pe 1.26 pb 5.16 dividend 0.200017 0.18%  operation 2 discount 7.97
            "603100",  # 川仪股份 roe 6.46 pe 3.86 pb 1.67 dividend 2.0 2.02%  operation 2 discount 2.59
            "601188",  # 龙江交通 roe 6.45 pe 7.59 pb 0.85 dividend 0.69 2.42%  operation 2 discount 1.32
            "000928",  # 中钢国际 roe 6.45 pe 4.69 pb 1.38 dividend 1.2 2.34%  operation 2 discount 2.13
            "600115",  # 东方航空 roe 6.43 pe 5.65 pb 1.14 dividend 0.51 1.08%  operation 0 discount 1.77
            "002042",  # 华孚时尚 roe 6.43 pe 3.92 pb 1.64 dividend 3.52452 5.15%  operation 2 discount 2.55
            "002526",  # 山东矿机 roe 6.42 pe 3.73 pb 1.72 dividend 0.0 0.0%  operation 6 discount 2.68
            "002519",  # 银河电子 roe 6.4 pe 3.12 pb 2.06 dividend 1.5 3.23%  operation 2 discount 3.21
            "600185",  # 格力地产 roe 6.39 pe 4.96 pb 1.29 dividend 3.0 6.11%  operation 0 discount 2.02
            "601666",  # 平煤股份 roe 6.38 pe 8.26 pb 0.77 dividend 0.26 0.57%  operation 2 discount 1.21
            "000636",  # 风华高科 roe 6.38 pe 1.66 pb 3.85 dividend 3.0 1.26%  operation 6 discount 6.04
            "000850",  # 华茂股份 roe 6.38 pe 5.89 pb 1.08 dividend 0.5 1.0%  operation 6 discount 1.7
            "000967",  # 盈峰环境 roe 6.38 pe 4.41 pb 1.45 dividend 1.00036 1.45%  operation 6 discount 2.27
            "002171",  # 楚江新材 roe 6.38 pe 2.98 pb 2.14 dividend 1.02015 1.14%  operation 2 discount 3.36
            "603006",  # 联明股份 roe 6.37 pe 3.06 pb 2.08 dividend 2.1 1.75%  operation 2 discount 3.27
            "000683",  # 远兴能源 roe 6.37 pe 7.38 pb 0.86 dividend 0.2 0.9%  operation 2 discount 1.35
            "000777",  # 中核科技 roe 6.37 pe 1.82 pb 3.5 dividend 0.9 0.69%  operation 2 discount 5.49
            "600792",  # 云煤能源 roe 6.36 pe 6.41 pb 0.99 dividend 0.0 0.0%  operation 2 discount 1.56
            "601965",  # 中国汽研 roe 6.36 pe 3.03 pb 2.1 dividend 2.5 2.56%  operation 2 discount 3.3
            "603128",  # 华贸物流 roe 6.36 pe 4.25 pb 1.5 dividend 0.98 1.65%  operation 2 discount 2.35
            "601766",  # 中国中车 roe 6.35 pe 4.4 pb 1.44 dividend 1.5 2.25%  operation 2 discount 2.27
            "603998",  # 方盛制药 roe 6.35 pe 2.19 pb 2.91 dividend 0.3 0.4%  operation 2 discount 4.58
            "300073",  # 当升科技 roe 6.35 pe 1.73 pb 3.66 dividend 1.4 0.48%  operation 2 discount 5.77
            "600061",  # 国投资本 roe 6.34 pe 4.13 pb 1.54 dividend 0.81 0.58%  operation 0 discount 2.42
            "603333",  # 尚纬股份 roe 6.34 pe 2.32 pb 2.73 dividend 0.34 0.43%  operation 2 discount 4.31
            "000155",  # 川能动力 roe 6.33 pe 3.83 pb 1.65 dividend 0.5 1.09%  operation 0 discount 2.61
            "002614",  # 奥佳华 roe 6.33 pe 2.74 pb 2.31 dividend 1.0 0.75%  operation 6 discount 3.65
            "300260",  # 新莱应材 roe 6.33 pe 1.51 pb 4.19 dividend 1.0 0.64%  operation 6 discount 6.61
            "600090",  # 同济堂 roe 6.32 pe 6.44 pb 0.98 dividend 2.0 4.54%  operation 6 discount 1.55
            "002010",  # 传化智联 roe 6.32 pe 3.61 pb 1.75 dividend 1.0 1.42%  operation 2 discount 2.77
            "601199",  # 江南水务 roe 6.31 pe 4.88 pb 1.29 dividend 0.7 1.78%  operation 0 discount 2.05
            "000920",  # 南方汇通 roe 6.31 pe 2.52 pb 2.51 dividend 0.3 0.46%  operation 2 discount 3.97
            "300036",  # 超图软件 roe 6.31 pe 1.06 pb 5.93 dividend 0.75 0.28%  operation 2 discount 9.4
            "600513",  # 联环药业 roe 6.3 pe 1.41 pb 4.45 dividend 0.78 0.51%  operation 6 discount 7.07
            "600853",  # 龙建股份 roe 6.29 pe 2.69 pb 2.34 dividend 0.2 0.43%  operation 2 discount 3.72
            "002061",  # 浙江交科 roe 6.28 pe 5.82 pb 1.08 dividend 1.2 2.06%  operation 2 discount 1.72
            "600116",  # 三峡水利 roe 6.27 pe 2.0 pb 3.13 dividend 1.0 1.04%  operation 2 discount 4.99
            "000488",  # 晨鸣纸业 roe 6.27 pe 7.32 pb 0.86 dividend 2.4 4.78%  operation 2 discount 1.37
            "002675",  # 东诚药业 roe 6.27 pe 2.17 pb 2.89 dividend 0.48 0.3%  operation 6 discount 4.61
            "600029",  # 南方航空 roe 6.24 pe 5.52 pb 1.13 dividend 0.5 0.83%  operation 0 discount 1.81
            "600106",  # 重庆路桥 roe 6.24 pe 6.36 pb 0.98 dividend 0.67 2.23%  operation 0 discount 1.57
            "002133",  # 广宇集团 roe 6.24 pe 8.02 pb 0.78 dividend 0.8 2.35%  operation 2 discount 1.25
            "002553",  # 南方轴承 roe 6.24 pe 2.27 pb 2.74 dividend 2.0 3.64%  operation 2 discount 4.4
            "002416",  # 爱施德 roe 6.23 pe 3.38 pb 1.84 dividend 2.0 2.74%  operation 2 discount 2.96
            "600650",  # 锦江投资 roe 6.22 pe 4.03 pb 1.54 dividend 2.5 2.62%  operation 6 discount 2.48
            "600869",  # 智慧能源 roe 6.22 pe 2.85 pb 2.18 dividend 0.41 0.81%  operation 2 discount 3.5
            "002733",  # 雄韬股份 roe 6.22 pe 1.73 pb 3.59 dividend 1.5 0.59%  operation 2 discount 5.77
            "300235",  # 方直科技 roe 6.22 pe 1.08 pb 5.77 dividend 0.14157 0.06%  operation 2 discount 9.29
            "300295",  # 三六五网 roe 6.22 pe 2.84 pb 2.19 dividend 1.1 0.79%  operation 2 discount 3.53
            "600976",  # 健民集团 roe 6.21 pe 2.79 pb 2.23 dividend 2.0 1.16%  operation 2 discount 3.59
            "002451",  # 摩恩电气 roe 6.21 pe 1.08 pb 5.77 dividend 1.75 1.89%  operation 2 discount 9.29
            "600088",  # 中视传媒 roe 6.2 pe 1.27 pb 4.9 dividend 0.87 0.58%  operation 2 discount 7.9
            "000778",  # 新兴铸管 roe 6.2 pe 8.68 pb 0.71 dividend 2.0 5.31%  operation 2 discount 1.15
            "002125",  # 湘潭电化 roe 6.2 pe 1.52 pb 4.08 dividend 0.6 0.67%  operation 6 discount 6.57
            "002241",  # 歌尔股份 roe 6.19 pe 1.37 pb 4.52 dividend 1.0 0.45%  operation 2 discount 7.29
            "000591",  # 太阳能 roe 6.18 pe 7.06 pb 0.87 dividend 1.04 2.7%  operation 0 discount 1.42
            "002115",  # 三维通信 roe 6.17 pe 1.86 pb 3.32 dividend 1.0 0.87%  operation 6 discount 5.38
            "000032",  # 深桑达Ａ roe 6.16 pe 1.13 pb 5.45 dividend 0.8 0.43%  operation 2 discount 8.86
            "600777",  # 新潮能源 roe 6.14 pe 7.28 pb 0.84 dividend 0.0 0.0%  operation 0 discount 1.37
            "000776",  # 广发证券 roe 6.14 pe 4.77 pb 1.29 dividend 2.0 1.29%  operation 2 discount 2.1
            "600393",  # 粤泰股份 roe 6.13 pe 5.38 pb 1.14 dividend 1.4 4.95%  operation 2 discount 1.86
            "002620",  # 瑞和股份 roe 6.13 pe 6.09 pb 1.01 dividend 0.6 0.98%  operation 6 discount 1.64
            "600491",  # 龙元建设 roe 6.12 pe 5.12 pb 1.2 dividend 0.6 0.75%  operation 6 discount 1.95
            "300315",  # 掌趣科技 roe 6.12 pe 1.96 pb 3.12 dividend 0.1 0.16%  operation 2 discount 5.1
            "600695",  # 绿庭投资 roe 6.11 pe 0.68 pb 9.04 dividend 0.5 0.54%  operation 0 discount 14.8
            "002013",  # 中航机电 roe 6.11 pe 2.01 pb 3.04 dividend 0.3 0.38%  operation 2 discount 4.98
            "002238",  # 天威视讯 roe 6.11 pe 2.99 pb 2.05 dividend 5.0 5.75%  operation 2 discount 3.35
            "002226",  # 江南化工 roe 6.09 pe 5.34 pb 1.14 dividend 0.65 1.2%  operation 4 discount 1.87
            "000790",  # 泰合健康 roe 6.08 pe 1.55 pb 3.93 dividend 0.3 0.54%  operation 2 discount 6.47
            "300034",  # 钢研高纳 roe 6.08 pe 1.58 pb 3.84 dividend 1.2 0.7%  operation 2 discount 6.32
            "000931",  # 中 关 村 roe 6.07 pe 1.32 pb 4.58 dividend 1.0 0.98%  operation 2 discount 7.55
            "300373",  # 扬杰科技 roe 6.06 pe 1.11 pb 5.44 dividend 2.5571270000000004 0.91%  operation 2 discount 8.98
            "600308",  # 华泰股份 roe 6.05 pe 8.53 pb 0.71 dividend 1.85 3.81%  operation 2 discount 1.17
            "002730",  # 电光科技 roe 6.05 pe 2.1 pb 2.88 dividend 0.5 0.57%  operation 6 discount 4.76
            "300220",  # 金运激光 roe 6.05 pe 0.25 pb 24.03 dividend 0.06 0.01%  operation 2 discount 39.71
            "600063",  # 皖维高新 roe 6.04 pe 3.53 pb 1.71 dividend 0.25 0.56%  operation 2 discount 2.83
            "600498",  # 烽火通信 roe 6.04 pe 1.57 pb 3.84 dividend 3.4 1.01%  operation 6 discount 6.36
            "603118",  # 共进股份 roe 6.04 pe 2.1 pb 2.88 dividend 5.2 3.19%  operation 2 discount 4.76
            "000977",  # 浪潮信息 roe 6.04 pe 0.93 pb 6.49 dividend 0.6 0.14%  operation 2 discount 10.74
            "002303",  # 美盈森 roe 6.04 pe 3.48 pb 1.74 dividend 2.0 3.52%  operation 6 discount 2.88
            "002281",  # 光迅科技 roe 6.03 pe 1.19 pb 5.07 dividend 1.7 0.52%  operation 2 discount 8.4
            "603889",  # 新澳股份 roe 6.02 pe 4.73 pb 1.27 dividend 3.0 5.09%  operation 2 discount 2.11
            "000813",  # 德展健康 roe 6.02 pe 2.56 pb 2.36 dividend 0.0 0.0%  operation 2 discount 3.91
            "000819",  # 岳阳兴长 roe 6.02 pe 1.69 pb 3.57 dividend 0.2 0.2%  operation 2 discount 5.92
            "000525",  # 红 太 阳 roe 6.01 pe 4.55 pb 1.32 dividend 1.5 1.36%  operation 2 discount 2.2
            "002479",  # 富春环保 roe 6.01 pe 4.0 pb 1.5 dividend 0.5 0.77%  operation 2 discount 2.5
            "600363",  # 联创光电 roe 6.0 pe 2.17 pb 2.77 dividend 0.52 0.32%  operation 2 discount 4.61
            "600180",  # 瑞茂通 roe 5.99 pe 5.13 pb 1.17 dividend 0.468 0.67%  operation 2 discount 1.95
            "600496",  # 精工钢构 roe 5.98 pe 4.31 pb 1.39 dividend 0.13 0.33%  operation 2 discount 2.32
            "601801",  # 皖新传媒 roe 5.98 pe 5.81 pb 1.03 dividend 1.75 3.31%  operation 2 discount 1.72
            "300190",  # 维尔利 roe 5.98 pe 3.43 pb 1.74 dividend 0.5 0.59%  operation 6 discount 2.92
            "002723",  # 金莱特 roe 5.97 pe 2.08 pb 2.87 dividend 0.5 0.53%  operation 2 discount 4.81
            "002661",  # 克明面业 roe 5.96 pe 2.36 pb 2.52 dividend 2.5 1.46%  operation 2 discount 4.23
            "600297",  # 广汇汽车 roe 5.95 pe 6.42 pb 0.93 dividend 0.15 0.35%  operation 2 discount 1.56
            "600837",  # 海通证券 roe 5.95 pe 4.3 pb 1.38 dividend 1.5 1.01%  operation 2 discount 2.32
            "300272",  # 开能健康 roe 5.95 pe 2.39 pb 2.49 dividend 1.5 2.98%  operation 2 discount 4.18
            "002189",  # 中光学 roe 5.94 pe 1.29 pb 4.61 dividend 0.625757 0.27%  operation 6 discount 7.75
            "002559",  # 亚威股份 roe 5.94 pe 2.54 pb 2.34 dividend 3.0 4.48%  operation 2 discount 3.94
            "600097",  # 开创国际 roe 5.93 pe 4.33 pb 1.37 dividend 1.8 1.85%  operation 2 discount 2.31
            "000060",  # 中金岭南 roe 5.93 pe 4.55 pb 1.3 dividend 0.8 2.04%  operation 2 discount 2.2
            "000823",  # 超声电子 roe 5.93 pe 2.67 pb 2.22 dividend 1.0 0.7%  operation 2 discount 3.74
            "000923",  # 河钢资源 roe 5.93 pe 4.59 pb 1.29 dividend 0.1 0.07%  operation 2 discount 2.18
            "600575",  # 淮河能源 roe 5.92 pe 5.81 pb 1.02 dividend 0.5 2.06%  operation 2 discount 1.72
            "601016",  # 节能风电 roe 5.92 pe 4.2 pb 1.41 dividend 0.464 1.91%  operation 0 discount 2.38
            "300271",  # 华宇软件 roe 5.92 pe 1.36 pb 4.35 dividend 0.614444 0.2%  operation 6 discount 7.34
            "601898",  # 中煤能源 roe 5.9 pe 9.68 pb 0.61 dividend 0.78 1.74%  operation 6 discount 1.03
            "002054",  # 德美化工 roe 5.9 pe 3.25 pb 1.82 dividend 0.52 0.64%  operation 2 discount 3.08
            "002712",  # 思美传媒 roe 5.9 pe 4.63 pb 1.28 dividend 0.082733 0.12%  operation 2 discount 2.16
            "002154",  # 报 喜 鸟 roe 5.89 pe 3.18 pb 1.85 dividend 1.0 2.37%  operation 6 discount 3.15
            "600299",  # 安迪苏 roe 5.87 pe 2.71 pb 2.16 dividend 2.76 2.47%  operation 2 discount 3.69
            "300129",  # 泰胜风能 roe 5.87 pe 3.73 pb 1.57 dividend 0.8 1.59%  operation 2 discount 2.68
            "600328",  # 兰太实业 roe 5.85 pe 3.98 pb 1.47 dividend 1.84 2.09%  operation 6 discount 2.51
            "002340",  # 格林美 roe 5.85 pe 2.59 pb 2.26 dividend 0.3 0.53%  operation 6 discount 3.86
            "300163",  # 先锋新材 roe 5.85 pe 1.82 pb 3.21 dividend 0.5 1.31%  operation 2 discount 5.49
            "000863",  # 三湘印象 roe 5.84 pe 5.94 pb 0.98 dividend 2.01529 4.75%  operation 0 discount 1.68
            "000899",  # 赣能股份 roe 5.84 pe 6.19 pb 0.94 dividend 1.2 2.58%  operation 2 discount 1.61
            "600481",  # 双良节能 roe 5.83 pe 2.34 pb 2.49 dividend 1.2 3.58%  operation 2 discount 4.27
            "000825",  # 太钢不锈 roe 5.83 pe 8.71 pb 0.67 dividend 1.0 2.69%  operation 2 discount 1.15
            "300387",  # 富邦股份 roe 5.83 pe 2.71 pb 2.15 dividend 0.5 0.57%  operation 2 discount 3.69
            "600171",  # 上海贝岭 roe 5.82 pe 1.29 pb 4.52 dividend 0.45 0.24%  operation 2 discount 7.77
            "601808",  # 中海油服 roe 5.82 pe 2.75 pb 2.11 dividend 0.7 0.43%  operation 2 discount 3.63
            "000166",  # 申万宏源 roe 5.8 pe 3.88 pb 1.5 dividend 0.5 1.02%  operation 2 discount 2.58
            "600769",  # 祥龙电业 roe 5.79 pe 0.17 pb 34.07 dividend 0.0 0.0%  operation 2 discount 58.85
            "600795",  # 国电电力 roe 5.79 pe 7.3 pb 0.79 dividend 0.4 1.86%  operation 0 discount 1.37
            "300021",  # 大禹节水 roe 5.79 pe 1.97 pb 2.95 dividend 1.0 1.87%  operation 6 discount 5.09
            "600021",  # 上海电力 roe 5.78 pe 4.75 pb 1.22 dividend 3.3 4.5%  operation 4 discount 2.1
            "600642",  # 申能股份 roe 5.78 pe 6.33 pb 0.91 dividend 2.0 3.71%  operation 2 discount 1.58
            "002320",  # 海峡股份 roe 5.78 pe 1.47 pb 3.92 dividend 1.5 1.0%  operation 2 discount 6.78
            "600162",  # 香江控股 roe 5.76 pe 3.81 pb 1.51 dividend 0.75 3.32%  operation 0 discount 2.62
            "002044",  # 美年健康 roe 5.76 pe 0.7 pb 8.26 dividend 0.531516 0.37%  operation 2 discount 14.34
            "002245",  # 澳洋顺昌 roe 5.76 pe 2.36 pb 2.44 dividend 0.25 0.49%  operation 2 discount 4.24
            "300390",  # 天华超净 roe 5.76 pe 0.69 pb 8.35 dividend 1.5 1.14%  operation 6 discount 14.5
            "600023",  # 浙能电力 roe 5.75 pe 7.47 pb 0.77 dividend 1.8 5.04%  operation 2 discount 1.34
            "000025",  # 特 力Ａ roe 5.75 pe 0.74 pb 7.77 dividend 0.0 0.0%  operation 6 discount 13.52
            "300194",  # 福安药业 roe 5.75 pe 3.1 pb 1.85 dividend 1.0 1.64%  operation 2 discount 3.22
            "601618",  # 中国中冶 roe 5.74 pe 6.93 pb 0.83 dividend 0.7 2.49%  operation 6 discount 1.44
            "002140",  # 东华科技 roe 5.74 pe 2.99 pb 1.92 dividend 1.0 1.27%  operation 2 discount 3.35
            "002343",  # 慈文传媒 roe 5.74 pe 1.8 pb 3.19 dividend 1.8 1.71%  operation 2 discount 5.55
            "601886",  # 江河集团 roe 5.73 pe 5.76 pb 0.99 dividend 3.0 4.29%  operation 6 discount 1.73
            "000078",  # 海王生物 roe 5.73 pe 2.3 pb 2.5 dividend 0.2 0.35%  operation 2 discount 4.35
            "002539",  # 云图控股 roe 5.73 pe 3.74 pb 1.53 dividend 1.0 2.06%  operation 2 discount 2.67
            "000058",  # 深 赛 格 roe 5.72 pe 1.26 pb 4.54 dividend 0.35 0.49%  operation 0 discount 7.93
            "002063",  # 远光软件 roe 5.72 pe 1.18 pb 4.84 dividend 0.5 0.37%  operation 6 discount 8.46
            "002202",  # 金风科技 roe 5.72 pe 3.44 pb 1.66 dividend 2.5 2.28%  operation 0 discount 2.91
            "300151",  # 昌红科技 roe 5.72 pe 1.15 pb 5.0 dividend 0.600215 0.67%  operation 6 discount 8.73
            "600814",  # 杭州解百 roe 5.71 pe 3.89 pb 1.47 dividend 0.65 1.28%  operation 2 discount 2.57
            "002106",  # 莱宝高科 roe 5.71 pe 3.08 pb 1.85 dividend 1.0 0.95%  operation 2 discount 3.24
            "002487",  # 大金重工 roe 5.71 pe 3.94 pb 1.45 dividend 0.1 0.2%  operation 2 discount 2.54
            "600688",  # 上海石化 roe 5.7 pe 3.43 pb 1.66 dividend 2.5 5.56%  operation 2 discount 2.91
            "000012",  # 南 玻Ａ roe 5.7 pe 3.05 pb 1.87 dividend 0.5 0.87%  operation 2 discount 3.28
            "000153",  # 丰原药业 roe 5.7 pe 3.32 pb 1.72 dividend 1.0 1.38%  operation 2 discount 3.02
            "000685",  # 中山公用 roe 5.7 pe 6.03 pb 0.95 dividend 1.39 1.67%  operation 0 discount 1.66
            "002434",  # 万里扬 roe 5.69 pe 2.78 pb 2.04 dividend 1.5 1.61%  operation 2 discount 3.59
            "300215",  # 电科院 roe 5.69 pe 1.88 pb 3.03 dividend 1.2 1.46%  operation 4 discount 5.33
            "002283",  # 天润曲轴 roe 5.68 pe 5.53 pb 1.03 dividend 0.31 0.76%  operation 6 discount 1.81
            "600592",  # 龙溪股份 roe 5.67 pe 2.02 pb 2.8 dividend 1.0 0.75%  operation 2 discount 4.95
            "002345",  # 潮宏基 roe 5.67 pe 5.67 pb 1.0 dividend 1.0 2.58%  operation 2 discount 1.76
            "000565",  # 渝三峡Ａ roe 5.66 pe 2.84 pb 1.99 dividend 0.13 0.25%  operation 2 discount 3.52
            "600027",  # 华电国际 roe 5.65 pe 7.36 pb 0.77 dividend 0.66 1.91%  operation 0 discount 1.36
            "002152",  # 广电运通 roe 5.65 pe 2.09 pb 2.7 dividend 1.2 1.2%  operation 2 discount 4.79
            "600382",  # 广东明珠 roe 5.64 pe 7.99 pb 0.71 dividend 0.6 0.9%  operation 6 discount 1.25
            "002441",  # 众业达 roe 5.64 pe 4.34 pb 1.3 dividend 2.1 2.3%  operation 2 discount 2.3
            "600699",  # 均胜电子 roe 5.63 pe 2.22 pb 2.53 dividend 0.0 0.0%  operation 2 discount 4.5
            "600378",  # 昊华科技 roe 5.62 pe 1.67 pb 3.36 dividend 0.63 0.29%  operation 6 discount 5.98
            "600581",  # 八一钢铁 roe 5.61 pe 4.41 pb 1.27 dividend 0.0 0.0%  operation 2 discount 2.27
            "002217",  # 合力泰 roe 5.61 pe 2.92 pb 1.92 dividend 0.44 0.6%  operation 2 discount 3.43
            "600039",  # 四川路桥 roe 5.6 pe 5.95 pb 0.94 dividend 0.5 1.31%  operation 4 discount 1.68
            "600838",  # 上海九百 roe 5.6 pe 3.06 pb 1.83 dividend 0.74 1.25%  operation 0 discount 3.27
            "000686",  # 东北证券 roe 5.6 pe 3.75 pb 1.49 dividend 1.0 1.01%  operation 2 discount 2.66
            "002457",  # 青龙管业 roe 5.59 pe 3.76 pb 1.48 dividend 1.0 1.21%  operation 2 discount 2.66
            "002187",  # 广百股份 roe 5.58 pe 5.64 pb 0.99 dividend 3.0 3.71%  operation 6 discount 1.77
            "601789",  # 宁波建工 roe 5.57 pe 3.24 pb 1.72 dividend 0.7 1.41%  operation 6 discount 3.09
            "000682",  # 东方电子 roe 5.56 pe 2.34 pb 2.38 dividend 0.2 0.35%  operation 2 discount 4.27
            "300154",  # 瑞凌股份 roe 5.56 pe 3.34 pb 1.66 dividend 2.0 3.34%  operation 2 discount 2.99
            "000733",  # 振华科技 roe 5.55 pe 2.41 pb 2.3 dividend 0.5 0.21%  operation 2 discount 4.15
            "000883",  # 湖北能源 roe 5.55 pe 6.22 pb 0.89 dividend 1.1 2.94%  operation 0 discount 1.61
            "002004",  # 华邦健康 roe 5.55 pe 4.94 pb 1.12 dividend 2.2 4.25%  operation 2 discount 2.02
            "601678",  # 滨化股份 roe 5.53 pe 4.27 pb 1.29 dividend 1.5 2.86%  operation 2 discount 2.34
            "002237",  # 恒邦股份 roe 5.53 pe 1.85 pb 2.99 dividend 1.0 0.66%  operation 2 discount 5.42
            "600497",  # 驰宏锌锗 roe 5.52 pe 4.18 pb 1.32 dividend 0.7 1.81%  operation 2 discount 2.39
            "002135",  # 东南网架 roe 5.52 pe 3.0 pb 1.84 dividend 0.17 0.22%  operation 2 discount 3.33
            "600089",  # 特变电工 roe 5.51 pe 5.95 pb 0.93 dividend 1.8 2.38%  operation 2 discount 1.68
            "601633",  # 长城汽车 roe 5.51 pe 3.51 pb 1.57 dividend 2.9 3.18%  operation 2 discount 2.85
            "300227",  # 光韵达 roe 5.5 pe 1.51 pb 3.63 dividend 0.35 0.22%  operation 2 discount 6.61
            "002538",  # 司尔特 roe 5.49 pe 5.16 pb 1.06 dividend 1.0 1.85%  operation 2 discount 1.94
            "002216",  # 三全食品 roe 5.48 pe 0.77 pb 7.1 dividend 0.3 0.16%  operation 6 discount 12.97
            "002371",  # 北方华创 roe 5.47 pe 0.33 pb 16.36 dividend 0.52 0.04%  operation 4 discount 29.91
            "002503",  # 搜于特 roe 5.47 pe 1.91 pb 2.87 dividend 2.0 3.88%  operation 2 discount 5.24
            "600231",  # 凌钢股份 roe 5.46 pe 6.16 pb 0.89 dividend 0.44 1.78%  operation 2 discount 1.62
            "600410",  # 华胜天成 roe 5.45 pe 1.96 pb 2.79 dividend 0.63 0.5%  operation 2 discount 5.11
            "600490",  # 鹏欣资源 roe 5.44 pe 3.81 pb 1.43 dividend 0.0 0.0%  operation 2 discount 2.62
            "600979",  # 广安爱众 roe 5.44 pe 4.99 pb 1.09 dividend 1.0 2.27%  operation 0 discount 2.0
            "601198",  # 东兴证券 roe 5.44 pe 3.19 pb 1.71 dividend 1.1 0.87%  operation 2 discount 3.14
            "000783",  # 长江证券 roe 5.44 pe 3.69 pb 1.47 dividend 0.2 0.28%  operation 2 discount 2.71
            "600353",  # 旭光股份 roe 5.42 pe 1.85 pb 2.94 dividend 0.6 1.0%  operation 2 discount 5.42
            "002700",  # 新疆浩源 roe 5.42 pe 2.05 pb 2.64 dividend 0.3 0.45%  operation 2 discount 4.88
            "002735",  # 王子新材 roe 5.42 pe 1.33 pb 4.08 dividend 2.35 1.31%  operation 2 discount 7.53
            "600833",  # 第一医药 roe 5.41 pe 1.68 pb 3.21 dividend 0.65 0.64%  operation 2 discount 5.94
            "000415",  # 渤海租赁 roe 5.41 pe 9.53 pb 0.57 dividend 0.6 1.7%  operation 0 discount 1.05
            "002244",  # 滨江集团 roe 5.41 pe 6.02 pb 0.9 dividend 0.6 1.3%  operation 0 discount 1.66
            "002322",  # 理工环科 roe 5.41 pe 2.76 pb 1.96 dividend 5.5 3.96%  operation 2 discount 3.62
            "000016",  # 深康佳Ａ roe 5.4 pe 1.63 pb 3.32 dividend 1.0 0.87%  operation 2 discount 6.14
            "002481",  # 双塔食品 roe 5.4 pe 0.93 pb 5.83 dividend 0.101608 0.08%  operation 2 discount 10.79
            "002053",  # 云南能投 roe 5.39 pe 3.84 pb 1.4 dividend 0.5 0.69%  operation 0 discount 2.61
            "000623",  # 吉林敖东 roe 5.38 pe 5.77 pb 0.93 dividend 2.0 1.16%  operation 2 discount 1.73
            "002461",  # 珠江啤酒 roe 5.38 pe 3.03 pb 1.77 dividend 1.0 1.48%  operation 6 discount 3.3
            "002724",  # 海洋王 roe 5.38 pe 1.87 pb 2.87 dividend 1.0 1.3%  operation 6 discount 5.34
            "600808",  # 马钢股份 roe 5.37 pe 6.74 pb 0.8 dividend 3.1 10.99%  operation 2 discount 1.48
            "601688",  # 华泰证券 roe 5.37 pe 3.56 pb 1.51 dividend 3.0 1.51%  operation 2 discount 2.81
            "002129",  # 中环股份 roe 5.35 pe 1.46 pb 3.66 dividend 0.3 0.17%  operation 4 discount 6.85
            "002301",  # 齐心集团 roe 5.34 pe 1.45 pb 3.68 dividend 3.0 1.74%  operation 6 discount 6.9
            "300300",  # 汉鼎宇佑 roe 5.34 pe 2.3 pb 2.32 dividend 0.2 0.23%  operation 2 discount 4.35
            "600703",  # 三安光电 roe 5.33 pe 1.16 pb 4.6 dividend 2.0 0.82%  operation 2 discount 8.63
            "600345",  # 长江通信 roe 5.32 pe 2.35 pb 2.26 dividend 3.6 1.63%  operation 2 discount 4.25
            "300308",  # 中际旭创 roe 5.32 pe 0.77 pb 6.86 dividend 1.23 0.19%  operation 2 discount 12.91
            "000539",  # 粤电力Ａ roe 5.29 pe 6.73 pb 0.79 dividend 0.6 1.58%  operation 0 discount 1.49
            "000543",  # 皖能电力 roe 5.29 pe 7.17 pb 0.74 dividend 0.44 1.03%  operation 2 discount 1.39
            "000541",  # 佛山照明 roe 5.28 pe 3.3 pb 1.6 dividend 1.56 3.13%  operation 2 discount 3.03
            "002252",  # 上海莱士 roe 5.28 pe 1.32 pb 4.01 dividend 0.17 0.18%  operation 2 discount 7.59
            "000751",  # 锌业股份 roe 5.27 pe 3.06 pb 1.72 dividend 0.0 0.0%  operation 2 discount 3.27
            "600446",  # 金证股份 roe 5.24 pe 0.52 pb 10.13 dividend 0.31 0.15%  operation 2 discount 19.34
            "002742",  # 三圣股份 roe 5.24 pe 2.92 pb 1.79 dividend 1.0 1.56%  operation 2 discount 3.42
            "300223",  # 北京君正 roe 5.23 pe 0.29 pb 17.91 dividend 0.3 0.03%  operation 2 discount 34.24
            "600633",  # 浙数文化 roe 5.22 pe 3.14 pb 1.66 dividend 0.8 0.79%  operation 2 discount 3.18
            "601010",  # 文峰股份 roe 5.22 pe 3.97 pb 1.31 dividend 0.4 1.2%  operation 2 discount 2.52
            "002726",  # 龙大肉食 roe 5.22 pe 2.21 pb 2.36 dividend 0.47 0.68%  operation 2 discount 4.52
            "300343",  # 联创股份 roe 5.22 pe 3.71 pb 1.41 dividend 0.0 0.0%  operation 2 discount 2.69
            "000690",  # 宝新能源 roe 5.21 pe 3.89 pb 1.34 dividend 1.0 1.79%  operation 0 discount 2.57
            "300112",  # 万讯自控 roe 5.21 pe 1.9 pb 2.74 dividend 1.2 1.28%  operation 6 discount 5.27
            "600335",  # 国机汽车 roe 5.2 pe 6.25 pb 0.83 dividend 1.5 2.6%  operation 2 discount 1.6
            "601700",  # 风范股份 roe 5.2 pe 1.92 pb 2.71 dividend 1.8 2.7%  operation 2 discount 5.2
            "002108",  # 沧州明珠 roe 5.2 pe 2.98 pb 1.74 dividend 1.0 2.49%  operation 2 discount 3.35
            "300042",  # 朗科科技 roe 5.2 pe 1.48 pb 3.51 dividend 2.0 1.16%  operation 6 discount 6.74
            "300254",  # 仟源医药 roe 5.2 pe 2.43 pb 2.14 dividend 0.2 0.23%  operation 2 discount 4.11
            "002631",  # 德尔未来 roe 5.19 pe 1.57 pb 3.3 dividend 0.6 0.7%  operation 2 discount 6.37
            "600008",  # 首创股份 roe 5.18 pe 2.95 pb 1.76 dividend 0.8 2.37%  operation 4 discount 3.39
            "600201",  # 生物股份 roe 5.18 pe 0.97 pb 5.34 dividend 3.5 1.54%  operation 2 discount 10.29
            "600499",  # 科达洁能 roe 5.18 pe 3.02 pb 1.72 dividend 0.5 0.96%  operation 2 discount 3.31
            "300304",  # 云意电气 roe 5.17 pe 2.55 pb 2.03 dividend 0.301057 0.66%  operation 2 discount 3.92
            "300065",  # 海兰信 roe 5.16 pe 1.95 pb 2.64 dividend 0.3 0.25%  operation 2 discount 5.12
            "300353",  # 东土科技 roe 5.16 pe 1.53 pb 3.37 dividend 0.38 0.25%  operation 2 discount 6.52
            "002168",  # 惠程科技 roe 5.15 pe 1.35 pb 3.81 dividend 0.6 0.67%  operation 2 discount 7.4
            "002397",  # 梦洁股份 roe 5.15 pe 2.25 pb 2.29 dividend 1.5 2.63%  operation 2 discount 4.44
            "600895",  # 张江高科 roe 5.13 pe 2.19 pb 2.34 dividend 1.1 0.79%  operation 0 discount 4.56
            "002540",  # 亚太科技 roe 5.13 pe 3.35 pb 1.53 dividend 4.80297 8.88%  operation 2 discount 2.98
            "600798",  # 宁波海运 roe 5.12 pe 4.57 pb 1.12 dividend 0.6 1.82%  operation 4 discount 2.19
            "600980",  # 北矿科技 roe 5.12 pe 1.51 pb 3.38 dividend 0.3 0.23%  operation 2 discount 6.61
            "002454",  # 松芝股份 roe 5.12 pe 4.86 pb 1.05 dividend 0.6 1.04%  operation 2 discount 2.06
            "002612",  # 朗姿股份 roe 5.12 pe 3.97 pb 1.29 dividend 3.5 3.85%  operation 2 discount 2.52
            "601377",  # 兴业证券 roe 5.1 pe 3.64 pb 1.4 dividend 0.5 0.7%  operation 2 discount 2.75
            "002410",  # 广联达 roe 5.09 pe 0.32 pb 15.73 dividend 2.0 0.46%  operation 2 discount 30.9
            "002403",  # 爱仕达 roe 5.08 pe 3.42 pb 1.49 dividend 1.5 1.66%  operation 2 discount 2.92
            "300068",  # 南都电源 roe 5.07 pe 2.95 pb 1.72 dividend 2.0 1.58%  operation 2 discount 3.39
            "600038",  # 中直股份 roe 5.06 pe 1.57 pb 3.22 dividend 2.6 0.6%  operation 2 discount 6.35
            "002464",  # 众应互联 roe 5.06 pe 2.28 pb 2.22 dividend 0.0 0.0%  operation 2 discount 4.39
            "000552",  # 靖远煤电 roe 5.04 pe 6.95 pb 0.72 dividend 1.0 4.15%  operation 2 discount 1.44
            "002087",  # 新野纺织 roe 5.04 pe 4.14 pb 1.22 dividend 0.5 0.83%  operation 6 discount 2.41
            "600459",  # 贵研铂业 roe 5.03 pe 2.26 pb 2.23 dividend 1.8 1.12%  operation 2 discount 4.43
            "002079",  # 苏州固锝 roe 5.03 pe 0.94 pb 5.33 dividend 0.3 0.24%  operation 2 discount 10.59
            "300184",  # 力源信息 roe 5.03 pe 2.77 pb 1.81 dividend 1.0 1.37%  operation 2 discount 3.61
            "002361",  # 神剑股份 roe 5.02 pe 2.22 pb 2.26 dividend 1.0 2.07%  operation 2 discount 4.5
            "300305",  # 裕兴股份 roe 5.02 pe 2.67 pb 1.88 dividend 0.652355 0.68%  operation 2 discount 3.74
            "600708",  # 光明地产 roe 5.01 pe 7.77 pb 0.64 dividend 2.0 6.04%  operation 0 discount 1.29
            "002484",  # 江海股份 roe 5.01 pe 2.12 pb 2.37 dividend 0.8 0.82%  operation 6 discount 4.72
            "002651",  # 利君股份 roe 5.01 pe 2.19 pb 2.29 dividend 0.6 1.26%  operation 2 discount 4.56
            "002707",  # 众信旅游 roe 5.01 pe 2.13 pb 2.35 dividend 0.23 0.38%  operation 2 discount 4.7
            "300062",  # 中能电气 roe 5.01 pe 2.17 pb 2.31 dividend 0.4 0.67%  operation 2 discount 4.6
            "600615",  # 丰华股份 roe 5.0 pe 1.78 pb 2.81 dividend 0.0 0.0%  operation 2 discount 5.62
            "000627",  # 天茂集团 roe 5.0 pe 3.32 pb 1.5 dividend 0.3 0.48%  operation 0 discount 3.01
            "300314",  # 戴维医疗 roe 5.0 pe 1.25 pb 3.99 dividend 0.9 0.81%  operation 2 discount 7.98
            "600277",  # 亿利洁能 roe 4.99 pe 6.41 pb 0.78 dividend 0.85 1.96%  operation 2 discount 1.56
            "002425",  # 凯撒文化 roe 4.99 pe 4.33 pb 1.15 dividend 0.6 1.04%  operation 6 discount 2.31
            "300263",  # 隆华科技 roe 4.99 pe 1.87 pb 2.66 dividend 0.200616 0.26%  operation 6 discount 5.34
            "002627",  # 宜昌交运 roe 4.98 pe 3.35 pb 1.49 dividend 1.5 1.53%  operation 2 discount 2.99
            "300276",  # 三丰智能 roe 4.98 pe 2.47 pb 2.02 dividend 2.3 2.45%  operation 6 discount 4.05
            "002455",  # 百川股份 roe 4.96 pe 2.24 pb 2.22 dividend 1.0 1.75%  operation 2 discount 4.47
            "002635",  # 安洁科技 roe 4.96 pe 2.09 pb 2.37 dividend 1.0 0.44%  operation 6 discount 4.78
            "600425",  # 青松建化 roe 4.95 pe 3.95 pb 1.25 dividend 0.4 0.94%  operation 2 discount 2.53
            "300218",  # 安利股份 roe 4.94 pe 2.86 pb 1.73 dividend 0.75 0.91%  operation 2 discount 3.49
            "600582",  # 天地科技 roe 4.93 pe 5.47 pb 0.9 dividend 0.5 1.4%  operation 6 discount 1.83
            "603456",  # 九洲药业 roe 4.93 pe 0.8 pb 6.19 dividend 2.0 0.95%  operation 2 discount 12.55
            "000976",  # 华铁股份 roe 4.93 pe 2.48 pb 1.99 dividend 0.0 0.0%  operation 2 discount 4.04
            "300078",  # 思创医惠 roe 4.93 pe 0.89 pb 5.54 dividend 0.18 0.11%  operation 2 discount 11.24
            "002101",  # 广东鸿图 roe 4.92 pe 4.89 pb 1.01 dividend 3.15 3.6%  operation 2 discount 2.04
            "002636",  # 金安国纪 roe 4.92 pe 1.94 pb 2.54 dividend 0.65 0.7%  operation 2 discount 5.16
            "002658",  # 雪迪龙 roe 4.92 pe 2.14 pb 2.29 dividend 1.0 1.33%  operation 2 discount 4.67
            "300397",  # 天和防务 roe 4.92 pe 0.45 pb 10.89 dividend 0.0 0.0%  operation 2 discount 22.12
            "601996",  # 丰林集团 roe 4.91 pe 3.99 pb 1.23 dividend 0.6 2.07%  operation 6 discount 2.51
            "600226",  # 瀚叶股份 roe 4.9 pe 2.38 pb 2.06 dividend 0.22 0.76%  operation 2 discount 4.2
            "000419",  # 通程控股 roe 4.9 pe 5.81 pb 0.84 dividend 1.6 3.65%  operation 2 discount 1.72
            "600551",  # 时代出版 roe 4.89 pe 5.52 pb 0.89 dividend 1.9 2.38%  operation 2 discount 1.81
            "603222",  # 济民制药 roe 4.89 pe 0.24 pb 20.12 dividend 0.21 0.04%  operation 2 discount 41.13
            "000821",  # 京山轻机 roe 4.89 pe 3.77 pb 1.3 dividend 0.3 0.43%  operation 2 discount 2.65
            "002250",  # 联化科技 roe 4.89 pe 1.97 pb 2.49 dividend 0.2 0.12%  operation 2 discount 5.09
            "002647",  # 仁东控股 roe 4.89 pe 0.37 pb 13.16 dividend 0.2 0.08%  operation 2 discount 26.9
            "300262",  # 巴安水务 roe 4.89 pe 3.63 pb 1.35 dividend 0.4 0.83%  operation 0 discount 2.75
            "600168",  # 武汉控股 roe 4.88 pe 4.0 pb 1.22 dividend 1.19 1.34%  operation 0 discount 2.5
            "002411",  # 延安必康 roe 4.88 pe 2.42 pb 2.02 dividend 1.0 0.76%  operation 2 discount 4.13
            "600739",  # 辽宁成大 roe 4.87 pe 3.29 pb 1.48 dividend 1.8 0.87%  operation 2 discount 3.04
            "000099",  # 中信海直 roe 4.87 pe 3.7 pb 1.32 dividend 0.25 0.36%  operation 6 discount 2.7
            "000551",  # 创元科技 roe 4.87 pe 2.53 pb 1.92 dividend 1.0 1.21%  operation 6 discount 3.95
            "300288",  # 朗玛信息 roe 4.86 pe 1.41 pb 3.44 dividend 0.5 0.36%  operation 2 discount 7.08
            "600622",  # 光大嘉宝 roe 4.85 pe 4.39 pb 1.11 dividend 1.6 3.48%  operation 4 discount 2.28
            "002560",  # 通达股份 roe 4.85 pe 2.85 pb 1.7 dividend 1.0 1.6%  operation 2 discount 3.5
            "002644",  # 佛慈制药 roe 4.84 pe 1.7 pb 2.84 dividend 0.13 0.15%  operation 0 discount 5.87
            "600111",  # 北方稀土 roe 4.83 pe 1.31 pb 3.68 dividend 0.5 0.52%  operation 6 discount 7.61
            "000407",  # 胜利股份 roe 4.81 pe 3.76 pb 1.28 dividend 0.2 0.57%  operation 6 discount 2.66
            "002634",  # 棒杰股份 roe 4.8 pe 1.22 pb 3.93 dividend 0.5 0.88%  operation 2 discount 8.18
            "300001",  # 特锐德 roe 4.8 pe 0.67 pb 7.17 dividend 0.1 0.04%  operation 2 discount 14.93
            "600500",  # 中化国际 roe 4.79 pe 3.21 pb 1.5 dividend 1.5 2.35%  operation 2 discount 3.12
            "002606",  # 大连电瓷 roe 4.78 pe 1.51 pb 3.17 dividend 0.15 0.21%  operation 2 discount 6.63
            "600967",  # 内蒙一机 roe 4.77 pe 2.31 pb 2.07 dividend 0.32 0.3%  operation 2 discount 4.33
            "600790",  # 轻纺城 roe 4.76 pe 5.2 pb 0.91 dividend 1.8 5.37%  operation 2 discount 1.92
            "600826",  # 兰生股份 roe 4.76 pe 3.56 pb 1.34 dividend 1.7 1.56%  operation 2 discount 2.81
            "000510",  # 新金路 roe 4.76 pe 1.63 pb 2.92 dividend 0.4 0.85%  operation 2 discount 6.13
            "600409",  # 三友化工 roe 4.75 pe 3.99 pb 1.19 dividend 2.31 3.61%  operation 2 discount 2.5
            "600118",  # 中国卫星 roe 4.74 pe 0.62 pb 7.67 dividend 1.1 0.3%  operation 6 discount 16.2
            "600578",  # 京能电力 roe 4.74 pe 5.36 pb 0.88 dividend 0.8 2.61%  operation 0 discount 1.87
            "000989",  # 九 芝 堂 roe 4.74 pe 2.45 pb 1.93 dividend 4.0 4.51%  operation 2 discount 4.08
            "002208",  # 合肥城建 roe 4.74 pe 2.4 pb 1.98 dividend 1.0 1.35%  operation 0 discount 4.17
            "002722",  # 金轮股份 roe 4.74 pe 3.66 pb 1.29 dividend 2.0 1.44%  operation 2 discount 2.73
            "600392",  # 盛和资源 roe 4.73 pe 1.95 pb 2.42 dividend 0.3 0.4%  operation 2 discount 5.12
            "600894",  # 广日股份 roe 4.73 pe 5.82 pb 0.81 dividend 0.5 0.69%  operation 2 discount 1.72
            "002738",  # 中矿资源 roe 4.73 pe 2.66 pb 1.78 dividend 0.5 0.29%  operation 6 discount 3.77
            "000722",  # 湖南发展 roe 4.72 pe 4.78 pb 0.99 dividend 0.5 0.79%  operation 2 discount 2.09
            "000729",  # 燕京啤酒 roe 4.72 pe 3.66 pb 1.29 dividend 0.22 0.36%  operation 2 discount 2.73
            "002277",  # 友阿股份 roe 4.72 pe 6.06 pb 0.78 dividend 0.5 1.31%  operation 2 discount 1.65
            "002324",  # 普利特 roe 4.72 pe 1.01 pb 4.65 dividend 2.0 0.96%  operation 2 discount 9.86
            "600603",  # 广汇物流 roe 4.69 pe 4.07 pb 1.15 dividend 3.0 5.41%  operation 4 discount 2.46
            "000597",  # 东北制药 roe 4.69 pe 2.39 pb 1.96 dividend 0.0 0.0%  operation 6 discount 4.18
            "603636",  # 南威软件 roe 4.68 pe 1.06 pb 4.4 dividend 1.2 0.82%  operation 2 discount 9.41
            "000960",  # 锡业股份 roe 4.68 pe 3.61 pb 1.3 dividend 0.2 0.21%  operation 2 discount 2.77
            "002599",  # 盛通股份 roe 4.68 pe 2.86 pb 1.63 dividend 0.0 0.0%  operation 6 discount 3.49
            "600444",  # 国机通用 roe 4.67 pe 1.79 pb 2.61 dividend 1.3 1.29%  operation 2 discount 5.59
            "601002",  # 晋亿实业 roe 4.67 pe 2.53 pb 1.85 dividend 1.0 1.59%  operation 2 discount 3.95
            "000156",  # 华数传媒 roe 4.66 pe 3.18 pb 1.47 dividend 2.2 1.98%  operation 6 discount 3.15
            "002435",  # 长江健康 roe 4.65 pe 4.92 pb 0.95 dividend 1.0 2.39%  operation 6 discount 2.03
            "300095",  # 华伍股份 roe 4.64 pe 2.06 pb 2.25 dividend 0.3 0.42%  operation 2 discount 4.86
            "600456",  # 宝钛股份 roe 4.63 pe 1.29 pb 3.6 dividend 1.0 0.33%  operation 2 discount 7.77
            "002448",  # 中原内配 roe 4.63 pe 3.73 pb 1.24 dividend 1.0 1.82%  operation 2 discount 2.68
            "600322",  # 天房发展 roe 4.62 pe 6.84 pb 0.68 dividend 0.02 0.07%  operation 0 discount 1.46
            "600216",  # 浙江医药 roe 4.61 pe 2.35 pb 1.96 dividend 1.5 0.94%  operation 2 discount 4.26
            "600637",  # 东方明珠 roe 4.61 pe 3.65 pb 1.26 dividend 2.7 2.57%  operation 2 discount 2.74
            "600736",  # 苏州高新 roe 4.61 pe 4.39 pb 1.05 dividend 1.45 2.56%  operation 4 discount 2.28
            "601788",  # 光大证券 roe 4.61 pe 3.87 pb 1.19 dividend 1.0 0.79%  operation 2 discount 2.59
            "002650",  # 加加食品 roe 4.61 pe 2.29 pb 2.01 dividend 0.4 1.01%  operation 2 discount 4.37
            "002136",  # 安 纳 达 roe 4.6 pe 1.83 pb 2.51 dividend 1.0 1.22%  operation 2 discount 5.46
            "002199",  # 东晶电子 roe 4.6 pe 0.73 pb 6.28 dividend 1.0 0.97%  operation 2 discount 13.65
            "002467",  # 二六三 roe 4.58 pe 0.83 pb 5.53 dividend 1.0 1.22%  operation 2 discount 12.09
            "300054",  # 鼎龙股份 roe 4.58 pe 1.39 pb 3.3 dividend 0.2 0.15%  operation 2 discount 7.21
            "600017",  # 日照港 roe 4.57 pe 6.42 pb 0.71 dividend 0.2 0.74%  operation 6 discount 1.56
            "600336",  # 澳柯玛 roe 4.57 pe 1.63 pb 2.8 dividend 0.3 0.45%  operation 2 discount 6.13
            "000959",  # 首钢股份 roe 4.57 pe 7.47 pb 0.61 dividend 0.1 0.32%  operation 2 discount 1.34
            "300378",  # 鼎捷软件 roe 4.57 pe 1.23 pb 3.73 dividend 1.00398 0.53%  operation 2 discount 8.16
            "600055",  # 万东医疗 roe 4.56 pe 1.17 pb 3.9 dividend 1.0 0.69%  operation 6 discount 8.55
            "300038",  # 数知科技 roe 4.56 pe 3.95 pb 1.16 dividend 0.7 0.65%  operation 6 discount 2.53
            "002224",  # 三 力 士 roe 4.55 pe 1.78 pb 2.55 dividend 0.15 0.19%  operation 2 discount 5.62
            "600006",  # 东风汽车 roe 4.54 pe 3.91 pb 1.16 dividend 0.833 1.96%  operation 6 discount 2.56
            "600163",  # 中闽能源 roe 4.54 pe 2.56 pb 1.77 dividend 0.0 0.0%  operation 0 discount 3.91
            "600662",  # 强生控股 roe 4.54 pe 3.46 pb 1.31 dividend 0.4 0.95%  operation 2 discount 2.89
            "000738",  # 航发控制 roe 4.53 pe 1.52 pb 2.98 dividend 0.4 0.28%  operation 2 discount 6.58
            "002678",  # 珠江钢琴 roe 4.53 pe 1.46 pb 3.09 dividend 0.65 0.85%  operation 6 discount 6.84
            "000859",  # 国风塑业 roe 4.52 pe 1.6 pb 2.83 dividend 0.1 0.16%  operation 2 discount 6.25
            "002482",  # 广田集团 roe 4.52 pe 4.94 pb 0.91 dividend 0.3 0.7%  operation 2 discount 2.02
            "002533",  # 金杯电工 roe 4.52 pe 3.13 pb 1.44 dividend 1.5 2.44%  operation 2 discount 3.19
            "300363",  # 博腾股份 roe 4.52 pe 1.04 pb 4.36 dividend 0.47 0.2%  operation 2 discount 9.63
            "300377",  # 赢时胜 roe 4.52 pe 1.34 pb 3.36 dividend 1.0 0.8%  operation 2 discount 7.45
            "600602",  # 云赛智联 roe 4.51 pe 1.52 pb 2.97 dividend 0.6 0.67%  operation 2 discount 6.59
            "601999",  # 出版传媒 roe 4.51 pe 2.26 pb 2.0 dividend 1.1 1.36%  operation 6 discount 4.43
            "000408",  # 藏格控股 roe 4.51 pe 2.49 pb 1.81 dividend 3.0 4.23%  operation 6 discount 4.02
            "000938",  # 紫光股份 roe 4.5 pe 1.32 pb 3.42 dividend 1.5 0.32%  operation 2 discount 7.6
            "300091",  # 金通灵 roe 4.5 pe 2.35 pb 1.91 dividend 0.08 0.2%  operation 2 discount 4.25
            "002382",  # 蓝帆医疗 roe 4.49 pe 2.18 pb 2.06 dividend 0.4 0.22%  operation 2 discount 4.6
            "601555",  # 东吴证券 roe 4.47 pe 3.0 pb 1.49 dividend 0.9 0.87%  operation 2 discount 3.33
            "300024",  # 机器人 roe 4.47 pe 1.12 pb 4.0 dividend 0.5 0.3%  operation 6 discount 8.96
            "000705",  # 浙江震元 roe 4.46 pe 2.71 pb 1.65 dividend 0.3 0.41%  operation 6 discount 3.69
            "000795",  # 英洛华 roe 4.46 pe 1.51 pb 2.95 dividend 0.0 0.0%  operation 6 discount 6.63
            "600774",  # 汉商集团 roe 4.44 pe 1.0 pb 4.42 dividend 0.3 0.25%  operation 2 discount 9.97
            "600148",  # 长春一东 roe 4.43 pe 1.13 pb 3.94 dividend 0.985 0.8%  operation 2 discount 8.89
            "600864",  # 哈投股份 roe 4.43 pe 3.7 pb 1.2 dividend 1.0 1.3%  operation 0 discount 2.7
            "002377",  # 国创高新 roe 4.43 pe 6.16 pb 0.72 dividend 0.45 1.08%  operation 2 discount 1.62
            "002470",  # 金正大 roe 4.43 pe 5.24 pb 0.85 dividend 0.8 2.84%  operation 2 discount 1.91
            "000880",  # 潍柴重机 roe 4.4 pe 2.94 pb 1.5 dividend 0.2 0.26%  operation 2 discount 3.4
            "600780",  # 通宝能源 roe 4.39 pe 6.02 pb 0.73 dividend 1.5 4.41%  operation 2 discount 1.66
            "002351",  # 漫步者 roe 4.39 pe 0.6 pb 7.33 dividend 1.0 0.44%  operation 2 discount 16.72
            "300006",  # 莱美药业 roe 4.39 pe 1.71 pb 2.57 dividend 0.5 0.91%  operation 2 discount 5.85
            "600367",  # 红星发展 roe 4.37 pe 2.45 pb 1.79 dividend 0.4 0.5%  operation 2 discount 4.09
            "300162",  # 雷曼光电 roe 4.37 pe 1.28 pb 3.41 dividend 1.0 1.09%  operation 2 discount 7.79
            "601116",  # 三江购物 roe 4.35 pe 1.95 pb 2.23 dividend 2.0 1.56%  operation 2 discount 5.13
            "002246",  # 北化股份 roe 4.35 pe 2.07 pb 2.1 dividend 0.55 0.58%  operation 2 discount 4.84
            "002542",  # 中化岩土 roe 4.35 pe 2.29 pb 1.9 dividend 0.2 0.49%  operation 2 discount 4.36
            "002365",  # 永安药业 roe 4.34 pe 2.41 pb 1.8 dividend 1.00711 1.03%  operation 2 discount 4.14
            "002669",  # 康达新材 roe 4.33 pe 2.1 pb 2.06 dividend 0.77 0.45%  operation 2 discount 4.75
            "600109",  # 国金证券 roe 4.32 pe 2.69 pb 1.61 dividend 0.4 0.37%  operation 2 discount 3.72
            "600988",  # 赤峰黄金 roe 4.31 pe 0.97 pb 4.43 dividend 0.0 0.0%  operation 2 discount 10.28
            "002144",  # 宏达高科 roe 4.31 pe 4.03 pb 1.07 dividend 1.0 0.97%  operation 2 discount 2.48
            "300155",  # 安居宝 roe 4.31 pe 1.08 pb 3.98 dividend 0.15 0.17%  operation 2 discount 9.24
            "000666",  # 经纬纺机 roe 4.3 pe 4.47 pb 0.96 dividend 0.5 0.42%  operation 2 discount 2.24
            "002270",  # 华明装备 roe 4.3 pe 2.71 pb 1.59 dividend 0.43 0.88%  operation 0 discount 3.69
            "002409",  # 雅克科技 roe 4.29 pe 1.08 pb 3.96 dividend 0.9 0.24%  operation 2 discount 9.24
            "600594",  # 益佰制药 roe 4.28 pe 3.66 pb 1.17 dividend 0.5 0.92%  operation 2 discount 2.74
            "300115",  # 长盈精密 roe 4.28 pe 0.92 pb 4.66 dividend 1.0 0.44%  operation 2 discount 10.89
            "300324",  # 旋极信息 roe 4.28 pe 1.45 pb 2.94 dividend 0.707409 0.8%  operation 2 discount 6.88
            "000563",  # 陕国投Ａ roe 4.27 pe 2.76 pb 1.54 dividend 0.2 0.48%  operation 2 discount 3.62
            "002165",  # 红 宝 丽 roe 4.27 pe 2.1 pb 2.03 dividend 0.4 0.77%  operation 2 discount 4.75
            "002235",  # 安妮股份 roe 4.27 pe 1.46 pb 2.93 dividend 0.0 0.0%  operation 2 discount 6.85
            "002666",  # 德联集团 roe 4.27 pe 2.58 pb 1.66 dividend 2.66 4.18%  operation 2 discount 3.88
            "600493",  # 凤竹纺织 roe 4.26 pe 1.86 pb 2.29 dividend 0.4 0.64%  operation 2 discount 5.37
            "600547",  # 山东黄金 roe 4.26 pe 0.84 pb 5.09 dividend 1.0 0.27%  operation 2 discount 11.95
            "600619",  # 海立股份 roe 4.26 pe 2.51 pb 1.7 dividend 1.5 1.74%  operation 2 discount 3.98
            "002423",  # 中粮资本 roe 4.25 pe 3.25 pb 1.31 dividend 0.05 0.05%  operation 0 discount 3.08
            "002739",  # 万达电影 roe 4.25 pe 2.35 pb 1.81 dividend 2.0 1.18%  operation 2 discount 4.25
            "300044",  # 赛为智能 roe 4.25 pe 1.59 pb 2.68 dividend 0.1 0.12%  operation 2 discount 6.3
            "600100",  # 同方股份 roe 4.24 pe 2.56 pb 1.65 dividend 0.15 0.16%  operation 0 discount 3.9
            "600126",  # 杭钢股份 roe 4.24 pe 3.86 pb 1.1 dividend 1.2 1.9%  operation 2 discount 2.59
            "600819",  # 耀皮玻璃 roe 4.23 pe 2.79 pb 1.52 dividend 0.3 0.57%  operation 2 discount 3.59
            "002335",  # 科华恒盛 roe 4.23 pe 2.04 pb 2.07 dividend 10.0 4.17%  operation 2 discount 4.89
            "300213",  # 佳讯飞鸿 roe 4.23 pe 1.87 pb 2.27 dividend 0.5 0.64%  operation 2 discount 5.36
            "000021",  # 深科技 roe 4.22 pe 0.99 pb 4.27 dividend 1.0 0.53%  operation 2 discount 10.14
            "002674",  # 兴业科技 roe 4.22 pe 3.3 pb 1.28 dividend 6.0 6.36%  operation 2 discount 3.03
            "300412",  # 迦南科技 roe 4.21 pe 1.61 pb 2.63 dividend 1.1 1.37%  operation 2 discount 6.23
            "300250",  # 初灵信息 roe 4.2 pe 1.17 pb 3.58 dividend 2.0 1.2%  operation 2 discount 8.52
            "600655",  # 豫园股份 roe 4.19 pe 4.21 pb 1.0 dividend 2.7 3.56%  operation 6 discount 2.38
            "002295",  # 精艺股份 roe 4.19 pe 2.76 pb 1.52 dividend 0.6 0.84%  operation 2 discount 3.62
            "002530",  # 金财互联 roe 4.19 pe 1.64 pb 2.55 dividend 0.5 0.35%  operation 2 discount 6.08
            "600284",  # 浦东建设 roe 4.18 pe 3.84 pb 1.09 dividend 1.5 2.24%  operation 6 discount 2.61
            "600748",  # 上实发展 roe 4.18 pe 4.04 pb 1.04 dividend 0.3 0.52%  operation 0 discount 2.48
            "000973",  # 佛塑科技 roe 4.17 pe 1.64 pb 2.54 dividend 0.3 0.48%  operation 2 discount 6.09
            "603077",  # 和邦生物 roe 4.16 pe 3.13 pb 1.33 dividend 0.2 1.19%  operation 2 discount 3.19
            "002460",  # 赣锋锂业 roe 4.16 pe 0.47 pb 8.85 dividend 3.0 0.55%  operation 2 discount 21.28
            "300280",  # 紫天科技 roe 4.16 pe 1.42 pb 2.93 dividend 0.1 0.03%  operation 2 discount 7.05
            "002520",  # 日发精机 roe 4.15 pe 2.13 pb 1.95 dividend 1.00066 1.4%  operation 6 discount 4.7
            "600131",  # 国网信通 roe 4.14 pe 0.51 pb 8.09 dividend 0.5 0.24%  operation 2 discount 19.52
            "603123",  # 翠微股份 roe 4.14 pe 2.81 pb 1.47 dividend 1.2 1.33%  operation 2 discount 3.55
            "603166",  # 福达股份 roe 4.14 pe 2.49 pb 1.66 dividend 1.5 2.55%  operation 2 discount 4.01
            "600098",  # 广州发展 roe 4.13 pe 4.18 pb 0.99 dividend 1.0 1.63%  operation 6 discount 2.39
            "600635",  # 大众公用 roe 4.13 pe 2.44 pb 1.7 dividend 0.6 1.32%  operation 0 discount 4.1
            "000547",  # 航天发展 roe 4.13 pe 1.27 pb 3.26 dividend 0.55 0.36%  operation 6 discount 7.89
            "000600",  # 建投能源 roe 4.12 pe 5.18 pb 0.8 dividend 1.0 2.0%  operation 2 discount 1.93
            "000912",  # 泸天化 roe 4.12 pe 2.86 pb 1.44 dividend 1.0 2.19%  operation 2 discount 3.5
            "300075",  # 数字政通 roe 4.12 pe 1.56 pb 2.65 dividend 0.3 0.21%  operation 2 discount 6.43
            "300328",  # 宜安科技 roe 4.12 pe 0.68 pb 6.1 dividend 0.5 0.3%  operation 2 discount 14.81
            "000096",  # 广聚能源 roe 4.11 pe 1.77 pb 2.33 dividend 0.2 0.18%  operation 2 discount 5.66
            "300329",  # 海伦钢琴 roe 4.11 pe 1.89 pb 2.17 dividend 0.35 0.43%  operation 2 discount 5.29
            "600488",  # 天药股份 roe 4.1 pe 2.07 pb 1.97 dividend 0.56 1.11%  operation 6 discount 4.82
            "002267",  # 陕天然气 roe 4.1 pe 3.29 pb 1.25 dividend 1.0 1.53%  operation 2 discount 3.04
            "002390",  # 信邦制药 roe 4.1 pe 2.2 pb 1.86 dividend 0.3 0.55%  operation 2 discount 4.54
            "300005",  # 探路者 roe 4.1 pe 2.61 pb 1.57 dividend 2.0 4.67%  operation 2 discount 3.83
            "300321",  # 同大股份 roe 4.1 pe 1.54 pb 2.66 dividend 0.6 0.31%  operation 2 discount 6.49
            "600717",  # 天津港 roe 4.09 pe 5.72 pb 0.71 dividend 1.08 1.84%  operation 2 discount 1.75
            "000607",  # 华媒控股 roe 4.09 pe 1.51 pb 2.71 dividend 0.11 0.24%  operation 2 discount 6.62
            "002276",  # 万马股份 roe 4.09 pe 1.63 pb 2.51 dividend 0.2 0.2%  operation 2 discount 6.14
            "300020",  # 银江股份 roe 4.09 pe 2.0 pb 2.05 dividend 0.3 0.29%  operation 2 discount 5.01
            "300331",  # 苏大维格 roe 4.08 pe 0.85 pb 4.79 dividend 1.0 0.32%  operation 2 discount 11.74
            "601007",  # 金陵饭店 roe 4.07 pe 2.35 pb 1.73 dividend 2.0 2.35%  operation 2 discount 4.26
            "002516",  # 旷达科技 roe 4.07 pe 2.81 pb 1.45 dividend 2.5 7.14%  operation 2 discount 3.56
            "600101",  # 明星电力 roe 4.05 pe 3.41 pb 1.19 dividend 0.5 0.76%  operation 6 discount 2.94
            "600120",  # 浙江东方 roe 4.05 pe 3.77 pb 1.07 dividend 1.0 0.98%  operation 2 discount 2.65
            "600824",  # 益民集团 roe 4.05 pe 2.86 pb 1.41 dividend 0.32 0.97%  operation 2 discount 3.49
            "300081",  # 恒信东方 roe 4.05 pe 1.59 pb 2.54 dividend 0.5 0.39%  operation 2 discount 6.28
            "002718",  # 友邦吊顶 roe 4.04 pe 2.43 pb 1.67 dividend 3.0 1.95%  operation 2 discount 4.12
            "600827",  # 百联股份 roe 4.03 pe 5.04 pb 0.8 dividend 1.8 2.26%  operation 2 discount 1.99
            "002316",  # 亚联发展 roe 4.03 pe 1.11 pb 3.62 dividend 0.15 0.18%  operation 2 discount 8.97
            "600259",  # 广晟有色 roe 4.02 pe 0.76 pb 5.32 dividend 0.2 0.06%  operation 2 discount 13.24
            "600362",  # 江西铜业 roe 4.02 pe 4.13 pb 0.97 dividend 2.0 1.39%  operation 2 discount 2.42
            "000089",  # 深圳机场 roe 4.02 pe 2.78 pb 1.45 dividend 0.86 1.02%  operation 6 discount 3.6
            "002026",  # 山东威达 roe 4.02 pe 4.29 pb 0.94 dividend 0.8 1.41%  operation 2 discount 2.33
            "002366",  # 台海核电 roe 4.02 pe 2.24 pb 1.8 dividend 0.39 0.61%  operation 2 discount 4.47
            "300164",  # 通源石油 roe 4.02 pe 3.02 pb 1.33 dividend 1.0 1.89%  operation 2 discount 3.32
            "002500",  # 山西证券 roe 4.01 pe 2.15 pb 1.87 dividend 0.5 0.6%  operation 2 discount 4.66        }

    def get_stock_list(self):
        return self.stock_list
