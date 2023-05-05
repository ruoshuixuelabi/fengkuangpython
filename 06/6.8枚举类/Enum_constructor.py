"""
6.8.2 枚举的构造器

枚举也是类,因此枚举也可以定义构造器。为枚举定义构造器之后,在定义枚举实例时必须为构造器参数设置值。例如如下程序。
"""
import enum


class Gender(enum.Enum):
    MALE = '男', '阳刚之力'
    FEMALE = '女', '柔顺之美'

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc

    @property
    def cn_name(self):
        return self._cn_name


# 访问FEMALE的name
print('FEMALE的name:', Gender.FEMALE.name)
# 访问FEMALE的value
print('FEMALE的value:', Gender.FEMALE.value)
# 访问自定义的cn_name属性
print('FEMALE的cn_name:', Gender.FEMALE.cn_name)
# 访问自定义的desc属性
print('FEMALE的desc:', Gender.FEMALE.desc)
"""
上面程序定义了 Gender 枚举类,并为它定义了一个构造器,调用该构造器需要传入 cn_name 和 desc 两个参数,
因此程序使用如下代码来定义 Gender 的枚举值。

    MALE = '男', '阳刚之力'
    FEMALE = '女', '柔顺之美'
    
上面代码为 MALE  枚举指定的value是'男'和'阳刚之力'这两个字符串,其实它们会被自动封装成元组后传给 MALE  的 value 属性;
而且此处传入的'男'和阳刚之力这两个参数值正好分别传给 cn_name 和 desc 两个参数。
简单来说,枚举的构造器需要几个参数,此处就必须指定几个值。
"""
