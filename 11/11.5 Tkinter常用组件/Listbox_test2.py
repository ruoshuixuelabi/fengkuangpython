"""
Listbox也支持使用listvariable选项与变量进行绑定,但这个变量并不是控制Listbox选中哪些 项,而是控制Listbox包含哪些项。简单来说,如果listvariable选项与变量进行了双向绑定,则无 须调用insert()、delete()方法来添加、删除列表项,只要通过绑定变量即可改变Listbox中的列表项。
下面程序示范了操作Listbox中选项的方法。
"""
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        topF = Frame(self.master)
        topF.pack(fill=Y, expand=YES)
        # 定义StringVar变量
        self.v = StringVar()
        # 创建Listbox组件,与v变量绑定
        self.lb = Listbox(topF, listvariable=self.v)
        self.lb.pack(side=LEFT, fill=Y, expand=YES)
        for item in range(20):
            self.lb.insert(END, str(item))
        # 创建Scrollbar组件,设置该组件与self.lb的纵向滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        Button(f, text="选中10项", command=self.select).pack(side=LEFT)
        Button(f, text="清除选中3项", command=self.clear_select).pack(side=LEFT)
        Button(f, text="删除3项", command=self.delete).pack(side=LEFT)
        Button(f, text="绑定变量", command=self.var_select).pack(side=LEFT)

    def select(self):
        # 选中指定项
        self.lb.selection_set(0, 9)

    def clear_select(self):
        # 取消选中指定项
        self.lb.selection_clear(1, 3)

    def delete(self):
        # 删除指定项
        self.lb.delete(5, 8)

    def var_select(self):
        # 修改与Listbox绑定的变量
        self.v.set(('12', '15'))


root = Tk()
root.title("Listbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码控制选中列表项中第一个到第十个选项;第二行粗体字代码控制取消选中列表项中的3项;
第三行粗体字代码删除列表项中的4项;第四行粗体字代码通过绑定变量来改 变Listbox 中的列表项。
运行上面程序,删除其中4项之后的运行效果如图11.23所示。

如果程序要获取 Listbox 当前选中的项,则可通过 curselection() 方法来实现,该方法会返回一个元组,该元组包含当前Listbox 的所 有选中项。
"""