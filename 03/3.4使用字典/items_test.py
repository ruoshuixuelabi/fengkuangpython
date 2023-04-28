"""
items() 、keys()、values() 分别用于获取字典中的所有key-value 对、所有key 、所有value。
这三个方法依次返回 dict_items、dict_keys和 dict_values对象,Python 不希望用户直接操作这几个方法,
但可通过 list() 函数把它们转换成列表。如下代码示范了这三个方法的用法。
"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 获取字典所有的 key-value 对,返回一个 dict_items 对象
ims = cars.items()
print(type(ims))  # <class 'dict_items'>
# 将dict_items转换成列表
print(list(ims))  # [('BMW', 8.5), ('BENS', 8.3), ('AUDI', 7.9)]
# 访问第2个 key-value 对
print(list(ims)[1])  # ('BENS', 8.3)
# 获取字典所有的 key,返回一个 dict_keys 对象
kys = cars.keys()
print(type(kys))  # <class 'dict_keys'>
# 将dict_keys转换成列表
print(list(kys))  # ['BMW', 'BENS', 'AUDI']
# 访问第2个key
print(list(kys)[1])  # 'BENS'
# 获取字典所有的value,返回一个dict_values对象
vals = cars.values()
# 将dict_values转换成列表
print(type(vals))  # [8.5, 8.3, 7.9]
# 访问第2个value
print(list(vals)[1])  # 8.3
"""
从上面代码可以看出,程序调用字典的 items()、keys()、values()方法之后,
都需要调用 list() 函数将它们转换为列表,这样即可把这三个方法的返回值转换为列表。

在Python 2.x中,items()、keys()、values()方法的返回值本来就是列表,完全可以不用list()函数进行处理。
当然,使用list()函数处理也行,列表被处理之后依然是列表。
"""