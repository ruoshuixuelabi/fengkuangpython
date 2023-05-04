"""
当然,也可按上面方法来遍历列表。例如,下面程序要计算列表中所有数值元素的总和、平均值。
"""
src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crazyit', 109.5]
my_sum = 0
my_count = 0
for ele in src_list:
    # 如果该元素是整数或浮点数
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        # 累加该元素
        my_sum += ele
        # 数值元素的个数加1
        my_count += 1
print('总和:', my_sum)
print('平均数:', my_sum / my_count)
"""
上面程序使用 for-in 循环遍历列表的元素,并对几何元素进行判断：只有当列表元素是数值(int、float) 时,
程序才会累加它们,这样就可以计算出列表中数值元素的总和。

上面程序使用了 Python 的 isinstance() 函数,该函数用于判断某个变量是否为指定类型的实例,
其中前一个参数是要判断的变量,后一个参数是类型。我们可以在 Python 的交互式解释器中测试该函数的功能。例如如下运行过程。
isinstance(2,int)
True
isinstance('a',int)
False
isinstance('a',str)
True

从上面的运行过程可以看出,使用isinstance()函数判断变量是否为指定类型非常方便、有效。
"""