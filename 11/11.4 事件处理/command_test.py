"""
前面介绍了如何放置各种组件,从而得到了丰富多彩的图形界面,但这些界面还不能响应用户的任何操作。
比如单击窗口上的按钮,该按钮并不会提供任何响应。这就是因为程序没有为这些组件绑定任何事件处理的缘故。

11.4.1 简单的事件处理

简单的事件处理可通过 command 选项来绑定,该选项绑定为一个函数或方法,当用户单击指定按钮时,
通过该 command 选项绑定的函数或方法就会被触发。

下面程序示范了为按钮的 command 绑定事件处理方法。
"""
# Python 2.x使用这行
# from Tkinter import *
# Python 3.x使用这行
from tkinter import *
import random


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.label = Label(self.master, width=30)
        self.label['font'] = ('Courier', 20)
        self.label['bg'] = 'white'
        self.label.pack()
        bn = Button(self.master, text='单击我', command=self.change)
        bn.pack()

    # 定义事件处理方法
    def change(self):
        self.label['text'] = '欢迎学习Python'
        # 生成3个随机数
        ct = [random.randrange(256) for x in range(3)]
        grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
        # 将元组中3个随机数格式化成16进制数,转成颜色格式
        bg_color = "#%02x%02x%02x" % tuple(ct)
        self.label['bg'] = bg_color
        self.label['fg'] = 'black' if grayness > 125 else 'white'


root = Tk()
root.title("简单事件处理")
App(root)
root.mainloop()
"""
上面程序中粗体字代码为 Button 的 command 选项指定为self.change,这意味着当该按钮被单击时,将会触发当前对象的 change()方法。
该 change()方法会改变界面上 Label 的文本和背景色。

运行该程序,单击界面上的"单击我"按钮,将看到如图11.10所示的界面。
"""