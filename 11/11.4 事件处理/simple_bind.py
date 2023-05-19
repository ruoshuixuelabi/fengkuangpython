"""
11.4.2 事件绑定

上面这种简单的事件绑定方式虽然简单,但它存在较大的局限性。
(1)程序无法为具体事件(比如鼠标移动、按键事件)绑定事件处理方法。
(2)程序无法获取事件相关信息。

为了弥补这种不足,Python 提供了更灵活的事件绑定方式,所有 Widget 组件都提供了一个bind() 方法,
该方法可以为"任意"事件绑定事件处理方法。

下面先看一个为按钮的单击、双击事件绑定事件处理方法的示例。
"""
# 将tkinter写成Tkinter可兼容Python 2.x
from tkinter import *


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.show = Label(self.master, width=30, bg='white', font=('times', 20))
        self.show.pack()
        bn = Button(self.master, text='单击我或双击我')
        bn.pack(fill=BOTH, expand=YES)
        # 为左键单击事件绑定处理方法
        bn.bind('<Button-1>', self.one)
        # 为左键双击事件绑定处理方法
        bn.bind('<Double-1>', self.double)

    def one(self, event):
        self.show['text'] = "左键单击:%s" % event.widget['text']

    def double(self, event):
        print("左键双击击, 退出程序:", event.widget['text'])
        import sys;
        sys.exit()


root = Tk()
root.title('简单绑定')
App(root)
root.mainloop()
"""
上面程序中两行粗体字代码为 Button 按钮的单击、双击事件绑定了事件处理方法,其中第一行粗体字代码为'<Btutton-1>'事件
绑定了 self.one 作为事件处理方法;第二行粗体字代码为'<Double-1>'事件绑定了self.double作为事件处理方法。

此时 self.one 和 self.double 方法都可定义一个 event 参数,该参数代表了传给该事件处理方法的事件对象,
因此上面程序示范了通过事件来获取事件源的方式——通过 event.widget 获取即可。
对于鼠标事件来说,鼠标相对当前组件的位置可通过 event 对象中的 x 和 y 属性来获取。

运行上面程序,单击界面上的按钮,将看到如图1. 11所示的运行结果。

从上面的例子可以看到,Tkinter 直接使用字符串来代表事件类型,比如使用<Button-1> 代表鼠标左键单击事件,
使用<Double-1>代表鼠标左键双击事件。那问题来了,其他事件应该怎么写呢?
代表Tkinter事件的字符串大致遵循如下格式。
<modifier-type-detail>

其中 type 是事件字符串的关键部分,用于描述事件的种类,比如鼠标事件、键盘事件等;modifier 则代表事件的修饰部分,比如单击、双击等;
detail 用于指定事件的详情,比如指定鼠标左键、右键、滚轮等。

Tkinter 支持的各种鼠标、键盘事件如表11.3所示。

表11.3 Tkinter支持的各种鼠标、键盘事件
事件	简介
<Button-detail>	鼠标按键的单击事件,detail指定哪一个鼠标键被单击。比如：单击鼠标左键为<Button-1>,单击鼠标中键为<Button-2>,单击鼠标右键为<Button-3>,单击向上滚动的滚轮为<Button-4>,单击向下滚动的滚轮为<Button-5>
<modifier-Motion>	鼠标在组件上的移动事件,modifier指定要求按住哪个鼠标键。比如按住鼠标左键移动为 <B1-Motion>,按住鼠标中键移动为<B2-Motion>,按住鼠标右键移动为<B3-Motion>
<ButtonRelease-detail>	鼠标按键的释放事件,detail指定哪 一 个鼠标键被释放。比如鼠标左键被释放为  <ButtonRelease-l>,鼠标中键被释放为<ButtonRelease-2>,鼠标右键被释放为<ButtonRelease-3>
<Double-Button-detail> 或<Double-detail>	用户双击某个鼠标键的事件,detail指定哪一个鼠标键被双击。比如双击鼠标左键为<Double-1>. 双击鼠标中键为<Double-2>,双击鼠标右键为<Double-3>,双击向上滚动的滚轮为<Double-4>,   双击向下滚动的滚轮为<Double-5>
<Enter>	鼠标进入组件的事件。注意：<Enter>事件不是按下回车键事件,按下回车键的事件是<Retumn>
<Leave>	鼠标移出组件事件
<FocusIn>	组件及其包含的子组件获得焦点
<FocusOut>	组件及其包含的子组件失去焦点
<Return>	按下回车键的事件。实际上可以为所有按键绑定事件处理方法。特殊键位名称包括Cancel、
BackSpace、Tab、Retum(回车)、Shift L(左Shif,如果只写Shift则代表任意Shift)、Control L (左Ctrl,如果只写Control则代表任意Ctrl)、Alt L(左Alt,如果只写Alt则代表任意Alt)、
Pause、Caps Lock、  Escape、Prior(Page Up)、Next(Page Down)、End、Home、Left、Up、
Right、Down、Print、Insert、Delete、F1、F2、F3、F4、F5、F6、F7、F8、F9、F10、F11、F12、
Num Lock和Scroll Lock
<Key>	键盘上任意键的单击事件,程序可通过event获取用户单击了哪个键
a	键盘上指定键被单击的事件。比如'a'代表a键被单击,b代表b键被单击(不要尖括号) ……
<Shift-Up>	在Shift键被按下时按Up键。类似的还有<Shif-Left>、<Shift-Down>、<Alt-Up>、<Control-Up> 等
<Configure>	组件大小、位置改变的事件。组件改变之后的大小、位置可通过event的width、height、x、y 获 取


"""