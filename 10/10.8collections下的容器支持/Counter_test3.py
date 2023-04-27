"""
此外,对于 Counter 对象还有一些很常用的操作,比如把 Counter 对象转换成set(集合)、list(列表)、dict (字典)等,
程序还可对Counter执行加、减、交、并运算,对 Counter 进行求正、求 负运算等。对Counter 执行各种运算的含义如下。
(1)加：将两个Counter 对象中各key出现的次数相加,且只保留出现次数为正的元素。
(2)减：将两个Counter对象中各key 出现的次数相减,且只保留出现次数为正的元素。
(3)交：取两个Counter 对象中都出现的key 且 各key 对应的次数的最小数。
(4)并：取两个Counter对象中各key 对应的出现次数的最大数。
(5)求正：只保留 Counter 对象中出现次数为0或正数的key-value对 。
(6)求负：只保留 Counter 对象中出现次数为负数的key-value对,并将出现次数改为正数。
下面程序示范了对Counter对象进行的这些常用操作。
"""
from collections import Counter

# 创建Counter对象
c = Counter(Python=4, Swift=2, Kotlin=3, Go=-2)
# 统计Counter中所有出现次数的总和
print(sum(c.values()))  # 7
# 将Counter转换为list,只保留各key
print(list(c))  # ['Python', 'Swift', 'Kotlin', 'Go']
# 将Counter转换为set,只保留各key
print(set(c))  # {'Go', 'Python', 'Swift', 'Kotlin'}
# 将Counter转换为dict
print(dict(c))  # {'Python': 4, 'Swift': 2, 'Kotlin': 3, 'Go': -2}
# 将Counter转换为list,列表元素都是(元素, 出现次数)组
list_of_pairs = c.items()
print(list_of_pairs)  # dict_items([('Python', 4), ('Swift', 2), ('Kotlin', 3), ('Go', -2)])
# 将列表元素为(元素, 出现次数)组的list转换成Counter
c2 = Counter(dict(list_of_pairs))
print(c2)  # Counter({'Python': 4, 'Kotlin': 3, 'Swift': 2, 'Go': -2})
# 获取Counter中最少出现的3个元素
print(c.most_common()[:-4:-1])  # [('Go', -2), ('Swift', 2), ('Kotlin', 3)]
# 清空所有key-value对
c.clear()
print(c)  # Counter()
c = Counter(a=3, b=1, c=-1)
d = Counter(a=1, b=-2, d=3)
# 对Counter执行加法
print(c + d)  # Counter({'a': 4, 'd': 3})
# 对Counter执行减法
print(c - d)  # Counter({'b': 3, 'a': 2})
Counter({'a': 2})
# 对Counter执行交运算
print(c & d)  # Counter({'a': 1})
print(c | d)  # Counter({'a': 3, 'd': 3, 'b': 1})
print(+c)  # Counter({'a': 3, 'b': 1})
print(-d)  # Counter({'b': 2})
