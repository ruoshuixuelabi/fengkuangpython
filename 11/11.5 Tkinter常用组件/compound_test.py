"""
11.5.3	使用 compound 选项

程序可以为按钮或Label 等组件同时指定text和 image 两个选项,其中text用于指定该组件上的文本;
image 用于显示该组件上的图片,当同时指定这两个选项时,通常image 会覆盖text。
但在某些时候,程序希望该组件能同时显示文本和图片,此时就需要通过 compound 选项进行控制。

compound 选项支持如下属性值。
(1)None:    图片覆盖文字。
(2)LEFT    常量(值为'left'字符串):图片在左,文本在右。
(3)RIGHT    常量(值为'right'字符串):图片在右,文本在左。
(4)TOP    常量(值为'top'字符串):图片在上,文本在下。
(5)BOTTOM      常量(值为'bottom'字符串):图片在底,文本在上。
(6)CENTER     常量(值为'center'字符串):文本在图片上方。

下面程序使用多个单选钮来控制Label 的 compound 选项。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个位图
        bm = PhotoImage(file='images/serial.png')
        # 创建一个Label,同时指定text和image
        self.label = ttk.Label(self.master, text='疯狂体\n系图书', \
                               image=bm, font=('StSong', 20, 'bold'), foreground='red')
        self.label.bm = bm
        # 设置Label默认的compound为None
        self.label['compound'] = None
        self.label.pack()
        # 创建Frame容器,用于装多个Radiobutton
        f = ttk.Frame(self.master)
        f.pack(fill=BOTH, expand=YES)
        compounds = ('None', "LEFT", "RIGHT", "TOP", "BOTTOM", "CENTER")
        # 定义一个StringVar变量,用作绑定Radiobutton的变量
        self.var = StringVar()
        self.var.set('None')
        # 使用循环创建多个Radionbutton组件
        for val in compounds:
            rb = Radiobutton(f,
                             text=val,
                             padx=20,
                             variable=self.var,
                             command=self.change_compound,
                             value=val).pack(side=LEFT, anchor=CENTER)

    # 实现change_compound方法,用于动态改变Label的compound选项
    def change_compound(self):
        self.label['compound'] = self.var.get().lower()


root = Tk()
root.title("compound测试")
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码设置 Label 默认的 compound 选项为 None,这意味着该 Label 默认图片覆盖文字;
第二行粗体字会根据单选钮的值(单选钮与 self.var 绑定)来确定 Label 的 compound 选项。

运行该程序,将会看到 Label 中只显示图片,并不显示文字,这就是compound 选项为 None  的效果。
随着用户单击下面的单选钮,将可以看到Label 上图片和文字的位置的改变,如图11.16 所示。
"""