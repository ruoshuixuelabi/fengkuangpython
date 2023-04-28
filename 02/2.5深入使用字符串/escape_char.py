"""
字符串是 Python 编程中最常用的类型之一,下面将会详细介绍字符串更深入的用法。

2.5.1 转义字符

前面已经提到,在字符串中可以使用反斜线进行转义;如果字符串本身包含反斜线,则需要使用"\\"表示,"\"就是转义字符。
Python 当然不会只支持这么几个转义字符,Python 支持的转义字符如表2.3所示。

\b 退格符
\n 换行符
\r 回车符
\t 制表符
\" 双引号
\' 单引号
\\ 反斜线
"""
# 掌握了上面的转义字符之后,下面在字符串中使用它们,例如如下代码
s = 'Hello\nCharlie\nGood\nMorning'
print(s)
# 也可以使用制表符进行分隔,例如如下代码
s2 = '商品名\t\t单价\t\t数量\t\t总价'
s3 = '疯狂Java讲义\t108\t\t2\t\t316'
print(s2)
print(s3)
