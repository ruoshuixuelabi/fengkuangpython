"""
defaultdict 是 dict 的子类,因此 defaultdict 也可被当成 dict 来使用,dict 支持的功能,defaultdict 基本都支持。
但它与 dict 最大的区别在于：如果程序试图根据不存在的 key 来访问 dict 中对应的 value,则会引发 KeyError 异常;
而 defaultdict 则可以提供一个 default_factory 属性,该属性所指定的函数负责为不存在的 key 来生成value。

通过下面程序进行对比。
"""
from collections import defaultdict

my_dict = {}
# 使用 int 作为 defaultdict 的 default_factory,将 key 不存在时,将会返回int()函数的返回值
my_defaultdict = defaultdict(int)
print(my_defaultdict['a'])  # 0
print(my_dict['a'])  # KeyError
"""
上面程序分别创建了空的 dict 对象和 defaultdict 对象,当程序试图访问 defaultdict 中不存在的 key 对应的value时,
程序输出 defaultdict 的 default_factory属性(int 函数)的返回值：0;
如果程序试图访问dict中不存在的 key 对应的value, 就会引发 KeyError 异常。
"""