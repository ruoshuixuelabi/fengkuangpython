"""
11.5.4	Entry 和 Text 组件

Entry 和 Text 组件都是可接收用户输入的输入框组件,区别是 Entry 是单行输入框组件,Text 是多行输入框组件,
而且 Text 可以为不同的部分添加不同的格式,甚至响应事件。

不管是 Entry 还是 Text 组件,程序都提供了get()方法来获取文本框中的内容;
但如果程序要改变文本框中的内容,则需要调用二者的insert()方法来实现。

如果要删除Entry或 Text 组件中的部分内容,则可通过delete(self,first, last=None)方法实现, 该方法指定删除从first到 last之间的内容。

关于Entry 和 Text支持的索引需要说明一下,由于Entry是单行文本框组件,因此它的索引很简单,
比如要指定第4个字符到第8个字符,索引指定为(3,8)即可。但Text是多行文本框组件,
因此它的索引需要同时指定行号和列号,比如1.0代表第1行、第1列(行号从1开始,列号从0 开始),
如果要指定第2行第3个字符到第3行第7个字符,索引应指定为(2.2,3.6)。

此外,正如从前面程序所看到的,Entry 支持双向绑定,程序可以将Entry与变量绑定在一起,
这样程序就可以通过该变量来改变、获取Entry组件中的内容。

下面程序示范了Entry和 Text组件的用法。
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
        # 创建Entry组件
        self.entry = ttk.Entry(self.master,
                               width=44,
                               font=('StSong', 14),
                               foreground='green')
        self.entry.pack(fill=BOTH, expand=YES)
        # 创建Entry组件
        self.text = Text(self.master,
                         width=44,
                         height=4,
                         font=('StSong', 14),
                         foreground='gray')
        self.text.pack(fill=BOTH, expand=YES)
        # 创建Frame作为容器
        f = Frame(self.master)
        f.pack()
        # 创建五个按钮,将其放入Frame中
        ttk.Button(f, text='开始插入', command=self.insert_start).pack(side=LEFT)
        ttk.Button(f, text='编辑处插入', command=self.insert_edit).pack(side=LEFT)
        ttk.Button(f, text='结尾插入', command=self.insert_end).pack(side=LEFT)
        ttk.Button(f, text='获取Entry', command=self.get_entry).pack(side=LEFT)
        ttk.Button(f, text='获取Text', command=self.get_text).pack(side=LEFT)

    def insert_start(self):
        # 在Entry和Text开始处插入内容
        self.entry.insert(0, 'Kotlin')
        self.text.insert(1.0, 'Kotlin')

    def insert_edit(self):
        # 在Entry和Text的编辑处插入内容
        self.entry.insert(INSERT, 'Python')
        self.text.insert(INSERT, 'Python')

    def insert_end(self):
        # 在Entry和Text的结尾处插入内容
        self.entry.insert(END, 'Swift')
        self.text.insert(END, 'Swift')

    def get_entry(self):
        messagebox.showinfo(title='输入内容', message=self.entry.get())

    def get_text(self):
        messagebox.showinfo(title='输入内容', message=self.text.get(1.0, END))


root = Tk()
root.title("Entry测试")
App(root)
root.mainloop()
"""
上面程序开始创建了一个 Entry 组件和一个 Text 组件,程序中前面两行粗体字代码用于在 Entry 和 Text 组件的开始部分插入指定文本内容——
如果要在 Entry、Text 的指定位置插入文本内容,通过 insert()方法的第一个参数指定位置即可。
如果要在编辑处插入内容,则将第一个参数设为 INSERT 常量(值为'insert');如果要在结尾处插入内容,则将第一个参数设为END 常量(值为'end')。

上面程序中后面两行粗体字代码调用了Entry和 Text组件的get)方法来获取其中的文本内容。

运行上面程序,尝试向 Entry、Text 中插入一些内 容,然后单击界面上的“获取Text”按钮,则可以看到 如图11.17所示的界面。
Text实际上是一个功能强大的"富文本"编辑组件,这意味着使用 Text 不仅可以插入文本内容,也可以插入图片,
可通过 image_create(self,index,cnf={},**kw)方法来插入。

Text 也可以设置被插入文本内容的格式,此时就需要为insert(self,index,chars,*args)方法的最后一个参数传入多个tag进行控制,
这样就可以使用Text组件实现图文并茂的效果。
"""