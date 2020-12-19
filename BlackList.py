# -*- coding: utf-8 -*-


class BlackList:
    def __init__(self):
        self.stock_list = {
            #民营企业
            "600466",  # 蓝光发展 roi=113.45 roe=32.86 1/pe=29.51 rate=1.17 pb=0.9 dividend=2.87 yield=5.8% delta=19.65%
            "601155",  # 新城控股 roi=112.11 roe=50.31 1/pe=18.57 rate=1.2 pb=2.0 dividend=17.0 yield=4.83% delta=25.99%
            "000672",  # 上峰水泥 roi=75.97 roe=51.01 1/pe=13.54 rate=1.1 pb=2.78 dividend=9.0 yield=4.23% delta=31.21%
            "002146",  # 荣盛发展 roi=75.96 roe=24.79 1/pe=30.04 rate=1.02 pb=0.71 dividend=4.8 yield=6.9% delta=22.96%
            "002244",  # 滨江集团 roi=66.17 roe=23.46 1/pe=24.74 rate=1.14 pb=0.89 dividend=1.32 yield=2.72% delta=11.0%
            "000656",  # 金科股份 roi=61.88 roe=29.57 1/pe=18.04 rate=1.16 pb=1.37 dividend=4.5 yield=5.96% delta=33.05%
            "600340",  # 华夏幸福 roi=54.4 roe=24.84 1/pe=23.55 rate=0.93 pb=1.12 dividend=15.0 yield=10.76% delta=45.7%
            "000876",  # 新 希 望 roi=48.16 roe=32.2 1/pe=7.83 rate=1.91 pb=2.92 dividend=1.5 yield=0.64% delta=8.16%
            "603444",  # 吉比特 roi=17.82 roe=41.0 1/pe=4.14 rate=1.05 pb=8.19 dividend=50.0 yield=1.24% delta=29.93%
            "603678",  # 火炬电子 roi=4.9 roe=17.4 1/pe=2.01 rate=1.4 pb=7.57 dividend=1.7 yield=0.29% delta=14.55%
            "601636",  # 旗滨集团 roi=14.22 roe=21.0 1/pe=4.87 rate=1.39 pb=3.84 dividend=3.0 yield=2.4% delta=49.32%
            "600566",  # 济川药业 roi=10.35 roe=20.55 1/pe=6.63 rate=0.76 pb=2.62 dividend=12.3 yield=5.68% delta=85.56%
            "002287",  # 奇正藏药 roi=6.15 roe=19.2 1/pe=2.69 rate=1.19 pb=6.4 dividend=3.5 yield=1.21% delta=44.91%
            "002372",  # 伟星新材 roi=9.15 roe=28.57 1/pe=3.17 rate=1.01 pb=8.46 dividend=5.0 yield=2.42% delta=76.55%
            "002508",  # 老板电器 roi=11.0 roe=26.01 1/pe=3.99 rate=1.06 pb=5.53 dividend=5.0 yield=1.14% delta=28.62%
            "600380",  # 健康元 roi=30.23 roe=23.91 1/pe=8.72 rate=1.45 pb=2.62 dividend=1.6 yield=1.1% delta=12.58%
            "000963",  # 华东医药 roi=17.64 roe=26.42 1/pe=6.07 rate=1.1 pb=3.57 dividend=2.8 yield=0.96% delta=15.9%
            "300244",  # 迪安诊断 roi=25.83 roe=28.89 1/pe=5.29 rate=1.69 pb=4.61 dividend=1.28 yield=0.36% delta=6.88%
            "600998",  # 九州通 roi=45.39 roe=21.33 1/pe=10.38 rate=2.05 pb=1.72 dividend=0.0 yield=0.0% delta=0.0%
            "002007",  # 华兰生物 roi=3.16 roe=17.69 1/pe=1.82 rate=0.98 pb=11.3 dividend=4.0 yield=0.93% delta=51.0%
            "600352",  # 浙江龙盛 roi 26.53 rate 1.13 roe 22.95 pe 10.23 pb 1.88 dividend 2.5 1.68%  operation 0
            "002020",  # 京新药业 roi=4.65 roe=11.22 1/pe=5.31 rate=0.78 pb=2.16 dividend=3.5 yield=3.23% delta=60.78%
            "600363",  # 联创光电 roi=3.69 roe=11.12 1/pe=2.72 rate=1.22 pb=3.76 dividend=0.45 yield=0.19% delta=6.96%
            "002867",  # 周大生 roi=12.22 roe=22.01 1/pe=5.34 rate=1.04 pb=3.59 dividend=4.5 yield=1.8% delta=33.72%
            "600872",  # 中炬高新 roi=5.01 roe=24.34 1/pe=1.66 rate=1.24 pb=12.62 dividend=2.8 yield=0.4% delta=24.27%
            "601877",  # 正泰电器 roi=11.4 roe=17.92 1/pe=5.89 rate=1.08 pb=2.72 dividend=5.0 yield=1.51% delta=25.73%
            "002677",  # 浙江美大 roi=17.78 roe=36.25 1/pe=4.34 rate=1.13 pb=7.57 dividend=5.42 yield=3.1% delta=71.35%
            "002223",  # 鱼跃医疗 roi=27.25 roe=25.56 1/pe=5.67 rate=1.88 pb=3.81 dividend=4.0 yield=1.47% delta=25.89%
            "000671",  # 阳 光 城 roi 44.39 rate 1.34 roe 22.43 pe 14.77 pb 1.26 dividend 1.99 2.91%  operation 0
            "600763",  # 通策医疗 roi=2.13 roe=29.13 1/pe=0.73 rate=1.0 pb=31.63 dividend=0.0 yield=0.0% delta=0.0%
            "300284",  # 苏交科 roi=7.16 roe=11.66 1/pe=8.08 rate=0.76 pb=1.33 dividend=1.5 yield=2.23% delta=27.62%
            "600031",  # 三一重工 roi=28.08 roe=34.77 1/pe=5.81 rate=1.39 pb=4.78 dividend=4.2 yield=1.4% delta=24.02%
            "002439",  # 启明星辰 roi=5.41 roe=17.82 1/pe=2.49 rate=1.22 pb=5.03 dividend=0.25 yield=0.09% delta=3.54%
            "601677",  # 明泰铝业 roi=17.39 roe=13.74 1/pe=11.4 rate=1.11 pb=1.12 dividend=1.0 yield=0.73% delta=6.38%
            "000333",  # 美的集团 roi=10.82 roe=25.33 1/pe=4.23 rate=1.01 pb=5.26 dividend=16.0 yield=1.89% delta=44.77%
            "300760",  # 迈瑞医疗 roi=7.3 roe=36.21 1/pe=1.42 rate=1.42 pb=20.3 dividend=15.0 yield=0.41% delta=28.6%
            "600388",  # 龙净环保 roi=14.98 roe=15.94 1/pe=8.95 rate=1.05 pb=1.7 dividend=2.0 yield=2.19% delta=24.42%
            "002475",  # 立讯精密 roi=8.73 roe=28.1 1/pe=1.93 rate=1.61 pb=13.97 dividend=1.2 yield=0.24% delta=12.48%
            "000513",  # 丽珠集团 roi 2.91 rate 1.16 roe 9.07 pe 2.77 pb 4.05 dividend 11.5 2.29%  operation 0
            "300003",  # 乐普医疗 roi=15.1 roe=28.02 1/pe=4.31 rate=1.25 pb=4.88 dividend=2.0 yield=0.74% delta=17.04%
            "603589",  # 口子窖 roi=4.68 roe=19.63 1/pe=3.14 rate=0.76 pb=6.01 dividend=15.0 yield=2.19% delta=69.86%
            "002230",  # 科大讯飞 roi=1.59 roe=9.7 1/pe=1.29 rate=1.27 pb=7.0 dividend=1.0 yield=0.26% delta=20.23%
            "600557",  # 康缘药业 roi=2.91 roe=8.68 1/pe=5.0 rate=0.67 pb=1.62 dividend=0.8 yield=0.72% delta=14.34%
            "002035",  # 华帝股份 roi=7.68 roe=18.4 1/pe=6.23 rate=0.67 pb=2.75 dividend=3.0 yield=3.18% delta=51.04%
            "002311",  # 海大集团 roi=11.94 roe=28.71 1/pe=2.65 rate=1.57 pb=8.42 dividend=3.5 yield=0.58% delta=21.74%
            "600196",  # 复星医药 roi=4.76 roe=13.18 1/pe=2.8 rate=1.29 pb=4.36 dividend=3.9 yield=0.69% delta=24.75%
            "600660",  # 福耀玻璃 roi=1.85 roe=10.88 1/pe=2.4 rate=0.71 pb=4.52 dividend=7.5 yield=1.98% delta=82.76%
            "002262",  # 恩华药业 roi=9.85 roe=20.82 1/pe=4.08 rate=1.16 pb=4.27 dividend=1.0 yield=0.57% delta=14.1%
            "002271",  # 东方雨虹 roi=8.3 roe=18.97 1/pe=3.29 rate=1.33 pb=4.05 dividend=3.0 yield=0.88% delta=26.84%
            "002236",  # 大华股份 roi=27.31 roe=29.32 1/pe=6.38 rate=1.46 pb=3.5 dividend=1.33 yield=0.61% delta=9.62%
            "603899",  # 晨光文具 roi=5.43 roe=29.17 1/pe=1.59 rate=1.17 pb=14.65 dividend=4.0 yield=0.51% delta=32.05%
            "600643",  # 爱建集团 roi=12.56 roe=12.63 1/pe=10.25 rate=0.97 pb=1.13 dividend=2.5 yield=3.14% delta=30.6%
            "300015",  # 爱尔眼科 roi=1.71 roe=21.07 1/pe=0.64 rate=1.27 pb=29.87 dividend=1.5 yield=0.22% delta=34.22%
            "000739",  # 普洛药业 roi=7.96 roe=20.62 1/pe=2.72 rate=1.42 pb=6.58 dividend=1.65 yield=0.7% delta=25.86%
            "600987",  # 航民股份 roi=15.49 roe=15.65 1/pe=12.07 rate=0.82 pb=1.19 dividend=2.2 yield=4.0% delta=33.15%
            "300760",  # 迈瑞医疗 roi=7.76 roe=36.21 1/pe=1.51 rate=1.42 pb=19.11 dividend=15.0 yield=0.43% delta=28.6%
            "600570",  # 恒生电子 roi=2.09 roe=21.52 1/pe=1.0 rate=0.97 pb=27.9 dividend=5.3 yield=0.52% delta=51.91%
            "002242",  # 九阳股份 roi=8.75 roe=23.64 1/pe=3.49 rate=1.06 pb=6.01 dividend=5.8 yield=1.86% delta=53.32%
            "002032",  # 苏 泊 尔 roi=7.76 roe=27.48 1/pe=2.91 rate=0.97 pb=9.17 dividend=13.3 yield=1.81% delta=62.42%
            "600801",  # 华新水泥 roi=32.81 roe=30.64 1/pe=12.9 rate=0.83 pb=2.14 dividend=12.1 yield=5.38% delta=41.72%
            "600276",  # 恒瑞医药 roi=3.06 roe=20.91 1/pe=1.21 rate=1.21 pb=16.93 dividend=2.3 yield=0.26% delta=21.01%

            "600466",  # 蓝光发展 roi=113.45 roe=32.86 1/pe=29.51 rate=1.17 pb=0.9 dividend=2.87 yield=5.8% delta=19.65%
            "601155",  # 新城控股 roi=112.11 roe=50.31 1/pe=18.57 rate=1.2 pb=2.0 dividend=17.0 yield=4.83% delta=25.99%
            "000672",  # 上峰水泥 roi=75.97 roe=51.01 1/pe=13.54 rate=1.1 pb=2.78 dividend=9.0 yield=4.23% delta=31.21%
            "002146",  # 荣盛发展 roi=75.96 roe=24.79 1/pe=30.04 rate=1.02 pb=0.71 dividend=4.8 yield=6.9% delta=22.96%
            "002244",  # 滨江集团 roi=66.17 roe=23.46 1/pe=24.74 rate=1.14 pb=0.89 dividend=1.32 yield=2.72% delta=11.0%
            "000656",  # 金科股份 roi=61.88 roe=29.57 1/pe=18.04 rate=1.16 pb=1.37 dividend=4.5 yield=5.96% delta=33.05%
            "600340",  # 华夏幸福 roi=54.4 roe=24.84 1/pe=23.55 rate=0.93 pb=1.12 dividend=15.0 yield=10.76% delta=45.7%
            "000876",  # 新 希 望 roi=48.16 roe=32.2 1/pe=7.83 rate=1.91 pb=2.92 dividend=1.5 yield=0.64% delta=8.16%
            "600998",  # 九州通 roi=45.39 roe=21.33 1/pe=10.38 rate=2.05 pb=1.72 dividend=0.0 yield=0.0% delta=0.0%
            "000671",  # 阳 光 城 roi=41.31 roe=23.99 1/pe=17.05 rate=1.01 pb=1.18 dividend=1.99 yield=2.89% delta=16.96%
            "600380",  # 健康元 roi=30.23 roe=23.91 1/pe=8.72 rate=1.45 pb=2.62 dividend=1.6 yield=1.1% delta=12.58%
            "002236",  # 大华股份 roi=28.64 roe=29.37 1/pe=6.68 rate=1.46 pb=3.35 dividend=1.33 yield=0.64% delta=9.61%
            "002223",  # 鱼跃医疗 roi=27.25 roe=25.56 1/pe=5.67 rate=1.88 pb=3.81 dividend=4.0 yield=1.47% delta=25.89%
            "600031",  # 三一重工 roi=27.02 roe=34.77 1/pe=5.59 rate=1.39 pb=4.97 dividend=4.2 yield=1.34% delta=24.02%
            "300244",  # 迪安诊断 roi=25.83 roe=28.89 1/pe=5.29 rate=1.69 pb=4.61 dividend=1.28 yield=0.36% delta=6.88%
            "002677",  # 浙江美大 roi=18.43 roe=36.25 1/pe=4.5 rate=1.13 pb=7.31 dividend=5.42 yield=3.21% delta=71.35%
            "600352",  # 浙江龙盛 roi=17.83 roe=19.16 1/pe=9.9 rate=0.94 pb=1.7 dividend=2.5 yield=1.78% delta=17.97%
            "603444",  # 吉比特 roi=17.82 roe=41.0 1/pe=4.14 rate=1.05 pb=8.19 dividend=50.0 yield=1.24% delta=29.93%
            "000963",  # 华东医药 roi=17.64 roe=26.42 1/pe=6.07 rate=1.1 pb=3.57 dividend=2.8 yield=0.96% delta=15.9%
            "601677",  # 明泰铝业 roi=17.39 roe=13.74 1/pe=11.4 rate=1.11 pb=1.12 dividend=1.0 yield=0.73% delta=6.38%
            "000513",  # 丽珠集团 roi=16.09 roe=19.27 1/pe=5.25 rate=1.59 pb=3.47 dividend=11.5 yield=2.7% delta=51.36%
            "600987",  # 航民股份 roi=15.49 roe=15.65 1/pe=12.07 rate=0.82 pb=1.19 dividend=2.2 yield=4.0% delta=33.15%
            "300003",  # 乐普医疗 roi=15.1 roe=28.02 1/pe=4.31 rate=1.25 pb=4.88 dividend=2.0 yield=0.74% delta=17.04%
            "600388",  # 龙净环保 roi=14.98 roe=15.94 1/pe=8.95 rate=1.05 pb=1.7 dividend=2.0 yield=2.19% delta=24.42%
            "601636",  # 旗滨集团 roi=14.97 roe=21.0 1/pe=5.13 rate=1.39 pb=3.65 dividend=3.0 yield=2.53% delta=49.32%
            "600643",  # 爱建集团 roi=12.56 roe=12.63 1/pe=10.25 rate=0.97 pb=1.13 dividend=2.5 yield=3.14% delta=30.6%
            "002867",  # 周大生 roi=12.22 roe=22.01 1/pe=5.34 rate=1.04 pb=3.59 dividend=4.5 yield=1.8% delta=33.72%
            "002311",  # 海大集团 roi=11.94 roe=28.71 1/pe=2.65 rate=1.57 pb=8.42 dividend=3.5 yield=0.58% delta=21.74%
            "002508",  # 老板电器 roi=11.83 roe=26.01 1/pe=4.29 rate=1.06 pb=5.15 dividend=5.0 yield=1.23% delta=28.62%
            "601877",  # 正泰电器 roi=11.4 roe=17.92 1/pe=5.89 rate=1.08 pb=2.72 dividend=5.0 yield=1.51% delta=25.73%
            "000333",  # 美的集团 roi=10.82 roe=25.33 1/pe=4.23 rate=1.01 pb=5.26 dividend=16.0 yield=1.89% delta=44.77%
            "600566",  # 济川药业 roi=10.35 roe=20.55 1/pe=6.63 rate=0.76 pb=2.62 dividend=12.3 yield=5.68% delta=85.56%
            "002372",  # 伟星新材 roi=10.1 roe=28.57 1/pe=3.5 rate=1.01 pb=7.67 dividend=5.0 yield=2.68% delta=76.55%
            "002262",  # 恩华药业 roi=9.85 roe=20.82 1/pe=4.08 rate=1.16 pb=4.27 dividend=1.0 yield=0.57% delta=14.1%
            "002242",  # 九阳股份 roi=8.75 roe=23.64 1/pe=3.49 rate=1.06 pb=6.01 dividend=5.8 yield=1.86% delta=53.32%
            "002475",  # 立讯精密 roi=8.73 roe=28.1 1/pe=1.93 rate=1.61 pb=13.97 dividend=1.2 yield=0.24% delta=12.48%
            "002271",  # 东方雨虹 roi=8.3 roe=18.97 1/pe=3.29 rate=1.33 pb=4.05 dividend=3.0 yield=0.88% delta=26.84%
            "000739",  # 普洛药业 roi=7.96 roe=20.62 1/pe=2.72 rate=1.42 pb=6.58 dividend=1.65 yield=0.7% delta=25.86%
            "002032",  # 苏 泊 尔 roi=7.94 roe=27.48 1/pe=2.98 rate=0.97 pb=8.93 dividend=13.3 yield=1.86% delta=62.42%
            "002035",  # 华帝股份 roi=7.68 roe=18.4 1/pe=6.23 rate=0.67 pb=2.75 dividend=3.0 yield=3.18% delta=51.04%
            "300760",  # 迈瑞医疗 roi=7.3 roe=36.21 1/pe=1.42 rate=1.42 pb=20.3 dividend=15.0 yield=0.41% delta=28.6%
            "300284",  # 苏交科 roi=7.16 roe=11.66 1/pe=8.08 rate=0.76 pb=1.33 dividend=1.5 yield=2.23% delta=27.62%
            "002287",  # 奇正藏药 roi=6.15 roe=19.2 1/pe=2.69 rate=1.19 pb=6.4 dividend=3.5 yield=1.21% delta=44.91%
            "002439",  # 启明星辰 roi=5.41 roe=17.82 1/pe=2.49 rate=1.22 pb=5.03 dividend=0.25 yield=0.09% delta=3.54%
            "603899",  # 晨光文具 roi=5.05 roe=29.17 1/pe=1.48 rate=1.17 pb=15.72 dividend=4.0 yield=0.48% delta=32.05%
            "600872",  # 中炬高新 roi=5.01 roe=24.34 1/pe=1.66 rate=1.24 pb=12.62 dividend=2.8 yield=0.4% delta=24.27%
            "603678",  # 火炬电子 roi=4.9 roe=17.4 1/pe=2.01 rate=1.4 pb=7.57 dividend=1.7 yield=0.29% delta=14.55%
            "600196",  # 复星医药 roi=4.76 roe=13.18 1/pe=2.8 rate=1.29 pb=4.36 dividend=3.9 yield=0.69% delta=24.75%
            "603589",  # 口子窖 roi=4.68 roe=19.63 1/pe=3.14 rate=0.76 pb=6.01 dividend=15.0 yield=2.19% delta=69.86%
            "002020",  # 京新药业 roi=4.65 roe=11.22 1/pe=5.31 rate=0.78 pb=2.16 dividend=3.5 yield=3.23% delta=60.78%
            "600363",  # 联创光电 roi=3.69 roe=11.12 1/pe=2.72 rate=1.22 pb=3.76 dividend=0.45 yield=0.19% delta=6.96%
            "002007",  # 华兰生物 roi=3.16 roe=17.69 1/pe=1.82 rate=0.98 pb=11.3 dividend=4.0 yield=0.93% delta=51.0%
            "600276",  # 恒瑞医药 roi=3.06 roe=20.91 1/pe=1.21 rate=1.21 pb=16.93 dividend=2.3 yield=0.26% delta=21.01%
            "600557",  # 康缘药业 roi=2.91 roe=8.68 1/pe=5.0 rate=0.67 pb=1.62 dividend=0.8 yield=0.72% delta=14.34%
            "600570",  # 恒生电子 roi=2.09 roe=21.52 1/pe=1.0 rate=0.97 pb=27.9 dividend=5.3 yield=0.52% delta=51.91%
            "600660",  # 福耀玻璃 roi=1.85 roe=10.88 1/pe=2.4 rate=0.71 pb=4.52 dividend=7.5 yield=1.98% delta=82.76%
            "600763",  # 通策医疗 roi=1.81 roe=29.13 1/pe=0.62 rate=1.0 pb=37.28 dividend=0.0 yield=0.0% delta=0.0%
            "300015",  # 爱尔眼科 roi=1.71 roe=21.07 1/pe=0.64 rate=1.27 pb=29.87 dividend=1.5 yield=0.22% delta=34.22%
            "002230",  # 科大讯飞 roi=1.59 roe=9.7 1/pe=1.29 rate=1.27 pb=7.0 dividend=1.0 yield=0.26% delta=20.23%
        }

    def get_stock_list(self):
        return self.stock_list
