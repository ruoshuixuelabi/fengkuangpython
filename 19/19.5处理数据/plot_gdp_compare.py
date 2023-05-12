"""
在掌握了使用 json 模块读取这份 JSON 数据的方法之后,接下来我们将会从中读取从2001年到2016年中国、美国、日本、俄罗斯、
加拿大这5个国家的GDP 数据,并使用柱状图进行对比。

下面程序将会使用 Matplotlib 生成柱状图来展示这5个国家的 GDP 数据。
"""
import json
from matplotlib import pyplot as plt
import numpy as np

filename = 'gdp_json.json'
# 读取JSON格式的GDP数据
with open(filename) as f:
    gpd_list = json.load(f)
# 使用list列表依次保存中国、美国、日本、俄罗斯、加拿大的GDP值
country_gdps = [{}, {}, {}, {}, {}]
country_codes = ['CHN', 'USA', 'JPN', 'RUS', 'CAN']
# 遍历列表的每个元素,每个元素是一个GDP数据项
for gpd_dict in gpd_list:
    for i, country_code in enumerate(country_codes):
        # 只读取指定国家的数据
        if gpd_dict['Country Code'] == country_code:
            year = gpd_dict['Year']
            # 只读取2001年到2016
            if 2017 > year > 2000:
                country_gdps[i][year] = gpd_dict['Value']
# 使用list列表依次保存中国、美国、日本、俄罗斯、加拿大的GDP值
country_gdp_list = [[], [], [], [], []]
# 构建时间数据
x_data = range(2001, 2017)
for i in range(len(country_gdp_list)):
    for year in x_data:
        # 除以1e8,让数值变成以亿为单位
        country_gdp_list[i].append(country_gdps[i][year] / 1e8)
bar_width = 0.15
fig = plt.figure(dpi=128, figsize=(15, 8))
colors = ['indianred', 'steelblue', 'gold', 'lightpink', 'seagreen']
# 定义国家名称列表
countries = ['中国', '美国', '日本', '俄罗斯', '加拿大']
# 采用循环绘制5组柱状图
for i in range(len(colors)):
    # 使用自定义X坐标将数据分开
    plt.bar(x=np.arange(len(x_data)) + bar_width * i, height=country_gdp_list[i],
            label=countries[i], color=colors[i], alpha=0.8, width=bar_width)
    # 仅为中国、美国的条柱上绘制GDP数值
    if i < 2:
        for x, y in enumerate(country_gdp_list[i]):
            plt.text(x, y + 100, '%.0f' % y, ha='center', va='bottom')
# 为X轴设置刻度值
plt.xticks(np.arange(len(x_data)) + bar_width * 2, x_data)
# 设置标题
plt.title("2001到2016年各国GDP对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("GDP(亿美元)")
# 显示图例
plt.legend()
plt.show()
"""
本程序的重点其实在于前半部分代码,这部分代码控制程序从 JSON 数据中只读取中国、美国、 日本、俄罗斯、加拿大这5个国家的数据,
且只读取从 2001 年到 2016 年的 GDP 数据,因此程序处理起来稍微有点麻烦——
程序先以年份为 key 的 dict(如程序中 country_gdps 列表的元素所示)来保存各国的GDP 数据。

但由于 Matplotlib 要求被展示数据是 list 列表,因此上面程序中的前两行粗体字代码使用循环依次读取从2001年到2016年的 GDP 数据,
并将这些数据添加到country gdp list列表的元素中。 这样就把dict形式的GDP 数据转换成list形式的GDP 数据。

上面程序中的后两行粗体字代码采用循环添加了5组柱状图,接下来程序还在中国、美国的条柱上绘制了GDP 值。
运行上面程序,可以看到如图 19.35所示的柱状图。
"""