"""
11.8.4	为图形项绑定事件
Canvas 提供了一个tag bind()方法,该方法用于为指定图形项绑定事件处理函数或方法,这样 图形项就可以响应用户动作了。
下面程序示范了为矩形的单击事件绑定事件处理函数。
"""
from tkinter import *

root = Tk()
# 创建一个Canvas,设置其背景色为白色
cv = Canvas(root,bg = 'white')
cv.pack()
# 创建一个rectangle
cv.create_rectangle(30, 30, 220, 150,
    width = 8,
    tags = ('r1','r2','r3'))
def first(event):
    print('第一次的函数')
def second(event):
    print('第二次的函数')
# 为指定图形项的左键单击事件绑定处理函数
cv.tag_bind('r1','<Button-1>', first)
# 为指定图形项的左键单击事件绑定处理函数
cv.tag_bind('r1','<Button-1>', second, add=True) # add为True是添加,否则是替代
root.mainloop()
"""
上面程序中第 一行粗体字代码为rl 对应的图形项的左键单击事件绑定事件处理函数,第二行 粗体字代码依然为r1 对应的图形项的左键单击事件绑定事件处理函数,其中的add 选 项 为True,  表示为该图形项再次添加 一个事件处理函数(即为该图形项的单击事件绑定两个事件处理函数);  如果将add 选 项 设 为False,则表示第二次添加的事件处理函数会取代第一次添加的事件处理函数。
"""