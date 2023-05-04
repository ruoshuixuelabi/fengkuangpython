"""
下面代码示范了通过lambda 表达式来调用 Python 内置的map()函数。
"""
# 传入计算平方的lambda表达式作为参数
x = map(lambda x1: x1 * x1, range(8))
print([e for e in x])  # [0, 1, 4, 9, 16, 25, 36, 49]
# 传入计算平方的lambda表达式作为参数
y = map(lambda y1: y1 * y1 if y1 % 2 == 0 else 0, range(8))
print([e for e in y])  # [0, 0, 4, 0, 16, 0, 36, 0]
