"""
2.4.3 repr和字符串

有时候,我们需要将字符串与数值进行拼接,而 Python 不允许直接拼接数值和字符串,程序必须先将数值转换成字符串。

为了将数值转换成字符串,可以使用 str() 或 repr() 函数,例如如下代码。
"""
s1 = "这本书的价格是："
p = 99.8
# 字符串直接拼接数值,程序报错
# print(s1 + p)
# 使用str()将数值转换成字符串
print(s1 + str(p))
# 使用repr()将数值转换成字符串
print(s1 + repr(p))
st = "I will play my fife"
print(st)
print(repr(st))
"""
上面程序中粗体字代码直接拼接字符串和数值,程序会报错。

str() 和 repr() 函数都可以将数值转换成字符串,其中 str 本身是 Python 内置的类型(和int、float一样),而 repr() 则只是一个函数。
此外,repr 还有一个功能,它会以 Python 表达式的形式来表示值。对比如下两行粗体字代码。
print(st)   #  I will play my fife
print(repr(st)) #  'I will play my fife'


通过下面的输出结果可以看出,如果直接使用 print() 函数输出字符串,将只能看到字符串的内容,没有引号;

但如果先使用 repr() 函数对字符串进行处理,然后再使用 print() 执行输出,将可以看到带引号的字符串——这就是字符串的 Python 的表达式形式

在交互式解释器中输入一个变量或表达式时,Python 会自动使用 repr() 函数处理该变量或表达式。
"""
