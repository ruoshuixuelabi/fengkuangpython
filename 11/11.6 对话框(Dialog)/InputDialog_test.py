"""
11.6.3	输入对话框
在simpledialog模块下还有如下便捷的工具函数,通过这些工具函数可以更方便地生成各种输 入对话框。
askinteger:  生成一个让用户输入整数的对话框。
> askfloat: 生成一个让用户输入浮点数的对话框。
askstring:  生成一个让用户输入字符串的对话框。
上面三个工具函数的前两个参数分别指定对话框的标题和提示信息,后面还可以通过选项来设 置对话框的初始值、最大值和最小值。


( 322
仅供非商业用途或交流学习使用


下面程序示范了simpledialog模块下三个工具函数的用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入simpledialog
from tkinter import simpledialog
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建3个按钮,并为之绑定事件处理函数
        ttk.Button(self.master, text='输入整数对话框',
            command=self.open_integer # 绑定open_integer方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
        ttk.Button(self.master, text='输入浮点数对话框',
            command=self.open_float # 绑定open_integer方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
        ttk.Button(self.master, text='输入字符串对话框',
            command=self.open_string # 绑定open_integer方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
    def open_integer(self):
         # 调用askinteger函数生成一个让用户输入整数的对话框
        print(simpledialog.askinteger("猜糖果", "你猜我手上有几个糖果:",
            initialvalue=3, minvalue=1, maxvalue=10))
    def open_float(self):
        # 调用askfloat函数生成一个让用户输入浮点数的对话框
        print(simpledialog.askfloat("猜体重", "你猜我我体重多少公斤:", 
            initialvalue=27.3, minvalue=10, maxvalue=50))
    def open_string(self):
        # 调用askstring函数生成一个让用户输入字符串的对话框
        print(simpledialog.askstring("猜名字", "你猜我叫什么名字:",
            initialvalue='Charlie'))
root = Tk()
root.title("输入对话框测试")
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码生成让用户输入整数的对话框；第二行粗体字代码生成让用户输 入浮点数的对话框；第三行粗体字代码生成让用户输入字符串的对话框。
askinteger()、askfloat和 askstring这三个函数会返回用户输入的数据,因此上面三行粗体字代 码打印了这三个函数的返回值,这样就可以打印出用户输入的内容。
运行该程序,单击界面上的“输入整数对话框”按钮,可以看到如图11.38所示的对话框。
在图11.38所示的对话框中,用户只能输入整数,而且输入的整数必须在指定范围内；否则, 系统会生成错误提示。当用户输入所允许范围内的整数并单击“OK” 按钮后,可以看到控制台打 印了用户输入的整数。
单击界面上的“输入浮点数对话框”按钮,可以看到如图11.39所示的对话框。

图11.38 输入整数的对话框                    图11.39 输入浮点数的对话框
在图11.39所示的对话框中,用户只能输入浮点数,而且输入的浮点数必须在指定范围内；否

( 323
仅供非商业用途或交流学习使用


则,系统会生成错误提示。当用户输入所允许范围内的浮点数并单击 “OK” 按钮后,可以看到控 制台打印了用户输入的浮点数。
单击界面上的“输入字符串对话框”按钮,可以看到如图11.40 所示的对话框。
在图11.40所示的对话框中,用户只能输入字符串。当用户输 入合适的字符串并单击“OK” 按钮后,可以看到控制台打印了用 户输入的字符串。
"""