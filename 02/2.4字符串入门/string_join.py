"""
2.4.2   拼接字符串

如果直接将两个字符串紧挨着写在一起,Python 就会自动拼接它们,例如如下代码。
s1 = "Hello,"  'Charlie'
print(s1)

上面代码将会输出：
Hello,Charlie

上面这种写法只是书写字符串的一种特殊方法,并不能真正用于拼接字符串。
Python 使用加号(+)作为字符串的拼接运算符,例如如下代码。
"""
s1 = "Hello,"  'Charlie'
print(s1)
s2 = "Python "
s3 = "is Funny"
# 使用+拼接字符串
s4 = s2 + s3
print(s4)
