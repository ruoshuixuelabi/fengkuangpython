"""
1.  popitem()方法用于随机弹出字典中的一个key-value 对
2.  此处的随机其实是假的,正如列表的pop()方法总是弹出列表中最后一个元素,
实际上字典的 popitem()其实也是弹出字典中最后一个 key-value 对。由于字典存储key-value对的顺序是不可知的,
因此开发者感觉字典的 popitem()方法是"随机"”"弹出 的,但实际上字典的popitem()方法总是弹出底层存储的最后一个key-value对。
3.  由于实际上popitem 弹出的就是一个元组,因此程序完全可以通过序列解包的方式用两个变量分别接收key 和 value。
"""
cars = {'AUDI': 7.9, 'BENS': 8.3, 'BMW': 8.5}
print(cars)
# 弹出字典底层存储的最后一个key-value对
print(cars.popitem())  # ('AUDI', 7.9)
print(cars)  # {'BMW': 8.5, 'BENS': 8.3}
# 将弹出项的key赋值给k、value赋值给v
k, v = cars.popitem()
print(k, v)  # BENS 8.3
