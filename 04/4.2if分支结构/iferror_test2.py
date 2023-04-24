"""
运行程序，得到了正确结果。实际上，上面程序等同于下面程序。
"""
age = 45
if age > 20:
    print("青年人")
# 在原本的if条件中增加了else的隐含条件
if age > 40 and not (age > 20):
    print("中年人")
# 在原本的if条件中增加了else的隐含条件
if age > 60 and not (age > 20) and not (age > 40 and not (age > 20)):
    print("老年人")
