"""
掌握了如何管理 GUI 组件的大小、位置之后,接下来自然就需要进一步掌握各组件的详细用法了,就相当于掌握各个"积木块"的详细功能。

11.5.1 使用ttk组件

前面程序都是直接使用 tkinter 模块下的 GUI 组件的,这些组件看上去特别"复古",也就是丑,仿佛是从20年前的程序上抠出来的组件。
为了弥补这点不足,Tkinter 后来引入了一个 ttk 组件作为补充(主要就是简单包装、美化一下),
并使用功能更强大的 Combobox  取代了原来的 Listbox,且新增了 LabeledScale(带标签的Scale)、Notebook(多文档窗口)、
Progressbar(进度条)、Treeview (树)等组件。

ttk 作为一个模块被放在 tkinter 包下,使用ttk组件与使用普通的 Tkinter 组件并没有多大的区别,只要导入 ttk 模块即可。

下面程序示范了如何使用 ttk 组件。
"""

from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # ttk使用Combobox取代了Listbox
        cb = ttk.Combobox(self.master, font=24)
        # 为Combobox设置列表项
        cb['values'] = ('Python', 'Swift', 'Kotlin')
        #        cb = Listbox(self.master, font=24)
        # 为Listbox设置列表项
        #        for s in ('Python', 'Swift', 'Kotlin'):
        #            cb.insert(END, s)
        cb.pack(side=LEFT, fill=X, expand=YES)
        f = ttk.Frame(self.master)
        #        f = Frame(self.master)
        f.pack(side=RIGHT, fill=BOTH, expand=YES)
        lab = ttk.Label(self.master, text='我的标签', font=24)
        #        lab = Label(self.master, text='我的标签', font=24)
        lab.pack(side=TOP, fill=BOTH, expand=YES)
        bn = ttk.Button(self.master, text='我的按钮')
        #        bn = Button(self.master, text='我的按钮')
        bn.pack()


root = Tk()
root.title("简单事件处理")
App(root)
root.mainloop()
"""
上面程序中被注释的代码是使用 tk 组件的代码,未被注释的代码是直接使用 Tkinter 组件的代码。
直接运行上面程序,可以看到如图11.14所示的界面。

如果将上面程序中被注释的代码取消注释,并注释使用Tkinter组件的代码,改为使用ttk组件,再次运行上面程序,则可以看到如图11.15所示的界面。

对比两个界面上 Tkinter 的 Button和 ttk 的 Button,不难发现 ttk 下的 Button 更接近Windows 7本地平台的风格,
显得更漂亮,这就是ttk组件的优势。
提示：笔者一般不喜欢开启Windows 7 的主题风格,但这里为了演示 Tkinter 组件和 ttk 组件的差异,
不得不开启Windows 7 的主题风格。本书后面依然会关闭 Windows 7 的主题风格。
"""