"""
1.  断言语句和if分支有点类似，它用于对一个bool表达式进行断言，如果该bool表达式为True, 该程序可以继续向下执行；
否则程序会引发AssertionError错误。
2.  从下面的运行过程可以看出，断言也可以对逻辑表达式进行判断，因此实际上断言也相当于一种特殊的分支。
"""
s_age = input("请输入您的年龄:")
age = int(s_age)
assert 20 < age < 80
print("您输入的年龄在20和80之间")