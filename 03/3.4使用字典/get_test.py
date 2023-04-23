"""
get() 方法其实就是根据key来获取value,它相当于方括号语法的增强版——当使用方括号语法访问并不存在的 key 时，
字典会引发KeyError 错误;但如果使用 get()方法访问不存在的key,该方法会简单地返回None,不会导致错误。例如如下代码。
"""
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 获取'BMW'对应的value
print(cars.get('BMW'))  # 8.5
print(cars.get('PORSCHE'))  # None
print(cars['PORSCHE'])  # KeyError
