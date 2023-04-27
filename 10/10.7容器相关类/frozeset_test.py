"""
1.  frozenset 是 set的不可变版本,因此 set 集合中所有能改变集合本身的方法(如add、remove、discard、xxx_update等),
frozenset都不支持;set集合中不改变集合本身的方法,frozenset都支持。
2.  在交互式解释器中输入[e for e in dir(frozenset) if not e.startswith(_)]命令来查看frozenset集合的全部方法,可以看到如下输出结果。

3.  很明显, frozenset的这些方法和set集合的同名方法的功能完全相同。
4.  frozenset的作用主要有两点。
(1)当集合元素不需要改变时,使用frozenset代替set更安全。
(2)当某些 API 需要不可变对象时,必须用 frozenset 代替 set。 比如 dict 的 key 必须是不可变对象,因此只能用frozenset;
再比如set本身的集合元素必须是不可变的,因此set不能包含set,set 只能包含frozenset。
5.  如下程序示范了在set中添加frozenset。
"""
s = set()
frozen_s = frozenset('Kotlin')
# 为set集合添加frozenset
s.add(frozen_s)
print('s集合的元素：', s)
sub_s = {'Python'}
# 为set集合添加普通set集合,程序报错
s.add(sub_s)
"""
上面程序中第一行粗体字代码为set添加 frozenset, 程序完全没有问题,这样 set 中就包括一个 frozenset 子集合;
第二行粗体字代码试图向 set 中添加普通 set, 程序会报出 TypeError 异常。运行上面代码,可以看到如下输出结果。
"""