"""
与 list() 对应的是,Python 也提供了一个 tuple() 函数,该函数可用于将列表、区间 (range)等对象转换为元组。

例如如下代码
"""
a_list = ['crazyit', 20, -1.2]
# 将列表转换成元组
a_tuple = tuple(a_list)
print(a_tuple)
# 使用range()函数创建区间(range)对象
a_range = range(1, 5)
print(a_range)  # range(1, 5)
# 将区间转换成元组
b_tuple = tuple(a_range)
print(b_tuple)  # [1, 2, 3, 4]
# 创建区间时还指定步长
c_tuple = tuple(range(4, 20, 3))
print(c_tuple)  # [4, 7, 10, 13, 16, 19]
