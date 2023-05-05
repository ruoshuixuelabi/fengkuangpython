"""
但 Python 的异常处理使用 else 块绝不是多余的语法,当 try 块没有异常,而 else 块有异常时,就能体现出 else 块的作用了。例如如下程序。
"""


def else_test():
    s = input('请输入除数:')
    result = 20 / int(s)
    print('20除以%s的结果是: %g' % (s, result))


def right_main():
    try:
        print('try块的代码,没有异常')
    except:
        print('程序出现异常')
    else:
        # 将else_test放在else块中
        else_test()


def wrong_main():
    try:
        print('try块的代码,没有异常')
        # 将else_test放在try块代码的后面
        else_test()
    except:
        print('程序出现异常')


wrong_main()
right_main()
"""
上面程序中定义了一个 else_test()函数,该函数在运行时需要接收用户输入的参数,随着用户输入数据的不同可能导致异常。
接下来程序定义了 right_main()和 wrong_main()两个函数,其中 right_main()将else_test()函数放在else块内;
而 wrong_main()将 else_test()函数放在try块的代码的后面。

正如上面所介绍的,当 try块和 else 块都没有异常时,将 else_test()函数放在try块的代码的后面和放在 else 块中没有任何区别。
例如,如果用户输入的数据没有导致程序出现异常,则将看到程序产生如下输出结果。

try块的代码,没有异常
请输入除数:4
20除以4的结果是: 5
try块的代码,没有异常
请输入除数:4
20除以4的结果是: 5

但如果用户输入的数据让 else_test() 函数出现异常(try 块依然没有任何异常),此时程序就会产生如下输出结果。

try块的代码,没有异常
请输入除数:0
程序出现异常
try块的代码,没有异常
请输入除数:0
Traceback (most recent call last):
 result = 20 / int(s)
ZeroDivisionError: division by zero

对比上面两个输出结果,用户输入的都是0,这样都会导致 else_test()函数出现异常。如果将 else_test()函数放在try块的代码的后面,
此时 else_test()函数运行产生的异常将会被 try 块对应的 except 捕获,这正是 Python 异常处理机制的执行流程;
但如果将 else_test()函数放在else块中,当 else_test()函数出现异常时,
程序没有 except 块来处理该异常,该异常将会传播给 Python 解释器,导致程序中止。

对比上面两个输出结果,不难发现,放在else块中的代码所引发的异常不会被except块捕获。
所以,如果希望某段代码的异常能被后面的except块捕获,那么就应该将这段代码放在try块的代码之后;
如果希望某段代码的异常能向外传播(不被except块捕获),那么就应该将这段代码放在 else 块中。
"""
