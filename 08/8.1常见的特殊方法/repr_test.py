"""
1.  object类提供的 __repr__()方法总是返回该对象实现类的"类名+object at+内存地址"值,
这个返回值并不能真正实现"自我描述"的功能,因此,如果用户需要自定义类能实现"自我描述"的功能,就必须重写__repr__()方法。例如下面程序。
"""


class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color;
        self.weight = weight;

    # 重写toString()方法,用于实现Apple对象的"自我描述"
    def __repr__(self):
        return "Apple[color=" + self.color + \
            ", weight=" + str(self.weight) + "]"


a = Apple("红色", 5.68)
# 打印Apple对象
print(a)
