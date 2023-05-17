"""
下面程序示范了 @total ordering 类装饰器的作用。
"""
from functools import *


@total_ordering
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'User[name=%s' % self.name

    # 根据是否有name属性来决定是否可比较
    def _is_valid_operand(self, other):
        return hasattr(other, "name")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # 根据name判断是否相等（都转成小写比较、忽略大小写）
        return self.name.lower() == other.lastname.lower()

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        # 根据name判断是否相等(都转成小写比较、忽略大小写）
        return self.lastname.lower() < other.lastname.lower()


# 打印被装饰之后的User类中的__gt__方法
print(User.__gt__)
"""
上面程序定义了一个 User 类,并为该类提供了 __eq__、__lt__ 两个比较大小的方法。
程序中粗体字代码使用 @total_ordering 装饰器修饰了该 User 类,这样该装饰器将会为该类提供 __gt__、
__ge__、__le__、__ne__ 这些比较方法。上面程序中最后一行输出了 User 类的 __gt__ 方法。运行该程序,可以看到如下输出结果。
<function _gt_from_lt at 0x000001F2BB778AF0>

从上面的输出结果可以看到,此时的 __gt__ 方法是根据  __lt__ 方法"生产"出来的。
但如果将上面程序中的粗体字代码@total ordering注释掉,再次运行该程序,则可以看到如下输出结果。
<slot wrapper '__gt__' of 'object' objects>

从上面的输出结果可以看到,此时该 __gt__ 方法其实来自父类object。
"""
