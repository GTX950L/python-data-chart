# 📊 数据画图工具

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Level](https://img.shields.io/badge/练习-初学者-blue?style=flat-square)

</div>

一个用 Python + matplotlib 编写的命令行数据可视化工具，支持从 Excel/CSV 读取数据并生成各类图表。

## ✨ 功能

- 📈 **折线图** — 展示数据趋势变化
- 📊 **柱状图** — 对比不同类别数据
- 🥧 **饼图** — 展示占比分布
- 📂 支持 Excel (.xlsx) 和 CSV 两种格式
- 🎨 自动生成示例数据，方便测试
- 💾 图表自动保存为高清 PNG

## 📦 安装依赖

```bash
pip install matplotlib pandas openpyxl
```

## ⚡ 快速开始

```bash
# 直接运行，会自动生成示例数据
python data_chart.py
```

或者用代码调用：

```python
from data_chart import 生成折线图, 生成柱状图

# 从 Excel 生成折线图
生成折线图("生产数据.xlsx", x轴列="日期", y轴列="产量", 标题="月度产量趋势")
```

## 🧠 学到的知识点

| 知识点 | 应用 |
|--------|------|
| matplotlib | 绘制折线图、柱状图、饼图 |
| pandas | 读取 Excel/CSV 数据 |
| 中文字体设置 | 解决图表中文乱码问题 |
| 函数参数设计 | 灵活的图表生成接口 |
| 文件IO | 自动保存图表为 PNG |

---

📓 这是我的 Python 学习项目之一，记录从零开始学编程的过程。
