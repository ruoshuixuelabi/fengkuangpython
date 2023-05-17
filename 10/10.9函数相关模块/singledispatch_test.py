"""
@singledispatch 函数装饰器的作用是根据函数参数类型转向调用另一个函数,从而实现函数重载的功能。

例如,如下程序示范了该函数装饰器的用法。
"""
from functools import *


@singledispatch
def test(arg, verbose):
    if verbose:
        print("默认参数为：", end=" ")
    print(arg)


# 限制test函数第一个参数为int型的函数版本
@test.register(int)
def _(argu, verbose):
    if verbose:
        print("整型参数为：", end=" ")
    print(argu)


test('Python', True)  # ①
# 调用第一个参数为int型的版本
test(20, True)  # ②
"""
上面程序中第一行粗体字代码使用 @singledispatch 装饰器修饰了 test()函数,
接下来程序即可通过 test()函数的 register()方法来注册被转向调用的函数。
程序中第二行粗体字代码使用 @test.register(int)修饰了目标函数,这意味着如果 test()函数的第一个参数为 int 类型,
实际上则会转向调用被@test.register(int)修饰的函数。

使用 @singledispatch 装饰器修饰之后的函数就有了 register()方法,该方法用于为指定类型注册被转向调用的函数。

程序中①号代码在调用test()函数时第一个参数是str类型,因此程序依然调用test()函数本身;
程序中②号代码在调用test()函数时第一个参数是 int 类型,因此将会转向调用被 @test.register(int) 修饰的函数。

运行上面程序,可以看到如下输出结果。
默认参数为： Python
整型参数为： 20

程序还可继续使用 @test.register() 装饰器来绑定被转向调用的函数。例如如下代码(程序清单同上)。
"""


# 限制test函数第一个参数为list型的函数版本
@test.register(list)
def _(argb, verbose=False):
    if verbose:
        print("列表中所有元素为:")
    for i, elem in enumerate(argb):
        print(i, elem, end=" ")


test([20, 10, 16, 30, 14], True)  # ③
print("\n---------------")
"""
上面粗体字代码显示test()函数的第一个参数是list时将转向调用被@test.register(list)修饰的函数。
而上面程序中③号代码在调用 test()函数时第一个参数是 list 对象,因此这行代码将会转向调用被 @test.register(list) 修饰的函数。
运行上面代码,将看到如下输出结果。
列表中所有元素为:
0 20 1 10 2 16 3 30 4 14 
---------------

此外,程序也可使用 register(类型,被转向调用的函数)方法来执行绑定。这种方式与前面使用函数装饰器的本质是一样的,
只不过这种语法没有修饰被转向调用的函数,因此额外多传入一个参数。例如如下代码(程序清单同上)。
"""


# 定义一个函数,不使用函数装饰器修饰
def nothing(arg, verbose=False):
    print("~~None参数~~")


# 当test函数第一个参数为None类型时,转向为调用nothing函数
test.register(type(None), nothing)
test(None, True)  # ④
print("\n---------------")
"""
上面程序中粗体字代码指定调用 test()函数的第一个参数为 None 类型时,程序将会转向调用 nothing 函数。
而上面程序中④号代码在调用 test()函数时第一个参数是 None, 因此这行代码将会转向调用nothing函数。
运行上面代码,可以看到如下输出结果。
~~None参数~~

---------------

此外,@singledispatch 也允许为参数的多个类型绑定同一个被转向调用的函数：只要使用多个 @函数名 .register()装饰器即可。
例如如下代码(程序清单同上)。
"""
from decimal import Decimal


# 限制test函数第一个参数为float或Decimal型的函数版本
@test.register(float)
@test.register(Decimal)
def test_num(arg, verbose=False):
    if verbose:
        print("参数的一半为:", end=" ")
    print(arg / 2)


"""
上面程序中两行粗体字代码使用@test.register(float)、@test.register(Decimal)修饰 test_num 函数,
这意味着程序在调用test()函数时无论第一个参数是 float 类型还是 Decimal 类型,其实都会转向调用 test_num 函数

当程序为 @singledispatch 函数执行绑定之后,程序就可以通过该函数的 dispatch(类型)方法来找到该类型所对应转向的函数。
例如如下代码(程序清单同上)。
"""

# test.dispatch(类型)即可获取它转向的函数
# 当test()函数第一个参数为float时将转向到调用test_num
print(test_num is test.dispatch(float))  # True
# 当test()函数第一个参数为Decimal时将转向到调用test_num
print(test_num is test.dispatch(Decimal))  # True
# 直接调用test并不等于test_num
print(test_num is test)  # False
"""
由于程序在调用test()函数时无论第一个参数类型是 float 还是Decimal,都会转向调用 test_num 函数,
因此test.dispatch(float)和 test.dispatch(Decimal)其实就是 test_num 函数。运行上面代码,将看到如下输出结果。
True
True
False

此外,如果想访问 @singledispatch 函数所绑定的全部类型及对应的dispatch函数,则可通过该函数的只读属性 registry 来实现,
该属性相当于一个只读的dict对象。例如如下代码(程序清单同上)。
"""
# 获取test函数所绑定的全部类型
print(test.registry.keys())
# 获取test函数为int类型绑定的函数
print(test.registry[int])
"""
运行上面代码,可以看到如下输出结果。
dict_keys([<class 'object'>, <class 'int'>, <class 'list'>, <class 'NoneType'>, <class 'decimal.Decimal'>, <class 'float'>])
<function _ at 0x000002B8DEA2C820>
"""
