"""
数据画图工具 —— Python 入门练手项目

功能：
  读取 Excel/CSV 数据，生成折线图、柱状图、饼图
  适合制造业数据处理场景

依赖：
  pip install matplotlib pandas openpyxl
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# 设置中文字体，确保图表中的中文正常显示
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "WenQuanYi Micro Hei"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题


def 生成折线图(数据文件, x轴列, y轴列, 标题="折线图"):
    """从 Excel/CSV 读取数据生成折线图"""
    df = 读取数据(数据文件)

    if x轴列 not in df.columns or y轴列 not in df.columns:
        print(f"⚠️  列名不存在！可用列：{list(df.columns)}")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df[x轴列], df[y轴列], marker="o", linewidth=2, markersize=4)
    plt.title(标题, fontsize=14)
    plt.xlabel(x轴列)
    plt.ylabel(y轴列)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    保存文件 = f"{标题}.png"
    plt.savefig(保存文件, dpi=150)
    print(f"✅ 折线图已保存：{保存文件}")
    plt.show()


def 生成柱状图(数据文件, x轴列, y轴列, 标题="柱状图"):
    """从 Excel/CSV 读取数据生成柱状图"""
    df = 读取数据(数据文件)

    if x轴列 not in df.columns or y轴列 not in df.columns:
        print(f"⚠️  列名不存在！可用列：{list(df.columns)}")
        return

    plt.figure(figsize=(10, 5))
    plt.bar(df[x轴列], df[y轴列], color="#4A90D9", edgecolor="white")
    plt.title(标题, fontsize=14)
    plt.xlabel(x轴列)
    plt.ylabel(y轴列)
    plt.xticks(rotation=45)
    plt.tight_layout()

    保存文件 = f"{标题}.png"
    plt.savefig(保存文件, dpi=150)
    print(f"✅ 柱状图已保存：{保存文件}")
    plt.show()


def 生成饼图(数据文件, 标签列, 数值列, 标题="饼图"):
    """从 Excel/CSV 读取数据生成饼图"""
    df = 读取数据(数据文件)

    if 标签列 not in df.columns or 数值列 not in df.columns:
        print(f"⚠️  列名不存在！可用列：{list(df.columns)}")
        return

    plt.figure(figsize=(8, 8))
    plt.pie(df[数值列], labels=df[标签列], autopct="%1.1f%%",
            startangle=90, colors=plt.cm.Set3.colors)
    plt.title(标题, fontsize=14)
    plt.tight_layout()

    保存文件 = f"{标题}.png"
    plt.savefig(保存文件, dpi=150)
    print(f"✅ 饼图已保存：{保存文件}")
    plt.show()


def 读取数据(文件路径):
    """根据文件扩展名读取 Excel 或 CSV"""
    if 文件路径.endswith(".csv"):
        return pd.read_csv(文件路径)
    else:
        return pd.read_excel(文件路径)


def 查看数据文件(文件路径):
    """快速预览数据文件的结构"""
    df = 读取数据(文件路径)
    print(f"\n📂 文件：{文件路径}")
    print(f"📊 形状：{df.shape[0]} 行 × {df.shape[1]} 列")
    print(f"📋 列名：{list(df.columns)}")
    print(f"\n前 5 行数据：")
    print(df.head().to_string())
    return df


def 生成示例数据():
    """生成一个示例 Excel 文件，方便测试"""
    数据 = {
        "月份": ["1月", "2月", "3月", "4月", "5月", "6月",
                "7月", "8月", "9月", "10月", "11月", "12月"],
        "产量（件）": [1200, 1350, 1280, 1500, 1450, 1600,
                     1550, 1700, 1650, 1800, 1750, 2000],
        "良品率（%）": [95.2, 96.1, 94.8, 97.0, 96.5, 97.3,
                      96.8, 97.5, 97.1, 97.8, 97.4, 98.0]
    }
    df = pd.DataFrame(数据)
    文件名 = "示例数据.xlsx"
    df.to_excel(文件名, index=False)
    print(f"✅ 示例数据已生成：{文件名}")
    return 文件名


def 主菜单():
    """交互式主菜单"""
    print("=" * 45)
    print("📊 Python 数据画图工具")
    print("=" * 45)

    # 首次使用：生成示例数据
    if not os.path.exists("示例数据.xlsx"):
        print("\n💡 检测到首次使用，已自动生成示例数据文件。")
        生成示例数据()

    while True:
        print("\n🎛️  请选择功能：")
        print("  1. 查看数据文件结构")
        print("  2. 生成折线图")
        print("  3. 生成柱状图")
        print("  4. 生成饼图")
        print("  5. 重新生成示例数据")
        print("  q. 退出")

        选择 = input("\n👉 请输入选项：").strip()

        if 选择.lower() == "q":
            break

        elif 选择 == "1":
            文件 = input("  数据文件路径（默认：示例数据.xlsx）：").strip()
            文件 = 文件 if 文件 else "示例数据.xlsx"
            if os.path.exists(文件):
                查看数据文件(文件)
            else:
                print(f"⚠️  文件不存在：{文件}")

        elif 选择 in ["2", "3", "4"]:
            文件 = input("  数据文件路径（默认：示例数据.xlsx）：").strip()
            文件 = 文件 if 文件 else "示例数据.xlsx"
            if not os.path.exists(文件):
                print(f"⚠️  文件不存在：{文件}")
                continue

            df = 查看数据文件(文件)
            x列 = input("  X轴/标签列名：").strip()
            y列 = input("  Y轴/数值列名：").strip()
            标题 = input("  图表标题（可选）：").strip() or "数据图表"

            if 选择 == "2":
                生成折线图(文件, x列, y列, 标题)
            elif 选择 == "3":
                生成柱状图(文件, x列, y列, 标题)
            else:
                生成饼图(文件, x列, y列, 标题)

        elif 选择 == "5":
            生成示例数据()

        else:
            print("⚠️  无效选项，请重新输入！")

    print("\n👋 再见！")


if __name__ == "__main__":
    主菜单()
