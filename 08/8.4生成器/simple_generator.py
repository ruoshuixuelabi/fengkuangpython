"""
生成器和迭代器的功能非常相似,它也会提供 __next__()方法,这意味着程序同样可调用内置的 next()函数来获取生成器的下一个值,
也可使用for循环来遍历生成器。

生成器与迭代器的区别在于：迭代器通常是先定义一个迭代器类,然后通过创建实例来创建迭代器;
而生成器则是先定义一个包含 yield 语句的函数,然后通过调用该函数来创建生成器。

生成器是一种非常优秀的语法,Python 使用生成器可以让程序变得很优雅。

8.4.1 创建生成器

创建生成器需要两步操作。
① 定义一个包含 yield 语句的函数。
② 调用第①步创建的函数得到生成器。

下面程序使用生成器来定义一个差值递增的数列。程序先定义了一个包含yield语句的函数。
"""


def test(val, step):
    print("--------函数开始执行------")
    cur = 0
    # 遍历0～val
    for i in range(val):
        # cur添加i*step
        cur += i * step
        yield cur


"""
上面函数与前面介绍的普通函数的最大区别在于yield cur这行,如果将这行代码改为print(cur),那么这个函数就显得比较普通了——
该函数只是简单地遍历区间,并将循环计数器乘以step后添加到cur变量上,该数列中两个值之间的差值会逐步递增。

如果将上面的 yield cur 语句改为 print(cur,end=''),执行test(10,2)函数将会看到如下输出结果。
0   2   6   12  20  30  42  56  72  90

yield cur 语句的作用有两点。
(1)每次返回一个值,有点类似于return语句。
(2)冻结执行,程序每次执行到yield语句时就会被暂停。

在程序被 yield 语句冻结之后,当程序再次调用next()函数获取生成器的下一个值时,程序才会继续向下执行。

需要指出的是,调用包含 yield 语句的函数并不会立即执行,它只是返回一个生成器。
只有当程序通过next()函数调用生成器或遍历生成器时,函数才会真正执行。

保留上面函数中的yield cur语句,执行如下语句。
"""

# print(cur, end=' ')
# 执行函数,返回生成器
t = test(10, 2)
print('=================')
# 获取生成器的第一个值
print(next(t))  # 0,生成器"冻结"在yield处
print(next(t))  # 2,生成器再次"冻结"在yield处
"""
运行上面代码,可以看到如下输出结果。

=================
--------函数开始执行------
0
2

从上面的输出结果不难看出,当程序执行t=test(10,2)调用函数时,程序并未开始执行test()函数;
当程序第一次调用next(t)时,test()函数才开始执行。

注意：Python 2.x 不使用next()函数来获取生成器的下一个值,而是直接调用生成器的next()方法。也就是说,在Python 2.x中应该写成t.next()。

当程序调用next(t)时,生成器会返回 yield cur 语句返回的值(第一次返回0),程序被"冻结"在yield语句处,
因此可以看到上面生成器第一次输出的值为0。

当程序第二次调用next(t)时,程序的"冻结"被解除,继续向下执行,这一次循环计数器i变成1,在执行cur+=i*step之后,
cur变成2,生成器再次返回yield cur语句返回的值(这一次返回2),程序再次被"冻结"在该yield语句处,
因此可以看到上面生成器第二次输出的值为2。

程序可使用for循环来遍历生成器,相当于不断地使用next()函数获取生成器的下一个值。例如如下代码。
"""
for ele in t:
    print(ele, end=' ')
"""
运行上面循环代码,会生成如下输出结果。
6 12 20 30 42 56 72 90

由于前面两次调用next()函数已经获取了生成器的前两个值,因此此处循环时第一次输出的值就是6。

此外,程序可使用 list()函数将生成器能生成的所有值转换成列表,也可使用 tuple() 函数将生成器能生成的所有值转换成元组。例如如下代码。
"""
# 再次创建生成器
t = test(10, 1)
# 将生成器转换成列表
print(list(t))
# 再次创建生成器
t = test(10, 3)
# 将生成器转换成列表
print(tuple(t))
"""
运行上面代码,可以看到如下输出结果。

-------函数开始执行------
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
--------函数开始执行------
(0, 3, 9, 18, 30, 45, 63, 84, 108, 135)

如果读者还记得4.4.8节的内容,应该知道前面还介绍过使用for循环来创建生成器(将for表达式放在圆括号里)。
可见,Python 主要提供了以下两种方式来创建生成器。
(1)使用for循环的生成器推导式。
(2)调用带yield语句的生成器函数。

生成器是 Python 的一个特色功能,在其他语言中往往没有对应的机制,因此很多 Python 开发者对生成器机制不甚了解。
但实际上生成器是一种非常优秀的机制,以我们实际开发的经验来看,使用生成器至少有以下几个优势。
(1)当使用生成器来生成多个数据时,程序是按需获取数据的,它不会一开始就把所有数据都生成出来,而是每次调用 next()获取下一个数据时,
生成器才会执行一次,因此可以减少代码的执行次数。比如前面介绍的示例,
程序不会一开始就把生成器函数中的循环都执行完成,而是每次调用next()时才执行一次循环体。
(2)当函数需要返回多个数据时,如果不使用生成器,程序就需要使用列表或元组来收集函数返回的多个值,当函数要返回的数据量较大时,
这些列表、元组会带来一定的内存开销;如果使用生成器就不存在这个问题,生成器可以按需、逐个返回数据。
(3)使用生成器的代码更加简洁。
"""
