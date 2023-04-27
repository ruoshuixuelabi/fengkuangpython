"""
10.7.3	Python的堆操作

1.  Python提供了关于堆的操作,下面先简单介绍有关堆的概念。
2.  假设有n 个数据元素的序列k,k₁,…,k,  当且仅当满足如下关系时,可以将这组数据称为小顶堆(小根堆)。
k₁ ≤kz+1且k₁ ≤ kz+2 (其中i=0,2,… ,(n-1)/2)
或者满足如下关系时,可以将这组数据称为大顶堆(大根堆)。
k₁ ≥k2+1 且k₁ ≥k₂+2  (其中i=0,2,…,(n-1)/2)
3.  对于满足小顶堆的数据序列k,k₁…,k,如果将它们顺序排成一棵完全二叉树,则此树的特点是：
树中所有节点的值都小于其左、右子节点的值,此树的根节点的值必然最小。反之,对于满 足大顶堆的数据序列k0,k1,…,k(n-1),
如果将它们顺序排成一棵完全二叉树,则此树的特点是：树中所有节点的值都大于其左、右子节点的值,此树的根节点的值必然最大。
4.  通过上面介绍不难发现,小顶堆的任意子树也是小顶堆,大顶堆的任意子树还是大顶堆。
5.  Python 提供的是基于小顶堆的操作,因此Python 可以对list中的元素进行小顶堆排列,这样程序每次获取堆中元素时,总会取得堆中最小的元素。
6.  例如,判断数据序列9,30,49,46,58,79是否为堆,可以将其转换为一棵完全二叉树,如图10.9所示。
7.  在图10.9中,每个节点上的灰色数字代表该节点数据在底层数组中的索引。图10.9所示的完全二叉树完全满足小顶堆的特征,
每个父节点的值总小于或等于它的左、右子节点的值。
8.  Python并没有提供"堆"这种数据类型,它是直接把列表当成堆处理的。Python提供的heapq 包中有一些函数,当程序用这
些函数来操作列表时,该列表就会表现出"堆"的行为。
9.  在交互式解释器中先导入heapq包,然后输入heapq.__all__命令来查看heapq 包下的全部函数, 可以看到如下输出结果。
10. 上面这些函数就是执行堆操作的工具函数,这些函数的功能大致如下。
(1)heappush(heap,item):将 item 元素加入堆。
(2)heappop(heap):将堆中最小元素弹出。
(3)heapify(heap):将堆属性应用到列表上。
(4)heapreplace(heap,x):将堆中最小元素弹出,并将元素x入堆。
(5)merge(*iterables,key=None,reverse=False): 将多个有序的堆合并成 一个大的有序堆,然后再输出。
(6)heappushpop(heap,item):   将 item 入堆,然后弹出并返回堆中最小的元素。
(7)nlargest(n,iterable,key=None):  返回堆中最大的n 个元素。
(8)nsmallest(n,iterable,key=None):  返回堆中最小的n 个元素。
下面程序示范了这些函数的用法。
"""
from heapq import *

my_data = list(range(10))
my_data.append(0.5)
# 此时my_data依然是一个list列表
print('my_data的元素：', my_data)
# 对my_data应用堆属性
heapify(my_data)
print('应用堆之后my_data的元素：', my_data)
heappush(my_data, 7.2)
print('添加7.2之后my_data的元素：', my_data)
# 弹出堆中最小的元素
print(heappop(my_data))  # 0
print(heappop(my_data))  # 0.5
print('弹出两个元素之后my_data的元素：', my_data)
# 弹出最小元素,压入指定元素
print(heapreplace(my_data, 8.1))
print('执行replace之后my_data的元素：', my_data)
print('my_data中最大的3个元素：', nlargest(3, my_data))
print('my_data中最小的4个元素：', nsmallest(4, my_data))
