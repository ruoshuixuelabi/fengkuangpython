"""
19.4.6	仪表(Gauge)

仪表图类似于一个仪表盘,在仪表盘内使用不同的指针代表不同的数据。Pygal使用 pygal.Gauge 类表示仪表图。
程序在创建 pygal.Gauge 对象之后,为 pygal.Gauge 对象添加数据的方式与为 pygal.Pie 对象添加数据的方式相似。

pygal.Gauge对象有一个特别的属性：range,该属性用于指定仪表图的最小值和最大值。
下面程序示范了使用仪表图来展示各编程语言所占的市场比例。
"""
import pygal

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992, 
    0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python',
    'Visual Basic .NET', 'C#', 'PHP', 'JavaScript',
    'SQL', 'Assembly langugage', '其他']
# 创建pygal.Gauge对象（仪表图）
gauge = pygal.Gauge()
gauge.range = [0, 1]
# 采用循环为仪表图添加数据
for i, per in enumerate(data):
    gauge.add(labels[i], per)
gauge.title = '2018年8月编程语言'
# 设置将图例放在底部
gauge.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
gauge.render_to_file('language_percent.svg')
"""
上面程序中第一行粗体字代码创建了 pygal.Gauge 对象,接下来第二行粗体字代码对该对象的range 属性赋值,
将该仪表图的最大值赋值为1,最小值赋值为0。

运行该程序,将会生成如图19.31所示的仪表图。
"""