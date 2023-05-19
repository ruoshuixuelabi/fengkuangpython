"""
Checkbutton 与 Radiobutton 很相似,只是 Checkbutton 允许选择多项,而每组Radiobutton 只能选择一项。
其他功能基本相似,同样可以显示文字和图片,同样可以绑定变量,同样可以为选中事件绑定处理函数和处理方法。
但由于 Checkbutton 可以同时选中多项,因此程序需要为每个 Checkbutton都绑定一个变量。

Checkbutton 就像开关一样,它支持两个值：开关打开的值和开关关闭的值。
因此,在创建 Checkbutton时可同时设置onvalue和 offvalue 选项为打开和关闭分别指定值。
如果不指定onvalue 和 offvalue, 则 onvalue默认为1, offvalue默认为0。

下面程序通过两组Checkbutton 示 范 了Checkbutton 的用法。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个Label组件
        ttk.Label(self.master, text='选择您喜欢的人物:') \
            .pack(fill=BOTH, expand=YES)
        self.chars = []
        # 定义元组
        characters = ('孙悟空', '猪八戒', '唐僧', '牛魔王')
        # 采用循环创建多个Checkbutton
        for ch in characters:
            intVar = IntVar()
            self.chars.append(intVar)
            cb = ttk.Checkbutton(self.master,
                                 text=ch,
                                 variable=intVar,  # 将Checkbutton绑定到intVar变量
                                 command=self.change)  # 将选中事件绑定到self.change方法
            cb.pack(anchor=W)
        # 创建一个Label组件
        ttk.Label(self.master, text='选择您喜欢的图书:') \
            .pack(fill=BOTH, expand=YES)
        # --------------下面是第二组Checkbutton---------------
        self.books = []
        # 定义两个元组
        books = ('疯狂Python讲义', '疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Java讲义')
        vals = ('python', 'kotlin', 'swift', 'java')
        i = 0
        # 采用循环创建多个Checkbutton
        for book in books:
            strVar = StringVar()
            self.books.append(strVar)
            cb = ttk.Checkbutton(self.master,
                                 text=book,
                                 variable=strVar,  # 将Checkbutton绑定到strVar变量
                                 onvalue=vals[i],
                                 offvalue='无',
                                 command=self.books_change)  # 将选中事件绑定到books_change方法
            cb.pack(anchor=W)
            i += 1

    def change(self):
        # 将self.chars列表转换成元素为str的列表
        new_li = [str(e.get()) for e in self.chars]
        # 将new_li列表连接成字符串
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)

    def books_change(self):
        # 将self.books列表转换成元素为str的列表
        new_li = [e.get() for e in self.books]
        # 将new_li列表连接成字符串
        st = ', '.join(new_li)
        messagebox.showinfo(title=None, message=st)


root = Tk()
root.title("Checkbutton测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中第一组 Checkbutton 没有指定onvalue 和 ofivalue,因此它们的onvalue和 offvalue默认分别为1、0,
所以程序将这组Checkbutton 绑 定 到 IntVar 类型的变量;
第二组 Checkbutton 将onvalue和 offvalue都指定为字符串,因此程序将这组Checkbutton绑定到StringVar类型的变量。

运行该程序,选中"疯狂 Kotlin 讲义"选项,可以看到如图11.21所示的运行效果。
"""