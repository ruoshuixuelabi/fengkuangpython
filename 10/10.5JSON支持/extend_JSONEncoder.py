"""
此外,我们还需要考虑一个问题：Python 支持更多的 JSON 所不支持的类型,比如复数、矩阵等,
如果直接使用 dumps() 或 dump() 函数进行转换,程序肯定会出问题。
此时就需要开发者对 JSONEncoder 类进行扩展,通过这种扩展来完成从 Python 特殊类型到 JSON 类型的转换。

例如,如下程序示范了通过扩展 JSONEncoder 来实现从 Python 复数到 JSON 字符串的转换。
"""
import json


# 定义JSONEncoder的子类
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        # 如果要转换的对象是复数类型,程序负责处理
        if isinstance(obj, complex):
            return {"__complex__": 'true', 'real': obj.real, 'imag': obj.imag}
        # 对于其他类型,还使用JSONEncoder的默认处理
        return json.JSONEncoder.default(self, obj)


s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
print(s1)  # '{"__complex__": "true", "real": 2.0, "imag": 1.0}'
s2 = ComplexEncoder().encode(2 + 1j)
print(s2)  # '{"__complex__": "true", "real": 2.0, "imag": 1.0}'
"""
上面程序扩展了 JSONEncoder 类的子类,并重写了它的 default()方法,在方法中判断如果要转换的目标类型是复数(complex),
程序就会进行自定义转换——将复数转换成JSON对象,且该对 象包含"__complex__":'true'属性。

一旦扩展了JSONEncoder 的子类之后,程序有两种方式来使用自定义的子类。
在 dumps()或 dump (函数中通过cls属性指定使用JSONEncoder 的自定义子类。
直 接 使 用JSONEncoder 的自定义子类的encode()方法来执行转换。
运行该程序,可以看到如下输出结果。
"""