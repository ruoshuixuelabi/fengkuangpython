"""
6.5.4	使用未绑定方法调用被重写的方法
1.  如果在子类中调用重写之后的方法,Python 总是会执行子类重写的方法,不会执行父类中被重写的方法。
如果需要在子类中调用父类中被重写的实例方法,那该怎么办呢?
2.  读者别忘了,Python 类相当于类空间,因此Python 类中的方法本质上相当于类空间内的函数。
所以,即使是实例方法, Python 也允许通过类名调用。区别在于：在通过类名调用实例方法时,
Python不会为实例方法的第一个参数self自动绑定参数值,而是需要程序显式绑定第一个参数self。 这种机制被称为未绑定方法。
3.  通过使用未绑定方法即可在子类中再次调用父类中被重写的方法。例如如下程序。
4.  下面程序中 SubClass 继承了 BaseClass 类,并重写了父类的 foo()方法。
接下来程序在 SubClass 类中定义了 bar()方法,该方法的第一行粗体字代码直接通过self调用 foo()方法,
Python 将会执行子类重写之后的 foo()方法；第二行粗体字代码通过未绑定方法显式调用 BaseClass 中的foo 实例方法,
并显式为第一个参数self绑定参数值,这就实现了调用父类中被重写的方法。
"""


class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')


class SubClass(BaseClass):
    # 重写父类的foo方法
    def foo(self):
        print('子类重写父类中的foo方法')

    def bar(self):
        print('执行bar方法')
        # 直接执行foo方法,将会调用子类重写之后的foo()方法
        self.foo()
        # 使用类名调用实例方法（未绑定方法）调用父类被重写的方法
        BaseClass.foo(self)


sc = SubClass()
sc.bar()
