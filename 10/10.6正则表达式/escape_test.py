"""
(1)re.purge(): 清除正则表达式缓存。
(2)re.escape(pattern): 对模式中除ASCII字符、数值、下画线(_)之外的其他字符进行转义。 如下程序示范了escape()函数的用法。
从上面的输出结果可以看出,使用 escape()函数对模式执行转义之后,
模式中除 ASCII 字符、数值、下画线(_)之外的其他字符都被添加了反斜线进行转义。
此外,在re模块中还包含两个类,它们分别是正则表达式对象(其具体类型为 _sre.SRE_Pattern)和匹配(Match)对象,
其中正则表达式对象就是调用re.compile()函数的返回值。该对象的方法与前面介绍的re模块中的函数大致对应。
"""
import re

# 对模式中特殊字符进行转义
print(re.escape(r'www.crazyit.org is good, i love it!'))
# 输出：www\.crazyit\.org\ is\ good\,\ i\ love\ it\!
print(re.escape(r'A-Zand0-9?'))
# 输出：A\-Zand0\-9\?
