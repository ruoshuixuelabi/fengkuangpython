"""
11.6.5	颜色选择对话框
在colorchooser模块下提供了用于生成颜色选择对话框的askcolor()工具函数,为该工具函数可 指定如下选项。
> parent: 指定该对话框的属主窗口。
title:  指定该对话框的标题。
> color: 指定该对话框初始选择的颜色。
下面程序示范了颜色选择对话框的功能和用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入colorchooser
from tkinter import colorchooser
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建1个按钮,并为之绑定事件处理函数
        ttk.Button(self.master, text='选择颜色',
            command=self.choose_color # 绑定choose_color方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
    def choose_color(self):
        # 调用askcolor函数获取选中的颜色
        print(colorchooser.askcolor(parent=self.master, title='选择画笔颜色', 
            color = 'blue')) # 初始颜色
root = Tk()
root.title("颜色对话框测试")
App(root)
root.mainloop()
"""
上面程序中粗体字代码就是调用 askcolor()函数生 成颜色选择对话框的关键代码。运行该程序,单击界面 上的“选择颜色”按钮,将可以看到如图11.42所示的 对话框。
提 示 ：- · ·— · ·—. ·—. ·—.          —
通过colorchooser模块下的工具函数打开 的颜色选择对话框依赖所在的平台,因此在不
同的平台上看到的颜色选择对话框是不同的。
当用户选择指定颜色,并单击颜色选择对话框中的“确定”按钮后, askcolor()函数会返回用 户所选择的颜色,因此可以在控制台看到用户所选择的颜色。
"""