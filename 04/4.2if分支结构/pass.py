"""
4.2.6  if表达式

正如前面所介绍的,if 分支语句还可作为表达式,此时 if 表达式相当于其他语言中的三目运算符。
由于前面在介绍三目运算符时已经介绍了if表达式的用法,故此处不再详述。

4.2.7  pass 语句

很多程序都提供了"空语句"支持, Python 也不例外,Python 的 pass 语句就是空语句。

有时候程序需要占一个位、放一条语句,但又不希望这条语句做任何事情,此时就可通过 pass 语句来实现。

通过使用pass语句,可以让程序更完整。
"""
s = input("请输入一个整数: ")
s = int(s)
if s > 5:
    print("大于5")
elif s < 5:
    # 空语句,相当于占位符
    pass
else:
    print("等于5")
"""
正如从上面程序所看到的,对于 s 小于5的情形,程序暂时不想处理(或不知道如何处理),
此时程序就需要通过空语句来占一个位,这样即可使用 pass 语句了。
"""