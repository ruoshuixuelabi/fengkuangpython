"""
19.1.5 管理多个子图

使用 Matplotlib 除可以生成包含多条折线的复式折线图之外,它还允许在一张数据图上包含多个子图。

调用 subplot() 函数可以创建一个子图,然后程序就可以在子图上进行绘制。
subplot(nrows, ncols, index, **kwargs) 函数的 nrows 参数指定将数据图区域分成多少行;ncols 参数指定将数据图区域分成多少列;
index 参数指定获取第几个区域。

subplot()函数也支持直接传入一个三位数的参数,其中第一位数将作为nrows 参数;第二位数将作为ncols参数;第三位数将作为index 参数。
下面程序示范了生成多个子图。
"""
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# 定义从-pi到pi之间的数据,平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①
# 将整个figure分成两行两列,第三个参数表示该图形放在第1个网格
plt.subplot(2, 2, 1)
# 绘制正弦曲线
plt.plot(x_data, np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线')

# 将整个figure分成两行两列,并将该图形放在第2个网格
plt.subplot(222)
# 绘制余弦曲线
plt.plot(x_data, np.cos(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('余弦曲线')

# 将整个figure分成两行两列,并该图形放在第3个网格
plt.subplot(223)
# 绘制正切曲线
plt.plot(x_data, np.tan(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正切曲线')
plt.show()
"""
上面程序多次调用 subplot() 函数来生成子图,每次调用 subplot() 函数之后的代码表示在该子图区域绘图。
上面程序将整个数据图区域分成2×2的网格,程序分别在第1个网格中绘制正弦曲线,在第2个网格中绘制余弦曲线,在第3个网格中绘制正切曲线。

可能有读者感到疑问：plot()函数不是用于绘制折线图的吗?怎么此处还可用于绘制正弦曲线、余弦曲线呢?其实此处绘制的依然是折线图。
看程序中的①号代码,这行代码调用 numpy  的  linspace()函数生成了一个包含多个数值的列表,
该数值列表的范围是从-pi到 pi, 平均分成64个数据点,程序中用到的numpy.sin()、numpy.cos()、numpy.tan()等函数也返回一个列表：
传入这些函数的列表包含多少个值,这些函数返回的列表也包含多少个值。
这意味着上面程序所绘制的折线图会包含64个转折点,由于这些转折点非常密集,看上去显得比较光滑,因此就变成了曲线。

提示：如果读者将程序中 x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True) 代码的64改为4、6等较小的数,
将会看到程序绘制的依然是折线图。

运行上面程序,可以看到如图19. 10所示的效果。
"""