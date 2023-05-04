"""
为了使用 break 语句跳出嵌套循环的外层循环,可先定义bool类型的变量来标志是否需要跳出外层循环,
然后在内层循环、外层循环中分别使用两条break语句来实现。
"""
exit_flag = False
# 外层循环
for i in range(0, 5):
    # 内层循环
    for j in range(0, 3):
        print("i的值为: %d, j的值为: %d" % (i, j))
        if j == 1:
            exit_flag = True
            # 跳出里层循环
            break
    # 如果exit_flag为True,跳出外层循环
    if exit_flag:
        break
