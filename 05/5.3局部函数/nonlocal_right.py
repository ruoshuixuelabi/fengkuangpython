"""
为了声明 bar()函数中的"name= '孙悟空'"赋值语句不是定义新的局部变量,
只是访问它所在 foo() 函数内的 name 局部变量, Python提供了nonlocal关键字,
通过 nonlocal 语句即可声明访问赋值语句只是访问该函数所在函数内的局部变量。将上面程序改为如下形式。

nonlocal和前面介绍的 global功能大致相似,区别只是global用于声明访问全局变量,
而 nonlocal 用于声明访问当前函数所在函数内的局部变量。
"""


def foo():
    # 局部变量name
    name = 'Charlie'

    def bar():
        nonlocal name
        # 访问bar函数所在的foo函数的name局部变量
        print(name)  # Charlie
        name = '孙悟空'

    bar()


foo()
