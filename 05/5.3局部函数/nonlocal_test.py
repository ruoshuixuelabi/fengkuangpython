"""
局部函数内的变量也会遮蔽它所在函数内的局部变量(这句话有点拗口),请看如下代码。

运行上面代码,会导致如下错误。 UnboundLocalError: local variable 'name' referenced before assignment

该错误是由局部变量遮蔽局部变量导致的,在bar()函数中定义的name局部变量遮蔽了它所在foo()函数内的name局部变量,
因此导致程序中粗体字代码报错。
"""


def foo():
    # 局部变量name
    name = 'Charlie'

    def bar():
        # 访问bar函数所在的foo函数的name局部变量
        print(name)  # Charlie
        name = '孙悟空'

    bar()


foo()
