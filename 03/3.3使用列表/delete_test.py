"""
1.  删除列表元素使用del语句。 del语句是Python的一种语句，专门用于执行删除操作，不仅可用于删除列表的元素，也可用于删除变量等。
2.  使用del 语句既可删除列表中的单个元素，也可直接删除列表的中间一段。例如如下代码。
3.  使用del语句不仅可以删除列表元素，也可以删除普通变量
4.   除使用del语句之外，Python 还提供了remove()方法来删除列表元素，该方法并不是根据索引来删除元素的，
而是根据元素本身来执行删除操作的。该方法只删除第一个找到的元素，如果找不到该元素，该方法将会引发ValueError错误。
5.  列表还包含一个clear()方法，正如它的名字所暗示的，该方法用于清空列表的所有元素。
"""
a_list = ['crazyit', 20, -2.4, (3, 4), 'fkit']
# 删除第3个元素
del a_list[2]
print(a_list)  # ['crazyit', 20, (3, 4), 'fkit']
# 删除第2个到第4个(不包含)元素
del a_list[1: 3]
print(a_list)  # ['crazyit', 'fkit']
b_list = list(range(1, 10))
# 删除第3个到倒数第2个(不包含)元素，间隔为2
del b_list[2: -2: 2]
print(b_list)  # [1, 2, 4, 6, 8, 9]
# 删除第3个到第5个(不包含)元素
del b_list[2: 4]
print(b_list)  # [1, 2, 8, 9]

name = 'crazyit'
print(name)  # crazyit
# 删除name变量
del name
# print(name) # NameError

c_list = [20, 'crazyit', 30, -4, 'crazyit', 3.4]
# 删除第一次找到的30
c_list.remove(30)
print(c_list)  # [20, 'crazyit', -4, 'crazyit', 3.4]
# 删除第一次找到的'crazyit'
c_list.remove('crazyit')
print(c_list)  # [20, -4, 'crazyit', 3.4]
# 列表还包含一个clear()方法，正如它的名字所暗示的，该方法用于清空列表的所有元素。
c_list.clear()
print(c_list)  # []
