"""
1.  对于 if 分支,还有一个很容易出现的逻辑错误,这个逻辑错误并不属于语法问题,但引起错误的可能性更大。看下面程序。
2.  从表面上看,上面的程序没有任何问题：人的年龄大于20岁是青年人,年龄大于40岁是中年人,年龄大于60岁是老年人。
但运行上面程序,就会发现打印结果是：青年人。而实际上希望45 岁应被判断为中年人——这显然出现了一个问题。
"""
age = 45
if age > 60:
    print("老年人")
elif age > 40:
    print("中年人")
elif age > 20:
    print("青年人")
