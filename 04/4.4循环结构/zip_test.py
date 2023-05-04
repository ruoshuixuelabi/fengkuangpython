"""
4.4.9 常用工具函数

使用zip()函数可以把两个列表"压缩"成一个zip对象(可迭代对象),这样就可以使用一个循环并行遍历两个列表。
为了测试 zip()函数的功能,我们可以先在交互式解释器中"试验"一下该函数的功能。
a =['a','b','c']
b =[1,2,3]
[x for x in zip(a,b)]
[('a',1),('b',2),('c',3)]
从上面的测试结果来看,zip()函数压缩得到的可迭代对象所包含的元素是由原列表元素组成的元组。

提示：Python 2.x的 zip() 函数直接返回列表,而不是返回 zip 对象。
Python 2.x的 zip()函数返回的列表所包含的元素和Python 3.x的 zip()返回的zip对象所包含的元素相同。
c=[0.1,0.2]
[x for x in zip(a,c)]
[('a',0.1),('b',20.)]

从上面代码可以看出,如果 zip()函数压缩的两个列表长度不相等,那么zip()函数将以长度更短的列表为准。

zip()函数不仅可以压缩两个列表,也可以压缩多个列表。比如下面试验同时压缩3个列表。
[x for   x  in  zip(a,b,c)]
[('a',1,0. 1),('b',2,0.2)]

从上面代码可以看出,如果使用zip(函数压缩 N 个列表,那么 zip()函数返回的可迭代对象的元素就是长度为 N 的元组。

有些时候,程序需要进行反向遍历,此时可通过 reversed()函数,该函数可接收各种序列(元组、列表、区间等)参数,
然后返回一个"反序排列"的迭代器,该函数对参数本身不会产生任何影响。

"""
books = ['疯狂Kotlin讲义', '疯狂Swift讲义', '疯狂Python讲义']
prices = [79, 69, 89]
# 使用zip()函数压缩两个列表,从而实现并行遍历
for book, price in zip(books, prices):
    print("%s的价格是: %5.2f" % (book, price))
    