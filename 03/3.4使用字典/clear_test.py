"""
3.4.4  字典的常用方法
1.  字典由dict类代表，因此我们同样可使用dir(dict)来查看该类包含哪些方法。
在交互式解释器 中输入dir(dict)命令，将看到如下输出结果。
下面介绍 dict的一些方法。
clear() 用于清空字典中所有的 key-value 对，对一个字典执行 clear() 方法之后，该字典就会变成一个空字典。
"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars)  # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 清空cars所有key-value对
cars.clear()
print(cars)  # {}
