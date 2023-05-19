"""
Combobox  的用法更加简单,程序可通过 values 选项直接为它设置多个选项。该组件的 state选项支持 'readonly状态,该状态代表 Combobox  的文本框不允 许编辑,只能通过下拉列表框的列表项来改变。
Combobox  同样可通过textvariable选项将它与指定变量绑定,这样程序可通过该变量来获取或修改Combobox 组件的值。
Combobox 还可通过postcommand 选项指定事件处理函数或方法：当用户单击Combobox 的 下 拉箭头时,程序就会触发 postcommand 选项指定的事件处理函数或方法。
下面程序示范了Combobox  组件的用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.strVar = StringVar()
        # 创建Combobox组件
        self.cb = ttk.Combobox(self.master,
                               textvariable=self.strVar,  # 绑定到self.strVar变量
                               postcommand=self.choose)  # 当用户单击下拉箭头时触发self.choose方法
        self.cb.pack(side=TOP)
        # 为Combobox配置多个选项
        self.cb['values'] = ['Python', 'Ruby', 'Kotlin', 'Swift']
        f = Frame(self.master)
        f.pack()
        self.isreadonly = IntVar()
        # 创建Checkbutton,绑定到self.isreadonly变量
        Checkbutton(f, text='是否只读:',
                    variable=self.isreadonly,
                    command=self.change).pack(side=LEFT)
        # 创建Button,单击该按钮激发setvalue方法
        Button(f, text='绑定变量设置',
               command=self.setvalue).pack(side=LEFT)

    def choose(self):
        from tkinter import messagebox
        # 获取Combbox的当前值
        messagebox.showinfo(title=None, message=str(self.cb.get()))

    def change(self):
        self.cb['state'] = 'readonly' if self.isreadonly.get() else 'enable'

    def setvalue(self):
        self.strVar.set('我爱Python')


root = Tk()
root.title("Combobox测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码将Combobox  组件绑定到self.strVar变量;第二行粗体字代码为Combobox 的 command 绑定了事件处理方法。

程序中第三行粗体字代码根据列表框的值来确定 Combobox 否允许编辑。

运行上面程序,可以看到如图11.25所示的运行界面。
"""