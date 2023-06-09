"""
3.3.5  列表的其他常用方法

除上面介绍的增加元素、删除元素、修改元素方法之外,列表还包含了一些常用的方法。
例如,在交互式解释器中输入dir(list)即可看到列表包含的所有方法,如下所示。

备注：在上面输出结果中已经剔除了那些以双下画线开头的方法。按照约定,这些方法都具有特殊的意义,不希望被用户直接调用。

上面有些方法前面已经介绍过了,列表还包含如下常用方法可以使用。
(1)count()：用于统计列表中某个元素出现的次数。
(2)index()：用于判断某个元素在列表中出现的位置。
(3)pop()：用于将列表当成"栈"使用,实现元素出栈功能。
(4)reverse()：用于将列表中的元素反向存放。
(5)sort()：用于对列表元素排序。

下面代码示范了count()方法的用法。
"""
a_list = [2, 30, 'a', [5, 30], 30]
# 计算列表中30的出现次数
print(a_list.count(30))  # 2
# 计算列表中[5, 30]的出现次数
print(a_list.count([5, 30]))  # 1
