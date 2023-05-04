"""
4.4.4  使用for-in 循环遍历列表和元组

在使用 for-in 循环遍历列表和元组时,列表或元组有几个元素,for-in 循环的循环体就执行几次,
针对每个元素执行一次,循环计数器会依次被赋值为元素的值。

如下代码使用for-in循环遍历元组。
"""
a_tuple = ('crazyit', 'fkit', 'Charlie')
for ele in a_tuple:
    print('当前元素是:', ele)
