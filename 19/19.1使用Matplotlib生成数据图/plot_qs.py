"""
数据可视化、数据分析是 Python 的主要应用场景之一,Python 提供了丰富的数据分析、数据展示库来支持数据的可视化分析。
数据可视化分析对于挖掘数据的潜在价值、企业决策都具有非常大的帮助。

Python 为数据展示提供了大量优秀的功能包,其中 Matplotlib 和 Pygal 是两个极具代表性的功能包。
本章将从最简单的数据展示入门开始介绍,详细讲解 Matplotlib 和 Pygal 两个数据展示包的功能与用法。
本章也会通过实际的数据分析,来示范如何使用 Matplotlib 和 Pygal 展示本地数据文件和来自网络的数据。

19.1 使用 Matplotlib 生成数据图

Matplotlib 是一个非常优秀的 Python  2D绘图库,只要给出符合格式的数据,
通过 Matplotlib 就可以方便地制作折线图、柱状图、散点图等各种高质量的数据图。

19.1.1 安装Matplotlib包

安装 Matplotlib 包与安装其他 Python 包没有区别,同样可以使用 pip 来安装。

启动命令行窗口,在命令行窗口中输入如下命令。
pip install  matplotlib

上面命令将会自动安装 Matplotlib 包的最新版本。运行上面命令,可以看到程序先下载 Matplotlib包,然后提示Matplotlib包安装成功。

如果在命令行窗口中提示找不到 pip 命令,则也可以通过 python 命令运行 pip 模块来安装 Matplotlib包。
例如,通过如下命令来安装 Matplotlib 包。
python -m  pip   install   matplotlib

在成功安装 Matplotlib 包之后,可以通过 pydoc 来查看 Matplotlib 包的文档。在命令行窗口中输入如下命令。
python -m   pydoc -p  8899

运行上面命令之后,打开浏览器查看 http:/localhost:8899/页面,可以在 Python 安装目录的 lib/site-packages下看到Matplotlib包的文档

19.1.2	Matplotlib数据图入门

Matplotlib 的用法非常简单,对于最简单的折线图来说,程序只需根据需要给出对应的X 轴、Y 轴数据,
调用 pyplot 子模块下的 plot()函数即可生成简单的折线图。

假设分析《疯狂Java 讲义》这本书从2011年到2017年的销售数据,此时可考虑将年份作为X 轴数据,将图书各年销量作为Y 轴数据。
程序只要将2011—2017年定义成list列表作为X 轴数据,并将对应年份的销量作为Y 轴数据即可。

例如,使用如下简单的入门程序来展示这本书从2011年到2017年的销售数据。
"""
import matplotlib.pyplot as plt

# 定义2个列表分别作为X轴、Y轴数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# 第一个列表代表横坐标的值,第二个代表纵坐标的值
plt.plot(x_data, y_data)
# plt.plot(y_data)
# 调用show()函数显示图形
plt.show()
"""
上面程序中的第一行粗体字代码调用plot()函数根据X 轴、Y 轴数据来生成折线图,第二行粗体字代码则调用show()函数将折线图显示出来。

运行上面程序,可以看到生成如图19.3所示的简单折线图。

如果在调用 plot()函数时只传入一个list列表,该list列表的数据将作为Y 轴数据,那么Matplotlib 会自动使用0、1、2、3作为X 轴数据。
例如,将上面程序中的第一行粗体字代码改为如下形式。
plt.plot(y_data)

再次运行该程序,将看到如图19.4所示的结果。
"""