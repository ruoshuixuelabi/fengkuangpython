"""
11.7.2	右键菜单
实现右键菜单很简单,程序只要先创建菜单,然后为目标组件的右键单击事件绑定处理函数,

4  334
仅供非商业用途或交流学习使用


当用户单击鼠标右键时,调用菜单的post()方法即可在指定位置弹出右键菜单。 如下程序示范了创建并添加右键菜单。
"""
from tkinter import *
# 导入ttk
from tkinter import ttk
from collections import OrderedDict
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        self.text = Text(self.master, height=12, width=60,
            foreground='darkgray', 
            font=('微软雅黑', 12),
            spacing2=8, # 设置行间距
            spacing3=12) # 设置段间距
        self.text.pack()
        st = '《疯狂Java讲义》历时十年沉淀,现已升级到第4版,' +\
            '经过无数Java学习者的反复验证,被包括北京大学在内的大量985、' +\
            '211高校的优秀教师引荐为参考资料、选作教材。\n'
        self.text.insert(END, st)
        # 为text组件的右键单击事件绑定处理方法
        self.text.bind('<Button-3>',self.popup)
        # 创建Menu对象,准备作为右键菜单
        self.popup_menu = Menu(self.master,tearoff = 0)
        self.my_items = (OrderedDict([('超大', 16), ('大',14), ('中',12),
            ('小',10), ('超小',8)]),
            OrderedDict([('红色','red'), ('绿色','green'), ('蓝色', 'blue')]))
        i = 0
        for k in ['字体大小','颜色']:
            m = Menu(self.popup_menu, tearoff = 0)
            # 添加子菜单
            self.popup_menu.add_cascade(label=k ,menu = m)
            # 遍历OrderedDict的key（默认就是遍历key）
            for im in self.my_items[i]:
                m.add_command(label=im, command=self.handlerAdaptor(self.choose, x=im))
            i += 1
    def popup(self, event):
        # 在指定位置显示菜单
        self.popup_menu.post(event.x_root,event.y_root)  #①
    def choose(self, x):
        # 如果用户选择修改字体大小的子菜单项
        if x in self.my_items[0].keys():
            # 改变字体大小
            self.text['font'] = ('微软雅黑', self.my_items[0][x])
        # 如果用户选择修改颜色的子菜单项
        if x in self.my_items[1].keys():
            # 改变颜色
            self.text['foreground'] = self.my_items[1][x]
    def handlerAdaptor(self, fun,**kwds):
        return lambda fun=fun, kwds=kwds: fun(**kwds)
root = Tk()
root.title("右键菜单测试")
App(root)
root.mainloop()
"""
上面程序中的粗体字代码用于创建一个Menu,  并为之添加菜单项。这段代码与前面介绍的创
建菜单、添加菜单项的代码并没有区别。
程序中①号代码位于Text组件的右键单击事件的处 理函数内,这行代码调用Menu 对象的post()方法弹出右  键菜单,这意味着当用户在Text组件内单击鼠标右键时, Text组件就会弹出右键菜单。
运行该程序,在界面上的Text组件内单击鼠标右键, 将可以看到如图11.48所示的右键菜单。
"""