"""
6.7 多态

对于弱类型的语言来说,变量并没有声明类型,因此同一个变量完全可以在不同的时间引用不同的对象。
当同一个变量在调用同一个方法时,完全可能呈现出多种行为(具体呈现出哪种行为由该变量所引用的对象来决定),
这就是所谓的多态(Polymorphism)。

6.7.1 多态性

先看下面程序
"""


class Bird:
    def move(field):
        print('鸟在%s上自由地飞翔' % field)


class Dog:
    def move(field):
        print('狗在%s里飞快的奔跑' % field)


# x变量被赋值为Bird对象
x = Bird()
# 调用x变量的move()方法
x.move('天空')
# x变量被赋值为Dog对象
x = Dog()
# 调用x变量的move()方法
x.move('草地')
"""
上面程序中x变量开始被赋值为 Bird 对象,因此当x变量执行move()方法时,它会表现出鸟类的飞翔行为;
接下来x变量被赋值为Dog 对象,因此当x变量执行move()方法时,它会表现出狗的奔跑行为。

从上面的运行结果可以看出,同一个变量x在执行同一个 move() 方法时,由于x指向的对象不同,因此它呈现出不同的行为特征,这就是多态。

看到这里,可能有读者感到失望：这个多态有什么用啊?不就是创建对象、调用方法吗?看不出多态有什么优势啊?
"""
