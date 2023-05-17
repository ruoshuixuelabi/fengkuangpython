"""
在 functools 模块中主要包含了一些函数装饰器和便捷的功能函数。在 Python 的交互式解释器中先导入 functools 模块,
然后输入[e for e in dir(functools) if not e.startswith('_')]命令,即可看到该模 块所包含的全部属性和函数。
import functools
[e for e in dir(functools) if not e.startswith('_')]
['GenericAlias', 'RLock', 'WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', 'cache', 'cached_property', 'cmp_to_key',
'get_cache_token', 'lru_cache', 'namedtuple', 'partial', 'partialmethod', 'recursive_repr', 'reduce', 'singledispatch',
'singledispatchmethod', 'total_ordering', 'update_wrapper', 'wraps']

在 functools 模块中常用的函数装饰器和功能函数如下。
(1)functools.cmp_to_key(func)：将老式的比较函数(func)转换为关键字函数(key function)。
在 Python3 中比较大小、排序都是基于关键字函数的,Python 3不支持老式的比较函数。
(2)@functools.Iru_cache(maxsize=128,typed=False)：该函数装饰器使用LRU(最近最少使用)缓存算法来缓存相对耗时的函数结果,
避免传入相同的参数重复计算。同时,缓存并不会无限增长,不用的缓存会被释放。
其中 maxsize 参数用于设置缓存占用的最大字节数,typed 参数用于设置将不同类型的缓存结果分开存放。
(3)@functools.total_ordering：这个类装饰器(作用类似于函数装饰器,只是它用于修饰类)用于为类自动生成比较方法。
通常来说,开发者只要提供__It__()、__le__()、__gt__()、__ge__()其中之一(最好能提供__eq__()方法),
@functools.total_ordering装饰器就会为该类生成剩下的比较方法。
(4)functools.partial(func,*args,**keywords)：该函数用于为 func 函数的部分参数指定参数值,
从而得到一个转换后的函数,程序以后调用转换后的函数时,就可以少传入那些已指定值的参数。
(5)functools.partialmethod(func,*args,**keywords)：该函数与上一个函数的含义完全相同,只不过该函数用于为类中的方法设置参数值。
(6)functools.reduce(function, iterable[, initializer])：将初始值(默认为0,可由initializer参数指定)、
迭代器的当前元素传入function 函数,将计算出来的函数结果作为下一次计算的初始值、
迭代器的下一个元素再次调用 function 函数 ……依此类推,直到迭代器的最后一个元素。
(7)@functools.singledispatch：该函数装饰器用于实现函数对多个类型进行重载。比如同样的函数名称,为不同的参数类型提供不同的功能实现。该函数的本质就是根据参数类型的变 换,将函数转向调用不同的函数。
(8)functools.update_wrapper(wrapper,wrapped,assigned=WRAPPER ASSIGNMENTS,updated=WRAPPER UPDATES):
对 wrapper 函数进行包装,使之看上去就像wrapped (被包装)函数。
(9)@functools.wraps(wrapped,assigned=WRAPPER ASSIGNMENTS,updated=WRAPPER_UPDATES):
该函数装饰器用于修饰包装函数,使包装函数看上去就像 wrapped 函数。

提示： 通过介绍不难发现,functools.update_wrapper和 @functools.wraps的功能是一样的,
只不过前者是函数,因此需要把包装函数作为第一个参数传入;而后者是函数装饰器,
因此使用该函数装饰器修饰包装函数即可,无须将包装函数作为第一个参数传入。

提示：比较函数接收两个参数,比较这两个参数并根据它们的大小关系返回负值(代表前者小于后者)、
零或正值(代表前者大于后者);关键字函数则只需要一个参数,通过该 参数可返回一个用于排序关键字的值。

下面程序示范了 functools 模块中部分函数或函数装饰器的用法。
"""
from functools import *

# 以初始值（默认为0）为x,以当前序列元素为y,x+y的和作为下一次的初始值
print(reduce(lambda x, y: x + y, range(5)))  # 10
print(reduce(lambda x, y: x + y, range(6)))  # 15
# 设初始值为10
print(reduce(lambda x, y: x + y, range(6), 10))  # 25
print('----------------')


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'User[name=%s' % self.name


# 定义一个老式的大小比较函数,User的name越长,该User越大
def old_cmp(u1, u2):
    return len(u1.name) - len(u2.name)


my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
# 对my_data排序,需要关键字参数（调用cmp_to_key将old_cmp转换为关键字参数
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('----------------')


@lru_cache(maxsize=32)
def factorial(n):
    print('~~计算%d的阶乘~~' % n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 只有这行会计算,然后会缓存5、4、3、2、1的解乘
print(factorial(5))
print(factorial(3))
print(factorial(5))
print('----------------')
# int函数默认将10进制的字符串转换为整数
print(int('12345'))
# 为int函数的base参数指定参数值
basetwo = partial(int, base=2)
basetwo.__doc__ = '将二进制的字符串转换成整数'
# 相当于执行base为2的int()函数
print(basetwo('10010'))
print(int('10010', 2))
"""
上面程序中第一行粗体字代码调用 reduce()函数来计算序列的"累计"结果,在调用该函数时传入的第一个参数(函数)决定了累计算法,
此处使用的累计算法是"累加"。

程序中第二行粗体字代码调用 cmp_to_key()函数将老式的大小比较函数(old_cmp)转换为关键字函数,
这样该关键字函数即可作为列表对象的 sort()方法的参数。

程序中第三行粗体字代码调用@lru_cache 对函数结果进行缓存,后面程序第一次执行 factorial(5)时将会看到执行结果;
但接下来调用factorial(3)、factorial(5)时都不会看到执行结果,因为它们的结果已被缓存起来。

程序中第四行粗体字代码调用partial()函数为int()函数的base参数绑定值"2",
这样程序以后调用该函数时实际上就相当于调用base 为 2 的int()函数。所以,上面程序中最后两行代码的本质是完全一样的。
"""