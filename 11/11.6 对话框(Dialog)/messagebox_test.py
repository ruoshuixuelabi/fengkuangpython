"""
11.6.6	消息框
在 messagebox 模块下提供了大量工具函数来生成各种消息框,这
些消息框的结构大致如图11.43所示。
在默认情况下,开发者在调用messagebox 的工具函数时只要设置
提示区的字符串即可,图标区的图标、按钮区的按钮都有默认设置。

如果有必要,则完全可通过如下两个选项来定制图标和按钮。
icon:定制图标的选项。该选项支持"error"、"info"、"question"、


图11.43 消息框的结构

"warning"这几个选项值。
type:   定制按钮的选项。该选项支持"abortretryignore”(取消、重试、忽略)、"ok" (确定)、
"okcancel"(确定、取消)、"retrycancel"(重试、取消)、"yesno"(是、否)、"yesnocancel" (是、否、取消)这些选项值。
下面的示例程序不仅示范了messagebox 的各工具函数的用法,而且还通过两组单选钮让用户 动态选择不同的icon 和 type选项的效果。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入messagebox
from tkinter import messagebox as msgbox
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        #-----------创建第1个Labelframe,用于选择图标类型-----------
        topF = Frame(self.master)
        topF.pack(fill=BOTH)
        lf1 = ttk.Labelframe(topF, text='请选择图标类型')
        lf1.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=5)
        i = 0
        self.iconVar = IntVar()
        self.icons = [None, "error", "info", "question", "warning"]
        # 使用循环创建多个Radiobutton,并放入Labelframe中
        for icon in self.icons:
            Radiobutton(lf1, text = icon if icon is not None else '默认',
            value=i,
            variable=self.iconVar).pack(side=TOP, anchor=W)
            i += 1
        self.iconVar.set(0)
        #-----------创建第二个Labelframe,用于选择按钮类型-----------
        lf2 = ttk.Labelframe(topF, text='请选择按钮类型')
        lf2.pack(side=LEFT,fill=BOTH, expand=YES, padx=10, pady=5)
        i = 0
        self.typeVar = IntVar()
        # 定义所有按钮类型
        self.types = [None, "abortretryignore", "ok", "okcancel", 
            "retrycancel", "yesno", "yesnocancel"]
        # 使用循环创建多个Radiobutton,并放入Labelframe中
        for tp in self.types:
            Radiobutton(lf2, text= tp if tp is not None else '默认',
            value=i,
            variable=self.typeVar).pack(side=TOP, anchor=W)
            i += 1
        self.typeVar.set(0)
        #-----------创建Frame,用于包含多个按钮来生成不同的消息框-----------
        bottomF = Frame(self.master)
        bottomF.pack(fill=BOTH)
        # 创建8个按钮,并为之绑定事件处理函数
        btn1 = ttk.Button(bottomF, text="showinfo", 
            command=self.showinfo_clicked)
        btn1.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn2 = ttk.Button(bottomF, text="showwarning", 
            command=self.showwarning_clicked)
        btn2.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn3 = ttk.Button(bottomF, text="showerror",
            command=self.showerror_clicked)
        btn3.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn4 = ttk.Button(bottomF, text="askquestion",
            command=self.askquestion_clicked)
        btn4.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn5 = ttk.Button(bottomF, text="askokcancel",
            command=self.askokcancel_clicked)
        btn5.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn6 = ttk.Button(bottomF, text="askyesno",
            command=self.askyesno_clicked)
        btn6.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn7 = ttk.Button(bottomF, text="askyesnocancel",
            command=self.askyesnocancel_clicked)
        btn7.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
        btn8 = ttk.Button(bottomF, text="askretrycancel",
            command=self.askretrycancel_clicked)
        btn8.pack(side=LEFT, fill=X, ipadx=5, ipady=5,
            pady=5, padx=5)
    def showinfo_clicked(self):
        print(msgbox.showinfo("Info", "showinfo测试.", 
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def showwarning_clicked(self):
        print(msgbox.showwarning("Warning", "showwarning测试.",
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def showerror_clicked(self):
        print(msgbox.showerror("Error", "showerror测试.", 
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def askquestion_clicked(self):
        print(msgbox.askquestion("Question", "askquestion测试.",
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def askokcancel_clicked(self):
        print(msgbox.askokcancel("OkCancel", "askokcancel测试.",
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def askyesno_clicked(self):
        print(msgbox.askyesno("YesNo", "askyesno测试.", 
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def askyesnocancel_clicked(self):
        print(msgbox.askyesnocancel("YesNoCancel", "askyesnocancel测试.",
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
    def askretrycancel_clicked(self):
        print(msgbox.askretrycancel("RetryCancel", "askretrycancel测试.",
            icon=self.icons[self.iconVar.get()],
            type=self.types[self.typeVar.get()]))
root = Tk()
root.title("消息框测试")
App(root)
root.mainloop()
"""
上面程序先创建了两组单选钮来让用户选择图标类型(通过 icon 选项改变)和按钮类型(通 过type选项改变)。
接下来的几行粗体字代码就是调用函数生成不同消息框的关键代码。运行上面程序,可以看到 如图11.44所示的界面。

读者可通过左边的单选钮选择图标类型,通过右边的单选钮选择按钮类型。比如在左边选择 “error”, 在右边选择“abortretryignore”, 然后单击 “showinfo”按钮,将可以看到如图11.45所示

( 329
仅供非商业用途或交流学习使用

疯  担Python                                                                      疯狂软件教育

的消息框。
showinfo()函数默认生成的消息框的图标应该是一个感叹号,下方也只有一个按钮(读者可通
过两组单选钮都选择“默认”来看默认效果);但从图11.45
中看到通过showinfo()函数生成的消息框被改变了,这就是
因为指定了icon和 type选项的缘故。
上面程序打印出消息框返回的结果,这些消息框到底返
回什么呢?消息框返回的是用户单击的按钮,比如用户单击
“中止”按钮,消息框就返回'abort'字符串；用户单击“重试”
按钮,消息框就返回'retry'字符串……
"""