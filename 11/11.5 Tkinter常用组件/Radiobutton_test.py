"""
11.5.5	Radiobutton和 Checkbutton 组件

Radiobutton 组件代表单选钮,该组件可以绑定一个方法或函数,当单选钮被选择时,该方法或函数将会被触发。

为了将多个 Radiobutton 编为一组,程序需要将多个 Radiobutton 绑定到同一个变量,
当这组 Radiobutton 的其中一个单选钮被选中时,该变量会随之改变;
反过来,当该变量发生改变时,这 组 Radiobutton也会自动选中该变量值所对应的单选钮。

下面程序示范了Radiobutton组件的用法。
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
        ttk.Label(self.master, text='选择您喜欢的图书:') \
            .pack(fill=BOTH, expand=YES)
        self.intVar = IntVar()
        # 定义元组
        books = ('疯狂Kotlin讲义', '疯狂Python讲义',
                 '疯狂Swift讲义', '疯狂Java讲义')
        i = 1
        # 采用循环创建多个Radiobutton
        for book in books:
            ttk.Radiobutton(self.master,
                            text=book,
                            variable=self.intVar,  # 将Radiobutton绑定到self.intVar变量
                            command=self.change,  # 将选中事件绑定到self.change方法
                            value=i).pack(anchor=W)
            i += 1
        # 设置Radiobutton绑定的变量的值为2,
        # 则选中value为2的Radiobutton
        self.intVar.set(2)

    def change(self):
        from tkinter import messagebox
        # 通过Radiobutton绑定变量获取选中的单选框
        messagebox.showinfo(title=None, message=self.intVar.get())


root = Tk()
root.title("Radiobutton测试")
App(root)
root.mainloop()
"""
上面程序使用循环创建了多个 Radiobutton 组件,程序中第一行粗体字代码指定将这些 Radiobutton绑定到selfintVar 变量,
这意味着这些Radiobutton位于同一组内；第二行粗体字代码 为这组Radiobutton 的选中事件绑定了selfchange方法,
因此每次当用户选择不同的单选钮时,总 会触发该对象的change()方法。

运行上面程序,可以看到程序默认选中第二个单选钮,这是因为第二个单选钮的value为2,而程序将这组单选钮绑定的selfintVar
的值设置为2;如果用户改变选中其他单选钮,程序将会弹出提示框显示用户的选择项,如图11.19所示。
"""