"""
19.3.3 配置 Pygal 数据图

正如从前面程序所看到的,使用 pygal.Bar 生成数据图之后,程序可以通过对该对象的属性赋值来配置数据图。
那么,除设置上面这些简单的属性之外,是否还可以设置其他属性呢?答案是肯定的,查阅 http://localhost:8899/pygal.config.html
页面(其中8899是运行pydoc 的端口),可以看到 config 模块的相关说明,该模块包含了BaseConfig、CommonConfig、
Config、SerieConfig等配置类,这些类所包含的属性正是用于配置 Pygal 数据图的。

下面程序示范了该页面中部分配置属性的作用。
"""
import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两组柱状图的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.Bar对象（柱状图）
bar = pygal.Bar()
# 添加两组代表条柱的数据
bar.add('疯狂Java讲义', y_data)
bar.add('疯狂Android讲义', y_data2)
# 设置X轴的刻度值
bar.x_labels = x_data
bar.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
bar.x_title = '年份'
bar.y_title = '销量'
# 设置X轴的刻度值旋转45度
bar.x_label_rotation = 45
# 设置将图例放在底部
bar.legend_at_bottom = True
# 设置数据图四周的页边距
# 也可通过margin_bottom、margin_left、margin_right、margin_top只设置单独一边的页边距
bar.margin = 35
# 隐藏X轴上的网格线
bar.show_y_guides = False
# 显示X轴上的网格线
bar.show_x_guides = True
# 指定将数据图输出到SVG文件中
bar.render_to_file('fk_books.svg')
"""
运行上面程序,将会生成如图19.24所示的数据图。

对比图19.23和图19.24所示的数据图,可以发现图 19.24 所示的数据图的X 轴刻度值旋转了45°,这是 x_label_rotation 属性的作用;
数据图的图例被显示在底部,这是 legend_at_bottom 属性的作用;数据图不再显示水平方向的网格线,这是 show_y_guides 属性的作用;
数据图显示垂直方向的网格线,这是 show_x_guides 属性的作用。

对于不同的数据图,Pygal 支持大量对应的配置,具体可结合 http:/localhost:8899/pygal.config.html页面给出的属性进行设置、
测试,此处不再一一讲解。
"""