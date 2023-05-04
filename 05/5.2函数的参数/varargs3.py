"""
Python 还可以收集关键字参数,此时 Python 会将这种关键字参数收集成字典。
为了让 Python 能收集关键字参数,需要在参数前面添加两个星号。
在这种情况下,一个函数可同时包含一个支持"普通"参数收集的参数和一个支持关键字参数收集的参数。例如如下代码。

上面程序在调用test()函数时,前面的1、2、3将会传给普通参数x、 y、z; 接下来的两个字符串将会由 books 参数收集成元组;
最后的两个关键字参数将会被收集成字典。运行上面代码,会看到如下输出结果。
"""


# 定义了支持参数收集的函数
def test(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)


test(1, 2, 3, "疯狂iOS讲义", "疯狂Android讲义", 语文=89, 数学=94)
test(1, 2, "疯狂iOS讲义", "疯狂Android讲义", 语文=89, 数学=94)
# 如果希望让z 参数的默认值发挥作用,则需要只传入两个位置参数。例如如下调用代码。
test(1, 2, 语文=89, 数学=94)
