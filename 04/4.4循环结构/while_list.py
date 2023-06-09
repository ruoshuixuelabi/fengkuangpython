"""
下面示范一个小程序,实现对一个整数列表的元素进行分类,能整除3的放入一个列表中;
除以3余1的放入另一个列表中;除以3余2的放入第三个列表中。
"""
src_list = [12, 45, 34, 13, 100, 24, 56, 74, 109]
a_list = []  # 定义保存整除3的元素
b_list = []  # 定义保存除以3余1的元素
c_list = []  # 定义保存除以3余2的元素
# 只要src_list还有元素,继续执行循环体
while len(src_list) > 0:
    # 弹出src_list最后一个元素
    ele = src_list.pop()
    # 如果ele % 2不等于0
    if ele % 3 == 0:
        a_list.append(ele)  # 添加元素
    elif ele % 3 == 1:
        b_list.append(ele)  # 添加元素
    else:
        c_list.append(ele)  # 添加元素
print("整除3:", a_list)
print("除以3余1:", b_list)
print("除以3余2:", c_list)
