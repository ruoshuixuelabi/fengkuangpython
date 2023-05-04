"""
4.4.2  使用 while 循环遍历列表和元组

由于列表和元组的元素都是有索引的,因此程序可通过while循环、列表或元组的索引来遍历列表和元组中的所有元素。例如如下程序。
"""
a_tuple = ('fkit', 'crazyit', 'Charli')
i = 0
# 只有i小于len(a_list),继续执行循环体
while i < len(a_tuple):
    print(a_tuple[i])  # 根据i来访问元组的元素
    i += 1
