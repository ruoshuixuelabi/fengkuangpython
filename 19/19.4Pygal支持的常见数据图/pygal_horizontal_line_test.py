"""
与水平柱状图类似的还有水平折线图,水平折线图使用 pygal.HorizontalLine 类来表示,水平折线图的 X 轴刻度值同样使用 y_labels 属
性来设置,而 Y 轴刻度值才使用x_labels属性来设置。
关于水平折线图的示例程序,可以参考pygal_horizontal_line_test.py文件。
"""
import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.HorizontalLine对象（水平折线图）
horizontal_line = pygal.HorizontalLine()
# 添加两组代表折线的数据
horizontal_line.add('疯狂Java讲义', y_data)
horizontal_line.add('疯狂Android讲义', y_data2)
# 设置Y轴（确实如此）的刻度值
horizontal_line.x_labels = x_data
# 重新设置X轴（确实如此）的刻度值
horizontal_line.y_labels = [20000, 40000, 60000, 80000, 100000]
horizontal_line.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
horizontal_line.x_title = '销量'
horizontal_line.y_title = '年份'
# 设置将图例放在底部
horizontal_line.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
horizontal_line.render_to_file('fk_books.svg')
