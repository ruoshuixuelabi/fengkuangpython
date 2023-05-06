"""
如果读者不想这么费劲来计算行、列,则可考虑使用 GridSpec 对绘图区域进行分割。例如,将上面程序改为如下形式。
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

plt.figure()
# 定义从-pi到pi之间的数据,平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)  # ①

# 将绘图区域分成2行3列
gs = gridspec.GridSpec(2, 3)
# 指定ax1占用第一行（0）整行
ax1 = plt.subplot(gs[0, :])
# 指定ax1占用第二行（1）的第一格（第二个参数0代表）
ax2 = plt.subplot(gs[1, 0])
# 指定ax1占用第二行（1）的第二、三格（第二个参数0代表）
ax3 = plt.subplot(gs[1, 1:3])

# 绘制正弦曲线
ax1.plot(x_data, np.sin(x_data))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.set_title('正弦曲线')

# 绘制余弦曲线
ax2.plot(x_data, np.cos(x_data))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.set_title('余弦曲线')

# 绘制正切曲线
ax3.plot(x_data, np.tan(x_data))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正切曲线')

plt.show()
"""
上面程序中的第一行粗体字代码将绘图区域分成两行三列;第二行粗体字代码调用 subplot(gs[0, :]), 指定 ax1 子图区域占用第一行整行,
其中第一个参数0代表行号,没有指定列范围,因此该子图在整个第一行;第三行粗体字代码调用subplot(gs[1,0]),
指定 ax2 子图区域占用第二行的第一格,其中第一个参数1代表第二行,第二个参数0代表第一格,因此该子图在第二行的第一格;
第四行粗体字代码调用subplot(gs[1,1:3]),指定 ax3 子图区域占用第二行的第二格到第三格,其中第一个参数 1代表第二行,
第二个参数1:3代表第二格到第三格, 因此该子图在第二行的第二格到第三格。

定义完ax1、ax2、ax3 这3个子图所占用的区域 之后,接下来程序就可以通过ax1、ax2、ax3 的方法在各自的子图区域绘图了。
运行上面程序,可以看到如图19.12所示的效果。
"""