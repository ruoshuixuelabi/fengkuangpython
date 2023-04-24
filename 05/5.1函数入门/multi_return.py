"""
1.  如果程序需要有多个返回值,则既可将多个值包装成列表之后返回,也可直接返回多个值。
如果Python函数直接返回多个值,Python 会自动将多个返回值封装成元组。
2.  如下程序示范了函数直接返回多个值的情形。
3.  上面程序中的粗体字代码返回了多个值,当①号代码调用该函数时,
该函数返回的多个值将会被自动封装成元组,因此程序看到tp是一个包含两个元素(由于被调用函数返回了两个值)的元组。
4.  此外,也可使用Python 提供的序列解包功能,直接使用多个变量接收函数返回的多个值。例如如下代码(程序清单同上)。
"""


def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        # 如果元素e是数值
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            sum += e
    return sum, sum / count


my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
# 获取sum_and_avg函数返回的多个值,多个返回值被封装成元组
tp = sum_and_avg(my_list)  # ①
print(tp)
# 使用序列解包来获取多个返回值
s, avg = sum_and_avg(my_list)  # ②
print(s)
print(avg)
