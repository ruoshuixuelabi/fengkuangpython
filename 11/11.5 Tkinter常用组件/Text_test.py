"""
此外,当Text 内容较多时就需要对该组件使用滚动条,以便该Text 能实现滚动显示。
为了让 滚动条控制Text 组件内容的滚动,实际上就是将它们进行双向关联。这里需要两步操作。
① 将 Scrollbar  的 command 设为目标组件的xview 或 yview,  其 中 xview 用于水平滚动条控制 目标组件水平滚动;
yview 用于垂直滚动条控制目标组件垂直滚动。
② 将目标组件的xscrollcommand  或 yscrollcommand  属性设为Scrollbar  的 set 方法。

如下程序示范了使用Text来实现一个图文并茂的界面。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建第一个Text组件
        text1 = Text(self.master, height=27, width=32)
        # 创建图片
        book = PhotoImage(file='images/java.png')
        text1.bm = book
        text1.insert(END, '\n')
        # 在结尾处插入图片
        text1.image_create(END, image=book)
        text1.pack(side=LEFT, fill=BOTH, expand=YES)
        # 创建第二个Text组件
        text2 = Text(self.master, height=33, width=50)
        text2.pack(side=LEFT, fill=BOTH, expand=YES)
        self.text = text2
        # 创建Scrollbar组件,设置该组件与text2的纵向滚动关联
        scroll = Scrollbar(self.master, command=text2.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置text2的纵向滚动影响scroll滚动条
        text2.configure(yscrollcommand=scroll.set)
        # 配置名为title的样式
        text2.tag_configure('title', font=('楷体', 20, 'bold'), foreground='red', justify=CENTER, spacing3=20)
        text2.tag_configure('detail', foreground='darkgray', font=('微软雅黑', 11, 'bold'),
                            spacing2=10,  # 设置行间距
                            spacing3=15)  # 设置段间距
        text2.insert(END, '\n')
        # 插入文本内容,设置使用title样式
        text2.insert(END, '疯狂Java讲义\n', 'title')
        # 创建图片
        star = PhotoImage(file='images/g016.gif')
        text2.bm = star
        details = ('《疯狂Java讲义》历时十年沉淀,现已升级到第4版,' + \
                   '经过无数Java学习者的反复验证,被包括北京大学在内的大量985、' + \
                   '211高校的优秀教师引荐为参考资料、选作教材。\n',
                   '《疯狂Java讲义》曾翻译为中文繁体字版,在宝岛台湾上市发行。\n',
                   '《疯狂Java讲义》屡获殊荣,多次获取电子工业出版社的“畅销图书”、' + \
                   '“长销图书”奖项,作者本人也多次获得“优秀作者”称号。' + \
                   '仅第3版一版的印量即达9万多册。\n')
        # 采用循环插入多条介绍信息
        for de in details:
            text2.image_create(END, image=star)
            text2.insert(END, de, 'detail')
        url = ['https://item.jd.com/12261787.html', 'http://product.dangdang.com/23532609.html']
        name = ['京东链接', '当当链接']
        m = 0
        for each in name:
            # 为每个链接创建单独的配置
            text2.tag_configure(m, foreground='blue', underline=True,
                                font=('微软雅黑', 13, 'bold'))
            text2.tag_bind(m, '<Enter>', self.show_arrow_cursor)
            text2.tag_bind(m, '<Leave>', self.show_common_cursor)
            # 使用handlerAdaptor包装,将当前链接参数传入事件处理函数
            text2.tag_bind(m, '<Button-1>', self.handlerAdaptor(self.click, x=url[m]))
            text2.insert(END, each + '\n', m)
            m += 1

    def show_arrow_cursor(self, event):
        # 光标移上去时变成箭头
        self.text.config(cursor='arrow')

    def show_common_cursor(self, event):
        # 光标移出去时恢复原样
        self.text.config(cursor='xterm')

    def click(self, event, x):
        import webbrowser
        # 使用默认浏览器打开链接
        webbrowser.open(x)

    def handlerAdaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)


root = Tk()
root.title("Text测试")
App(root)
root.mainloop()
"""
上面程序中第一段粗体字代码使用 Text 的 tag_configure(也写作tag_config) 方法创建了 title 和 detail 两个 tag,
每个 tag 可用于控制一段文本的格式、事件等。

接下来程序使用 title_tag 插入了一个标题内容,因此该标题内容的格式将受到 title_tag 的控制;
然后程序使用循环插入了三条受 detail_tag 控制的描述信息,每次在插入描述信息之前都先插入一张图片。

上面程序中第二段粗体字代码在循环内创建了 tag,并调用 Text 组件的 tag_bind()方法为 tag 绑定事件处理方法。

与前面的描述信息不同的是,此处程序需要让每个链接打开不同的页面,因此程序为每条链接内容分别创建了不同的tag,
从而实现为每个链接打开对应的页面。

运行上面程序,将看到如图11.18所示的图文并茂的界面。
"""