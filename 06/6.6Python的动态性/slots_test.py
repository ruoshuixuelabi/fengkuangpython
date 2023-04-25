"""
1.  __slots__  属性的值是一个元组,该元组的所有元素列出了该类的实例允许动态添加的所有属性名和方法名
(对于Python 而言,方法相当于属性值为函数的属性)。例如如下程序。
2.  下面程序中第一行粗体字代码定义了 __slots__ = ('walk', 'age', 'name'), 这意味着程序只允许为 Dog 实例动态添加
walk、age、name 这三个属性或方法。因此上面程序中第二行、第三行粗体字代 码为Dog 对象动态添加walk()方法和age 属性都是允许的。
3.  但如果程序尝试为Dog 对象添加其他额外属性,程序就会引发AttributeError错误,如下面最后一行代码所示。
运行上面程序,可以看到如下输出结果。
4.  需要说明的是,__slots__ 属性并不限制通过类来动态添加属性或方法,因此下面代码是合法的。
# slots    属性并不限制通过类来动态添加方法
Dog.bar = lambda self: print('abc')  # AttributeError
d.bar()
5.  下面代码通过Dog 类动态添加了bar()方法,这样 Dog 对象就可以调用该bar()方法了。
6.  此外,__slots__ 属性指定的限制只对当前类的实例起作用,对该类派生出来的子类是不起作用的。例如如下代码(程序清单同上)。
7.  正如从上面代码所看到的, Dog 的子类 GunDog 的实例完全可以动态添加 speed 属性,这说明 __slots__  属性指定的限制只对当前类起作用。
8.  如果要限制子类的实例动态添加属性和方法,则需要在子类中也定义 __slots__ 属性,这样,
子类的实例允许动态添加属性和方法就是子类的 __slots__ 元组加上父类的 __slots__ 元组的和。
"""


class Dog:
    __slots__ = ('walk', 'age', 'name')

    def __init__(self, name):
        self.name = name

    def test():
        print('预先定义的test方法')


d = Dog('Snoopy')
from types import MethodType

# 只允许动态为实例添加walk、age、name这3个属性或方法
d.walk = MethodType(lambda self: print('%s正在慢慢地走' % self.name), d)
d.age = 5
d.walk()
# d.foo = 30 # AttributeError
# __slots__属性并不限制通过类来动态添加方法
Dog.bar = lambda self: print('abc')  # AttributeError
d.bar()


class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    pass


gd = GunDog('Puppy')
# 完全可以为Gundog实例动态添加属性
gd.speed = 99
print(gd.speed)
