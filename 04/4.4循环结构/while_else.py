"""
4.4.6 循环使用else

Python 的循环都可以定义 else 代码块,当循环条件为 False 时,程序会执行 else 代码块。如下代码示范了为 while 循环定义 else 代码块。
"""
count_i = 0
while count_i < 5:
    print('count_i小于5: ', count_i)
    count_i += 1
else:
    print('count_i大于或等于5: ', count_i)
"""
从上面的运行过程来看,当循环条件 count_i <5 变成 False 时,程序执行了 while 循环的 else 代码块。

简单来说,程序在结束循环之前,会先执行else代码块。从这个角度来看,else代码块其实没 有太大的价值——
将 else 代码块直接放在循环体之外即可。也就是说,上面的循环其实可改为如下形式。
count_i   =   0
while  count_i <5:
    print('count i 小于5:',count_i)
    count_i +=1
print('count_i 大于或等于5:',count_i)

上面代码直接将 else 代码块放在 while 循环体之外,程序执行结果与使用 else 代码块的执行结果完全相同。
"""