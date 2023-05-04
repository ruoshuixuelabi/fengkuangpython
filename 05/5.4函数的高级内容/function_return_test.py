"""
5.4.3 使用函数作为返回值

前面已经提到,Python 还支持使用函数作为其他函数的返回值。例如如下程序。
"""


def get_math_func(type):
    # 定义一个计算平方的局部函数
    def square(n):  # ①
        return n * n

    # 定义一个计算立方的局部函数
    def cube(n):  # ②
        return n * n * n

    # 定义一个计算阶乘的局部函数
    def factorial(n):  # ③
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    # 返回局部函数
    if type == "square":
        return square
    if type == "cube":
        return cube
    else:
        return factorial


# 调用get_math_func(),程序返回一个嵌套函数
math_func = get_math_func("cube")  # 得到cube函数
print(math_func(5))  # 输出125
math_func = get_math_func("square")  # 得到square函数
print(math_func(5))  # 输出25
math_func = get_math_func("other")  # 得到factorial函数
print(math_func(5))  # 输出120
"""
上面程序中的粗体字代码定义了一个 get_math_func()函数,该函数将返回另一个函数。
接下来在 get_math_func() 函数体内的 ① 、 ② 、 ③ 号粗体字代码分别定义了三个局部函数 ,
最后 get_math_func()函数会根据所传入的参数,使用这三个局部函数之一作为返回值。

在定义了会返回函数的 get_math_func()函数之后,接下来程序调用 get_math_func()函数时即可
返回所需的函数,如上面程序中最后三行粗体字代码所示。
"""