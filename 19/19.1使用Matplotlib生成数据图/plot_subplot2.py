"""
如图19.10所示的显示效果比较差,程序明明只要显示3个子图,但第4个位置被空出来了,能不能让某个子图占多个网格呢?
答案是肯定的,程序做好控制即可。例如,将上面程序改为如下形式。
"""
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# 定义从-pi到pi之间的数据,平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①
# 将整个figure分成两行一列,第三个参数表示该图形放在第1个网格
plt.subplot(2, 1, 1)
# 绘制正弦曲线
plt.plot(x_data, np.sin(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正弦曲线')

# 将整个figure分成两行两列,并将该图形放在第4个网格
plt.subplot(223)
# 绘制余弦曲线
plt.plot(x_data, np.cos(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('余弦曲线')

# 将整个figure分成两行两列,并该图形放在第4个网格
plt.subplot(224)
# 绘制正切曲线
plt.plot(x_data, np.tan(x_data))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title('正切曲线')

plt.show()
"""
上面程序中第一行粗体字代码将整个区域分成两行一列,并指定子图占用第1个网格,也就是整个区域的第一行;
第二行粗体字代码将整个区域分成两行两列,并指定子图占用第3个网格——注意不是第2个网络,因为第一个子图已经占用了第一行——
对于两行两列的网格来说,第一个子图已经占用了两个网格,因此此处指定子图占用第3个网格,这意味着该子图在第二行第一格;
第三行粗体字代码将整个区域分成两行两列,并指定子图占用第4个网格,这意味着该子图会在第二行第二格。

运行上面程序,可以看到如图19. 11所示的效果。
"""