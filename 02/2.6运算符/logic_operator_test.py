"""
2.6.7 逻辑运算符
1. 逻辑运算符用于操作 bool 类型的变量、常量或表达式，逻辑运算的返回值也是bool值。
2. Python的逻辑运算符有如下三个。
(1)and：与，前后两个操作数必须都是True 才返回True; 否则返回False。
(2)or：或，只要两个操作数中有一个是True, 就可以返回True; 否则返回False。
(3)not：非，只需要一个操作数，如果操作数为True, 则返回False; 如果操作数为False, 则返回True。
"""
# 直接对False求非运算，将返回True
print(not False)
# 5>3返回True，20.0大于10，因此结果返回True
print(5 > 3 and 20.0 > 10)
# 4>=5返回False，"c">"a"返回True。求或后返回True
print(4 >= 5 or "c" > "a")
