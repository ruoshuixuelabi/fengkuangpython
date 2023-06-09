"""
如果通过 https://datahub.io 网站下载了世界各国人口数据,就可以计算出以上各国的人均GDP。
下面程序会使用 Pygal 来展示世界各国的人均 GDP 数据
"""

import json
import pygal

filename = 'gdp_json.json'
# 读取JSON格式的GDP数据
with open(filename) as f:
    gpd_list = json.load(f)
pop_filename = 'population-figures-by-country.json'
# 读取JSON格式的人口数据
with open(pop_filename) as f:
    pop_list = json.load(f)

# 使用list列表依次保存美国、日本、俄罗斯、加拿大的人均GDP值
country_mean_gdps = [{}, {}, {}, {}]
country_codes = ['USA', 'JPN', 'RUS', 'CAN']
# 遍历列表的每个元素,每个元素是一个GDP数据项
for gpd_dict in gpd_list:
    for i, country_code in enumerate(country_codes):
        # 只读取指定国家的数据
        if gpd_dict['Country Code'] == country_code:
            year = gpd_dict['Year']
            # 只读取2001年到2016
            if 2017 > year > 2000:
                for pop_dict in pop_list:
                    # 获取指定国家的人口数据
                    if pop_dict['Country_Code'] == country_code:
                        # 使用该国GDP总值除以人口数量,得到人均GDP
                        country_mean_gdps[i][year] = round(gpd_dict['Value']
                                                           / pop_dict['Population_in_%d' % year])
# 使用list列表依次保存美国、日本、俄罗斯、加拿大的人均GDP值
country_mean_gdp_list = [[], [], [], []]
# 构建时间数据
x_data = range(2001, 2017)
for i in range(len(country_mean_gdp_list)):
    for year in x_data:
        country_mean_gdp_list[i].append(country_mean_gdps[i][year])
# 定义国家名称列表
countries = ['美国', '日本', '俄罗斯', '加拿大']
# 创建pygal.Bar对象（柱状图）
bar = pygal.Bar()
# 采用循环添加代表条柱的数据
for i in range(len(countries)):
    bar.add(countries[i], country_mean_gdp_list[i])
bar.width = 1100
# 设置X轴的刻度值
bar.x_labels = x_data
bar.title = '2001到2016年各国人均GDP对比'
# 设置X、Y轴的标题
bar.x_title = '年份'
bar.y_title = '人均GDP(美元)'
# 设置X轴的刻度值旋转45度
bar.x_label_rotation = 45
# 设置将图例放在底部
bar.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
bar.render_to_file('mean_gdp.svg')
"""
上面程序中第一行粗体字代码加载了一份新的关于人口数据的 JSON 文件,这样程序即可通过该文件获取世界各国历年的人口数据。
第二行粗体字代码使用 GDP 总值除以该国的人口数量,这样就可以得到该国的人均 GDP。

该程序的后半部分代码创建了 pygal.Bar 对象,程序中第三行、第四行代码使用循环为该对象添加了各国人均GDP 数据,
这样该柱状图就可以展示各国的人均 GDP 值。
"""
