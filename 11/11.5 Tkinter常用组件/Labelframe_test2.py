"""
Labelframe 允许通过如下选项对标签进行定制。
(1)labelwidget：设置可以将任意GUI 组件作为标签。
(2)labelanchor：设置标签的位置。该选项支持'e'、's'、'w'、'n'、'es'、'ws'、'en'、'wn'、'ne'、'nw'、 'se'、'sw'这12个选项值,
用于控制标签的位置。

如下程序示范了对Labelframe 的标签进行定制。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建Labelframe容器
        self.lf = ttk.Labelframe(self.master, padding=20)
        self.lf.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        # 创建一个显示图片的Label
        bm = PhotoImage(file='images/z.png')
        lb = Label(self.lf, image=bm)
        lb.bm = bm
        # 将Labelframe的标题设为显示图片的Label
        self.lf['labelwidget'] = lb
        # 定义代表Labelframe的标题位置的12个常量
        self.books = ['e', 's', 'w', 'n', 'es', 'ws', 'en', 'wn',
                      'ne', 'nw', 'se', 'sw']
        i = 0
        self.intVar = IntVar()
        # 使用循环创建多个Radiobutton,并放入Labelframe中
        for book in self.books:
            Radiobutton(self.lf, text=book,
                        value=i,
                        command=self.change,
                        variable=self.intVar).pack(side=LEFT)
            i += 1
        self.intVar.set(9)

    def change(self):
        # 通过labelanchor选项改变Labelframe的标题的位置
        self.lf['labelanchor'] = self.books[self.intVar.get()]


root = Tk()
root.title("Labelframe测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码通过 labelwidget选项定制了该Labelframe 的标签,该选项值指定为一个显示图片的 Label,
因此该Labelframe的标签就是一张图片。程序中第二行粗体字代码将会根据单选钮的选中状态设置Labelframe的标签的位置。

运行该程序,改变Labelframe的标签的位置到右下角(se) 处,将看到如图11.30所示的界面。
"""