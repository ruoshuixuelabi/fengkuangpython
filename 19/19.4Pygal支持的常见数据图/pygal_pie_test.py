"""
19.4.4 饼图

Pygal 提供了 pygal.Pie 类来支持饼图,程序在创建 pygal.Pie 对象之后,同样需要调用 add() 方法来添加统计数据。

pygal.Pie对象支持如下两个特有的属性。
(1)inner_radius：设置饼图内圈的半径。通过设置该属性可实现环形数据图。
(2)half_pie：将该属性设置为 True,可实现半圆的饼图。

下面程序示范了使用饼图来展示2018年8月编程语言的统计数据。
"""
import pygal

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992, 0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python', 'Visual Basic .NET', 'C#', 'PHP', 'JavaScript',
          'SQL', 'Assembly langugage', '其他']
# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
# 采用循环为饼图添加数据
for i, per in enumerate(data):
    pie.add(labels[i], per)
pie.title = '2018年8月编程语言'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 设置内圈的半径长度
pie.inner_radius = 0.4
# 创建半圆数据图
pie.half_pie = True
# 指定将数据图输出到SVG文件中
pie.render_to_file('language_percent.svg')
"""
上面程序中第一行粗体字代码创建了一个 pygal.Pie 对象,该对象就表示一个饼图。
接下来程序使用循环为饼图添加了数据。程序中第二行粗体字代码设置 pygal.Pie 的 inner_radius 半径为0.4,这表明将该饼图设为空心环;
第三行粗体字代码设置 pygal.Pie 的 half_pie 为 True, 这表明将该饼图设为半圆。

如果将上面程序中后面两行粗体字代码注释掉,运行该程序,将会生成如图19.28所示的传统饼图。
如果取消这两行代码的注释,程序将会生成空心的半圆饼图,如图19.29所示。
"""