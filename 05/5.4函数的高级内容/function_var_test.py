"""
5.4 函数的高级内容

1.	Python 的函数是"一等公民",因此函数本身也是一个对象,函数既可用于赋值,也可用作其他函数的参数,还可作为其他函数的返回值。

5.4.1   使用函数变量

2.  Python 的函数也是一种值：所有函数都是function对象,这意味着可以把函数本身赋值给变量,
就像把整数、浮点数、列表、元组赋值给变量一样。
3.  当把函数赋值给变量之后,接下来程序也可通过该变量来调用函数。例如如下代码。
4.  从上面代码可以看出,程序依次将 pow()、area()函数赋值给 my_fun 变量,接下来即可通过 my_fun 变量分别调用pow()、area()函数。
5.  其实Python已经内置了计算乘方的方法,因此此处的pow()函数并没有太大的实际意义,只是作为示范使用。
6.  通过对 my_fun 变量赋值不同的函数,可以让 my_fun 在不同的时间指向不同的函数,从而让程序更加灵活。
由此可见,使用函数变量的好处是让程序更加灵活。
7.  除此之外,程序还可使用函数作为另一个函数的形参和(或)返回值。
"""


# 定义一个计算乘方的函数
def pow(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


# 将pow函数赋值给my_fun,则my_fun可当成pow使用
my_fun = pow
print(my_fun(3, 4))  # 输出81


# 定义一个计算面积的函数
def area(width, height):
    return width * height


# 将area函数赋值给my_fun,则my_fun可当成area使用
my_fun = area
print(my_fun(3, 4))  # 输出12
