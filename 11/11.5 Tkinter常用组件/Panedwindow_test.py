"""
11.5.10 Panedwindow 组件

Panedwindow  是一个管理窗口布局的容器,它允许添加多个子组件(不需要使用 Pack、Grid 或 Place布局)并为每个子组件划分一个区域,
用户可用鼠标移动各区域的分隔线来改变各子组件 的大小(如果没有显式指定大小,子组件总是自动占满整个区域)。

提示：ttk.Panedwindow 继 承 了 tkinter.PanedWindow, 为 了 让 ttk.Panedwindow 与 tkinter.PanedWindow 保持名字上的兼容,
ttk 为 ttk.Panedwindow 起了 一 个别名： ttk.PanedWindow ( 注 意 w 的大小写),因此在程序中既可使用 ttk.Panedwindow,
也 可 使 用ttk.PanedWindow, 它们二者完全相同。

Panedwindow 是一个非常有特色的容器,它自带布局管理功能,它允许通过orient选项指定水 平或垂直方向,让容器中的各组件按水平或垂直方向排列。

在创建Panedwindow 之后,程序可通过如下方法操作Panedwindow 容器中的子组件。 >add(self,child,**kw): 添加一个子组件。
insert(self,pos,child,**kw): 在 pos 位置插入一个子组件。
remove(self,child):  删除一个子组件,该子组件所在区域也被删除。
下面程序示范了为Panedwindow 添加、插入、删除子组件。
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
        style.configure("fkit.TPanedwindow", background='darkgray', relief=RAISED)
        # 创建Panedwindow组件,通过style属性配置分隔线
        pwindow = ttk.Panedwindow(self.master,
                                  orient=VERTICAL, style="fkit.TPanedwindow")
        pwindow.pack(fill=BOTH, expand=1)
        first = ttk.Label(pwindow, text="第一个标签")
        # 调用add方法添加组件,每个组件一个区域
        pwindow.add(first)
        okBn = ttk.Button(pwindow, text="第二个按钮",
                          # 调用remove()方法删除组件,该组件所在区域消失
                          command=lambda: pwindow.remove(okBn))
        # 调用add方法添加组件,每个组件一个区域
        pwindow.add(okBn)
        entry = ttk.Entry(pwindow, width=30)
        # 调用add方法添加组件,每个组件一个区域
        pwindow.add(entry)
        # 调用insert方法插入组件
        pwindow.insert(1, Label(pwindow, text='插入的标签'))


root = Tk()
root.title("Panedwindow测试")
App(root)
root.mainloop()
"""
上面程序中前面两行粗体字代码创建了一个 ttk.Style对象,该对象专门用于管理ttk组件的样 式,这样ttk组件即可通过style选项复用ttk.Style管理的样式。此处使用tk.Style为 ttk.Panedwindow 指定样式,这样才能看到ttk.Panedwindow容器内的分隔线(默认是看不到的)。
上面程序中第三行粗体字代码调用了add()方法为Panedwindow 容器添加子组件；第四行粗体 字代码调用了remove()方法删除 Panedwindow 容器中的子组件；第五行粗体字代码调用了insert() 方法向 Panedwindow 容器中添加了子组件。
运行上面程序,将看到如图11.31所示的运行界面。
如果单击该界面上的“第二个按钮”,将会删除Panedwindow 组件中的该按钮,该按钮所占的


区域也会消失。此时将看到如图11.32所示的界面。
"""