"""
6.5.5	使用super函数调用父类的构造方法
1.  Python 的子类也会继承得到父类的构造方法,如果子类有多个直接父类,那么排在前面的父类的构造方法会被优先使用。例如如下代码。
2.  下面程序中粗体字代码定义了 Manager 类,该类继承了 Employee 和 Customer 两个父类。
接下来程序中的 Manager 类将会优先使用 Employee 类的构造方法(因为它排在前面),所以程序使用 Manager(25000)来创建
Manager 对象。该构造方法只会初始化salary实例变量,因此执行上面程序中①号代码是没有任何问题的。
3.  但是当执行到②号代码时就会引发错误,这是由于程序在使用 Employee 类的构造方法创建 Manager 对象时,
程序并未初始化Customer 对象所需的两个实例变量：favorite 和 address,因此程序引发错误。
4.  如果将程序中粗体字代码改为如下形式。
class  Manager(Customer,Employee)
上面 Manager 类将优先使用 Customer 类的构造方法,因此程序必须使用如下代码来创建 Manager 对象。
m = Manager('IT产品’,'广州')
5.  上面代码为Manager 的构造方法传入两个参数,这明显是调用从Customer 类继承得到的两个构造方法,
此时程序将可以初始化 Customer 类中的 favorite 和 address 实例变量,但它又不能初始化Employee 类中的salary实例变量。
因此,此时程序中的②号代码可以正常运行,但①号代码会报错。
6.  为了让 Manager 能同时初始化两个父类中的实例变量,Manager 应该定义自己的构造方法——就是重写父类的构造方法。
Python 要求：如果子类重写了父类的构造方法,那么子类的构造方法必须调用父类的构造方法。
子类的构造方法调用父类的构造方法有两种方式。
(1)使用未绑定方法,这种方式很容易理解。因为构造方法也是实例方法,当然可以通过这种方式来调用。
(2)使用super()函数调用父类的构造方法。
7.  在交互式解释器中输入 help(super) 查看 super() 函数的帮助信息,可以看到如下输出信息。
8.  从上面介绍可以看出, super其实是一个类,因此调用 super() 的本质就是调用super 类的构造方法来创建super对象。
9.  从上面的帮助信息可以看到,使用super()构造方法最常用的做法就是不传入任何参数(这种做法与super(type,obj)的效果相同),
然后通过super对象的方法既可调用父类的实例方法,也可调用父类的类方法。
在调用父类的实例方法时,程序会完成第一个参数self的自动绑定,如上帮助信 息中①号信息所示。
在调用类方法时,程序会完成第一个参数cls的自动绑定,如上面帮助信息中 ② 号信息所示。
"""


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print('普通员工正在写代码,工资是:', self.salary)


class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address

    def info(self):
        print('我是一个顾客,我的爱好是: %s,地址是%s' % (self.favorite, self.address))


# Manager继承了Employee、Customer
# class Manager (Employee, Customer):
class Manager(Customer, Employee):
    pass


# m = Manager(25000)
m = Manager('IT产品', '广州')
# m.work()  #①
m.info()  # ②
