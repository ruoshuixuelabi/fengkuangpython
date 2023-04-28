"""
3.2.4   乘法

列表和元组可以和整数执行乘法运算,列表和元组乘法的意义就是把它们包含的元素重复 N 次——N 就是被乘的倍数。

如下代码示范了列表和元组的乘法。
"""
a_tuple = ('crazyit', 20)
# 执行乘法
mul_tuple = a_tuple * 3
print(mul_tuple)  # ('crazyit', 20, 'crazyit', 20, 'crazyit', 20)
a_list = [30, 'Python', 2]
mul_list = a_list * 3
print(mul_list)  # [30, 'Python', 2, 30, 'Python', 2, 30, 'Python', 2]
