"""
fromkeys() 方法使用给定的多个key 创建字典，这些key 对应的value 默认都是None;
也可以额外传入一个参数作为默认的value。该方法一般不会使用字典对象调用(没什么意义),通常会使用dict类直接调用。例如如下代码。
"""
# 使用列表创建包含2个key的字典
a_dict = dict.fromkeys(['a', 'b'])
print(a_dict)  # {'a': None, 'b': None}
# 使用元组创建包含2个key的字典
b_dict = dict.fromkeys((13, 17))
print(b_dict)  # {13: None, 17: None}
# 使用元组创建包含2个key的字典，指定默认的value
c_dict = dict.fromkeys((13, 17), 'good')
print(c_dict)  # {13: 'good', 17: 'good'}
