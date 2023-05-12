"""
19.5.2	JSON数据

本书第10章已经介绍过 JSON 格式的数据,这种格式的数据通常会被转换为 Python 的 list 列表或 dict 字典 。

本节展示的是世界各国历年 GDP  总和,数据来源于https://datahub.io网站。数据格式如下：
[{"Country Code": "ARB", "Country Name": "Arab World", "Value": 25760683041.0857, "Year": 1968},
{"Country Code": "ARB", "Country Name": "Arab World", "Value": 28434203615.4829, "Year": 1969}

上面的 JSON 格式数据被保存在方括号内,这些数据将会被转换为 Python 的 list列表,而 list 列表的每个元素将会是一个 dict 对象 。

使用 Python 的 json 模块读取 JSON 数据非常简单,只要使用load()函数加载 JSON 值 。

下面程序示范了读取2016年中国的 GDP



"""
import json

filename = 'gdp_json.json'

with open(filename) as f:
    gpd_list = json.load(f)
# 遍历列表的每个元素,每个元素是一个GDP数据项
for gpd_dict in gpd_list:
    # 只显示中国、2016年的GDP
    if gpd_dict['Year'] == 2016 and gpd_dict['Country Code'] == 'CHN':
        print(gpd_dict['Country Name'], gpd_dict['Value'])
"""
上面程序中的一行粗体字代码调用 json 模块的 load() 函数加载 JSON 数据,该函数将会返回一个 list 列表,
接下来程序遍历该 list 列表即可访问到指定年份、指定国家的 GDP 值。

运行上面程序,可以看到如下输出结果。
China 11199145157649.2
"""