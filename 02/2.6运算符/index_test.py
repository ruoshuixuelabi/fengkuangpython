"""
2.6.4 扩展后的赋值运算符
1. 赋值运算符可以与算术运算符、位运算符等结合,扩展成功能更加强大的运算符。扩展后的赋值运算符如下。
(1) +=：对于x+=y, 即对应于x=x+y。
(2) -=：对于x-=y, 即对应于x=x-y。
(3) *=:对于x*=y, 即对应于x=x*y。
(4) /=:对于x/=y, 即对应于x=x/y。
(5) //=: 对于x//=y, 即对应于x=x//y。
(6) %= : 对 于 x%=y, 即对应于x=x%y。
(7) **=:对于x**=y, 即对应于x=x**y。
(8) &= : 对 于 x & =y, 即对应于x=x&y。
(9) |=:对于x |= y, 即对应于x=x|y。
(10) ^=:对于x ^= y, 即对应于x=x^y。
(11) <<=:对于x <<= y, 即对应于x=x<<y。
(12) >>=:对于x >>= y, 即对应于x=x>>y
只要能使用扩展后的赋值运算符,通常都推荐使用这种赋值运算符。
2.6.5 索引运算符
2. 前面介绍字符串时已经使用了索引运算符,索引运算符就是方括号,在方括号中既可使用单个索引值,也可使用索引范围。
实际上,在使用索引范围时,还可指定步长。下面代码示范了在索引范围中指定步长的用法。
"""
a = 'abcdefghijklmn'
# 获取索引2到索引8的子串,步长为3
print(a[2:8:3])  # 输出cf
# 获取索引2到索引8的子串,步长为2
print(a[2:8:2])  # 输出ceg
