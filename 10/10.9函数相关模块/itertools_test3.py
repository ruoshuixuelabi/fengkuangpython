"""
在 itertools模块中还有 一 些用于生成排列组合的工具函数。

(1)product(p,q.… [repeat=1])：用序列 p、q、…中的元素进行排列组合,就相当于使用嵌套循环组合。
(2)permutations(p[,r])：从序列 p 中取出 r 个元素组成全排列,将排列得到的元组作为新迭代器的元素。
(3)combinations(p,r)：从序列 p 中取出 r 个元素组成全组合,元素不允许重复,将组合得到的元组作为新迭代器的元素。
(4)combinations_with_replacement(p,r)：从序列 p 中取出 r 个元素组成全组合,元素允许重复,将组合得到的元组作为新迭代器的元素。

如下程序示范了上面4个函数的用法。
"""
import itertools as it

# 使用两个序列进行排列组合
for e in it.product('AB', 'CD'):
    print(''.join(e), end=', ')  # AC, AD, BC, BD,
print('\n---------')
# 使用一个序列、重复2次进行全排列
for e in it.product('AB', repeat=2):
    print(''.join(e), end=', ')  # AA, AB, BA, BB,
print('\n---------')
# 从序列中取2个元素进行排列
for e in it.permutations('ABCD', 2):
    print(''.join(e), end=', ')  # AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC,
print('\n---------')
# 从序列中取2个元素进行组合、元素不允许重复
for e in it.combinations('ABCD', 2):
    print(''.join(e), end=', ')  # AB, AC, AD, BC, BD, CD,
print('\n---------')
# 从序列中取2个元素进行组合、元素允许重复
for e in it.combinations_with_replacement('ABCD', 2):
    print(''.join(e), end=', ')  # AA, AB, AC, AD, BB, BC, BD, CC, CD, DD,
