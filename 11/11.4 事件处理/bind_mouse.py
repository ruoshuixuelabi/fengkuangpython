"""
下面通过一个示例来示范为鼠标移动事件绑定事件处理方法。
"""
# 将tkinter写成Tkinter可兼容Python 2.x
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        lb = Label(self.master, width=40, height=3)
        lb.config(bg='lightgreen', font=('Times', 20))
        # 为鼠标移动事件绑定事件处理方法
        lb.bind('<Motion>', self.motion)
        # 为按住左键时的鼠标移动事件绑定事件处理方法
        lb.bind('<B1-Motion>', self.press_motion)
        lb.pack()
        self.show = Label(self.master, width=38, height=1)
        self.show.config(bg='white', font=('Courier New', 20))
        self.show.pack()

    def motion(self, event):
        self.show['text'] = "鼠标移动到: (%s %s)" % (event.x, event.y)
        return

    def press_motion(self, event):
        self.show['text'] = "按住鼠标的位置为: (%s %s)" % (event.x, event.y)
        return


root = Tk()
root.title('鼠标事件')
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码为<Motion>(鼠标移动)事件绑定了事件处理方法,因此鼠标在lb组件上移动时将会不断触发motion()方法;
第二行粗体字代码为<B1-Motion>(按住左键时鼠标移动)事件绑定了事件处理方法,
因此按住鼠标左键在 lb 组件上移动时将会不断触发 press_motion()方法。

运行该程序,如果让鼠标直接在第一个 Label 组件 (Ib) 上移动,将看到如图11.12所示的运行结果。
如果按住鼠标左键并让鼠标在第一个Label 组件 (Ib) 上移动,将看到如图11.13所示的运行结果。
"""