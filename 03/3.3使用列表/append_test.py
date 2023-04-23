"""
1.  为列表增加元素可调用列表的append()方法，该方法会把传入的参数追加到列表的最后面。
2.  append()方法既可接收单个值，也可接收元组、列表等，但该方法只是把元组、列表当成单个元素，
这样就会形成在列表中嵌套列表、嵌套元组的情形。例如如下代码。
3.  从上面代码可以看出，为列表追加另一个列表时， Python 会将被追加的列表当成一个整体的元素，而不是追加目标列表中的元素。
如果希望不将被追加的列表当成一个整体，而只是追加列表中的元素，则可使用列表的extend()方法。
4.  此外，如果希望在列表中间增加元素，则可使用列表的 insert()方法，使用insert()方法时要指定将元素插入列表的哪个位置。
"""
a_list = ['crazyit', 20, -2]
# 追加元素
a_list.append('fkit')
print(a_list)  # ['crazyit', 20, -2, 'fkit']
a_tuple = (3.4, 5.6)
# 追加元组，元组被当成一个元素
a_list.append(a_tuple)
print(a_list)  # ['crazyit', 20, -2, 'fkit', (3.4, 5.6)]
# 追加列表，列表被当成一个元素
a_list.append(['a', 'b'])
print(a_list)  # ['crazyit', 20, -2, 'fkit', (3.4, 5.6), ['a', 'b']]
# 如果希望不将被追加的列表当成一个整体，而只是追加列表中的元素，则可使用列表的extend()方法
b_list = ['a', 30]
# 追加元组中的所有元素
b_list.extend((-2, 3.1))
print(b_list)  # ['a', 30, -2, 3.1]
# 追加列表中的所有元素
b_list.extend(['C', 'R', 'A'])
print(b_list)  # ['a', 30, -2, 3.1, 'C', 'R', 'A']
# 追加区间中的所有元素
b_list.extend(range(97, 100))
print(b_list)  # ['a', 30, -2, 3.1, 'C', 'R', 'A', 97, 98, 99]
# 此外，如果希望在列表中间增加元素，则可使用列表的 insert()方法，使用insert()方法时要指 定将元素插入列表的哪个位置。
c_list = list(range(1, 6))
print(c_list)  # [1, 2, 3, 4, 5]
# 在索引3处插入字符串
c_list.insert(3, 'CRAZY')
print(c_list)  # [1, 2, 3, 'CRAZY', 4, 5]
# 在索引3处插入元组，元组被当成一个元素
c_list.insert(3, tuple('crazy'))
print(c_list)  # [1, 2, 3, ('c', 'r', 'a', 'z', 'y'), 'CRAZY', 4, 5]
