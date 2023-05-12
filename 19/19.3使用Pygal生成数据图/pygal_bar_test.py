"""
19.3	使用 Pygal 生成数据图

Pygal 是另一个简单易用的数据图库,它以面向对象的方式来创建各种数据图,而且使用 Pygal 可以非常方便地生成各种格式的数据图,
包括PNG、SVG 等。使用 Pygal 也可以生成XML etree、HTML 表格(这些都需要安装其他包)。

19.3.1 安装 Pygal 包

安装 Pygal 包与安装其他 Python 包基本相同,同样可以使用pip来安装。

启动命令行窗口,在命令行窗口中输入如下命令。
pip install pygal

上面命令将会自动安装 Pygal 包的最新版本。运行上面命令,可以看到程序先下载 Pygal 包, 然后提示 Pygal 包安装成功。
Installing	collected	packages:pygal
Successfully	installed	pygal-2.4.0

如果在命令行窗口中提示找不到 pip 命令,则也可以通过 python 命令运行 pip 模块来安装 Pygal。 例如,通过如下命令来安装Pygal包。
python -m pip install pygal

在成功安装 Pygal 包之后,可以通过 pydoc 来查看 Pygal 包的文档。在命令行窗口中输入如下命令,
python -m pydoc -p 8899

运行上面命令之后,打开浏览器查看 http://localhost:8899/页面,可以在 Python 安装目录的 liblsite-packages下看到Pygal包的文档,
如图19.20所示。
单击图19.20所示页面上的"pygal(package)"链接,将可以看到如图19.21所示的API 页面。
通过图19.21所示的页面,即可查看Pygal包下的子模块和类。

19.3.2 Pygal数据图入门

Pygal使用面向对象的方式来生成数据图。使用 Pygal 生成数据图的步骤大致如下。
① 创建 Pygal 数据图对象。Pygal 为不同的数据图提供了不同的类,比如柱状图使用 pygal.Bar 类,饼图使用 pygal.Pie类,
折线图使用 pygal.Line 类,等等。
② 调用数据图对象的 add() 方法添加数据。
③ 调用 Config 对象的属性配置数据图。
④ 调用数据图对象的 render_to_xxx()方法将数据图渲染到指定的输出节点——此处的输出节点可以是PNG 图片、
SVG 文件,也可以是其他节点。

下面通过生成简单的柱状图来演示如何使用 Pygal 生成数据图,该柱状图展示了两种图书从 2011年到2017年的销量统计数据。
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
## 设置X轴的刻度值
# bar.x_labels = x_data
# bar.title = '疯狂图书的历年销量'
## 设置X、Y轴的标题
# bar.x_title = '年份'
# bar.y_title = '销量'
# 指定将数据图输出到SVG文件中
bar.render_to_file('fk_books.svg')
"""
上面程序中第一行粗体字代码创建了 pygal.Bar 对象,该对象就代表一个柱状图。接下来的两行粗体字代码为 pygal.Bar 
对象添加了两组柱状图数据。通过上面程序,实际上已经可以生成简单的柱状图了。如果注释掉后面对 pygal.Bar 对象的属性赋值的代码,运行
该程序,将可以看到在程序当前目录下生成了一个 fk_books.svg 文件,使用浏览器查看该文件,可以看到如图19.22所示的柱状图。

从图19.22所示的柱状图可以看到,这个数据图的 X 轴没有刻度值, X 轴、Y轴没有名称,它们都可以通过 pygal.Bar对象来配置。
接下来程序为 pygal.Bar 对象的title、x_labels、x_title、y_title 属性赋值,已经属于配置数据图的部分了,其分别配置了数据图的标题、
X 轴的刻度值、X 轴的名称、Y 轴的名称。

在增加上面的配置代码之后,再次运行该程序,程序会再次生成一个 SVG 文件。由于 SVG 文件支持交互,因此,
当用户把鼠标指针移到某个条柱上时,将可以看到关于该条柱的信息,如图19.23所示。

"""