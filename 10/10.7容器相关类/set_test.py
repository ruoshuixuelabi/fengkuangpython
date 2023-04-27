"""
1.  除前面介绍的列表(list)、元组(tuple)和字典(dict)等容器类型之外,Python 还提供了集合(set)、双端队列(deque)等数据类型,
这些数据类型可能不如列表、字典等容器类型常用,但它们也是Python 编程的基础内容,也应该重点掌握。
2.  绝大部分编程语言都会提供list、set、dict(在有的语言中叫dictionary或 map)、deque 这些数据类型,
如果你有Java、Objective-C等其他语言的编程经验,那么你会对这些类型感到似曾相识。 这是为什么呢?
3.  早期学计算机编程的人可能听过一句话：程序 = 数据结构 + 算法
4.  一直以来,这句话被国内多少计算机专业奉为圭臬,"数据结构"也是不少本科院校软件专业的基础课程,
"数据结构"课程所讲授的其实就是list、set、dict、deque等内容。其原因就在于：list.  set、dict、deque等数据结构确实是软件开发的基础。
5.  提示：以笔者的经验来看,软件专业一开始就上"数据结构"课程未必是好事,这些内容虽然非常重要,但对于普通开发者而言,
他们往往并不需要掌握实现 list、set、dict、deque 的具体细节,只要会用它们即可。此外, 一开始就学习"数据结构"比较容易打
击初学者的信心,因此完全可以等学习者有一定的编程基础之后再来学习这些数据结构
6.  总的来说,绝大部分编程语言通常总会提供的4种主流的数据结构是list、set、dict 和 deque, 其中set集合类似于一个罐子,
把一个对象添加到set集合时, set集合无法记住添加这个元素的顺序,所以set里的元素不能重复(否则系统无法准确识别这个元素);
list容器就是前面介绍的列表,它可以记住每次添加元素的顺序,因此程序可通过索引来存取元素, list容器的元素允许重复;
dict  容器也像一个罐子,只是它里面的每项数据都由key-value对组成,因此程序可通过key 来存取value。
deque 则代表一个双端队列。双端队列的特征是它的两端都可以添加、删除元素,它既可作为栈(stack)使用,也可作为队列(queue)使用。

10.7.1	set和frozenset

7.  set集合有如下两个特征。
(1)set不记录元素的添加顺序。
(2)元素不允许重复。

8.  set集合是可变容器,程序可以改变容器中的元素。与set对应的还有frozenset集合, frozenset 是set的不可变版本,它的元素是不可变的。
9.  在交互式解释器中输入[e for e in dir(set) if not e.startswith(_)]来查看set集合的全部方法,可以看到如下输出结果。
10. 对于上面这些方法,其方法名已经暗示了它们的作用,比如add()很明显就是向set集合中添加元素, remove()、discard()就是删除元素,
clear()就是清空set集合,等等。
11. remove()与 discard()方法都用于删除集合中的元素,但区别在于：如果集合中不包含被删除的元素,
remove()方法会报出KeyError 异常,而discard()方法则什么也不做。
12. 下面程序示范了set集合的方法的用法。
"""
# 使用花括号构建set集合
c = {'白骨精'}
# 添加元素
c.add("孙悟空")
c.add(6)
print("c集合的元素个数为:", len(c))  # 输出3
# 删除指定元素
c.remove(6)
print("c集合的元素个数为:", len(c))  # 输出2
# 判断是否包含指定字符串
print("c集合是否包含'孙悟空'字符串:", ("孙悟空" in c))  # 输出True
c.add("轻量级Java EE企业应用实战")
print("c集合的元素：", c)
# 使用set()函数（构造器）来创建set集合
books = set()
books.add("轻量级Java EE企业应用实战")
books.add("疯狂Java讲义")
print("books集合的元素：", books)
# issubset()方法判断是否为子集合
print("books集合是否为c的子集合？", books.issubset(c))  # 输出False
# issubset()方法与<=运算符效果相同
print("books集合是否为c的子集合？", (books <= c))  # 输出False
# issuperset()方法判断是否为父集合
# issubset和issuperset其实就是倒过来判断
print("c集合是否完全包含books集合？", c.issuperset(books))  # 输出False
# issuperset()方法与>=运算符效果相同
print("c集合是否完全包含books集合？", (c >= books))  # 输出False
# 用c集合减去books集合里的元素,不改变c集合本身
result1 = c - books
print(result1)
# difference()方法也是对集合做减法,与用-执行运算的效果完全一样
result2 = c.difference(books)
print(result2)
# 用c集合减去books集合里的元素,改变c集合本身
c.difference_update(books)
print("c集合的元素：", c)
# 删除c集合里的所有元素
c.clear()
print("c集合的元素：", c)
# 直接创建包含元素的集合
d = {"疯狂Java讲义", '疯狂Python讲义', '疯狂Kotlin讲义'}
print("d集合的元素：", d)
# 计算两个集合的交集,不改变d集合本身
inter1 = d & books
print(inter1)
# intersection()方法也是获取两个集合的交集,与用&执行运算的效果完全一样
inter2 = d.intersection(books)
print(inter2)
# 计算两个集合的交集,改变d集合本身
d.intersection_update(books)
print("d集合的元素：", d)
# 将range对象包装成set集合
e = set(range(5))
f = set(range(3, 7))
print("e集合的元素：", e)
print("f集合的元素：", f)
# 对两个集合执行异或运算
xor = e ^ f
print('e和f执行xor的结果：', xor)
# 计算两个集合的并集,不改变e集合本身
un = e.union(f)
print('e和f执行并集的结果：', un)
# 计算两个集合的并集,改变e集合本身
e.update(f)
print('e集合的元素：', e)
"""
1.  上面程序基本示范了set集合中所有方法的用法。不仅如此,该程序还示范了set集合支持的 如下几个运算符。
(1)<= : 相当于调用issubset()方法,判断前面的set集合是否为后面的set集合的子集合。
(2)>= : 相当于调用issuperset()方法,判断前面的set集合是否为后面的set集合的父集合。
(3)- : 相当于调用difference()方法,用前面的set集合减去后面的set集合的元素。 
(4)& : 相当于调用intersection()方法,用于获取两个set集合的交集。
(5)^:计算两个集合异或的结果,就是用两个集合的并集减去交集的元素。

2.  此外,由于 set集合本身是可变的,因此它除了提供add()、remove()、discard()方法来操作单个元素,
还支持进行集合运算来改变集合内的元素。因此,它的集合运算方法都有两个版本。
(1)交集运算：intersection()和 intersection_update(), 前者不改变集合本身,而是返回两个集合的交集;后者会通过交集运算改变第一个集合。
(2)并集运算：union()和 update(),前者不改变集合本身,而是返回两个集合的并集；后者会通过并集运算改变第一个集合。
(3)减法运算：difference()和 difference_update(),前者不改变集合本身,而是返回两个集合做减法的结果;后者改变第一个集合。
"""