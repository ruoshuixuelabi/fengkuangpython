"""
2.5.5  删除空白

str还提供了如下常用的方法来删除空白。
(1)strip()：删除字符串前后的空白。
(2)lstrip)：删除字符串前面(左边)的空白。
(3)rstrip()：删除字符串后面(右边)的空白。

需要说明的是,Python 的 str 是不可变的(不可变的意思是指,字符串一旦形成,它所包含的字符序列就不能发生任何改变),
因此这三个方法只是返回字符串前面或后面空白被删除之后的副本,并没有真正改变字符串本身。

如果在交互式解释器中输入help(str.lstrip)来查看lstrip()方法的帮助信息,则可看到如下输出结果。

从上面介绍可以看出,lstrip()方法默认删除字符串左边的空白,但如果为该方法传入指定参数,则可删除该字符串左边的指定字符。
如下代码示范了上面方法的用法。
"""
s = '  this is a puppy  '
# 删除左边的空白
print(s.lstrip())
# 删除右边的空白
print(s.rstrip())
# 删除两边的空白
print(s.strip())
# 再次输出s,将会看到s并没有改变
print(s)
s2 = 'i think it is a scarecrow'
# 删除左边的i、t、o、w字符
print(s2.lstrip('itow'))
# 删除右边的i、t、o、w字符
print(s2.rstrip('itow'))
# 删除两边的i、t、o、w字符
print(s2.strip('itow'))
