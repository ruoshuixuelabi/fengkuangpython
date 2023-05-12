"""
19.4.5 点图

与柱状图使用条柱高度来代表数值的大小不同,点图使用点(圆)的大小来表示数值的大小。
Pygal 使用 pygal.Dot 类表示点图,创建点图的方式与创建柱状图的方式基本相同。

下面程序示范了使用点图来展示图书销量的统计数据。
"""
import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.Dot对象（点图）
dot = pygal.Dot()
dot.dots_size = 5
# 添加两组数据
dot.add('疯狂Java讲义', y_data)
dot.add('疯狂Android讲义', y_data2)
# 设置X轴的刻度值
dot.x_labels = x_data
# 重新设置Y轴的刻度值
dot.y_labels = ['疯狂Java讲义', '疯狂Android讲义']
# 设置Y轴刻度值的旋转角度
dot.y_label_rotation = 45
dot.title = '疯狂图书的历年销量'
# 设置X轴的标题
dot.x_title = '年份'
# 设置将图例放在底部
dot.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
dot.render_to_file('fk_books.svg')
"""
上面程序中的一行粗体字代码创建了 pygal.Dot 对象,该对象代表点图。在创建了pygal.Dot对象之后,
程序为该对象添加要展示的数据,然后配置该点图。

运行该程序,将会生成如图19.30所示的点图。
"""
