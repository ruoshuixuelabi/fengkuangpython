"""
1.  在程序中定义一个变量时,这个变量是有作用范围的,变量的作用范围被称为它的作用域。根据定义变量的位置,变量分为两种。
(1)局部变量。在函数中定义的变量,包括参数,都被称为局部变量。
(2)全局变量。在函数外面、全局范围内定义的变量,被称为全局变量。
2.  每个函数在执行时,系统都会为该函数分配一块"临时内存空间",所有的局部变量都被保存在这块临时内存空间内。
当函数执行完成后,这块内存空间就被释放了,这些局部变量也就失效了, 因此离开函数之后就不能再访问局部变量了。
3.  全局变量意味着它们可以在所有函数内被访问。
4.  不管是在函数的局部范围内还是在全局范围内,都可能存在多个变量,每个变量"持有"该变量的值。
从这个角度来看,不管是局部范围还是全局范围,这些变量和它们的值就像一个"看不见"的字典,
其中变量名就是字典的key, 变量值就是字典的value。
5.  实际上, Python 提供了如下三个工具函数来获取指定范围内的"变量字典"。
(1)globals():  该函数返回全局范围内所有变量组成的"变量字典"。
(2)locals(): 该函数返回当前局部范围内所有变量组成的"变量字典"。
(3)vars(object):  获取在指定对象范围内所有变量组成的"变量字典"。如果不传入 object 参 数, vars()和 locals()的作用完全相同。
6.  globals()和 locals()看似完全不同,但它们实际上也是有联系的,关于这两个函数的区别和联系 大致有以下两点。
(1)locals() 总是获取当前局部范围内所有变量组成的"变量字典",因此,如果在全局范围内 (在函数之外)调用 locals()函数,
同样会获取全局范围内所有变量组成的"变量字典；而 globals()无论在哪里执行,总是获取全局范围内所有变量组成的"变量字典"。
(2)一 般 来 说 , 使 用locals()和 globals()获取的"变量字典"只应该被访问,不应该被修改。
但实际上,不管是使用globals()还是使用locals()获取的全局范围内的"变量字典",都可以 被修改,而这种修改会真正改变全局变量本身；
但通过locals()获取的局部范围内的"变量 字典",即使对它修改也不会影响局部变量。
7.  下面程序示范了如何使用locals()、globals()函数访问局部范围和全局范围内的"变量字典"。
8.  从下面程序可以清楚地看出,locals()函数用于访问特定范围内的所有变量组成的"变量字典",
而globalsO)函数则用于访问全局范围内的全局变量组成的"变量字典"。
9.  在使用 globals()或 locals()访问全局变量的"变量字典"时,将会看到程序输出的"变量字典"默认包含了很多变量,
这些都是Python 主程序内置的,读者暂时不用理会它们 。

"""


def test():
    age = 20
    # 直接访问age局部变量
    print(age)  # 输出20
    # 访问函数局部范围的"变量数组"
    print(locals())  # {'age': 20}
    # 通过函数局部范围的"变量数组"访问age变量
    print(locals()['age'])  # 20
    # 通过locals函数局部范围的"变量数组"改变age变量的值
    locals()['age'] = 12
    # 再次访问age变量的值
    print('xxx', age)  # 依然输出20
    # 通过globals函数修改x全局变量
    globals()['x'] = 19


x = 5
y = 20
print(globals())  # {..., 'x': 5, 'y': 20}
# 在全局访问内使用locals函数,访问的是全局变量的"变量数组"
print(locals())  # {..., 'x': 5, 'y': 20}
# 直接访问x全局变量
print(x)  # 5
# 通过全局变量的"变量数组"访问x全局变量
print(globals()['x'])  # 5
# 通过全局变量的"变量数组"对x全局变量赋值
globals()['x'] = 39
print(x)  # 输出39
# 在全局范围内使用locals函数对x全局变量赋值
locals()['x'] = 99
print(x)  # 输出99
