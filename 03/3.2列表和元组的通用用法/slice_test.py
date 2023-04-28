"""
3.2.2  子序列

与前面介绍的字符串操作类似的是,列表和元组同样也可使用索引获取中间一段,这种用法被称为slice(分片或切片)。
slice 的完整语法格式如下：
[start: end: step]

上面语法中start、end两个索引值都可使用正数或负数,其中负数表示从倒数开始。该语法表示从start索引的元素开始(包含),
到end索引的元素结束(不包含)的所有元素------这和所有编程语言的约定类似。

step表示步长,因此step使用负数没有意义。

下面代码示范了使用start、end获取元组中间一段的用法。
"""
a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
# 访问从第2个到倒数第4个(不包含)所有元素
print(a_tuple[1: 3])  # (20, 5.6)
# 访问从倒数第3个到倒数第1个(不包含)所有元素
print(a_tuple[-3: -1])  # (5.6, 'fkit')
# 访问从第2个到倒数第2个(不包含)所有元素
print(a_tuple[1: -2])  # (20, 5.6)
# 访问从倒数第3个到第5个(不包含)所有元素
print(a_tuple[-3: 4])  # (5.6, 'fkit')
# 如果指定step参数,则可间隔step个元素再取元素
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 访问从第3个到第9个(不包含)、间隔为2的所有元素
print(b_tuple[2: 8: 2])  # (3, 5, 7)
# 访问从第3个到第9个(不包含)、间隔为3的所有元素
print(b_tuple[2: 8: 3])  # (3, 6)
# 访问从第3个到倒数第2个(不包含)、间隔为3的所有元素
print(b_tuple[2: -2: 2])  # (3, 5, 7)
