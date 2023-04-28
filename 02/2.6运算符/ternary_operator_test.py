"""
2.6.8 三目运算符

Python可通过if语句来实现三目运算符的功能,因此可以近似地把这种if语句当成三目运算符。作为三目运算符的if语句的语法格式如下：

True  statements       if       expression       else       False  statements

三目运算符的规则是：先对逻辑表达式expression求值,如果逻辑表达式返回True, 则执行并返回True statements 的值；
如果逻辑表达式返回False, 则执行并返回False statements的值。看如下代码。

Python 允许在三目运算符的True statements或 False statements中放置多条语句。 Python主要支持两种放置方式。
(1)多条语句以英文逗号隔开：每条语句都会执行,程序返回多条语句的返回值组成的元组。
(2)多条语句以英文分号隔开：每条语句都会执行,程序只返回第一条语句的返回值。
"""
a = 5
b = 3
st = "a大于b" if a > b else  "a不大于b"
# 输出"a大于b"
print(st)

# 输出"a大于b"
print("a大于b") if a > b else print("a不大于b")

# 第一个返回值部分使用两条语句,逗号隔开
st = print("crazyit"), 'a大于b' if a > b else  "a不大于b"
print(st)

# 第一个返回值部分使用两条语句,分号隔开
st = print("crazyit"); x = 20 if a > b else  "a不大于b"
print(st)
print(x)

c = 5
d = 5
# 下面将输出c等于d
print("c大于d") if c > d else (print("c小于d") if c < d else print("c等于d"))
