"""
循环的 else 代码块是 Python 的一个很特殊的语法(其他编程语言通常不支持),else 代码块的主要作用是便于生成更优雅的 Python 代码。

for 循环同样可使用 else 代码块,当 for 循环把区间、元组或列表的所有元素遍历一次之后,
for 循环会执行 else 代码块,在else代码块中,循环计数器的值依然等于最后一个元素的值。例如如下代码。
"""
a_list = [330, 1.4, 50, 'fkit', -3.5]
for ele in a_list:
    print('元素: ', ele)
else:
    # 访问循环计数器的值,依然等于最后一个元素的值
    print('else块: ', ele)
