"""
10.8.5	OrderedDict对象
1.  OrderedDict也是dict的子类,其最大特征是：它可以“维护”添加key-value对的顺序。简单 来说,就是先添加的key-value对排在前面,后添加的key-value对排在后面。
由于OrderedDict 能维护 key-value对的添加顺序,因此即使两个OrderedDict中的 key-value 对完全相同,但只要它们的顺序不同,程序在判断它们是否相等时也依然会返回false。
例如如下程序。
2.  正如前面所说的,两个 OrderedDict 中即使包含的key-value对完全相同,但只要它们的顺序不同,
程序也依然会判断出两个 OrderedDict 是不相等的。例如如下程序。
"""
from collections import OrderedDict

# 创建OrderedDict对象
dx = OrderedDict(b=5, c=2, a=7)
print(dx)  # OrderedDict([('b', 5), ('c', 2), ('a', 7)])
d = OrderedDict()
# 向OrderedDict中添加key-value对
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] = 97
d['Go'] = 87
# 遍历OrderedDict的key-value对
for k, v in d.items():
    print(k, v)
"""
1.  上面程序首先创建了 OrderedDict 对象,接下来程序向其中添加了4个key-value对 ,OrderedDict 完全可以"记住"它们的添加顺序。
运行该程序,可以看到如下输出结果。
2.  正如前面所说的,两个 OrderedDict 中即使包含的key-value对完全相同,但只要它们的顺序不同,
程序也依然会判断出两个 OrderedDict 是不相等的。例如如下程序。
"""

# 创建普通的dict对象
my_data = {'Python': 20, 'Swift': 32, 'Kotlin': 43, 'Go': 25}
# 创建基于key排序的OrderedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
# 创建基于value排序的OrderedDict
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d1)  # OrderedDict([('Go', 25), ('Kotlin', 43), ('Python', 20), ('Swift', 32)])
print(d2)  # OrderedDict([('Python', 20), ('Go', 25), ('Swift', 32), ('Kotlin', 43)])
print(d1 == d2)  # False
"""
1.  上面程序先创建了一个普通的 dict 对象,该对象中包含4个key-value对;
接下来程序中两行粗体字代码分别使用 sorted() 函数对 my_data(dict 对象)的items进行排序： 
d1 是按 key 排序的;d2 是按 value 排序的,这样得到的d1、d2 两个 OrderedDict 中的key-value对是一样的,只不过顺序不同。

2.  运行上面程序,可以看到如下输出结果。

OrderedDict([('Go', 25), ('Kotlin', 43), ('Python', 20), ('Swift', 32)])
OrderedDict([('Python', 20), ('Go', 25), ('Swift', 32), ('Kotlin', 43)])
False

从上面的输出结果可以看到,虽然两个OrderedDict所包含的key-value对完全相同,但由于它们的顺序不同,因此程序判断它们不相等。
"""