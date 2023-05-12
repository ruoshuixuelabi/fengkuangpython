"""
19.2.4	散点图

散点图和折线图需要的数组非常相似,区别是折线图会将各数据点连接起来;而散点图则只是描绘各数据点,并不会将这些数据点连接起来。

调用Matplotlib 的 scatter()函数来绘制散点图,该函数支持如下常用参数。
(1)x：指定 X 轴数据。
(2)y：指定 Y 轴数据。
(3)s：指定散点的大小。
(4)c：指定散点的颜色。
(5)alpha：指定散点的透明度。
(6)linewidths：指定散点边框线的宽度。
(7)edgecolors：指定散点边框的颜色。
(8)marker：指定散点的图形样式。该参数支持'.'(点标记)、','(像素标记)、'o'(圆形标记)'v'(向下三角形标记)、
'^'(向上三角形标记)、'<'(向左三角形标记)、'>'(向右三角 形标记)、'1'(向下三叉标记)、'2'(向上三叉标记)、
'3'(向左三叉标记)、'4'(向右三叉标记)、 's'(正方形标记)、 'p'(五边形标记)、'*'(星形标记)、 'h'(八边形标记)、
'H'(另一种八边形标记)、'+'(加号标记)、'x'(x标记)、'D' (菱形标记)、'd'(尖菱形标记)、'|'(竖线标记)、'_'(横线标记)等值。
(9)cmap：指定散点的颜色映射,会使用不同的颜色来区分散点的值。

下面程序示范了如何使用scatter()函数来绘制散点图。
"""
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# 定义从-pi到pi之间的数据,平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①
# 将整个figure分成两行两列,第三个参数表示该图形放在第1个网格
# 沿着正弦曲线绘制散点图
plt.scatter(x_data, np.sin(x_data), c='purple',  # 设置点的颜色
            # plt.scatter(x_data, np.sin(x_data), cmap=plt.get_cmap('rainbow'), # 设置点的颜色
            s=50,  # 设置点半径
            alpha=0.5,  # 设置透明度
            marker='p',  # 设置使用五边形标记
            linewidths=1,  # 设置边框的线宽
            edgecolors=['green', 'yellow'])  # 设置边框的颜色
# 绘制第二个散点图（只包含一个起点）,突出起点
plt.scatter(x_data[0], np.sin(x_data)[0], c='red',  # 设置点的颜色
            s=150,  # 设置点半径
            alpha=1)  # 设置透明度
# 绘制第三个散点图（只包含一个结束点）,突出结束点
plt.scatter(x_data[63], np.sin(x_data)[63], c='black',  # 设置点的颜色
            s=150,  # 设置点半径
            alpha=1)  # 设置透明度
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线的散点图')
plt.show()
"""
上面程序使用 numpy 中的 linespace() 函数创建了一个列表作为 X 轴数据,程序使用np.sin()函数计算一系列sin 值作为 Y 轴数据。
程序中的粗体字代码负责生成一个散点图,该散点图包含64个数据点。

此外,程序在粗体字代码之后还调用了两次 scatter() 函数,这意味将会叠加两个散点图。
后面两次绘制散点图的代码分别用于绘制 x_data、sin(x+data)的第一个点和最后一个点,这样即可突出显示散点图的起点和结束点。

运行上面程序,可以看到如图19.17所示的效果。
"""