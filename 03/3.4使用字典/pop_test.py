"""
pop() 方法用于获取指定key 对应的value,   并删除这个key-value 对。如下方法示范了pop()方法的用法。
"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
print(cars.pop('AUDI'))  # 7.9
print(cars)  # {'BMW': 8.5, 'BENS': 8.3}
