"""
与 reversed()函数类似的还有sorted()函数,该函数接收一个可迭代对象作为参数,返回一个对元素排序的列表。
"""
my_list = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
for s in sorted(my_list, key=len):
    print(s)