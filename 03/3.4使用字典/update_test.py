"""
1.  update() 方法可使用一个字典所包含的key-value 对来更新已有的字典。
在执行update() 方法时， 如果被更新的字典中已包含对应的key-value对，那么原value会被覆盖；
如果被更新的字典中不包含对应的key-value对，则该key-value对被添加进去。例如如下代码。
2.  从下面的执行过程可以看出，由于被更新的dict中已包含key 为"BMW"的 key-value对，因此更新时该key-value对 的value将被改写；
但如果被更新的dict中不包含key为"PORSCHE"的 key-value对，那么更新时就会为原字典增加一个key-value对。
"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
cars.update({'BMW': 4.5, 'PORSCHE': 9.3})
print(cars)
