"""
5.5 局部函数与lambda 表达式

1.  lambda 表达式是现代编程语言争相引入的一种语法,如果说函数是命名的、方便复用的代码块,
那么lambda 表达式则是功能更灵活的代码块,它可以在程序中被传递和调用。
2.  如果使用lambda 表达式来简化function return test.py, 则可以将程序改写成如下形式。
3.  在上面三行粗体字代码中,return后面的部分使用lambda 关键字定义的就是lambda 表达式,
Python要求lambda 表达式只能是单行表达式。
4.  由于lambda 表达式只能是单行表达式,不允许使用更复杂的函数形式,因此上面③号粗体字代码处改为计算1+2+3+ …+n 的总和。
5.  lambda 表达式的语法格式如下：
    lambda [parameter list] : 表达式
6.  从上面的语法格式可以看出lambda 表达式的几个要点。
(1)lambda表达式必须使用lambda关键字定义。
(2)在lambda关键字之后、冒号左边的是参数列表,可以没有参数,也可以有多个参数。
如果有多个参数,则需要用逗号隔开,冒号右边是该lambda 表达式的返回值。
7.  实际上,lambda 表达式的本质就是匿名的、单行函数体的函数。因此,lambda 表达式可以写成函数的形式。
例如,对于如下lambda 表达式。
lambda  x,y:x+ y
可改写为如下函数形式。
def  add(x,y):return x+y
8.  上面定义函数时使用了简化语法：当函数体只有一行代码时,可以直接把函数体的代码放在与函数头同一行。
9.  总体来说,函数比lambda 表达式的适应性更强, lambda 表达式只能创建简单的函数对象(它只适合函数体为单行的情形)。
但lambda 表达式依然有如下两个用途。
(1)对于单行函数,使用lambda 表达式可以省去定义函数的过程,让代码更加简洁。
(2)对于不需要多次复用的函数,使用lambda 表达式可以在用完之后立即释放,提高了性能。
"""


def get_math_func(type):
    result = 1
    # 该函数返回的是Lambda表达式
    if type == 'square':
        return lambda n: n * n  # ①
    elif type == 'cube':
        return lambda n: n * n * n  # ②
    else:
        return lambda n: (1 + n) * n / 2  # ③


# 调用get_math_func(),程序返回一个嵌套函数
math_func = get_math_func("cube")
print(math_func(5))  # 输出125
math_func = get_math_func("square")
print(math_func(5))  # 输出25
math_func = get_math_func("other")
print(math_func(5))  # 输出15.0

a = lambda x, y: x + y


def add(x, y): return x + y
