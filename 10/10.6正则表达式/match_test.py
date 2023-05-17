"""
正则表达式(Regular Expression)用于描述一种字符串匹配的模式(Pattern),它可用于检查一个字符串是否含有某个子串,
也可用于从字符串中提取匹配的子串,或者对字符串中匹配的子串执行替换操作。

很多读者都会觉得正则表达式是非常神奇、高级的知识,实际上正则表达式确实是一种非常实用的工具。
但正则表达式的入门并不难,任意字符串都可以被当成正则表达式来使用,例如"abc",它也是一个正则表达式,只是它只能匹配"abc"字符串。

当然,如果正则表达式仅能匹配"abc"这样的字符串,那么正则表达式也就不值得学习了。
事实上,正则表达式包含的知识点比较多,它的模式匹配能力也非常强,初学者可以由浅入深地学习。

但对于 Python 开发者来说,掌握正则表达式确实是一个很重要的技能。在掌握了正则表达式之后,
Python 开发者也可使用正则表达式来开发数据抓取、网络爬虫等程序。
实际上,掌握 Python 的正则表达式并不难,无非就是几个简单的函数,因此下面先介绍 Python 的正则表达式支持。

10.6.1	Python 的正则表达式支持

在 Python 的交互式解释器中先导入re模块,然后输入 re.__all__ 命令,即可看到该模块所包含的全部属性和函数。
import re
re.__all__
['match', 'fullmatch', 'search', 'sub', 'subn', 'split', 'findall', 'finditer', 'compile', 'purge', 'template', 'escape', 'error',
'Pattern', 'Match', 'A', 'I', 'L', 'M', 'S', 'X', 'U', 'ASCII', 'IGNORECASE', 'LOCALE', 'MULTILINE', 'DOTALL', 'VERBOSE', 'UNICODE']

从上面的输出结果可以看出,re 模块包含了为数不多的几个函数和属性(用于控制正则表达式匹配的几个选项)。下面先介绍这些函数的作用。
(1)re.compile(pattern,flags=0):该函数用于将正则表达式字符串编译成 _sre.SRE_Pattern对象,
该对象代表了正则表达式编译之后在内存中的对象,它可以缓存并复用正则表达式字符串。
如果程序需要多次使用同一个正则表达式字符串,则可考虑先编译它。

该函数的 pattern 参数就是它所编译的正则表达式字符串,flags 则代表了正则表达式的匹配旗标。关于旗标的介绍请参考10.6.2节。

编译得到的 _sre.SRE_Pattern 对象包含了 re 模块中绝大部分函数对应的方法。
比如下面两行代码表示先编译正则表达式,然后调用正则表达式的search()方法执行匹配。
先编译正则表达式
p =  re.compile('abc')
调用 _sre.SRE_Pattern 对象的 search()方法
p.search("www.abc.com")
上面两行代码和下面代码的效果基本相同。
p.search("www.abc.com")

对于上面两种方式,由于第一种方式预编译了正则表达式,因此程序可复用 p 对象(该对象缓存了正则表达式字符串),所以具有更好的性能。

(2)re.match(pattern,string,flags=0)：尝试从字符串的开始位置来匹配正则表达式,如果从开始位置匹配不成功,match()函数就返回None。
其中 pattern 参数代表正则表达式;string 代表被匹配的字符串;flags 则代表正则表达式的匹配旗标。
该函数返回 _sre.SRE_Pattern 对象, 该对象包含的 span(n) 方法用于获取第 n+1 个组的匹配位置,
group(n)方法用于获取第 n+1 个组所匹配的子串。
(3)re.search(pattern,string,flags=0)：扫描整个字符串,并返回字符串中第一处匹配 pattern 的匹配对象。
其中 pattern 参数代表正则表达式;string 代表被匹配的字符串;flags 则代表正则表达式的匹配旗标。该函数也返回 _sre.SRE_Pattern 对象。

根据上面介绍不难发现,match()与 search()的区别在于：match()必须从字符串开始处就匹配,但 search()则可以搜索整个字符串。例如如下程序。
"""
import re

m1 = re.match('www', 'www.fkit.org')  # 开始位置可以匹配
print(m1.span())  # span返回匹配的位置
print(m1.group())  # group返回匹配的组
print(re.match('fkit', 'www.fkit.com'))  # 开始位置匹配不到,返回None
m2 = re.search('www', 'www.fkit.org')  # 开始位置可以匹配
print(m2.span())
print(m2.group())
m3 = re.search('fkit', 'www.fkit.com')  # 中间位置可以匹配,返回Match对象
print(m3.span())
print(m3.group())
"""
运行上面程序,可以看到如下输出结果。
(0, 3)
www
None
(0, 3)
www
(4, 8)
fkit

从上面的输出结果可以看出,match()函数要求必须从字符串开始处匹配,而 search()函数则可扫描整个字符串,从中间任意位置开始匹配。

(4)re.findall(pattern, string,flags=0)：扫描整个字符串,并返回字符串中所有匹配 pattern 的子串组成的列表。
其中 pattern 参数代表正则表达式;string 代表被匹配的字符串;flags 则代表正则表达式的匹配旗标。
(5)re.finditer(pattern, string,flags=0)：扫描整个字符串,并返回字符串中所有匹配 pattern 的子串组成的迭代器,
迭代器的元素是 _sre.SRE_Pattern 对象。其中 pattern 参数代表正则表达式;string 代表被匹配的字符串;flags 则代表正则表达式的匹配旗标。

从上面介绍不难看出,findall()与 finditer()函数的功能基本相似,区别在于它们的返回值不同,
findall()函数返回所有匹配patten的子串组成的列表;而 finditer()函数则返回所有匹配 pattern 的子串组成的迭代器。
"""