"""
11.5.9	Labelframe 组件

Labelframe是 Frame 容器的改进版,它允许为容器添加一个标签,该标签既可以是普通的文字 标签,也可以将任意GUI 组件作为标签。
提示：为了让ttk.Labelframe与 tkinter:LabelFrame保持名字上的兼容,ttk为 ttk.Labelframe 起了一个别名：ttk.LabelFrame(注意f 的大小写),因此在程序中既可使用ttk.Labelframe, 也可使用ttk.LabelFrame, 它们二者完全相同。

为了给 Labelframe 设置文字标签,只要为它指定 text选项即可。如下程序示范了Labelframe 组件的用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建Labelframe容器
        lf = ttk.Labelframe(self.master, text='请选择图书',
            padding=20)
        lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        books = ['Swift', 'Python', 'Kotlin', 'Ruby']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个Radiobutton,并放入Labelframe中
        for book in books:
            Radiobutton(lf, text='疯狂' + book + '讲义',
            value=i,
            variable=self.intVar).pack(side=LEFT)
            i += 1     
root = Tk()
root.title("Labelframe测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序首先创建了一个简单的 Labelframe 组件,并为它指定了 text 选项,该选项的内容将会作为该容器的标签。
接下来程序向 Labelframe 容器中添加了4个Radiobutton。运行该程序,可以看到如图11.29所示的效果。         
"""