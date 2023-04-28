"""
setdefault()方法也用于根据 key 来获取对应 value 的值。但该方法有一个额外的功能------当程序要获取的 key 在字典中不存在时,
该方法会先为这个不存在的key设置一个默认的value,然后再返回该 key 对应的 value。
总之,setdefault()方法总能返回指定 key 对应的 value——如果该 key-value对存在,则直接返回该key 对应的value;
如果该key-value对不存在,则先为该key 设置默认的value, 然后再返回该key 对应的value。

如下代码示范了setdefault()方法的用法。
"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 设置默认值,该key在dict中不存在,新增key-value对
print(cars.setdefault('PORSCHE', 9.2))  # 9.2
print(cars)
# 设置默认值,该key在dict中存在,不会修改dict内容
print(cars.setdefault('BMW', 3.4))  # 8.5
print(cars)
