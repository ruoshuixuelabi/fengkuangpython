"""
在调用plot()函数时还可以传入额外的参数来指定折线的样子,如线宽、颜色、样式等。例如如下程序。
"""
import matplotlib.pyplot as plt

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.')
# 调用show()函数显示图形
plt.show()
"""
上面两行粗体字代码分别绘制了两条折线,并通过color指定折线的颜色,linewidth 指定线宽,linestyle 指定折线样式。

在使用 linestyle 指定折线样式时,该参数支持如下字符串参数值。
(1)-    代表实线,这是默认值。
(2)--   代表虚线。
(3):     代表点线 。
(4)-.   代表短线、点相间的虚线。
运行上面程序,可以看到如图19.6所示的折线图。
"""