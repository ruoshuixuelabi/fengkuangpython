"""
4.4 循环结构
1.  循环语句可以在满足循环条件的情况下,反复执行某一段代码,这段被重复执行的代码被称为循环体。
当反复执行这个循环体时,需要在合适的时候把循环条件改为假,从而结束循环；否则循环将一直执行下去,形成死循环。
循环语句可能包含如下4个部分。
(1)初始化语句(init statements):一条或多条语句,用于完成一些初始化工作。初始化语句在循环开始之前执行。
(2)循环条件(test expression): 这是一个布尔表达式,这个表达式能决定是否执行循环体。
(3)循环体(body statements): 这个部分是循环的主体,如果循环条件允许,这个代码块将被重复执行。
(4)迭代语句(iteration statements): 这个部分在一次执行循环体结束后,对循环条件求值之前执行,
通常用于控制循环条件中的变量,使得循环在合适的时候结束。
上面4个部分只是一般分类,并不是每个循环中都非常清晰地分出这4个部分。

4.4.1 while  循 环

2.  while循环的语法格式如下：
[init  statements]
while  test_expression:
    body  statements
    [iteration_statements]
3.  while循环在每次执行循环体之前,都要先对 test_expression 循环条件求值,如果循环条件为真,则运行循环体部分。
从上面的语法格式来看,迭代语句 iteration_statements 总是位于循环体的最后,因此只有当循环体能成功执行完成时,
while循环才会执行迭代语句 iteration_statements。
4.  从这个意义上看,while循环也可被当成分支语句使用——如果test expression条件一开始就为假,则循环体部分将永远不会获得执行的机会。
下面程序示范了一个简单的while循环。
5.  在使用while循环时,一定要保证循环条件有变成假的时候；否则这个循环将成为一个死循环,永远无法结束这个循环。
"""
# 循环的初始化条件
count_i = 0
# 当count_i小于10时,执行循环体
while count_i < 10:
    print("count:", count_i)
    # 迭代语句
    count_i += 1
print("循环结束!")

# 下面是一个死循环
count_i2 = 0
while count_i2 < 10:
    print("不停执行的死循环:", count_i2)
    count_i2 -= 1
print("永远无法跳出的循环体")
