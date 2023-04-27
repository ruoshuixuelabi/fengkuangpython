"""
1.  在 collections包中除包含 deque 容器类之外,还包含另外一些容器类,这些容器类可能不如前面介绍的容器类那么常用,
但在实际开发中同样也是很实用的,掌握它们会使编程更加方便。

10.8.1	ChainMap对象

2.  ChainMap 是一个方便的工具类,它使用链的方式将多个 dict "链"在一起,从而允许程序可直接获取任意一个dict所包含的key 对应的value。
3.  简单来说, ChainMap 相当于把多个dict合并成一个大的 dict,但实际上底层并未真正合并这些 dict,
因此程序无须调用多个update()方法将多个dict进行合并。所以说ChainMap 是一种"假"合并,但实际用起来又具有较好的效果。
4.  需要说明的是,由于 ChainMap 只是将多个dict链在一起,并未真正合并它们,因此在多个 dict 中完全可能具有重复的key,
在这种情况下,排在"链"前面的dict中的key 具有更高的优先级。
5.  例如,下面程序示范了ChainMap 的用法。
"""
from collections import ChainMap

# 定义3个dict对象
a = {'Kotlin': 90, 'Python': 86}
b = {'Go': 93, 'Python': 92}
c = {'Swift': 89, 'Go': 87}
# 将3个dict对象链在一起,就像变成了一个大的dict
cm = ChainMap(a, b, c)
print(cm)
# 获取Kotlin对应的value
print(cm['Kotlin'])  # 90
# 获取Python对应的value
print(cm['Python'])  # 86
# 获取Go对应的value
print(cm['Go'])  # 93
"""
1.  上面程序中粗体字代码将a、b、c 三 个dict链在一起,组成一个ChainMap,这个链的顺序就是 a、b、c,
因此 a 的优先级最高, b 的优先级次之, c 的优先级最低。运行上面程序,可以看到如下输出结果。
2.  从上面第一行输出可以看到,ChainMap 其实并未将这三个dict合并成一个大的dict, 只是将它们链在一起而已。
"""
