"""
4.4.5 使用for-in循环遍历字典

使用 for-in 循环遍历字典其实也是通过遍历普通列表来实现的。前面在介绍字典时已经提到,字典包含了如下三个方法。
(1)items()：返回字典中所有key-value对的列表。
(2)keys()：返回字典中所有key的列表。
(3)values()：返回字典中所有value 的列表。
因此,如果要遍历字典,完全可以先调用字典的上面三个方法之一来获取字典的所有key-value

其是通过字典的 items() 遍历所有的 key-value 对时,由于 items() 方法返回的是字典中所有key-value
对组成的列表,列表元素都是长度为2的元组,因此程序要声明两个变量来分别代表 key、value ——这也是序列解包的应用。
"""
my_dict = {'语文': 89, '数学': 92, '英语': 80}
# 通过items()方法遍历所有key-value对
# 由于items方法返回的列表元素是key-value对,因此要声明两个变量
for key, value in my_dict.items():
    print('key:', key)
    print('value:', value)
print('-------------')
# 通过keys()方法遍历所有key
for key in my_dict.keys():
    print('key:', key)
    # 在通过key获取value
    print('value:', my_dict[key])
print('-------------')
# 通过values()方法遍历所有value
for value in my_dict.values():
    print('value:', value)
