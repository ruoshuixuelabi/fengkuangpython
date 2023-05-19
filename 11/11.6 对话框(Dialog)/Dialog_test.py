"""
11.6	对话框(Dialog)
对话框也是图形界面编程中很常用的组件,通常用于向用户生成某种提示信息,或者请求用户 输入某些简单的信息。
对话框看上去有点类似于顶级窗口,但对于对话框有如下两点需要注意。
对话框通常依赖其他窗口,因此程序在创建对话框时同样需要指定master属性(该对话框 的属主窗口)。
>对话框有非模式 (non-modal) 和模式 (modal) 两种,当某个模式对话框被打开之后,该 模式对话框总是位于它依赖的窗口之上；在模式对话框被关闭之前,它依赖的窗口无法获 得焦点。
11.6.1	普通对话框
Tkinter在 simpledialog和 dialog模块下分别提供了SimpleDialog类 和Dialog 类,它们都可作 为普通对话框使用,而且用法也差不多。
在使用simpledialog.SimpleDialog创建对话框时,可指定如下选项。
> title: 指定该对话框的标题。
> text: 指定该对话框的内容。
> button: 指定该对话框下方的几个按钮。
default:  指定该对话框中默认第几个按钮得到焦点。
>cancel:  指定当用户通过对话框右上角的X 按钮关闭对话框时,该对话框的返回值。
如果使用dialog.Dialog创建对话框,除可使用master 指定对话框的属主窗口之外,还可通过 dict来指定如下选项。
> title: 指定该对话框的标题。
>text:  指定该对话框的内容。
strings:  指定该对话框下方的几个按钮。
default:  指定该对话框中默认第几个按钮得到焦点。
> bitmap: 指定该对话框上的图标。
对比上面介绍不难发现, simpledialog.SimpleDialog 和 dialog.Dialog所支持的选项大同小异, 区别只是dialog.Dialog需要使用dict来传入多个选项。
如下程序分别示范了使用SimpleDialog 和 Dialog 来创建对话框。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入simpledialog
from tkinter import simpledialog
# 导入dialog
from tkinter import dialog

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.msg = '《疯狂Java讲义》历时十年沉淀,现已升级到第4版,'+\
            '经过无数Java学习者的反复验证,被包括北京大学在内的大量985、'+\
            '211高校的优秀教师引荐为参考资料、选作教材。'
        # 创建2个按钮,并为之绑定事件处理函数
        ttk.Button(self.master, text='打开SimpleDialog',
            command=self.open_simpledialog # 绑定open_simpledialog方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)
        ttk.Button(self.master, text='打开Dialog',
            command=self.open_dialog # 绑定open_dialog方法
            ).pack(side=LEFT, ipadx=5, ipady=5, padx = 10)
    def open_simpledialog(self):
        # 使用simpledialog.SimpleDialog创建对话框
        d = simpledialog.SimpleDialog(self.master, # 设置该对话框所属的窗口
            title='SimpleDialog测试', # 标题
            text=self.msg,  # 内容
            buttons=["是", "否", "取消"],
            cancel=3,
            default=0 # 设置默认是哪个按钮得到焦点
        )
        print(d.go())  #①
    def open_dialog(self):
        # 使用dialog.Dialog创建对话框
        d = dialog.Dialog(self.master # 设置该对话框所属的窗口
            , {'title': 'Dialog测试',  # 标题
            'text':self.msg, # 内容
            'bitmap': 'question', # 图标
            'default': 0,  # 设置默认选中项
            # strings选项用于设置按钮
            'strings': ('确定',
                '取消',
                '退出')})
        print(d.num)  #②

root = Tk()
root.title("对话框测试")
App(root)
root.mainloop()
"""
上面程序中第一行粗体字代码使用simpledialog.SimpleDialog创建了对话框；第二行粗体字代 码使用dialog.Dialog创建了对话框。从上面代码可以看到,创建两个对话框的代码相似,区别只是


创建dialog.Dialog时需要使用dict传入选项。
运行上面程序,单击界面上的“打开SimpleDialog”按钮, 可以看到如图11.35所示的效果。
程序中①号代码打印了该对话框 go()方法的返回值,该 返回值会获取用户单击了对话框的哪个按钮。如果用户通过 对话框右上角的X 按钮关闭对话框,则返回cancel选项指定 的值。




图11.35  SimpleDialog对话框

如果单击界面上的“打开Dialog”按钮,可以看到如图11.36所示的效果。



319
仅供非商业用途或交流学习使用




程序中②号代码打印了该对话框num 属性的值,该返回 值会获取用户单击了对话框的哪个按钮。
在图11.36所示对话框的左边还显示了一个问号图标, 这 是Python 内置的10个位图之一 ,可以直接使用。共有如 下几个常量可用于设置位图。
>"error"
>"gray75"
>"gray50"
>"gray25"
>"gray12"
>"hourglass"
>"info"
>"questhead"
"question"
>"warning"
"""