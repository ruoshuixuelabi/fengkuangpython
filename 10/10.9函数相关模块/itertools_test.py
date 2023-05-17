"""
10.9	函数相关模块

Python 完全支持函数式编程,它还提供了一些与函数相关的模块。

10.9.1	itertools模块的功能函数

在 itertools 模块中主要包含了一些用于生成迭代器的函数。在 Python 的交互式解释器中先导入 itertools 模块,
然后输入[e for e in dir(itertools) if not e.startswith('_')]命令,即可看到该模块所包含的全部属性和函数。
import itertools
[e for e in dir(itertools) if not e.startswith('_')]
['accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile',
'filterfalse', 'groupby', 'islice', 'pairwise', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']

从上面的输出结果可以看出,itertools 模块中的不少函数都可以用于生成迭代器。先看 itertools 模块中三个生成无限迭代器的函数。
(1)count(start,[step])：生成start,start+step,start+2 * step,…的迭代器,其中step默认为1。
比如使用count(10)生成的迭代器包含：10,11,12,13,14,…。
(2)cycle(p)：对序列 p 生成无限循环p0,p1,…,p0,p1,…  的迭代器。比如使用cycle('ABCD')生成的迭代器包含：A,B,C,D,A,B,C,D,…
(3)repeat(elem [,n]): 生成无限个 elem 元素重复的迭代器,如果指定了参数n, 则只生成n 个elem 元素。
比如使用repeat(10,3)生成的迭代器包含：10,10,10。

4.  下面程序示范了使用上面三个函数来生成迭代器。
"""
import itertools as it

# count(10, 3)生成10、13、16……迭代器
for e in it.count(10, 3):
    print(e)
    # 用于跳出无限循环
    if e > 20:
        break
print('---------')
my_counter = 0
# cycle用于对序列生成无限循环的迭代器
for e in it.cycle(['Python', 'Kotlin', 'Swift']):
    print(e)
    # 用于跳出无限循环
    my_counter += 1
    if my_counter > 7:
        break
print('---------')
# repeat用于生成n个元素重复的迭代器
for e in it.repeat('Python', 3):
    print(e)
