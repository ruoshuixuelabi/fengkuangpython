"""
11.7	菜单
Tkinter 为菜单提供了Menu 类,该类既可代表菜单条,也可代表菜单,还可代表上下文菜单 (右键菜单)。简单来说, Menu 类就可以搞定所有菜单相关内容。
程序可调用Menu 的构造方法来创建菜单,在创建菜单之后可通过如下方法添加菜单项。 add command():   添加菜单项。
add checkbutton(): 添加复选框菜单项。
add radiobutton(): 添加单选钮菜单项。
add separator(): 添加菜单分隔条。
上面的前三个方法都用于添加菜单项,因此都支持如下常用选项。
label:  指定菜单项的文本。
 command: 指定为菜单项绑定的事件处理方法。
image:   指定菜单项的图标。
compound:    指定在菜单项中图标位于文字的哪个方位。
有了菜单之后,接下来就是如何使用菜单了。菜单有两种用法。
在窗口上方通过菜单条管理菜单
通过鼠标右键触发右键菜单(上下文菜单)。
11.7.1   窗口菜单
在创建菜单之后,如果要将菜单设置为窗口的菜单条 (Menu  对象可被当成菜单条使用),则 只要将该菜单设为窗口的menu 选项即可。例如如下代码。
self.master['menu']=                      menubar
如果要将菜单添加到菜单条中,或者添加为子菜单,则调用Menu 的 add cascade()方法。 下面程序示范了如何为窗口添加菜单。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
from tkinter import messagebox as msgbox

class App:
    def __init__(self, master):
        self.master = master
        self.init_menu()
    # 创建菜单
    def init_menu(self):
        # 创建menubar,它被放入self.master中
        menubar = Menu(self.master)
        self.master.filenew_icon = PhotoImage(file='images/filenew.png')
        self.master.fileopen_icon = PhotoImage(file='images/fileopen.png')
        # 添加菜单条
        self.master['menu'] = menubar
        # 创建file_menu菜单,它被放入menubar中
        file_menu = Menu(menubar, tearoff=0)
        # 使用add_cascade方法添加file_menu菜单
        menubar.add_cascade(label='文件', menu=file_menu)
        # 创建lang_menu菜单,它被放入menubar中
        lang_menu = Menu(menubar, tearoff=0)
        # 使用add_cascade方法添加lang_menu菜单
        menubar.add_cascade(label='选择语言', menu=lang_menu)
        # 使用add_command方法为file_menu添加菜单项
        file_menu.add_command(label="新建", command = None, 
            image=self.master.filenew_icon, compound=LEFT)
        file_menu.add_command(label="打开", command = None, 
            image=self.master.fileopen_icon, compound=LEFT)
        # 使用add_command方法为file_menu添加分隔条
        file_menu.add_separator()
        # 为file_menu创建子菜单
        sub_menu = Menu(file_menu, tearoff=0)
        # 使用add_cascade方法添加sub_menu子菜单
        file_menu.add_cascade(label='选择性别', menu=sub_menu)
        self.genderVar = IntVar()
        # 使用循环为sub_menu子菜单添加菜单项
        for i, im in enumerate(['男', '女', '保密']):
            # 使用add_radiobutton方法为sub_menu子菜单添加单选菜单项
            # 绑定同一个变量,说明它们是一组
            sub_menu.add_radiobutton(label=im, command=self.choose_gender, 
                variable=self.genderVar, value=i)
        self.langVars = [StringVar(), StringVar(), StringVar(), StringVar()]
        # 使用循环为lang_menu菜单添加菜单项
        for i, im in enumerate(('Python', 'Kotlin','Swift', 'Java')):
            # 使用add_add_checkbutton方法为lang_menu菜单添加多选菜单项
            lang_menu.add_checkbutton(label=im, command=self.choose_lang, 
                onvalue=im, variable=self.langVars[i])
    def choose_gender(self):
        msgbox.showinfo(message=('选择的性别为: %s' % self.genderVar.get()))
    def choose_lang(self):
        rt_list = [e.get() for e in self.langVars]
        msgbox.showinfo(message=('选择的语言为: %s' % ','.join(rt_list)))
root = Tk()
root.title("菜单测试")
root.geometry('400x200')  
# 禁止改变窗口大小
root.resizable(width=False, height=False)
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码将Menu 设置为窗口的menu 选项,这意味着该菜单变成了菜 单条；第二行、第三行粗体字代码调用add cascade()方法添加菜单,这意味着为菜单条添加了两 个菜单。
接下来程序调用add command  方法为file menu添加多个菜单项,直到第四行粗体字代码调用
file menu的 add cascade()方法再次为file menu添加子菜单。
第五行粗体字代码位于循环中,这样程序调用add radiobutton()方法添加多个单选菜单项,这 些单选菜单项都绑定了一个变量,因此它们就是一组的；第六行粗体字代码位于循环中,这样程序调 用 add checkbutton()方法添加多个多选菜单项,每个多
选菜单项都有单独的值,因此它们都需要绑定 一个变量。
运行上面程序,可以看到如图11.46所示的效果。
由于程序为单选菜单项、多选菜单项都绑定了事件处 理方法,因此单击这些菜单项,程序将会弹出消息框提示 用户的选择。
"""