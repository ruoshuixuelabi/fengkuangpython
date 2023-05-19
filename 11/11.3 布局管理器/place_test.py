"""
11.3.3	Place布局管理器

Place 布局就是其他 GUI 编程中的"绝对布局",这种布局方式要求程序显式指定每个组件的绝对位置或相对于其他组件的位置。

如果要使用 Place 布局,调用相应组件的 place()方法即可。在使用该方法时同样支持一些详细的选项,关于这些选项的介绍如下。
(1)x：指定组件的 X 坐标。x 为0代表位于最左边。
(2)y：指定组件的 Y 坐标。 y 为0代表位于最右边。
(3)relx：指定组件的 X 坐标,以父容器总宽度为单位1,该值应该在0.0~1.0之间,
其中0.0 代表位于窗口最左边,1.0代表位于窗口最右边,0.5代表位于窗口中间。
(4)rely：指定组件的 Y 坐标,以父容器总高度为单位1,该值应该在0.0~1.0之间,
其中0.0 代表位于窗口最上边,1.0代表位于窗口最下边,0.5代表位于窗口中间。
(5)width：指定组件的宽度,以pixel为单位。
(6)height：指定组件的高度,以pixel为单位。
(7)relwidth：指定组件的宽度,以父容器总宽度为单位1,该值应该在0.0~1.0之间,其中1.0 代表整个窗口宽度,0.5代表窗口的一半宽度。
(8)relheight：指定组件的高度,以父容器总高度为单位1,该值应该在0.0~1.0之间,其中1.0 代表整个窗口高度,0.5代表窗口的一半高度。
(9)bordermode：该属性支持"inside"或"outside"属性值,用于指定当设置组件的宽度、高度时是否计算该组件的边框宽度。

当使用Place布局管理容器中的组件时,需要设置组件的x、y 或 relx、rely选项,
Tkinter容器 内的坐标系统的原点(0,0)在左上角,其中X 轴向右延伸, Y 轴向下延伸,如图11.8所示。

如果通过x、y 指定坐标,单位就是pixel(像素);如果通过relx、rely指定坐标,则以整个父容器的宽度、高度为1。
不管通过哪种方式指定坐标,通过图11.8不难发现,通过x指定的坐标值 越大,该组件就越靠右;通过 y 指定的坐标值越大,该组件就越靠下。

下面介绍一个使用Place进行布局的例子,该示例将会动态计算各Label 的大小和位置,并通过 place()方法设置各Label 的大小和位置。
"""
# Python 2.x使用这行
# from Tkinter import *
# Python 3.x使用这行
from tkinter import *
import random


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 定义字符串元组
        books = ('疯狂Python讲义', '疯狂Swift讲义', '疯狂Kotlin讲义', '疯狂Java讲义', '疯狂Ruby讲义')
        for i in range(len(books)):
            # 生成3个随机数
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
            # 将元组中3个随机数格式化成16进制数,转成颜色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)
            # 创建Label,设置背景色和前景色
            lb = Label(root,
                       text=books[i],
                       fg='White' if grayness < 120 else 'Black',
                       bg=bg_color)
            # 使用place()设置该Label的大小和位置
            lb.place(x=20, y=36 + i * 36, width=180, height=30)


root = Tk()
root.title("Place布局")
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
root.geometry("250x250+30+30")
App(root)
root.mainloop()
