"""
1.  在使用 property()函数定义属性时,也可根据需要只传入少量的参数。
例如,如下代码使用 property()函数定义了一个读写属性,该属性不能删除。
2.  下面粗体字代码使用property()定义了fullname属性,该程序使用propertyO函数时只传入两个参数,
分别作为getter和 setter方法,因此该属性是一个读写属性,不能删除。
3.  在某些编程语言中,类似于这种property合成的属性被称为计算属性。
这种属性并不真正存储任何状态,它的值其实是通过某种算法计算得到的。当程序对该属性赋值时,被赋的值也会被存储到其他实例变量中。
"""


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first + ',' + self.last

    def setfullname(self, fullname):
        first_last = fullname.rsplit(',');
        self.first = first_last[0]
        self.last = first_last[1]

    # 使用property()函数定义fullname属性,只传入2个参数
    # 该属性是一个读写属性,但不能删除
    fullname = property(getfullname, setfullname)


u = User('悟空', '孙')
# 访问fullname属性
print(u.fullname)
# 对fullname属性赋值
u.fullname = '八戒,朱'
print(u.first)
print(u.last)
