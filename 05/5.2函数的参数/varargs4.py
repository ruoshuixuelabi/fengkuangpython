"""
5.2.4 逆向参数收集
所谓逆向参数收集,指的是在程序已有列表、元组、字典等对象的前提下,把它们的元素"拆开"后传给函数的参数。

逆向参数收集需要在传入的列表、元组参数之前添加一个星号,在字典参数之前添加两个星号。 例如如下代码。
"""


def test(name, message):
    print("用户是: ", name)
    print("欢迎消息: ", message)


my_list = ['孙悟空', '欢迎来疯狂软件']
test(*my_list)
"""
上面粗体字代码定义了一个需要两个参数的函数,而程序中的 my_list 列表包含两个元素,
为了让程序将 my_list 列表的两个元素传给test()函数,程序在传入的 my_list 参数之前添加了一个星号。

实际上,即使是支持收集的参数,如果程序需要将一个元组传给该参数,那么同样需要使用逆向收集。例如如下代码(程序清单同上)。
"""


def foo(name, *nums):
    print("name参数: ", name)
    print("nums参数: ", nums)


my_tuple = (1, 2, 3)
# 使用逆向收集,将my_tuple元组的元素传给nums参数
foo('fkit', *my_tuple)
"""
上面粗体字代码调用将 'fkit' 传给 foo() 函数的 name 参数,然后使用逆向收集将 my_tuple 包含的多个元素传给nums 参数,
nums 再将 my_tuple 的多个元素收集成元组。

运行上面代码,将看到如下输出结果。

name参数:  fkit
nums参数:  (1, 2, 3)
"""
# 此外,也可使用如下方式调用foo()函数
# 使用逆向收集,将my_tuple元组的第一个元素传给name参数,剩下参数传给nums参数
foo(*my_tuple)
"""
此时程序会对 my_tuple 进行逆向收集,其中第一个元素传给 name 参数,后面剩下的元素传给 nums 参数。运行上面代码,将看到如下输出结果。

name参数:  1
nums参数:  (2, 3)
"""
# 如果不使用逆向收集(不在元组参数之前添加星号),整个元组将会作为一个参数,而不是将元组的元素作为多个参数
# 不使用逆向收集,my_tuple元组整体传给name参数
foo(my_tuple)
"""
上面调用没有使用逆向收集,因此my tuple 整体作为参数值传给name 参数。运行上面代码,将看到如下输出结果。

name参数:  (1, 2, 3)
nums参数:  ()
"""


# 字典也支持逆向收集,字典将会以关键字参数的形式传入。例如如下代码(程序清单同上)。
def bar(book, price, desc):
    print(book, " 这本书的价格是: ", price)
    print('描述信息', desc)


my_dict = {'price': 89, 'book': '疯狂Python讲义', 'desc': '这是一本系统全面的Python学习图书'}
# 按逆向收集的方式将my_dict的多个key-value传给bar()函数
bar(**my_dict)
"""
上面粗体字代码定义的bar()需要三个参数。接下来程序定义了一个 my_dict 字典,
该字典正好包含三个 key-value 对,程序使用逆向收集即可将 my_dict 包含的三个 key-value 对以关键字参数的形式传给bar()函数。
"""
