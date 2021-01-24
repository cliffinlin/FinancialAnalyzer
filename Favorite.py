# -*- coding: utf-8 -*-


stock_list = {
    "600383",  # 金地集团 roi=111.69 roe=33.14 1/pe=26.33 rate=1.28 pb=1.18 dividend=6.7 yield=4.9% delta=18.61%
    "600606",  # 绿地控股 roi=93.16 roe=29.17 1/pe=29.57 rate=1.08 pb=0.92 dividend=4.0 yield=6.56% delta=22.17%
    "601668",  # 中国建筑 roi=89.16 roe=27.16 1/pe=30.68 rate=1.07 pb=0.77 dividend=1.85 yield=3.6% delta=11.73%
    "600048",  # 保利地产 roi=79.38 roe=31.33 1/pe=19.95 rate=1.27 pb=1.32 dividend=8.2 yield=5.11% delta=25.6%
    "000951",  # 中国重汽 roi=59.47 roe=34.08 1/pe=10.45 rate=1.67 pb=2.71 dividend=5.5 yield=1.72% delta=16.45%
    "000002",  # 万 科Ａ roi=56.86 roe=32.92 1/pe=17.1 rate=1.01 pb=1.63 dividend=10.17 yield=3.57% delta=20.87%
    "000921",  # 海信家电 roi=51.85 roe=28.9 1/pe=11.96 rate=1.5 pb=2.18 dividend=3.95 yield=2.69% delta=22.5%
    "000786",  # 北新建材 roi=50.05 roe=19.19 1/pe=4.29 rate=6.08 pb=3.82 dividend=0.82 yield=0.23% delta=5.35%
    "600585",  # 海螺水泥 roi=36.92 roe=27.86 1/pe=12.62 rate=1.05 pb=1.86 dividend=20.0 yield=3.76% delta=29.81%
    "000581",  # 威孚高科 roi=26.81 roe=17.14 1/pe=11.76 rate=1.33 pb=1.35 dividend=11.0 yield=4.63% delta=39.37%
    "600612",  # 老凤祥 roi=23.23 roe=28.21 1/pe=7.77 rate=1.06 pb=3.21 dividend=11.5 yield=2.44% delta=31.46%
    "000877",  # 天山股份 roi=21.12 roe=19.31 1/pe=10.62 rate=1.03 pb=1.63 dividend=5.1 yield=3.2% delta=30.12%
    "000049",  # 德赛电池 roi=20.49 roe=31.89 1/pe=6.12 rate=1.05 pb=4.25 dividend=7.0 yield=1.35% delta=22.08%
    "000895",  # 双汇发展 roi=20.24 roe=41.58 1/pe=3.99 rate=1.22 pb=6.7 dividend=16.4 yield=3.44% delta=86.18%
    "601088",  # 中国神华 roi=15.08 roe=13.77 1/pe=12.59 rate=0.87 pb=1.06 dividend=12.6 yield=6.61% delta=52.46%
    "600056",  # 中国医药 roi=14.87 roe=16.53 1/pe=9.37 rate=0.96 pb=1.59 dividend=2.76 yield=1.87% delta=19.92%
    "601318",  # 中国平安 roi=14.71 roe=21.45 1/pe=8.57 rate=0.8 pb=2.26 dividend=21.0 yield=2.39% delta=27.92%
    "600036",  # 招商银行 roi=14.35 roe=16.49 1/pe=8.53 rate=1.02 pb=1.76 dividend=12.0 yield=2.78% delta=32.64%
    "601607",  # 上海医药 roi=13.35 roe=12.57 1/pe=9.4 rate=1.13 pb=1.23 dividend=4.4 yield=2.28% delta=24.31%
    "600298",  # 安琪酵母 roi=12.92 roe=27.21 1/pe=3.23 rate=1.47 pb=7.31 dividend=4.0 yield=0.82% delta=25.24%
    "601319",  # 中国人保 roi=12.75 roe=15.48 1/pe=9.58 rate=0.86 pb=1.46 dividend=1.52 yield=2.32% delta=24.21%
    "000028",  # 国药一致 roi=10.7 roe=12.67 1/pe=7.82 rate=1.08 pb=1.49 dividend=6.0 yield=1.27% delta=16.28%
    "601336",  # 新华保险 roi=10.44 roe=15.87 1/pe=6.85 rate=0.96 pb=1.97 dividend=14.1 yield=2.38% delta=34.74%
    "600887",  # 伊利股份 roi=9.34 roe=30.24 1/pe=2.97 rate=1.04 pb=8.72 dividend=8.1 yield=1.99% delta=67.07%
    "600900",  # 长江电力 roi=9.2 roe=16.04 1/pe=5.36 rate=1.07 pb=2.71 dividend=6.8 yield=3.44% delta=64.23%
    "600104",  # 上汽集团 roi=8.95 roe=11.78 1/pe=10.0 rate=0.76 pb=1.13 dividend=8.8 yield=3.57% delta=35.68%
    "601006",  # 大秦铁路 roi=8.65 roe=10.58 1/pe=12.02 rate=0.68 pb=0.84 dividend=4.8 yield=7.27% delta=60.53%
    "600519",  # 贵州茅台 roi=8.46 roe=37.85 1/pe=2.05 rate=1.09 pb=15.61 dividend=170.25 yield=0.92% delta=45.11%
    "601601",  # 中国太保 roi=8.45 roe=13.91 1/pe=6.98 rate=0.87 pb=1.78 dividend=12.0 yield=3.21% delta=45.93%
    "600511",  # 国药股份 roi=8.05 roe=17.37 1/pe=4.78 rate=0.97 pb=3.24 dividend=6.38 yield=1.34% delta=28.07%
    "000001",  # 平安银行 roi=7.31 roe=10.06 1/pe=7.57 rate=0.96 pb=1.23 dividend=2.18 yield=1.19% delta=15.68%
    "000568",  # 泸州老窖 roi=7.07 roe=30.26 1/pe=1.87 rate=1.25 pb=13.69 dividend=15.9 yield=0.78% delta=41.47%
    "600690",  # 海尔智家 roi=6.89 roe=20.0 1/pe=4.99 rate=0.69 pb=3.64 dividend=3.75 yield=1.36% delta=27.16%
    "000858",  # 五 粮 液 roi=6.53 roe=29.28 1/pe=1.89 rate=1.18 pb=13.38 dividend=22.0 yield=0.79% delta=42.01%
    "600563",  # 法拉电子 roi=6.45 roe=21.35 1/pe=2.54 rate=1.19 pb=7.66 dividend=13.0 yield=1.41% delta=55.52%
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
    "600309",  # 万华化学 roi=4.39 roe=19.66 1/pe=2.9 rate=0.77 pb=6.22 dividend=13.0 yield=1.49% delta=51.45%
    "000651",  # 格力电器 roi=4.33 roe=16.27 1/pe=4.44 rate=0.6 pb=3.22 dividend=22.0 yield=3.58% delta=80.69%
    "002304",  # 洋河股份 roi=4.27 roe=20.46 1/pe=2.32 rate=0.9 pb=8.37 dividend=30.0 yield=1.41% delta=60.91%
    "600597",  # 光明乳业 roi=4.19 roe=12.04 1/pe=3.25 rate=1.07 pb=3.4 dividend=1.3 yield=0.78% delta=24.1%
    "603288",  # 海天味业 roi=4.05 roe=33.72 1/pe=1.0 rate=1.2 pb=33.59 dividend=10.8 yield=0.57% delta=57.41%
    "600030",  # 中信证券 roi=3.98 roe=8.73 1/pe=4.0 rate=1.14 pb=2.07 dividend=5.0 yield=1.74% delta=43.36%
    "600271",  # 航天信息 roi=3.97 roe=13.05 1/pe=6.21 rate=0.49 pb=2.02 dividend=2.31 yield=1.84% delta=29.63%
    "002025",  # 航天电器 roi=3.97 roe=16.77 1/pe=2.17 rate=1.09 pb=6.91 dividend=1.5 yield=0.28% delta=13.09%
    "600085",  # 同仁堂 roi=3.72 roe=13.3 1/pe=3.78 rate=0.74 pb=3.6 dividend=2.6 yield=1.04% delta=27.38%
    "000547",  # 航天发展 roi=3.64 roe=11.27 1/pe=2.2 rate=1.47 pb=4.74 dividend=0.88 yield=0.37% delta=16.83%
    "600436",  # 片仔癀 roi=3.4 roe=25.78 1/pe=1.09 rate=1.21 pb=19.73 dividend=8.2 yield=0.33% delta=30.56%
    "600377",  # 宁沪高速 roi=3.06 roe=9.37 1/pe=5.54 rate=0.59 pb=1.69 dividend=4.6 yield=4.96% delta=89.41%
    "000596",  # 古井贡酒 roi=2.66 roe=22.23 1/pe=1.41 rate=0.85 pb=13.89 dividend=15.0 yield=0.56% delta=39.57%
    "600600",  # 青岛啤酒 roi=2.2 roe=11.51 1/pe=1.68 rate=1.14 pb=6.47 dividend=5.5 yield=0.54% delta=32.44%
    "600897",  # 厦门空港 roi=1.27 roe=6.46 1/pe=4.58 rate=0.43 pb=1.39 dividend=5.23 yield=3.05% delta=66.68%
    "601888",  # 中国中免 roi=1.08 roe=18.79 1/pe=0.86 rate=0.67 pb=21.58 dividend=7.2 yield=0.33% delta=38.41%
    "600009",  # 上海机场 roi=0.0 roe=1.33 1/pe=0.28 rate=0.08 pb=4.9 dividend=7.9 yield=1.04% delta=369.28%
}