"""
19.2.2	柱状图

使用 Matplotlib 提供的 bar()函数来绘制柱状图。与前面介绍的 plot() 函数类似,程序每次调用 bar()函数时都会生成一组柱状图,
如果希望生成多组柱状图,则可通过多次调用bar()函数来实现。

下面程序使用柱状图来展示《疯狂Java 讲义》和《疯狂 Android 讲义》两种图书历年的销量数据。
"""
import matplotlib.pyplot as plt

# 构建数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 绘图
plt.bar(x=x_data, height=y_data, label='疯狂Java讲义', color='steelblue', alpha=0.8)
plt.bar(x=x_data, height=y_data2, label='疯狂Android讲义', color='indianred', alpha=0.8)
# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt.text(x, y + 100, '%s' % y, ha='center', va='top')
# 设置标题
plt.title("Java与Android图书对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("销量")
# 显示图例
plt.legend()
plt.show()
"""
上面程序中的前两行粗体字代码用于在数据图上生成两组柱状图,程序设置了这两组柱状图的颜色和透明度。

在使用 bar()函数绘制柱状图时,默认不会在柱状图上显示具体的数值。
为了能在柱状图上显示具体的数值,程序可以调用 text()函数在数据图上输出文字,如上面程序中第三行粗体字代码所示。

在使用 text()函数输出文字时,该函数的前两个参数控制输出文字的X、Y 坐标,第三个参数则控制输出的内容。
其中va 参数控制文字的垂直对齐方式, ha 参  数控制文字的水平对齐方式。
对于上面的程序来说,由 于X 轴数据是一个字符串列表,因此X 轴实际上是以列 表元素的索引作为刻度值的。
因此,当程序指定输出文 字的X 坐标为0时,表明将该文字输出到第一个条柱处;
对于 Y 坐标而言,条柱的数值正好在条柱高度所在处,如果指定 Y 坐标为条柱的数值+100,就是控制将文字输出到条柱略上一点的位置。

运行上面程序,可以看到如图19.14所示的效果。

从图19.14所示的显示效果来看,第二次绘制的柱状图完全与第一次绘制的柱状图重叠,这并不是我们期望的结果,我们希望每组数据的条柱能并列显示。
"""