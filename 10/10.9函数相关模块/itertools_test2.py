"""
在 itertools 模块中还有一些常用的迭代器函数,如下所示。
(1)accumulate(p[,func]): 默认生成根据序列 p 元素累加的迭代器, p0,p0+p1,p0+p1+p2,…序列,
如果指定了 func 函数,则用 func 函数来计算下一个元素的值。
(2)chain(p,q,…): 将多个序列里的元素"链"在一起生成新的序列。
(3)compress(data,selectors):根据selectors序列的值对data序列的元素进行过滤。
如果selector[0] 为真,则保留data[0]: 如 果selector[1]为真,则保留data[1]…… 依此类推。
(4)dropwhile(pred,seq):使用 pred 函数对 seq 序列进行过滤,从 seq 中第一个使用 pred 函数计算为False的元素开始,
保留从该元素到序列结束的全部元素。
(5)takewhile(pred,seq): 该函数和上一个函数恰好相反。使用pred 函数对seq 序列进行过滤,
从 seq 中第 一 个使用pred 函数计算为False的元素开始,去掉从该元素到序列结束的全部元素。
(6)filterfalse(pred,seq):使用pred函数对seq 序列进行过滤,保留seq 中使用 pred 计算为 True 的元素。
比如filterfalse(lambda x:x%2,range(10)), 得到0,2,4,6,8。
(7)islice(seq,[start,] stop [,step]): 其功能类似于序列的 slice 方法,实际上就是返回 seq[start:stop:step]的结果。
(8)starmap(func,seq):  使用 func 对 seq 序列的每个元素进行计算,将计算结果作为新的序列元素。
当使用func 计算序列元素时,支持序列解包。
比如seq 序列的元素长度为3,那么 func 可以是一个接收三个参数的函数,该函数将会根据这三个参数来计算新序列的元素。
(9)zip_longest(p,q,…): 将 p、q 等序列中的元素按索引合并成元组,这些元组将作为新序列的元素。
上面这些函数的测试程序如下。
"""
import itertools as it

# 默认使用累加的方式计算下一个元素的值
for e in it.accumulate(range(6)):
    print(e, end=', ')  # 0, 1, 3, 6, 10, 15
print('\n---------')
# 使用x*y的方式来计算迭代器下一个元素的值
for e in it.accumulate(range(1, 6), lambda x, y: x * y):
    print(e, end=', ')  # 1, 2, 6, 24, 120
print('\n---------')
# 将两个序列“链”在一起,生成新的迭代器
for e in it.chain(['a', 'b'], ['Kotlin', 'Swift']):
    print(e, end=', ')  # 'a', 'b', 'Kotlin', 'Swift'
print('\n---------')
# 根据第二个序列来筛选第一个序列的元素,
# 由于第二个序列只有中间两个元素为1（True）,因此前一个序列只保留中间两个元素
for e in it.compress(['a', 'b', 'Kotlin', 'Swift'], [0, 1, 1, 0]):
    print(e, end=', ')  # 只有: 'b', 'Kotlin'
print('\n---------')
# 获取序列中从长度不小于4的元素开始、到结束的所有元素
for e in it.dropwhile(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')  # 只有: 'Kotlin', 'x', 'y'
print('\n---------')
# 去掉序列中从长度不小于4的元素开始、到结束的所有元素
for e in it.takewhile(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')  # 只有: 'a', 'b'
print('\n---------')
# 只保留序列中从长度不小于4的元素
for e in it.filterfalse(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')  # 只有: 'Kotlin'
print('\n---------')
# 使用pow函数对原序列的元素进行计算,将计算结果作为新序列的元素
for e in it.starmap(pow, [(2, 5), (3, 2), (10, 3)]):
    print(e, end=', ')  # 32, 9, 1000
print('\n---------')
# 将'ABCD'、'xy'的元素按索引合并成元组,这些元组作为新序列的元素
# 长度不够的序列元素使用'-'字符代替
for e in it.zip_longest('ABCD', 'xy', fillvalue='-'):
    print(e, end=', ')  # ('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')
