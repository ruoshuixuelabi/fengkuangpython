"""
1.  如果程序在运行过程中要动态判断是否包含某个属性(包括方法),甚至要动态设置某个属性值,则可通过Python 的反射支持来实现。

8.2.1	动态操作属性

2.  在动态检查对象是否包含某些属性(包括方法)相关的函数有如下几个。
(1)hasattr(obj,name):  检查obj对象是否包含名为name 的属性或方法。
(2)getattr(object, name[,default]):获 取object对象中名为name 的属性的属性值。
(3)setattr(obj, name, value,/): 将 obj 对象的name 属性设为value。
3.  下面程序示范了通过以上函数来动态操作Python对象的属性。
4.  上面程序先定义了一个Comment 类,接下来程序创建了Comment 类的实例。
程序后面部分示 范了 hasatt()、getatt()、setattr()三个函数的用法。从上面的示例代码可以看出,
hasattr()函数既可 判断属性,也可判断方法,但getattr()则只能获取属性的属性值。
5.  从上面最后两行输出来看,程序使用setattr()函数可改变Python 对象的属性值：如果使用该函数 对Python 对象设置的属性不存在,
那么就表现为添加属性—— 反正Python 是动态语言。看如下 代码。
6.  上面程序先定义了一个 bar()函数,在该函数中不能定义self参数(否则需要程序员显式为参 数传入参数值,
系统不会自动为该参数绑定参数值)。接下来程序调用setattr()函数将Comment  对 象的info()方法设置为bar()函数,
然后程序调用Comment 对象的info()方法,其实就是调用程序中 的bar()函数。
7.  不仅如此,程序完全可通过setattr()函数将info()方法设置成普通值,这样将会把info变成一个 属性,而不是方法,例如如下代码。
"""
class Comment:
    def __init__ (self, detail, view_times):
        self.detail = detail
        self.view_times = view_times
    def info ():
        print("一条简单的评论,内容是%s" % self.detail)
        
c = Comment('疯狂Python讲义很不错', 20)
# 判断是否包含指定的属性或方法
print(hasattr(c, 'detail')) # True
print(hasattr(c, 'view_times')) # True
print(hasattr(c, 'info')) # True
# 获取指定属性的属性值
print(getattr(c, 'detail')) # '疯狂Python讲义很不错'
print(getattr(c, 'view_times')) # 20
# 由于info是方法,故下面代码会提示：name 'info' is not defined
#print(getattr(c, info, '默认值'))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)
# 输出重新设置后的属性值
print(c.detail)
print(c.view_times)

# 设置不存在的属性,即为对象添加属性
setattr(c, 'test', '新增的测试属性')
print(c.test) # 新增的测试属性

def bar ():
    print('一个简单的bar方法')
# 将c的info方法设为bar函数    
setattr(c, 'info', bar)
c.info()

# 将c的info设置为字符串'fkit'
setattr(c, 'info', 'fkit')
c.info()
