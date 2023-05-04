"""
5.2.3 参数收集(个数可变的参数)

很多编程语言都允许定义个数可变的参数,这样可以在调用函数时传入任意多个参数。
Python 当然也不例外,Python 允许在形参前面添加一个星号(*),这样就意味着该参数可接收多个参数值,多个参数值被当成元组传入。
下面程序定义了一个形参个数可变的函数。

从下面的运行结果可以看出,当调用 test() 函数时 ,books 参数可以传入多个字符串作为参数值。
从 test()的函数体代码来看,参数收集的本质就是一个元组：Python会将传给books参数的多个值收集成一个元组。
"""


# 定义了支持参数收集的函数
def test(a, *books):
    print(books)
    # books被当成元组处理
    for b in books:
        print(b)
    # 输出整数变量a的值
    print(a)


# 调用test()函数
test(5, "疯狂iOS讲义", "疯狂Android讲义")
