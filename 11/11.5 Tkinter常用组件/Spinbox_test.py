"""
11.5.7	Spinbox组件

Spinbox 组件是一个带有两个小箭头的文本框,用户既可以通过两个小箭头上下调整该组件内的值,
也可以直接在文本框内输入内容作为该组件的值。

Spinbox 本质上也相当于持有一个列表框,这一点类似于 Combobox,但 Spinbox 不会展开下拉列表供用户选择。
Spinbox 只能通过向上、向下箭头来选择不同的选项。

在使用 Spinbox 组件时,既可通过from(由于 from 是关键字,实际使用时写成from)、to、increment 选项来指定选项列表,
也可通过 values 选项来指定多个列表项,该选项的值可以是 list 或 tuple。

Spinbox 同样可通过textvariable选项将它与指定变量绑定,这样程序即可通过该变量来获取或修改Spinbox 组件的值。

Spinbox 还可通过command 选项指定事件处理函数或方法：当用户单击Spinbox 的向上、向下 箭头时,
程序就会触发command  选项指定的事件处理函数或方法。

下面程序示范了Spinbox 组件的用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        ttk.Label(self.master, text='指定from、to、increment').pack()
        # 通过指定from_、to、increament选项创建Spinbox
        sb1 = Spinbox(self.master, from_=20,
                      to=100,
                      increment=5)
        sb1.pack(fill=X, expand=YES)
        ttk.Label(self.master, text='指定values').pack()
        # 通过指定values选项创建Spinbox
        self.sb2 = Spinbox(self.master,
                           values=('Python', 'Swift', 'Kotlin', 'Ruby'),
                           command=self.press)  # 通过command绑定事件处理方法
        self.sb2.pack(fill=X, expand=YES)
        ttk.Label(self.master, text='绑定变量').pack()
        self.intVar = IntVar()
        # 通过指定values选项创建Spinbox,并为之绑定变量
        sb3 = Spinbox(self.master,
                      values=list(range(20, 100, 4)),
                      textvariable=self.intVar,  # 绑定变量
                      command=self.press)
        sb3.pack(fill=X, expand=YES)
        self.intVar.set(33)  # 通过变量改变Spinbox的值

    def press(self):
        print(self.sb2.get())


root = Tk()
root.title("Spinbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中第一段粗体字代码使用from 、to、increment选项创建了Spinbox组件;
第二段粗体字代码使用values选项创建了Spinbox组件,并为该组件的command 选项指定了事件处理方法,
因此当单击Spinbox的向上、向下箭头调整 值时,该选项指定的事件处理方法就会被触发;
第三段粗体字代码在创建 Spinbox时使用textvariable选项绑定了变量,这样程序完全可通过绑 定变量来访问或修改该Spinbox组件的值。

运行上面程序,可以看到如图11.26所示的运行界面。
"""
