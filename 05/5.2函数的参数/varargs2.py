"""
Python 允许个数可变的形参可以处于形参列表的任意位置(不要求是形参列表的最后一个参数),
但 Python 要求一个函数最多只能带一个支持"普通"参数收集的形参。例如如下程序。

正如从下面程序中所看到的,test()函数的第一个参数就是个数可变的形参,由于该参数可接收个数不等的参数值,
因此如果需要给后面的参数传入参数值,则必须使用关键字参数;否则,程序会把所传入的多个值都当成是传给books参数的
"""


# 定义了支持参数收集的函数
def test(*books, num):
    print(books)
    # books被当成元组处理
    for b in books:
        print(b)
    print(num)


# 调用test()函数
test("疯狂iOS讲义", "疯狂Android讲义", num=20)

my_list = ["疯狂Swift讲义", "疯狂Python讲义"]
# 将列表的多个元素传给支持参数收集的参数
test(my_list, num=20)
my_tuple = ("疯狂Swift讲义", "疯狂Python讲义")
# 将元组的多个元素传给支持参数收集的参数
test(*my_tuple, num=20)
