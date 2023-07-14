"""
6.2.4 再论类命名空间

再次重申：Python 的类就像命名空间。Python 程序默认处于全局命名空间内,类体则处于类命名空间内,
Python 允许在全局范围内放置可执行代码——当 Python 执行该程序时,这些代码就会获得执行的机会;
类似地,Python 同样允许在类范围内放置可执行代码——当 Python 执行该类定义时,这些代码同样会获得执行的机会。

例如,如下程序测试了类命名空间。
"""


class Item:
    # 直接在类空间中放置执行性质代码
    print('正在定义Item类')
    for i in range(10):
        if i % 2 == 0:
            print('偶数:', i)
        else:
            print('奇数:', i)


"""
正如从上面代码所看到的,程序直接在 Item 类体中放置普通的输出语句、循环语句、分支语句,这都是合法的。
当程序执行 Item 类时,Item 类命名空间中的这些代码都会被执行。

从执行效果来看,这些可执行代码被放在 Python 类命名空间与全局空间并没有太大的区别——
确实如此,这是因为程序并没有定义"成员"(变量或函数),这些代码执行之后就完了,不会留下什么。
"""
