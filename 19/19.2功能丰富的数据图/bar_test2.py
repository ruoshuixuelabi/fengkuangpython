"""
为了实现条柱并列显示的效果,首先分析条柱重叠在一起的原因。
使用 Matplotlib 绘制柱状图时同样也需要 X 轴数据,本程序的 X 轴数据是元素为字符串的list列表,
因此程序实际上使用各字符串的索引作为X 轴数据。
比如'2011'字符串位于列表的第一个位置,因此代表该条柱的数据就被绘制在X 轴的刻度值1处——
由于两个柱状图使用了相同的X 轴数据,因此它们的条柱完全重合在一起。

为了将多个柱状图的条柱并列显示,程序需要为这些柱状图重新计算不同的X 轴数据。
为了精确控制条柱的宽度,程序可以在调用bar()函数时传入width参数,这样可以更好地计算条柱的并列方式。将上面程序改为如下形式。
"""
import matplotlib.pyplot as plt
import numpy as np

# 构建数据
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
bar_width = 0.3
# 将X轴数据改为使用range(len(x_data), 就是0、1、2...
plt.bar(x=range(len(x_data)), height=y_data, label='疯狂Java讲义', color='steelblue', alpha=0.8, width=bar_width)
# 将X轴数据改为使用np.arange(len(x_data))+bar_width, 
# 就是bar_width、1+bar_width、2+bar_width...这样就和第一个柱状图并列了
# plt.bar(x=np.arange(len(x_data))+bar_width, height=y_data2,
#    label='疯狂Android讲义', color='indianred', alpha=0.8, width=bar_width)
plt.bar(x=np.arange(len(x_data)) + bar_width + 0.05, height=y_data2,
        label='疯狂Android讲义', color='indianred', alpha=0.8, width=bar_width)
# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
    plt.text(x, y + 100, '%s' % y, ha='center', va='bottom')
for x, y in enumerate(y_data2):
    plt.text(x + bar_width, y + 100, '%s' % y, ha='center', va='top')
# 为X轴设置刻度值
plt.xticks(np.arange(len(x_data)) + bar_width / 2, x_data)
# 设置标题
plt.title("Java与Android图书对比")
# 为两条坐标轴设置名称
plt.xlabel("年份")
plt.ylabel("销量")
# 显示图例
plt.legend()
plt.show()
"""
该程序与前一个程序的区别就在于两行粗体字代码,这两行代码使用了不同的x参数,其中第一个柱状图的 X 轴数据为range(len(x data)),
也就是0、1、2 … ,这样第一个柱状图的各条柱恰好位于0、1、2 … 刻度值处;
第二个柱状图的X 轴数据为np.arange(len(x data))+bar_width, 也就是 bar_width、1+ bar_width、2+ bar_width… ,
这样第二个柱状图的各条柱位于0、1、2 … 刻度值的偏右一点 bar_width 处,这样就恰好与第一个柱状图的各条柱并列了。

运行上面程序,将会发现该柱状图的X 轴的刻度值变成0、1、2等值,不再显示年份。
为了让柱状图的X 轴的刻度值显示年份,程序可以调用xticks()函数重新设置X 轴的刻度值。例如,在程序中添加如下代码。
# 为X轴设置刻度值
plt.xticks(np.arange(len(x_data)) + bar_width / 2, x_data)

上面代码使用x data为 X 轴设置刻度值,第一个参数用于控制各刻度值的位置,该参数是(np.arange(len(x data))+bar_width/2,
也就是 bar_width/2、1+bar_width/2、2+bar_width/2等,这样这些刻度值将被恰好添加在两个条柱之间。

运行上面程序可看到如图19.15所示的运行结果。

有些时候,可能希望两个条柱之间有一点缝隙,那么程序只要对第二个条柱的X 轴数据略做修改即可。例如,将上面程序中的第二行粗体字
代码改为如下形式。
plt.bar(x=np.arange(len(x_data)) + bar_width + 0.05, height=y_data2,
        label='疯狂Android讲义', color='indianred', alpha=0.8, width=bar_width)

上面代码重新计算了 X 轴数据,使用mp.arange(len(x_data))+bar_width+0.05 作为 X 轴数据,因此两组柱状图的条柱之间会有0.05的距离。
"""