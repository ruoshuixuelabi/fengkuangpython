"""
3.4.3 字典的基本用法

对于初学者而言,应牢记字典包含多个 key-value 对,而 key 是字典的关键数据,因此程序对字典的操作都是基于 key 的。基本操作如下。
(1)通过key访问value。
(2)通过key添加key-value对。
(3)通过key删除key-value对。
(4)通过key修改key-value对。
(5)通过key判断指定key-value对是否存在。

通过 key 访问 value 使用的也是方括号语法,就像前面介绍的列表和元组一样,只是此时在方括号中放的是 key,而不是列表或元组中的索引。

如下代码示范了通过 key 访问 value。
"""
scores = {'语文': 89}
# 通过key访问value
print(scores['语文'])
# 对不存在的key赋值,就是增加key-value对
scores['数学'] = 93
scores[92] = 5.7
print(scores)  # {'语文': 89, '数学': 93, 92: 5.7}
# 使用del语句删除key-value对
del scores['语文']
del scores['数学']
print(scores)  # {92: 5.7}

cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 对存在的key-value对赋值,改变key-value对
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars)  # {'BMW': 8.5, 'BENS': 4.3, 'AUDI': 3.8}
# 如果要判断字典是否包含指定的 key,则可以使用 in 或 not in运算符。
# 需要指出的是,对于 dict 而言, in 或 not in 运算符都是基于 key 来判断的
# 判断cars是否包含名为'AUDI'的key
print('AUDI' in cars)  # True
# 判断cars是否包含名为'PORSCHE'的key
print('PORSCHE' in cars)  # False
print('LAMBORGHINI' not in cars)  # True
"""
如果要为 dict 添加 key-value 对,只需为不存在的 key 赋值即可
# 对不存在的key赋值,就是增加key-value对
scores['数学'] = 93
scores[92] = 5.7
print(scores)  # {'语文': 89, '数学': 93, 92: 5.7}

如果要删除字典中的 key-value 对,则可使用del语句。
# 使用del语句删除key-value对
del scores['语文']
del scores['数学']
print(scores)  # {92: 5.7}

如果对 dict 中存在的 key-value 对赋值,新赋的 value 就会覆盖原有的 value ,这样即可改变 dict 中的 key-value 对。
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 对存在的key-value对赋值,改变key-value对
cars['BENS'] = 4.3
cars['AUDI'] = 3.8
print(cars)  # {'BMW': 8.5, 'BENS': 4.3, 'AUDI': 3.8}

如果要判断字典是否包含指定的 key,则可以使用 in 或 not in运算符。
需要指出的是,对于 dict 而言, in 或 not in 运算符都是基于 key 来判断的。
# 判断cars是否包含名为'AUDI'的key
print('AUDI' in cars)  # True
# 判断cars是否包含名为'PORSCHE'的key
print('PORSCHE' in cars)  # False
print('LAMBORGHINI' not in cars)  # True

通过上面介绍可以看出,字典的 key 是它的关键。换个角度来看,
字典的 key 就相当于它的索引,只不过这些索引不一定是整数类型,字典的 key 可以是任意不可变类型。

可以这样说,字典相当于索引是任意不可变类型的列表;而列表则相当于 key 只能是整数的字典。
因此,如果程序中要使用的字典的 key 都是整数类型,则可考虑能否换成列表。

此外,还有一点需要指出,列表的索引总是从0开始、连续增大的;但字典的索引即使是整数类型,也不需要从0开始,而且不需要连续。
因此,列表不允许对不存在的索引赋值;但字典则允许直接对不存在的 key 赋值——这样就会为字典增加一个 key-value 对。

列表不允许对不存在的索引赋值;但字典则允许直接对不存在的 key 赋值。
"""
