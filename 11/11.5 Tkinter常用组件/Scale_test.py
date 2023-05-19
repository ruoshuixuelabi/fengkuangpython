"""
11.5.8	Scale 和 LabeledScale 组件

Scale组件代表一个滑动条,可以为该滑动条设置最小值和最大值,也可以设置滑动条每次调节的步长。 Scale组件支持如下选项。
from:   设置该Scale的最小值。
to: 设置该Scale的最大值。
resolution: 设置该Scale滑动时的步长 label:  为 Scale组件设置标签内容。
>length: 设置轨道的长度。
> width: 设置轨道的宽度。
>troughcolor: 设置轨道的背景色。
sliderlength: 设置滑块的长度。
sliderrelief: 设置滑块的立体样式。
showvalue:   设置是否显示当前值。
orient:  设置方向。该选项支持VERTICAL  和 HORIZONTAL   两个值。
digits:  设置有效数字至少要有几位。
>variable: 用于与变量进行绑定。
command:    用于为该Scale组件绑定事件处理函数或方法。
提示：      
如果使用ttk.Scale组件,则更接近操作系统本地的效果,但允许定制的选项少。

下面以一个示例程序来介绍Scale组件的选项的功能和用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.scale = Scale(self.master,
                           from_=-100,  # 设置最大值
                           to=100,  # 设置最小值
                           resolution=5,  # 设置步长
                           label='示范Sacle',  # 设置标签内容
                           length=400,  # 设置轨道的长度
                           width=30,  # 设置轨道的宽度
                           troughcolor='lightblue',  # 设置轨道的背景色
                           sliderlength=20,  # 设置滑块的长度
                           sliderrelief=SUNKEN,  # 设置滑块的立体样式
                           showvalue=YES,  # 设置显示当前值
                           orient=HORIZONTAL  # 设置水平方向
                           )
        self.scale.pack()
        # 创建一个Frame作为容器
        f = Frame(self.master)
        f.pack(fill=X, expand=YES, padx=10)
        Label(f, text='是否显示值:').pack(side=LEFT)
        i = 0
        self.showVar = IntVar()
        self.showVar.set(1)
        # 创建两个Radiobutton控制Scale是否显示值
        for s in ('不显示', '显示'):
            Radiobutton(f, text=s, value=i, variable=self.showVar,
                        command=self.switch_show).pack(side=LEFT)
            i += 1
        # 创建一个Frame作为容器
        f = Frame(self.master)
        f.pack(fill=X, expand=YES, padx=10)
        Label(f, text='方向:').pack(side=LEFT)
        i = 0
        self.orientVar = IntVar()
        self.orientVar.set(0)
        # 创建两个Radiobutton控制Scale的方向
        for s in ('水平', '垂直'):
            Radiobutton(f, text=s, value=i, variable=self.orientVar,
                        command=self.switch_orient).pack(side=LEFT)
            i += 1

    def switch_show(self):
        self.scale['showvalue'] = self.showVar.get()

    def switch_orient(self):
        # 根据单选框的选择设置orient选项的值
        self.scale['orient'] = VERTICAL if self.orientVar.get() else HORIZONTAL


root = Tk()
root.title("Scale测试")
App(root)
root.mainloop()
"""
上面程序中粗体字代码创建了Scale组件,并为该Scale组件指定了上面所介绍的选项。
此外, 程序中倒数第二行粗体字代码根据单选钮的选中状态来设置Scale组件的showvalue 选项,该选项 将会控制该 Scale 组件是否显示当前值；
程序中最后一行粗体字代码根据单选钮的选中状态设置 Scale是水平的还是垂直的—— 根据orient选项进行设置。

运行上面程序,如果将Scale组件默认显示为水平滑动条,则效果如图11.27所示。

如果将上面的Scale设置为垂直滑动条,并选中“不显示”单选钮,将会看到如图11.28所示 的效果。

"""