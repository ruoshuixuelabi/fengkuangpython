"""
Scale组件同样支持variable进行变量绑定,也支持使用command 选项绑定事件处理函数或方法,
这样每当用户拖动滑动条上的滑块时,都会触发 command 绑定的事件处理方法,不过 Scale 的事件处理方法比较奇葩：
它可以额外定义一个参数,用于获取Scale的当前值。例如如下程序。
"""
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 定义变量
        self.doubleVar = DoubleVar()
        self.scale = Scale(self.master,
                           from_=-100,  # 设置最大值
                           to=100,  # 设置最小值
                           resolution=5,  # 设置步长
                           label='示范Sacle',  # 设置标签内容
                           length=400,  # 设置轨道的长度
                           width=30,  # 设置轨道的宽度
                           orient=HORIZONTAL,  # 设置水平方向
                           digits=10,  # 设置十位有效数字
                           command=self.change,  # 绑定事件处理函数
                           variable=self.doubleVar  # 绑定变量
                           )
        self.scale.pack()
        # 设置Scale的当前值
        self.scale.set(20)

    # 这个事件处理函数比较奇葩,它可以接收到Scale的值
    def change(self, value):
        print(value, self.scale.get(), self.doubleVar.get())


root = Tk()
root.title("Scale测试")
App(root)
root.mainloop()
"""
上面程序中粗体字代码示范了通过三种方式来获取Scale组件的值。

通过事件处理方法的参数来获取。
通过Scale组件提供的get()方法来获取。
通过Scale组件绑定的变量来获取。
通过上面三种方式获取的变量值都是一样的,但由于Scale组件指定了digits选项(该选项指定 Scale的值的有效数字至少保留几位)为10,因此程序通过事件处理方法获取的值将有10位有 效数字,如-35.0000000。
"""