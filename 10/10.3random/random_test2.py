"""
实际上,使用 random 模块中的随机函数可以做很多很有趣的事情。比如下面程序(备注：部分程序参考了 Python 官方文档)。
"""
import random
import collections

# 指定随机抽取6个元素,各元素被抽取的权重(概率)不同
print(random.choices(['Python', 'swift', 'Kotlin'], [5, 5, 1], k=6))
# 下面模拟从52张扑克牌中抽取20张
# 在被抽到的20张牌中,牌面为10(包括J、Q、K) 的牌占多大比例
# 生成一个16个tens (代表10)和36个low cards  (代表其他牌)的集合
deck = collections.Counter(tens=16, low_cards=36)
# 从52张牌中随机抽取20张
seen = random.sample(list(deck.elements()), k=20)
# 统  计tens 元素有多少个,再除以20
print(seen.count('tens') / 20)
"""
从上面的输出结果来看,在第一次抽取的 6 个元素中 Kotlin 完全没有被抽取到,这是因为它的被抽取比例太低了。
"""