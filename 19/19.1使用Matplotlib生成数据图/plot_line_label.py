"""
19.1.4 管理坐标轴

可以调用 xlable()和 ylabel()函数分别设置 X 轴、Y 轴的名称,也可以通过title()函数设置整个数据图的标题,
还可以调用xticks()、yticks()函数分别改变X 轴 、Y 轴的刻度值(允许使用文本作 为刻度值)。
例如,如下程序为数据图添加了名称、标题和坐标轴刻度值。
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--', label='疯狂Java讲义年销量')
plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.', label='疯狂Android讲义年销量')
# 使用Matplotlib的字体管理器加载中文字体
# my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
my_font = fm.FontProperties(fname="C:\Windows\Fonts\STSONG.TTF")
# 调用legend函数设置图例
plt.legend(loc='best', prop=my_font)
# 设置两条坐标轴的名字
plt.xlabel("年份")
plt.ylabel("图书销量（本）")
# 设置数据图的标题
plt.title('疯狂图书的历年销量')
# 设置Y轴上的刻度值
# 第一个参数是点的位置,第二个参数是点的文字提示
plt.yticks([50000, 70000, 100000], [r'挺好', r'优秀', r'火爆'])
# 调用show()函数显示图形
plt.show()
"""
运行上面程序,可以看到如图19.8所示的效果。

上面程序中的前两行粗体字代码分别设置了X 轴 、Y 轴 的label, 因此可以看到图19.8中的X 轴和 Y 轴的标签发生了改变。
"""