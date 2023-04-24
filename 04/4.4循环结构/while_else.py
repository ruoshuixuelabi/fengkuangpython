"""
4.4.6 循环使用else
1.  Python 的循环都可以定义else代码块,当循环条件为False时,程序会执行else代码块。如下代码示范了为while循环定义else代码块。
"""
count_i = 0
while count_i < 5:
    print('count_i小于5: ', count_i) 
    count_i += 1
else:
    print('count_i大于或等于5: ', count_i) 
    