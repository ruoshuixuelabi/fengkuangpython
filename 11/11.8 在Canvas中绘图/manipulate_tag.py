"""
11.8.2	操作图形项的标签
在Canvas中通过create xxx 方法绘制图形项之后,这些图形项并不是完全静态的图形,每个 图形项都是一个独立的对象,程序完全可以动态地修改、删除这些图形项。


Canvas以“堆叠”的形式来管理这些图形项,先绘  制的图形项位于“堆叠”的下面,后绘制的图形项位于  “堆叠”的上面。因此,如果两个图形项有重叠的部分, 那么后绘制的图形项(位于上面)会遮挡先绘制的图形  项。 Canvas管理图形项的堆叠形式如图11.53所示。
为了修改、删除这些图形项,程序需要先获得这些 图形项的引用。获得这些图形项的引用有两种方式。
通过图形项的id,也就是Canvas执行create xxx() 方法的返回值。 一般来说,create xxx()会依次返  回1、2、3等整数作为图形项的id。



图11.53  Canvas 管理图形项的堆叠形式

>通过图形项的tag(标签)。
在Canvas中调用create xxx()方法绘图时,还可传入一个tags选项,该选项可以为所绘制的图 形项(比如矩形、椭圆、多边形等)添加一个或多个tag(标签)。
此外,Canvas还允许调用方法为图形项添加tag、删除tag等,这些tag也相当于该图形项的 标识,程序完全可以根据tag来获取图形项。
总结来说,Canvas提供了如下方法来为图形项添加tag。
addtag above(self, newtag,tagOrld): 为tagOrld对应图形项的上一个图形项添加新tag。 addtag all(self,newtag): 为所有图形项添加新tag。
addtag below(self,newtag,tagOrld): 为tagOrld对应图形项的下一个图形项添加新tag。 addtag closest(self,newtag,x,y): 为和x、y 点最接近的图形项添加新tag。
> addtag enclosed(self,newtag,x1,y₁,x2,y2): 为指定矩形区域内最上面的图形项添加新tag。 其中x1、yl 确定矩形区域的左上角坐标；x2、 y2 确定矩形区域的右下角坐标。
addtag overlapping(self,newtag,x1,yl,x2,y2):为与指定矩形区域重叠的最上面的图形项添 加tag。

注 意  ……………………………………………
addtag enclosed()和 addtag overlapping()方法的说明与官方文档不一致,但实际 运行就是这个效果,应该是官方文档有错误。

addtag withtag(self,newtag,tagOrld): 为tagOrld对应图形项添加新tag。 Canvas提供了如下方法来删除图形项的tag。
> dtag(self,*args):删除指定图形项的tag。
Canvas提供了如下方法来获取图形项的所有tag。
> gettags(self,*args): 获取指定图形项的所有tag。
Canvas提供了如下方法根据tag来获取其对应的所有图形项。


343
仅供非商业用途或交流学习使用


> find withtag(self,tagOrld): 获 取tagOrld 对应的所有图形项。
为了更好地理解上面方法的作用,下面用一个程序来进行演示。
"""
from tkinter import *

# 创建窗口
root = Tk()
root.title('操作标签')
# 创建并添加Canvas
cv = Canvas(root, background='white', width=620, height=250)
cv.pack(fill=BOTH, expand=YES)
# 绘制一个矩形框
rt = cv.create_rectangle(40, 40, 300, 220,
    outline='blue', width=2,
    tag = ('t1', 't2', 't3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的id,也就是编号
print(rt) # 1
# 绘制一个椭圆
oval = cv.create_oval(350, 50, 580, 200,
    fill='yellow', width=0,
    tag = ('g1', 'g2', 'g3', 'tag4'))  # 为该图形项指定标签
# 访问图形项的id,也就是编号
print(oval) # 2
# 根据指定tag该tag对应的所有图形项
print(cv.find_withtag('tag4')) # (1, 2)
# 获取指定图形项的所有tag
print(cv.gettags(rt))  # ('t1', 't2', 't3', 'tag4')
print(cv.gettags(2))  # ('g1', 'g2', 'g3', 'tag4')
cv.dtag(1, 't1') # 删除id为1的图形项上名为t1的tag
cv.dtag(oval, 'g1') # 删除id为oval的图形项上名为g1的tag
# 获取指定图形项的所有tag
print(cv.gettags(rt))  # ('tag4', 't2', 't3')
print(cv.gettags(2))  # ('tag4', 'g2', 'g3')
# 为所有图形项添加tag
cv.addtag_all('t5')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5')
# 为指定图形项添加tag
cv.addtag_withtag('t6', 'g2')
# 获取指定图形项的所有tag
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6')
# 为指定图形项上面的图形项添加tag, t2上面的就是oval图形项
cv.addtag_above('t7', 't2')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7')
# 为指定图形项下面的图形项添加tag, g2下面的就是rt图形项
cv.addtag_below('t8', 'g2')
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7')
# 为最接近指定点的图形项添加tag,最接近360、90的图形项是oval
cv.addtag_closest('t9', 360, 90)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9')
# 为位于指定区域内（几乎覆盖整个图形区）的最上面的图形项添加tag
cv.addtag_closest('t10', 30, 30, 600, 240)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9', 't10')
# 为与指定区域内重合的最上面的图形项添加tag
cv.addtag_closest('t11', 250, 30, 400, 240)
print(cv.gettags(1))  # ('tag4', 't2', 't3', 't5', 't8')
print(cv.gettags(oval))  # ('tag4', 'g2', 'g3', 't5', 't6', 't7', 't9', 't10', 't11')
root.mainloop()
"""
上面程序示范了操作图形项的tag的方法,而且列出了每次操作之后的输出结果。因此,读者 可以结合程序的运行结果来理解Canvas 是如何管理图形项的tag的。
"""