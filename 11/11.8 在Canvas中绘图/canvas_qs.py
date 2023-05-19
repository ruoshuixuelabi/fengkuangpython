"""
11.8	在 Canvas 中绘图

Tkinter提供了Canvas 组件来实现绘图。程序既可在 Canvas 中绘制直线、矩形、椭圆等各种 几何图形,也可绘制图片、文字、 UI 组件(如Button) 等 。Canvas 允许重新改变这些图形项(Tkinter 将程序绘制的所有东西统称为item) 的属性,比如改变其坐标、外观等。
11.8.1	Tkinter Canvas 的绘制功能
Canvas 组件的用法与其他GUI 组件一样简单,程序只要创建并添加Canvas 组件,然后调用该 组件的方法来绘制图形即可。如下程序示范了最简单的Canvas 绘图。
"""
from tkinter import *

# 创建窗口
root = Tk()
# 创建并添加Canvas
cv = Canvas(root, background='white')
cv.pack(fill=BOTH, expand=YES)
cv.create_rectangle(30, 30, 200, 200,
    outline='red', # 边框颜色
    stipple = 'question', # 填充的位图
    fill="red", # 填充颜色
    width=5 # 边框宽度
    )
cv.create_oval(240, 30, 330, 200,
    outline='yellow', # 边框颜色
    fill='pink', # 填充颜色
    width=4 # 边框宽度
    )
root.mainloop()
"""
上面程序先创建并添加了Canvas 组件,接下来粗体字
代码分别绘制了矩形和椭圆。运行上面程序,可以看到如
图11.49所示的效果。
从上面程序可以看到,Canvas 提供了create rectangle()
方法绘制矩形和create oval()方法绘制椭圆(包括圆,圆是
椭圆的特例)。实际上, Canvas 还提供了如下方法来绘制各
种图形。
> create arc: 绘制弧。
> create bitmap: 绘制位图。
> create image: 绘制图片。
> create line():绘制直线。
create    polygon: 绘制多边形。

( 336
仅供非商业用途或交流学习使用


create text:绘制文字。
create window:    绘制组件。
Canvas的坐标系统是绘图的基础,其默认的坐标系统如图11.8所示。其中点(0,0)位于Canvas 组件的左上角, X 轴水平向右延伸, Y 轴垂直向下延伸。
绘制上面这些图形时需要简单的几何基础。
在 使 用create line()绘制直线时,需要指定两个点的坐标,分别作为直线的起点和终点。
在 使 用create rectangle()绘制矩形时,需要指定两个点的坐标,分别作为矩形左上角点和右 下角点的坐标。
在 使 用 create oval()绘制椭圆时,需要指定两个点的坐标,分别作为左上角点和右下角点 的坐标来确定一个矩形,而该方法则负责绘制该矩形的内切椭圆,如图11.50所示。


从图11.50可以看出,只要矩形确定下来,该矩形的内切 椭圆就能确定下来,而 create oval()方法所需要的两个坐标正 是用于指定该矩形的左上角点和右下角点的坐标。
> 在 使 用create arc绘制弧时,和create oval的用法相似, 因为弧是椭圆的一部分,因此同样也是指定左上角和 右下角两个点的坐标,默认总是绘制从3点(0)开始,  逆时针旋转90°的那一段弧。程序可通过start改变起 始角度,也可通过extent改变转过的角度。
在 使 用create polygon绘制多边形时,需要指定多个点 的坐标来作为多边形的多个定点。



图11.50 内切椭圆

在 使 用create bitmap、create image、create text、create window等方法时,只要指定一个 坐标点,用于指定目标元素的绘制位置即可。
在绘制这些图形时可指定如下选项。
fll:  指定填充颜色。如果不指定该选项,默认不填充。
outline: 指定边框颜色。
> width: 指定边框宽度。如果不指定该选项,边框宽度默认为1。
dash:   指定边框使用虚线。该属性值既可为单独的整数,用于指定虚线中线段的长度；也 可为形如(5,2,3)格式的元素,此时5指定虚线中线段的长度,2指定间隔长度,3指定虚线 长度……依此类推。
stipple: 使用位图平铺进行填充。该选项可与fill选项结合使用, fill选项用于指定位图的 颜色。
style:  指定绘制弧的样式。该选项仅对create arc方法起作用。该选项支持PIESLICE (扇 形 ) 、CHORD  ( 弓 形 ) 、ARC  (仅绘制弧)选项值。
start: 指定绘制弧的起始角度。该选项仅对create arc方法起作用。
> extent: 指定绘制弧的角度。该选项仅对create arc方法起作用。
arrow:  指定绘制直线时两端是否有箭头。该选项支持NONE  (两端无箭头)、 FIRST ( 开 始端有箭头)、 LAST (结束端有箭头)、 BOTH  (两端都有箭头)选项值。
arrowshape:  指定箭头形状。该选项是一个形如"202010"的字符串,字符串中的三个整数 依次指定填充长度、箭头长度、箭头宽度。
>joinstyle: 指定直接连接点的风格。仅对绘制直线和多向形有效。该选项支持METTER  (连 接点形状如 → )、ROUND  (连接点形状如》)、 BEVEL  (连接点形状如)选项值。
>anchor: 指定绘制文字、 GUI 组件的位置。该选项仅对create text()、create window()方法 有效。

337
仅供非商业用途或交流学习使用

疯 担Python                                                疯狂软件教育

justify:  指定文字的对齐方式。该选项支持CENTER、LEFT、RIGHT      常量值,该选项仅对
create text方法有效。
"""