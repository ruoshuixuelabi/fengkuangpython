"""
10.8.2	Counter对象

collections 包下的 Counter 也是一个很有用的工具类,它可以自动统计容器中各元素出现的次数。

Counter 的本质就是一个特殊的 dict,只不过它的 key 都是其所包含的元素,而它的 value 则记录了该 key 出现的次数。
因此,如果通过 Counter 并不存在的 key 访问 value,将会输出0------代表该 key 出现了0次。

程序可通过任何可迭代对象参数来创建 Counter 对象,此时 Counter将会自动统计各元素出现的次数,并以元素为key,
出现的次数为value来构建 Counter 对象;程序也能以dict为参数来构建 Counter对象;还能通过关键字参数来构建Counter对象。例如如下程序。
"""
from collections import Counter

# 创建空的Counter对象
c1 = Counter()
# 以可迭代对象创建Counter对象
c2 = Counter('hannah')
print(c2)
# 以可迭代对象创建Counter对象
c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'])
print(c3)
# 以dict来创建Counter对象
c4 = Counter({'red': 4, 'blue': 2})
print(c4)
# 使用关键字参数的语法创建Counter
c5 = Counter(Python=4, Swift=8)
print(c5)
