"""
4.5.2   使用continue忽略本次循环的剩下语句
1.  continue 的功能和break有点类似,区别是continue只是忽略当次循环的剩下语句,接着开始下一次循环,并不会中止循环；
而break则是完全中止循环本身。如下程序示范了continue的用法。
2.  从上面的运行结果来看,当i等于1时,程序没有输出"continue后的输出语句"字符串,
因为程序执行到 continue 时,忽略了当次循环中 continue 语句后的代码。
从这个意义上看,如果把一条 continue语句放在当次循环的最后一行,那么这条continue语句是没有任何意义的—— 
因为它仅仅忽略了一片空白,没有忽略任何程序语句。
"""
# 一个简单的for循环
for i in range(0, 3 ) :
    print("i的值是: ", i)
    if i == 1 :
        # 忽略本次循环的剩下语句
        continue
    print("continue后的输出语句")