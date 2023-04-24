"""
1.  有时候需要定义一个函数,该函数的大部分计算逻辑都能确定,但某些处理逻辑暂时无法确定------
这意味着某些程序代码需要动态改变,如果希望调用函数时能动态传入这些代码,
那么就需要在函数中定义函数形参,这样即可在调用该函数时传入不同的函数作为参数,从而动态改变这段代码。
2.  Python支持像使用其他参数一样使用函数参数,例如如下程序。
3.  上面程序中定义了一个map()函数,该函数的第二个参数是一个函数类型的参数,
这意味着每次调用函数时可以动态传入一个函数,随着实际传入函数的改变,就可以动态改变map()函数中的部分计算代码。
4.  Python 3本身也提供了一个map()函数,Python3 内置的map()函数的功能和此处定义的map()函数功能类似,但更加强大。
本章5.5节也会示范Python 3内置的map()函 数的用法。
5.  从上面介绍不难看出，通过使用函数作为参数可以在调用函数时动态传入函数------实际上就可以动态改变被调用函数的部分代码。
"""


# 定义函数类型的形参,其中fn是一个函数
def map(data, fn):
    result = []
    # 遍历data列表中每个元素,并用fn函数对每个元素进行计算
    # 然后将计算结果作为新数组的元素
    for e in data:
        result.append(fn(e))
    return result


# 定义一个计算平方的函数
def square(n):
    return n * n


# 定义一个计算立方的函数
def cube(n):
    return n * n * n


# 定义一个计算阶乘的函数
def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


data = [3, 4, 9, 5, 8]
print("原数据: ", data)
# 下面程序代码3次调用map()函数,每次调用时传入不同的函数
print("计算数组元素的平方")
print(map(data, square))
print("计算数组元素的立方")
print(map(data, cube))
print("计算数组元素的阶乘")
print(map(data, factorial))
# 获取map的类型
print(type(map))
