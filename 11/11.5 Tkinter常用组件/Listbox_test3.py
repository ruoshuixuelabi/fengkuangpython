"""
Listbox并不支持使用command 选项来绑定事件处理函数或方法,如果程序需要为Listbox绑定事件处理函数或方法,
则可通过 bind()方法来实现。下面程序示范了通过 bind()方法为 Listbox 绑定事件处理方法。
"""
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        # 创建Listbox组件
        self.lb = Listbox(topF)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20):
            self.lb.insert(END, str(item))
        # 创建Scrollbar组件,设置该组件与self.lb的纵向滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        # 为双击事件绑定事件处理方法
        self.lb.bind("<Double-1>", self.click)

    def click(self, event):
        from tkinter import messagebox
        # 获取Listbox当前选中项
        messagebox.showinfo(title=None, message=str(self.lb.curselection()))


root = Tk()
root.title("Listbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
当用户双击 Listbox 时,程序将会触发该对象的 click 方法;在 click()方法中粗体字代码则调用了Listbox的 curselection()方法来获取当前选中项。

运行上面程序,双击某个列表项,将可以看到如 图11.24所示的运行效果。
"""