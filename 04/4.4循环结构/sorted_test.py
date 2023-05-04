"""
与 reversed()函数类似的还有sorted()函数,该函数接收一个可迭代对象作为参数,返回一个对元素排序的列表。

在使用 sorted()函数时,还可传入一个reverse参数,如果将该参数设置为True, 则表示反向排序。

在调用 sorted() 函数时,还可传入一个 key 参数,该参数可指定一个函数来生成排序的关键值。
比如希望根据字符串长度排序,则可为 key 参数传入 len 函数。
"""
my_list = ['fkit', 'crazyit', 'Charlie', 'fox', 'Emily']
for s in sorted(my_list, key=len):
    print(s)
