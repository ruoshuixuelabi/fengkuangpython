"""
3.2.7 序列封包和序列解包

Python 还提供了序列封包(Sequence Packing)和序列解包(Sequence Unpacking)的功能。简单来说,Python 允许支持以下两种赋值方式。
(1)程序把多个值赋给一个变量时,Python 会自动将多个值封装成元组。这种功能被称为序列封包。
(2)程序允许将序列(元组或列表等)直接赋值给多个变量,此时序列的各元素会被依次赋值给每个变量(要求序列的元素个数和变量个数相等)。
这种功能被称为序列解包。

下面代码示范了序列封包和序列解包的功能。
"""
# 序列封包：将10、20、30封装成元组后赋值给vals
vals = 10, 20, 30
print(vals)  # (10, 20, 30)
print(type(vals))  # <class 'tuple'>
print(vals[1])  # 20
a_tuple = tuple(range(1, 10, 2))
# 序列解包: 将a_tuple元组的各元素依次赋值给a、b、c、d、e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e)  # 1 3 5 7 9
a_list = ['fkit', 'crazyit']
# 序列解包: 将a_list序列的各元素依次赋值给a_str、b_str变量
a_str, b_str = a_list
print(a_str, b_str)  # fkit crazyit
# 如果在赋值中同时运用了序列封包和序列解包机制,就可以让赋值运算符支持同时将多个值赋给多个变量
# 将10、20、30依次赋值给x、y、z
x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30
# 使用这种语法也可以实现交换变量的值,例如如下代码。
# 将y,z, x依次赋值给x、y、z
x, y, z = y, z, x
print(x, y, z)  # 20 30 10
# 在序列解包时也可以只解出部分变量,剩下的依然使用列表变量保存。
# 为了使用这种解包方式,Python 允许在左边被赋值的变量之前添加"*",那么该变量就代表一个列表,可以保存多个集合元素
# first、second保存前2个元素,rest列表包含剩下的元素
first, second, *rest = range(10)
print(first)  # 0
print(second)  # 1
print(rest)  # [2, 3, 4, 5, 6, 7, 8, 9]
# last保存最后一个元素,begin保存前面剩下的元素
*begin, last = range(10)
print(begin)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last)  # 9
# first保存第一个元素,last保存最后一个元素,middle保存中间剩下的元素
first, *middle, last = range(10)
print(first)  # 0
print(middle)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last)  # 9
