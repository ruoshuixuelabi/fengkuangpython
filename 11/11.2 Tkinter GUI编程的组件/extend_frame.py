"""
此外,还有一种方式是不直接使用 Tk,只要创建 Frame 的子类,它的子类就会自动创建 Tk 对象作为窗口。例如如下程序。
"""
# Python 2.x使用这行
# from Tkinter import *
# Python 3.x使用这行
from tkinter import *


# 定义继承Frame的Application类
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        # 调用initWidgets()方法初始化界面
        self.initWidgets()

    def initWidgets(self):
        # 创建Label对象,第一个参数指定该Label放入root
        w = Label(self)
        # 创建一个位图
        bm = PhotoImage(file='serial.png')
        # 必须用一个不会被释放的变量引用该图片,否则该图片会被回收
        w.x = bm
        # 设置显示的图片是bm
        w['image'] = bm
        w.pack()
        # 创建Button对象,第一个参数指定该Button放入root
        okButton = Button(self, text="确定")
        #        okButton['background'] = 'yellow'
        okButton.configure(background='yellow')
        okButton.pack()


# 创建Application对象
app = Application()
# Frame有个默认的master属性,该属性值是Tk对象（窗口）
print(type(app.master))
# 通过master属性来设置窗口标题
app.master.title('窗口标题')
# 启动主窗口的消息循环
app.mainloop()
"""
上面程序创建了 Frame 的子类：Application,并在该类的构造方法中调用了 initWidgets()方法——
这个方法可以是任意方法名,程序在 initWidgets()方法中创建了两个组件,即 Label 和 Button。

上面程序只是创建了 Application 的实例(Frame 容器的子类),并未创建 Tk 对象(窗口),那么这个程序有窗口吗?答案是肯定的。
如果程序在创建任意 Widget 组件(甚至Button)时没有指定 master 属性(即创建 Widget 组件时第一个参数传入None),
那么程序会自动为该 Widget 组件创建一个 Tk 窗口,因此 Python 会自动为 Application 实例创建 Tk 对象来作为它的master。

该程序与上一个程序的差别在于：程序在创建 Label 和 Button 之后,对 Label 进行了配置,设置了 Label 显示的背景图片;
也对 Button 进行了配置,设置了 Button 的背景色。

可能有读者对上面程序中的如下代码感到好奇：
w.x=        bm

这行代码负责为w 的x属性赋值。这行代码有什么作用呢?因为程序在 initWidgets()方法中创建了 PhotoImage 对象,这是一个图片对象。
当该方法结束时,如果该对象没有被其他变量引用,这个图片可能会被系统回收,此处由于w(Label 对象)需要使用该图片,
因此程序就让w 的 x 属性引用该 PhotoImage 对象,阻止系统回收 PhotoImage 的图片。

运行上面程序,可以看到如图11.4所示的效果。

仔细体会上面程序中 initWidgets()方法的代码,虽然看上去代码量不小,但实际上只有3行代码。
(1)创建 GUI 组件。相当于创建"积木块"。
(2)添加 GUI 组件,此处使用 pack()方法添加。相当于把"积木块"添加进去。
(3)配置 GUI 组件。

其中创建 GUI 组件的代码很简单,与创建其他 Python 对象并没有任何区别,但通常至少要指定一个参数,
用于设置该 GUI 组件属于哪个容器(Tk 组件例外,因为该组件代表顶级窗口)。

配置 GUI 组件有两个时机。
(1)在创建 GUI 组件时以关键字参数的方式配置。例如Button(self,text="确定"),其中text="确定"就指定了该按钮上的文本是"确定"。
(2)在创建完成之后,以字典语法进行配置。例如okButton['background]='yellow',
这种语法使得okButton 看上去就像一个字典,它用于配置okButton 的 background 属性,从而改变该按钮的背景色。

上面两种方式完全可以切换。比如可以在创建按钮之后配置该按钮上的文本,例如如下代码。
okButton['text']= '确定'

这行代码其实是调用 configure()方法的简化写法。也就是说,这样代码等同于如下代码。
okButton.configure(text = '确定')

也可以在创建按钮时就配置它的文本和背景色,例如如下代码。
# 创建 Button 对象,在创建时就配置它的文本和背景色
okButton = Button(self,text="确定",background='yellow'

这里又产生了一个问题：除可配置background、image 等选项之外,GUI 组件还可配置哪些选项呢?
可以通过该组件的构造方法的帮助文档来查看。例如,查看Button 的构造方法的帮助文档, 可以看到如下输出结果。
import tkinter
help(tkinter.Button.__init__)
Help on function __init__ in module tkinter:

__init__(self, master=None, cnf={}, **kw)
    Construct a button widget with the parent MASTER.
    
    STANDARD OPTIONS
    
        activebackground, activeforeground, anchor,
        background, bitmap, borderwidth, cursor,
        disabledforeground, font, foreground
        highlightbackground, highlightcolor,
        highlightthickness, image, justify,
        padx, pady, relief, repeatdelay,
        repeatinterval, takefocus, text,
        textvariable, underline, wraplength
    
    WIDGET-SPECIFIC OPTIONS
    
        command, compound, default, height,
        overrelief, state, width
        
上面的帮助文档指出,Button 支持两组选项：标准选项(STANDARD OPTIONS)和组件特定选项(WIDGET-SPECIFIC OPTIONS)。
至于这些选项的含义,基本上通过它们的名字就可猜出来。

此处简单介绍一下这些GUI 组件的常见选项的含义。表11.2显示了大部分GUI 组件都支持的选项。
表11.2  GUI 组件支持的通用选项

选项名(别名)	                含义	        单位	典型值
activebackground	    指定组件处于激活状态时的背景色	color	'gray25'或'#ff4400'
activeforeground	    指定组件处于激活状态时的前景色	color	'gray25'或'#ff4400'
anchor	                        指定组件内的信息(比如文本或图片)在组件中如何显示。 必须为下面的值之一：N、NE、E、SE、S、SW、W、NW 或CENTER。比如NW(NorthWest)指定将信息显示在组件的左上角		CENTER
background(bg)	        指定组件正常显示时的背景色	        color	'gray25'或'#ff4400'
bitmap	                    指定在组件上显示该选项指定的位图,该选项值可以是 Tk_GetBitmap 接收的任何形式的位图,位图的显示方式受 anchor、justify选项的影响。如果同时指定了 bitmap 和 text,那么 bitmap 覆盖文本：如果同时指定了bitmap和image,那么image覆盖bitmap		
borderwidth	            指定组件正常显示时的3D边框的宽度,该值可以是 Tk_GetPixels 接收的任何格式	pixel	2
cursor	                        指定光标在组件上的样式。该值可以是Tk GetCursors接 收的任何格式	cursor	gumby
command	                指定按组件关联的命令方法,该方法通常在鼠标离开组件时被触发调用		
disabledforeground	指定组件处于禁用状态时的前景色	color	'gray25'或'#ff4400'
font	                            指定组件上显示的文本字体	font	Helvetica'或('Verdana',8)
foreground(fg)	        指定组件正常显示时的前景色	color	'gray'或'#ff4400'
highlightbackground	指定组件在高亮状态下的背景色	color	'gray'或'#ff4400'
highlightcolor	            指定组件在高亮状态下的前景色	color	'gray'或'#ff4400'
highlighithickness	    指定组件在高亮状态下的周围方形区域的宽度,该值可以 是Tk_GetPixels接收的任何格式	pixel	2
height	                        指定组件的高度,以font选项指定的字体的字符高度为单 位,至少为1	integer	14
image	                        指定组件中显示的图像,如果设置了image选项,它将会 覆盖text、bitmap选项	image	
justify	                        指定组件内部内容的对齐方式,该选项支持LEFT(左对齐)、CENTER(居中对齐)或RIGHT(右对齐)这三 个值	constant	RIGHT
padx	                        指定组件内部在水平方向上两边的空白,该值可以是 Tk_GetPixels接收的任何格式	pixel	12
pady	                        指定组件内部在垂直方向上两边的空白,该值可以是 Tk_GetPixels接收的任何格式	pixel	12
relief	                        指定组件的3D效果,该选项支持的值包括RAISED、 SUNKEN、FLAT、RIDGE、SOLID、GROOVE。该值指 出组件内部相对于外部的外观样式,比如RAISED表示组件内部相对于外部凸起	constant	GROOVE RAISED
selectbackground	    指定组件在选中状态下的背景色	color	'gray'或'#ff4400'
selectborderwidth	    指定组件在选中状态下的3D边框的宽度,该值可以是 Tk_GetPixels接收的任何格式	pixel	2
selectforeground	    指定组件在选中状态下的前景色	color	'gray'或'#ff4400
state	                        指定组件的当前状态。该选项支持NORMAL(正常)、 DISABLE(禁用)这两个值	constant	NORMAL
takefocus	                指定组件在键盘遍历(Tab或Shift+Tab)时是否接收焦点,将该选项设为1表示接收焦点：设为0表示不接收焦点	boolean	1或YES
text	                            指定组件上显示的文本,文本显示格式由组件本身、anchor 及justify选项决定	str	'确定'
textvariable	            指定一个变量名,GUI组件负责显示该变量值转换得到的字符串,文本显示格式由组件本身、anchor及justify选项 决定	variable	bnText
underline	                指定为组件文本的第几个字符添加下画线,该选项就相当于为组件绑定了快捷键	integer	2
width	                        指定组件的宽度,以font选项指定的字体的字符高度为单位,至少为1	integer	14
wraplength	                对于能支持字符换行的组件,该选项指定每行显示的最大字符数,超过该数量的字符将会转到下行显示	integer	20
xscrollcommand	        通常用于将组件的水平滚动改变(包括内容滚动或宽度发生改变)与水平滚动条的set方法关联,从而让组件的水 平滚动改变传递到水平滚动条	function	scroll.set
yscrollcommand	        通常用于将组件的垂直滚动改变(包括内容滚动或高度发生改变)与垂直滚动条的set方法关联,从而让组件的垂 直滚动改变传递到垂直滚动条	function	scroll.set
"""
