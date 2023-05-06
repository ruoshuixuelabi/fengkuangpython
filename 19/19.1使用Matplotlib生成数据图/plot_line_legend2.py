"""
Matplotlib 也允许在调用 plot() 函数时为每条折线分别传入 label 参数,这样程序在调用 legend() 函数时就无须传入labels、handles参数了。
例如如下程序。
"""
import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--', label='疯狂Java讲义年销量')
plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.', label='疯狂Android讲义年销量')
import matplotlib.font_manager as fm

# 使用Matplotlib的字体管理器加载中文字体
# my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
my_font = fm.FontProperties(fname="C:\Windows\Fonts\STSONG.TTF")
# 调用legend函数设置图例
plt.legend(loc='best', prop=my_font)
# 调用show()函数显示图形
plt.show()
"""
上面程序在调用 plot() 函数时传入了 label 参数,这样每条折线本身已经具有图例了,
因此程序在调用 legend()函数生成图例时无须传入labels参数,如上面程序中的第三行粗体字代码所示。

正如从上面程序中所看到的,每次绘制中文内容时都需要设置字体,那么是否能改变Matplotlib 的默认字体呢?答案是肯定的。

在 Python 的交互式解释器中输入如下两行命令。
import  matplotlib
matplotlib.matplotlib_fname()

其中 matplotlib_fname()函数会显示Matplotlib配置文件的保存位置,此处显示该文件的存储路径为
D:\Python\Python36lib lsite-packageslmatplotliblmpl-datalmatplotlibrc。打开该文件,找到如下这行代码。
#font.family :sans-serif

上面这行代码用于配置Matplotlib的默认字体,取消这行配置代码之前的注释符号(#),并将后面的 sans-serif修改为本地已有的中文字体。
例如使用微软雅黑字体,只要将上面的配置代码修改为如下形式即可。
font.family :Microsoft YaHei
通过上面设置,即可改变Matplotlib的默认字体,这样即可避免每次调用legend()函数时都需要额外指定字体。
"""