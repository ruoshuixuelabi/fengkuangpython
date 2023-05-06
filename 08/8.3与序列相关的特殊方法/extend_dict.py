"""
8.3.3 扩展列表、元组和字典

通过前面介绍的方法可实现自定义序列、自定义迭代器。实际上前面介绍的列表、元组等本身都实现了这些序列方法、迭代器方法,
因此它们既是序列,也是迭代器。

很多时候,如果程序明确需要一个特殊的列表、元组或字典类,我们有两种选择。
(1)自己实现序列、迭代器等各种方法,自己来实现这个特殊的类。
(2)扩展系统已有的列表、元组或字典。

很明显,第一种方式有点烦琐,因为这意味着开发者要把所有方法都自己实现一遍;
第二种方式就简单多了,只要继承系统已有的列表、元组或字典类,然后重写或新增方法即可。

下面程序将会示范开发一个新的字典类,这个字典类可根据 value 来获取key。
由于字典中 value 是可以重复的,因此该方法会返回指定 value 对应的全部 key 组成的列表。
"""


# 定义ValueDict类,继承dict类
class ValueDict(dict):
    # 定义构造函数
    def __init__(self, *args, **kwargs):
        # 调用父类的构造函数
        super().__init__(*args, **kwargs)

    # 新增getkeys方法
    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val: result.append(key)
        return result


my_dict = ValueDict(语文=92, 数学=89, 英语=92)
# 获取92对应的所有key
print(my_dict.getkeys(92))  # ['语文', '英语']
my_dict['编程'] = 92
print(my_dict.getkeys(92))  # ['语文', '英语', '编程']
"""
上面粗体字代码为扩展的 ValueDict 类新增了一个 getkeys 方法,该方法可以根据 value 获取它对应的所有 key 组成的列表。
运行该程序,可以看到如下输出结果。

['语文', '英语']
['语文', '英语', '编程']

从上面的输出结果不难看出,我们扩展的这个字典类可以根据value 获取对应的key,运行非常好,
而程序只要扩展dict类,并新增一个方法即可,非常方便。
"""