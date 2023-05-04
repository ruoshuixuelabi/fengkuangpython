"""
4.4.3 for-in 循环

for-in循环专门用于遍历范围、列表、元素和字典等可迭代对象包含的元素。for-in循环的语法格式如下：
for 变量 in 字符串|范围|集合等：
    statements

对于上面的语法格式有两点说明。
(1)for-in 循环中的变量的值受for-in循环控制,该变量将会在每次循环开始时自动被赋值,因此程序不应该在循环中对该变量赋值。
(2)for-in 循环可用于遍历任何可迭代对象。所谓可迭代对象,就是指该对象中包含一个__iter__方法,且该方法的返回值对象具有next()方法。

for-in循环可用于遍历范围。例如,如下程序使用for-in循环来计算指定整数的阶乘。
"""
s_max = input("请输入您想计算的阶乘:")
mx = int(s_max)
result = 1
# 使用for-in循环遍历范围
for num in range(1, mx + 1):
    result *= num
print(result)
"""
上面程序将会根据用户输入的数字进行循环。假如用户输入7,此时程序将会构建一个range(1, 8)对象(不包含8),
因此for-in 循环将会自动循环7次,在每次循环开始时,num 都会被依次自动赋值为range所包含的每个元素。

for-in循环中的变量完全接受for-in循环控制,因此该变量也被称为循环计数器。
"""
