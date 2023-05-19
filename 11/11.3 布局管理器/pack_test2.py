"""
当程序界面比较复杂时,就需要使用多个容器(Frame) 分开布局,然后再将Frame 添加到窗口中。例如如下程序。
"""
# Python 2.x使用这行
# from Tkinter import *
# Python 3.x使用这行
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建第一个容器
        fm1 = Frame(self.master)
        # 该容器放在左边排列
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 向fm1中添加3个按钮
        # 设置按钮从顶部开始排列,且按钮只能在垂直（X）方向填充
        Button(fm1, text='第一个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第二个').pack(side=TOP, fill=X, expand=YES)
        Button(fm1, text='第三个').pack(side=TOP, fill=X, expand=YES)
        # 创建第二个容器
        fm2 = Frame(self.master)
        # 该容器放在左边排列,就会挨着fm1
        #        fm2.pack(side=LEFT, padx=10, expand=YES)
        fm2.pack(side=LEFT, padx=10, fill=BOTH, expand=YES)
        # 向fm2中添加3个按钮
        # 设置按钮从右边开始排列
        Button(fm2, text='第一个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第二个').pack(side=RIGHT, fill=Y, expand=YES)
        Button(fm2, text='第三个').pack(side=RIGHT, fill=Y, expand=YES)
        # 创建第三个容器
        fm3 = Frame(self.master)
        # 该容器放在右边排列,就会挨着fm1
        fm3.pack(side=RIGHT, padx=10, fill=BOTH, expand=YES)
        # 向fm3中添加3个按钮
        # 设置按钮从底部开始排列,且按钮只能在垂直（Y）方向填充
        Button(fm3, text='第一个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第二个').pack(side=BOTTOM, fill=Y, expand=YES)
        Button(fm3, text='第三个').pack(side=BOTTOM, fill=Y, expand=YES)


root = Tk()
root.title("Pack布局")
display = App(root)
root.mainloop()
"""
上面程序创建了三个 Frame 容器,其中第一个 Frame 容器内包含三个从顶部(TOP)开始排列的按钮,
这意味着这三个按钮会从上到下依次排列,且这三个按钮能在水平(X)方向上填充;第二个 Frame 容器内包含三个从右边(RIGHT)
开始排列的按钮,这意味着这三个按钮会从右向左依次排列;
第三个 Frame 容器内包含三个从底部 (BOTTOM)开始排列的按钮,这意味着这三个按钮会从下到上依次排列,且这三个按钮能在垂直 (Y)

运行上面程序,将看到如图11.6所示的界面。

从图11.6中可以看到,为运行效果添加了三个框,分别代表 fm1、fm2、fm3(实际上容器是看不到的),
此时可以看到 fm1内的三个按钮从上到下排列,并且可以在水平方向上填充;fm3 内的三个按钮 从下到上排列,并且可以在垂直方向上填充。

可能有读者会有疑问： fm2 内的三个按钮也都设置了fll=Y,expand=YES,  这说明它们也能在垂直方方向上填充。
向上填充,为啥看不到呢?仔细看fm2.pack(side=LEFT,padx=10,expand=YES)这行代码,它说明
fm2 本身不在任何方向上填充,因此fm2 内的三个按钮都不能填充。

如果希望看到fm2 内的三个按钮也能在垂直方向上填充,则可将fm2 的 pack()方法改为如下代码。
fm2.pack(side=LEFT,padx=10,fill=BOTH,expand=YES)

通过上面介绍不难发现,Pack 布局其实还是非常灵活的,它完全可以实现很复杂的用户界面。
这里有一个界面分解的常识需要说明：无论看上去多么复杂、古怪的界面,其实大多可分解为水平排列和垂直排列,
而Pack 布局既可实现水平排列,也可实现垂直排列,然后再通过多个容器进行组合,这样就可以开发出更复杂的界面了。

对于打算使用 Pack 布局的开发者来说,首先要做的事情是将程序界面进行分解,分解成水平排列的容器和垂直排列的容器——
有时候甚至要容器嵌套容器,然后使用多个 Pack 布局的容器将它们组合在一起。
"""