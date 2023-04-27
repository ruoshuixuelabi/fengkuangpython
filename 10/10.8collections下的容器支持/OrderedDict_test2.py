"""
1.  此外,由于 OrderedDict 是有序的,因此 Python 为之提供了如下两个方法。
(1)popitem(last=True):默认弹出并返回最右边(最后加入)的key-value对;如果将 last 参数设为False,
则弹出并返回最左边(最先加入)的key-value对。
(2)move_to_end(key,last=True):默认将指定的key-value对移动到最右边(最后加入);如果将 last改 为False,
则将指定的key-value对移动到最左边(最先加入)。

2.  下面程序示范了OrderedDict的两个方法的用法。
"""
from collections import OrderedDict

d = OrderedDict.fromkeys('abcde')
# 将b对应的key-value对移动到最右边（最后加入）
d.move_to_end('b')
print(d.keys())  # odict_keys(['a', 'c', 'd', 'e', 'b'])
# 将b对应的key-value对移动到最左边（最先加入）
d.move_to_end('b', last=False)
print(d.keys())  # odict_keys(['b', 'a', 'c', 'd', 'e'])
# 弹出并返回最右边（最后加入）的key-value对
print(d.popitem()[0])  # e
# 弹出并返回最左边（最先加入）的key-value对
print(d.popitem(last=False)[0])  # b
"""
通过上面的输出结果可以看出,使用 OrderedDict 的 move_to_end()方法可以方便地将指定的 key-value 对移动到 OrderedDict 的任意一端;
而 popitem()方法则可用于弹出并返回 OrderedDict 任意一端的key-value对。
"""
