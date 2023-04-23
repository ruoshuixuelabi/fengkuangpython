"""
1.  sort()方法用于对列表元素进行排序。例如如下代码。
2.  sort()方法除支持默认排序之外，还可传入key 和 reverse两个参数，
而且这两个参数必须通过参数名指定(这种参数叫关键字参数，本书第5章会详细介绍)。
key 参数用于为每个元素都生成一个比较大小的"键"; reverse参数则用于执行是否需要反转排序——默认是从小到大排序；
如果将该参数设为True, 将会改为从大到小排序。
3.  需要指出的是，在Python 2.x中，列表的sort()方法还可传入一个比较大小的函数，该函数负责比较列表元素的大小。
该函数包含两个参数，当该函数返回正整数时，代表该函数的第一个参数大于第二个参数；
当该函数返回负整数时，代表该函数的第一个参数小于第二个参数；返回0则意味着两个参数相等。
"""
a_list = [3, 4, -2, -30, 14, 9.3, 3.4]
# 对列表元素排序
a_list.sort()
print(a_list)  # [-30, -2, 3, 3.4, 4, 9.3, 14]
b_list = ['Python', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erlang']
# 对列表元素排序：默认按字符串包含的字符的编码大小比较
b_list.sort()
print(b_list)  # ['Erlang', 'Go', 'Kotlin', 'Python', 'Ruby', 'Swift']

# 指定key为len，指定使用len函数对集合元素生成比较的键，也就是按字符串的长度比较大小
b_list.sort(key=len)
print(b_list)  # ['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']
# 指定反向排序
b_list.sort(key=len, reverse=True)
print(b_list)  # ['Erlang', 'Kotlin', 'Python', 'Swift', 'Ruby', 'Go']

# 以下代码只能在Python 2.x中执行
# 定义一个根据长度比较大小的比较函数
def len_cmp(x, y):
    # 下面代码比较大小的逻辑是：长度大的字符串就算更大
    return 1 if len(x) > len(y) else (-1 if len(x) < len(y) else 0)


b_list.sort(len_cmp)
print(b_list)  # ['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']
