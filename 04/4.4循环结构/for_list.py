"""
当然，也可按上面方法来遍历列表。例如，下面程序要计算列表中所有数值元素的总和、平均值。
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