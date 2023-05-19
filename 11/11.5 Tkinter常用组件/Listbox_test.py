"""
11.5.6	Listbox 和 Combobox 组件

Listbox代表一个列表框,用户可通过列表框来选择一个列表项。
ttk模块下的Combobox 则是 Listbox的改进版,它既提供了单行文本框让用户直接输入(就像Entry一样),
也提供了下拉列表 框供用户选择(就像Listbox一样),因此它被称为复合框。

程序创建Listbox起码需要两步。
① 创建 Listbox 对象,并为之执行各种选项。Listbox 除支持表11.2中所介绍的大部分通用选项之外,
还支持 selectmode 选项,用于设置 Listbox 的选择模式。
② 调用 Listbox 的 insert(self,index,*elements) 方法来添加选项。从最后一个参数可以看出,
该方法既可每次添加一个选项,也可传入多个参数,每次添加多个选项。
index 参数指定选项的插入位置,它支持END  (结尾处)、 ANCHOR    (当前位置)和ACTIVE  (选中处)等特殊索引。

Listbox的 selectmode支持的选择模式有如下几种。
(1)'browse': 单选模式,支持按住鼠标键拖动来改变选择。
(2)'multiple': 多选模式。
(3)'single': 单选模式,必须通过鼠标键单击来改变选择。
(4)'extended':  扩展的多选模式,必须通过Ctrl或 Shift键辅助实现多选。 下面程序示范了Listbox的基本用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


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
        for item in ['Python', 'Kotlin', 'Swift', 'Ruby']:
            self.lb.insert(END, item)
        # 或直接使用多个元素来插入
        self.lb.insert(ANCHOR, 'Python', 'Kotlin', 'Swift', 'Ruby')
        # 创建Scrollbar组件,设置该组件与self.lb的纵向滚动关联
        scroll = Scrollbar(topF, command=self.lb.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.lb的纵向滚动影响scroll滚动条
        self.lb.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        Label(f, text='选择模式:').pack(side=LEFT)
        modes = ('multiple', 'browse', 'single', 'extended')
        self.strVar = StringVar()
        for m in modes:
            rb = ttk.Radiobutton(f, text=m, value=m, variable=self.strVar, command=self.choose_mode)
            rb.pack(side=LEFT)
        self.strVar.set('browse')

    def choose_mode(self):
        print(self.strVar.get())
        self.lb['selectmode'] = self.strVar.get()


root = Tk()
root.title("Listbox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码表示每次插入一个选项,因此程序使用循环来控制插入多个选项;第二行粗体字代码则表示直接插入多个选项。

程序中第三行粗体字代码根据用户选择来改变 Listbox 的 selectmode 选项,这样读者可以体会 Listbox 不同选项的差异。
运行上面程序,可以看到如图11.22所示的效果。

除了最常见的insert()方法, Listbox还支持如下常见的操作列表项的方法。
(1)selection set(self, first,last=None):选中从first到 last(包 含)的所有列表项。如果不指定 last,则直接选中 first列表项。
(2)selection clear(self,first,last=None): 取消选中从first到 last (包含)的所有列表项。如果 不指定 last, 则只取消选中first列表项。
(3)delete(self, first,last=None): 删除从first到 last (包含)的所有列表项。如果不指定last, 则只删除first列表项。
"""
