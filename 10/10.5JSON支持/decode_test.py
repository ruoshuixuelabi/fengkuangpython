"""
正如从上面程序中粗体字代码所看到的,程序调用 json.JSONEncoder 对象的 encode()方法也可以将 Python 对象转换为 JSON 字符串。
而 dumps() 和 dump() 函数是更高级的调用方式,一般调用 dumps()和 dump() 函数对 Python 对象执行转换即可。

下面程序示范了loads()和 load()函数的 decode 操作(将 JSON 字符串转换成 Python 对象)。
"""
import json

# 将JSON字符串恢复成Python列表
result1 = json.loads('["yeeku", {"favorite": ["coding", null, "game", 25]}]')
print(result1)  # ['yeeku', {'favorite': ['coding', None, 'game', 25]}]
# 将JSON字符串恢复成Python字符串
result2 = json.loads('"\\"foo\\"bar"')
print(result2)  # "foo"bar


# 定义一个自定义的转化函数
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


# 使用自定义的恢复函数
# 自定义回复函数将real数据转成复数的实部,将imag转成复数的虚部
result3 = json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
print(result3)  # (1+2j)
f = open('a.json')
# 从文件流恢复JSON列表
result4 = json.load(f)
print(result4)  # ['Kotlin', {'Python': 'excellent'}]
"""
上面程序开始调用 loads() 函数从 JSON 字符串恢复 Python 列表、 Python 字符串等。接下来程序示范了一个比较特殊的例子------
程序定义了一个自定义的恢复函数,该函数负责将一个原本应该恢复成 dict 对象的 JSON 字符串恢复成复数,
并负责将字典中real对应的值转换成复数的实部,将字典中 imag 对应的值转换成复数的虚部。

通过使用自定义的恢复函数,可以完成 JSON 类型到 Python 特殊类型(如复数、矩阵)的转换。

上面程序最后使用 load()函数示范了从文件流来恢复 JSON 列表。运行上面程序,可以看到如下输出结果。
"""
