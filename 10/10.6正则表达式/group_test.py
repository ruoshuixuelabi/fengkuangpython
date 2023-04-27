"""
1.  re模块中的 Match 对象(其具体类型为 _sre.SRE_Match) 则是 match()、search()方法的返回值,
该对象中包含了详细的正则表达式匹配信息,包括正则表达式匹配的位置、正则表达式所匹配的子串。
2.  _sre.SRE_Match 对象包含了如下方法或属性。
(1)match.group([group1,…]): 获取该匹配对象中指定组所匹配的字符串。
(2)match.__getitem__(g):这是match.group(g)的简化写法。由于 match 对象提供了 __getitem__() 方法,
因此程序可使用match[g]来代替match.group(g)。
(3)match.groups(default=None):  返回 match 对象中所有组所匹配的字符串组成的元组。
(4)match.groupdict(default=None): 返回 match 对象中所有组所匹配的字符串组成的字典。
(5)match.start([group]): 获取该匹配对象中指定组所匹配的字符串的开始位置。
(6)match.end([group]): 获取该匹配对象中指定组所匹配的字符串的结束位置。
(7)match.span([group]): 获取该匹配对象中指定组所匹配的字符串的开始位置和结束位置。
该方法相当于同时返回start()和 end() 方法的返回值。

3.  上面这些方法都涉及了组的概念,组是正则表达式中很常见的一个东西：用圆括号将多个表达式括起来形成组。
如果正则表达式中没有圆括号,那么整个表达式就属于一个默认组。如下程序示范了正则表达式包含组的情形。
4.  上面程序中 search() 函数使用了一个正则表达式：r'(fkit).(org)',在该正则表达式内包含两个组,即(fkit)和(org),
因此程序可以依次获取group(0)、group(1)、group(2)的值——
也就是依次获取整个正则表达式所匹配的子串、第一个组所匹配的子串和第二个组所匹配的子串;
程序也可以依次获取span(0)、span(1)、span(2)的值——
也就是依次获取整个正则表达式所匹配的子串的开始位置和结束位置、第一个组所匹配的子串的开始位置和结束位置、
第二个组所匹配的子串的开始位置和结束位置。
5.  从该程序可以看出,只要正则表达式能匹配得到结果,则不管正则表达式是否包含组,group(0)、span(0) 总能获得内容,
因为它们分别是获取整个正则表达式所匹配的子串,以及该子串的开始位置和结束位置。
"""
import re

# 在正则表达式中使用组
m = re.search(r'(fkit).(org)', r"www.fkit.org is a good domain")
print(m.group(0))  # fkit.org
# 调用简化写法,底层是调用m.__getitem__(0)
print(m[0])  # fkit.org
print(m.span(0))  # (4, 12)
print(m.group(1))  # fkit
# 调用简化写法,底层是调用m.__getitem__(1)
print(m[1])  # fkit
print(m.span(1))  # (4, 8)
print(m.group(2))  # org
# 调用简化写法,底层是调用m.__getitem__(2)
print(m[2])  # org
print(m.span(2))  # (9, 12)
# 返回所有组所匹配的字符串组成的元组
print(m.groups())
# 如果在正则表达式中为组指定了名字(用?P<名字>为正则表达式的组指定名字),
# 就可以调用 groupdict()方法来获取所有组所匹配的字符串组成的字典——其中组名作为字典的 key。 例如如下代码。
# 正则表达式定义了2个组,并为组指定了名字
m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)', \
               r"www.fkit.org is a good domain")
# 上面程序为正则表达式的第一个组指定名字为 prefix, 为第二个组指定名字为suffix。 运行上面程序,可以看到如下输出结果。
print(m2.groupdict())  # {'prefix': 'fkit', 'suffix': 'org'}
# 从上面的输出结果可以看到,此处返回的字典的 key 为正则表达式中的组名, value为该组所匹配的子串。
# match.pos:  该属性返回传给正则表达式对象的 search()、match()等方法的 pos 参数。
# match.endpos:  该属性返回传给正则表达式对象的 search()、match()等方法的endpos 参数。
# match.lastindex: 该属性返回最后一个匹配的捕获组的整数索引。如果没有组匹配,该属性返回None。
# 例如用(a)b、((a)(b))或((ab))对字符串'ab'执行匹配,该属性都会返回1;但如果使用(a)(b)正则表达式对'ab'执行匹配,则lastindex等于2。
# match.lastgroup: 该属性返回最后一个匹配的捕获组的名字;如果该组没有名字或根本没有组匹配,该属性返回None。
# match.re：该属性返回执行正则表达式匹配时所用的正则表达式。
# match.string：该属性返回执行正则表达式匹配时所用的字符串。
