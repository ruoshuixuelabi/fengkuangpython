"""
19.2.6	3D图形

3D 图形需要的数据与等高线图基本相同：X、Y 数据决定坐标点,Z 轴数据决定X、Y 坐标点对应的高度。
与等高线图使用等高线来代表高度不同,3D 图形将会以更直观的形式来表示高度。

为了绘制 3D 图形,需要调用 Axes3D 对象的 plot_surface()方法来完成。

下面程序将使用与前面等高线图相同的数据来绘制3D 图形,此时将看到程序会以更直观的形式来显示高度。
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))
ax = Axes3D(fig)
# Python 3.9 以下不需要加下面这行
fig.add_axes(ax)
delta = 0.125
# 生成代表X轴数据的列表
x = np.arange(-3.0, 3.0, delta)
# 生成代表Y轴数据的列表
y = np.arange(-2.0, 2.0, delta)
# 对x、y数据执行网格化
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
# 计算Z轴数据（高度数据）
Z = (Z1 - Z2) * 2
# 绘制3D图形
ax.plot_surface(X, Y, Z,
                rstride=1,  # rstride（row）指定行的跨度
                cstride=1,  # cstride(column)指定列的跨度
                cmap=plt.get_cmap('rainbow'))  # 设置颜色映射
# 设置Z轴范围
ax.set_zlim(-2, 2)
# 设置标题
plt.title("3D图")
plt.show()
"""
上面程序开始准备了和前一个程序相同的数据,只是该程序将 delta 设置为0.125,
这样可以避免生成太多的数据点(在绘制 3D 图形时,计算开销较大,如果数据点太多,Matplotlib 将会很卡)。

程序中粗体字代码调用 Axes3D 对象的 plot_surface()方法来绘制 3D 图形,其中X、Y 参数负责确定坐标点,
Z 参数决定X、Y 坐标点的高度数据。

运行上面程序,可以看到如图19. 19所示的3D 图形。
"""
