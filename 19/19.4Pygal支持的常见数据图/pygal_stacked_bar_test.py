"""
19.4.3	叠加柱状图和叠加折线图

有些时候,客户重点关心的不是两个产品在同一年的销量对比(应该使用普通柱状图),
而是两个产品的累计销量,此时应该使用叠加柱状图或叠加折线图。

对于叠加柱状图而言,代表第二组数据的条柱会叠加在代表第一组数据的条柱上,这样可以更方便地看到两组数据的累加结果。
叠加柱状图使用 pygal.StackedBar 类来表示,程序使用 pygal.StackedBar 创建叠加柱状图的步骤与创建普通柱状图的步骤基本相同。
下面程序示范了使用 pygal.StackedBar创建叠加柱状图来展示两种图书销量数据汇总的方法。
"""
import pygal

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 构造数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 创建pygal.StackedBar对象（叠加柱状图）
stacked_bar = pygal.StackedBar()
# 添加两组数据
stacked_bar.add('疯狂Java讲义', y_data)
stacked_bar.add('疯狂Android讲义', y_data2)
# 设置X轴的刻度值
stacked_bar.x_labels = x_data
# 重新设置Y轴的刻度值
stacked_bar.y_labels = [20000, 40000, 60000, 80000, 100000]
stacked_bar.title = '疯狂图书的历年销量'
# 设置X、Y轴的标题
stacked_bar.x_title = '销量'
stacked_bar.y_title = '年份'
# 设置将图例放在底部
stacked_bar.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
stacked_bar.render_to_file('fk_books.svg')
"""
上面程序中的粗体字代码创建了 pygal.StackedBar对象,该对象就代表一个叠加柱状图。
接下来程序同样先为叠 加柱状图添加数据,然后配置叠加柱状图 。

运行上面程序,将会生成如图19.27 所示的叠加柱状图。

从图19.27可以看到,代表第二组数据的条柱叠加在代表第一组数据的条柱上。
"""