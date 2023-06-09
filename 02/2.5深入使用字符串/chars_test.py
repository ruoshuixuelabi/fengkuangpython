"""
2.5.3 序列相关方法

字符串本质上就是由多个字符组成的,因此程序允许通过索引来操作字符,比如获取指定索引处的字符,获取指定字符在字符串中的位置等。

Python 字符串直接在方括号([])中使用索引即可获取对应的字符,字符串中第一个字符的索引为0、第二个字符的索引为1,后面各字符依此类推。

此外,Python 也允许从后面开始计算索引,最后一个字符的索引为-1,倒数第二个字符的索引为-2…… 依此类推。
3. 除可获取单个字符之外,也可在方括号中使用范围来获取字符串的中间“一段”(被称为子串)。
4. 上面用法还允许省略起始索引或结束索引。如果省略起始索引,相当于从字符串开始处开始截取；
如果省略结束索引,相当于截取到字符串的结束处。
5. 此外, Python 字符串还支持用in运算符判断是否包含某个子串。
6. 如果要获取字符串的长度,则可调用Python 内置的len()函数。
7. 还可使用全局内置的min()和 max()函数获取字符串中最小字符和最大字符
"""
s = 'crazyit.org is very good'
# 获取s中索引2处的字符
print(s[2])  # 输出a
# 获取s中从右边开始,索引4处的字符
print(s[-4])  # 输出g
# 除可获取单个字符之外,也可在方括号中使用范围来获取字符串的中间"一段"(被称为子串)。
# 获取s中从索引3处到索引5处(不包含)的子串
print(s[3: 5])  # 输出zy
# 获取s中从索引3处到倒数第5个字符的子串
print(s[3: -5])  # 输出zyit.org is very
# 获取s中从倒数第6个字符到倒数第3个字符的子串
print(s[-6: -3])  # 输出y g
# 上面用法还允许省略起始索引或结束索引。如果省略起始索引,相当于从字符串开始处开始截取;
# 如果省略结束索引,相当于截取到字符串的结束处。
# 获取s中从索引5处到结束的子串
print(s[5:])  # 输出it.org is very good
# 获取s中从倒数第6个字符到结束的子串
print(s[-6:])  # 输出y good
# 获取s中从开始到索引5处的子串
print(s[: 5])  # 输出crazy
# 获取s中从开始到倒数第6个字符的子串
print(s[: -6])  # 输出crazyit.org is ver
# 此外,Python 字符串还支持用in运算符判断是否包含某个子串
# 判断s是否包含'very'子串
print('very' in s)  # True
print('fkit' in s)  # False
# 如果要获取字符串的长度,则可调用 Python 内置的len()函数
# 输出s的长度
print(len(s))  # 24
# 输出'test'的长度
print(len('test'))  # 4
# 还可使用全局内置的min()和 max()函数获取字符串中最小字符和最大字符
# 输出s字符串中最大的字符
print(max(s))  # z
# 输出s字符串中最大的字符
print(min(s))  # 空格
