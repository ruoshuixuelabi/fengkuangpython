"""
到上面例子,可能有读者会想： Panedwindow要么水平排列组件,要么垂直排列组件,这样

功能不是太局限了吗?请别忘记了, Panedwindow 组件同样也是可以嵌套的,以实现功能更丰富的 界面。例如,如下程序在水平Panedwindow 中嵌套了垂直Panedwindow。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建Style
        style = ttk.Style()
        style.configure("fkit.TPanedwindow",
            background='darkgray', relief=RAISED)
        # 创建Panedwindow组件,通过style属性配置分隔线
        pwindow = ttk.Panedwindow(self.master,
            orient=HORIZONTAL, style="fkit.TPanedwindow")
        pwindow.pack(fill=BOTH, expand=YES)
        left = ttk.Label(pwindow, text="左边标签", background='pink')
        pwindow.add(left)
        # 创建第二个Panedwindow组件,该组件的方向为垂直方向
        rightwindow = PanedWindow(pwindow, orient=VERTICAL)
        pwindow.add(rightwindow)
        top = Label(rightwindow, text="右上标签", background='lightgreen')
        rightwindow.add(top)  
        bottom = Label(rightwindow, text="右下标签", background='lightblue')
        rightwindow.add(bottom)  
root = Tk()
root.title("Panedwindow测试")
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码创建了一
个水平分布的Panedwindow 容器,在该容器
中先添加了一个Label 组件；第二行粗体字
代码创建了一个垂直分布的Panedwindow 容
器,该容器被添加到第一个Panedwindow 容
器中,这样就形成了嵌套,从而可以实现功
能更丰富的界面。
运行上面程序,可以看到如图11.33所
示的界面。
"""