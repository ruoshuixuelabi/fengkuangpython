"""
单选钮除了可以显示文本,也可以显示图片,只要为其指定image 选项即可。如果希望图片和文字同时显示也是可以的,
只要通过compound 选项进行控制即可(如果不指定compound 选项,该选项默认为None, 这意味着只显示图片)。如下程序示范了带图片的单选钮。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建一个Label组件
        ttk.Label(self.master, text='选择您喜欢的兵种:') \
            .pack(fill=BOTH, expand=YES)
        self.intVar = IntVar()
        # 定义元组
        races = ('z.png', 'p.pNg', 't.png')
        raceNames = ('虫族', '神族', '人族')
        i = 1
        # 采用循环创建多个Radiobutton
        for rc in races:
            bm = PhotoImage(file='images/' + rc)
            r = ttk.Radiobutton(self.master,
                                image=bm,
                                text=raceNames[i - 1],
                                compound=RIGHT,  # 图片在文字右边
                                variable=self.intVar,  # 将Radiobutton绑定到self.intVar变量
                                command=self.change,  # 将选中事件绑定到self.change方法
                                value=i)
            r.bm = bm
            r.pack(anchor=W)
            i += 1
        # 设置默认选中value为2的单选按钮
        self.intVar.set(2)

    def change(self): pass


root = Tk()
root.title("Radiobutton测试")
# 改变窗口图标
root.iconbitmap('images/fklogo.ico')
App(root)
root.mainloop()
"""
上面程序中粗体字代码为 RadioButton 同时指定了image 和 text选项,并指定compound 选项为RIGHT,
这意味着该单选钮的图片显示在文字的右边。运行上面程序,可以看到如图11.20所示的运行界面。

提示：上面程序还重新设置了窗口图标,因此在运行界面上可以看到窗口图标是自定义的图标。
"""