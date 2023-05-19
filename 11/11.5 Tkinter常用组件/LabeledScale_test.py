"""
ttk.LabeledScale 是平台化的滑动条,因此它允许设置的选项很少,只能设置 from、to 和 compound 等有限的几个选项,
而且它总是生成一个水平滑动条(不能变成垂直的),其中compound 选项控制滑动条的数值标签是显示在滑动条的上方,还是滑动条的下方。
下面程序示范了LabeledScale组件的功能和用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.scale = ttk.LabeledScale(self.master,
                                      from_=-100,  # 设置最大值
                                      to=100,  # 设置最小值
                                      #            compound = BOTTOM # 设置显示数值的Label在下方
                                      )
        self.scale.value = -20
        self.scale.pack(fill=X, expand=YES)


root = Tk()
root.title("LabeledScale测试")
App(root)
root.mainloop()
"""
上面程序中粗体字代码创建了一个LabeledScale组件,该组件会生成一个水平滑动条,并且滑动条的数值标签默认会显示在滑动条的上方;
如果取消程序中被注释代码的注释,也就是将 compound 选项设为BOTTOM,则意味着滑动条的数值标签默认会显示在滑动条的下方。
"""
