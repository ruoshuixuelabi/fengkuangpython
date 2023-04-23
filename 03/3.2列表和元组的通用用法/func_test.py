"""
1.  Python提供了内置的len()、max()、min()全局函数来获取元组或列表的长度、最大值和最小值。
2.  由于max()、min()要对元组、列表中的元素比较大小，因此程序要求传给max()、min()函数的
元组、列表的元素必须是相同类型且可以比较大小。
"""
# 元素都是数值的元组
a_tuple = (20, 10, -2, 15.2, 102, 50)
# 计算最大值
print(max(a_tuple))  # 102
# 计算最小值
print(min(a_tuple))  # -2
# 计算长度
print(len(a_tuple))  # 6
# 元素都是字符串的列表
b_list = ['crazyit', 'fkit', 'Python', 'Kotlin']
# 计算最大值（依次比较每个字符的ASCII码值，先比较第一个字符，若相同，继续比较第二个字符，以此类推）
print(max(b_list))  # fkit（26个小写字母的ASCII码为97~122）
# 计算最小值
print(min(b_list))  # Kotlin （26个大写字母的ASCII码为65~90）
# 计算长度
print(len(b_list))  # 4
