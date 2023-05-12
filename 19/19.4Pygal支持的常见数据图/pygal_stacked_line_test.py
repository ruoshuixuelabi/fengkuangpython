"""
与叠加柱状图类似的还有叠加折线图,叠加折线图使用 pygal.StackedLine 类来表示,
叠加折线图的第二组折线的数据点同样叠加在第一组折线的数据点上。

图19.27 叠加柱状图

关于叠加折线图的示例程序,可以参考本书配套代码中 pygal_stacked_line_test.py文件。

对应的是,如果客户需要让叠加柱状图和叠加折线图以水平方式显示,则 Pygal 提供了 pygal.HorizontalStackedBar
和pygal.HorizontalStackedLine类来生成水平叠加柱状图和水平叠加折线图 。
"""

import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.StackedBar对象（叠加折线图）
stacked_line = pygal.StackedLine()
# 添加两组数据
stacked_line.add('疯狂Java讲义', y_data)
stacked_line.add('疯狂Android讲义', y_data2)
# 设置X轴的刻度值
stacked_line.x_labels = x_data
# 重新设置Y轴的刻度值
stacked_line.y_labels = [20000, 40000, 60000, 80000, 100000]
stacked_line.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
stacked_line.x_title = '销量'
stacked_line.y_title = '年份'
# 设置将图例放在底部
stacked_line.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
stacked_line.render_to_file('fk_books.svg')
