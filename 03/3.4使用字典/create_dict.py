"""
3.4 使用字典
1.  字典也是 Python 提供的一种常用的数据结构,它用于存放具有映射关系的数据。

3.4.1 字典入门

2.  比如有成绩表数据—— 语文：79,数学：80,英语：92,这组数据看上去像两个列表,但这两个列表的元素之间有一定的关联关系。
如果单纯使用两个列表来保存这组数据,则无法记录两组数据之间的关联关系。
3.  为了保存具有映射关系的数据, Python 提供了字典,字典相当于保存了两组数据,其中一组数据是关键数据,被称为 key;
另一组数据可通过 key 来访问,被称为value。
4.  由于字典中的 key 是非常关键的数据,而且程序需要通过 key 来访问 value,因此字典中的 key 不允许重复。

3.4.2 创建字典

5.  程序既可使用花括号语法来创建字典,也可使用 dict() 函数来创建字典。实际上,dict 是一种类型,它就是Python 中的字典类型。
6.  在使用花括号语法创建字典时,花括号中应包含多个key-value对,key 与 value之间用英文冒号隔开;多个key-value对之间用英文逗号隔开。
如下代码示范了使用花括号语法创建字典。
7.  需要指出的是,元组可以作为dict的 key, 但列表不能作为元组的key。
这是由于dict要求key必须是不可变类型,但列表是可变类型,因此列表不能作为元组的key。
8.  在使用dict()函数创建字典时,可以传入多个列表或元组参数作为key-value对,每个列表或元组将被当成一个key-value对,
因此这些列表或元组都只能包含两个元素。
9.  还可通过为dict指定关键字参数创建字典,此时字典的key 不允许使用表达式
"""
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30): 'good', 30: 'bad'}
print(dict2)

vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
# 创建包含3组key-value对的字典
dict3 = dict(vegetables)
print(dict3)  # {'celery': 1.58, 'brocoli': 1.29, 'lettuce': 2.19}
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
# 创建包含3组key-value对的字典
dict4 = dict(cars)
print(dict4)  # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 创建空的字典
dict5 = dict()
print(dict5)  # {}
# 使用关键字参数来创建字典
dict6 = dict(spinach=1.39, cabbage=2.59)
print(dict6)  # {'spinach': 1.39, 'cabbage': 2.59}
