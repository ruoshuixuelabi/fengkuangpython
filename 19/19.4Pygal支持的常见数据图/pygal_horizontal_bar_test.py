"""
19.4.2	水平柱状图和水平折线图

使用 pygal.HorizontalBar 类来表示水平柱状图。使用 pygal.HorizontalBar 生成水平柱状图的步骤与创建普通柱状图的步骤基本相同。
下面程序示范了使用pygal.HorizontalBar生成水平柱状图来展示两种图书历年销量统计数据的方法。
"""
import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.HorizontalBar对象（水平柱状图）
horizontal_bar = pygal.HorizontalBar()
# 添加两组数据
horizontal_bar.add('疯狂Java讲义', y_data)
horizontal_bar.add('疯狂Android讲义', y_data2)
# 设置Y轴（确实如此）的刻度值
horizontal_bar.x_labels = x_data
# 重新设置X轴（确实如此）的刻度值
horizontal_bar.y_labels = [20000, 40000, 60000, 80000, 100000]
horizontal_bar.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
horizontal_bar.x_title = '销量'
horizontal_bar.y_title = '年份'
# 设置将图例放在底部
horizontal_bar.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
horizontal_bar.render_to_file('fk_books.svg')
"""
上面程序中第一行粗体字代码创建 pygal.HorizontalBar 对象作为水平柱状图,这与前面创建普通柱状图并无差别。
在设置 pygal.HorizontalBar 对象时有一点需要注意：x_labels 属性用于设置 Y 轴的刻度值,而y_labels属性用于设置X 轴的刻度值。

运行上面程序,将会生成如图19.26所示的水平柱状图。
"""
