"""
事实上,Counter 继承了 dict 类,因此它完全可以调用 dict 所支持的方法。此外, Counter 还提供了如下三个常用的方法。
(1)elements()：该方法返回该 Counter 所包含的全部元素组成的迭代器。
(2)most_common([n])：该方法返回 Counter 中出现最多的 n 个元素。
(3)subtract([iterable-or-mapping])：该方法计算 Counter 的减法,其实就是计算减去之后各元素出现的次数。

下面程序示范了Counter 类中这些方法的用法示例。
"""
from collections import Counter

# 创建Counter对象
cnt = Counter()
# 访问并不存在的key,将输出该key的次数为0.
print(cnt['Python'])  # 0
for word in ['Swift', 'Python', 'Kotlin', 'Kotlin', 'Swift', 'Go']:
    cnt[word] += 1
print(cnt)
# 只访问Counter对象的元素
print(list(cnt.elements()))
# 将字符串（迭代器）转换成Counter
chr_cnt = Counter('abracadabra')
# 获取出现最多的3个字母
print(chr_cnt.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
# 用Counter对象执行减法,其实就是减少各元素的出现次数
c.subtract(d)
print(c)  # Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
e = Counter({'x': 2, 'y': 3, 'z': -4})
# 调用del删除key-value对,会真正删除该key-value对
del e['y']
print(e)
# 访问'w'对应的value,'w'没有出现过,因此返回0
print(e['w'])  # 0
# 删除e['w'],删除该key-value对
del e['w']
# 再次访问'w'对应的value,'w'还是没有,因此返回0
print(e['w'])  # 0
"""
上面程序中第一行粗体字代码调用了 Counter 对象的 elements()方法,该方法返回容器中所有元素组成的迭代器,
Counter 记录了几个元素的出现次数,该方法就会返回几个对应的元素。

程序中第二行粗体字代码调用了 Counter 对象的 most_common(3) 方法,该方法会返回容器中出现次数最多的三个元素。

程序中第三行粗体字代码调用了 Counter 对象的 subtract()方法执行减法,实质上就是对元素出现的次数执行减法。
"""