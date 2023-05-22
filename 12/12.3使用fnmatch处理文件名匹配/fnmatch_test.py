"""
前面介绍的那些操作目录的函数只能进行简单的模式匹配,但 fnmatch 模块可以支持类似于 UNIX shell风格的文件名匹配。

fnmatch匹配支持如下通配符。
*：可匹配任意个任意字符。
?：可匹配一个任意字符。
[字符序列]：可匹配中括号里字符序列中的任意字符。该字符序列也支持中画线表示法。比如[a-c]可代表a、b 和 c 字符中任意一个。
[!字符序列]：可匹配不在中括号里字符序列中的任意字符。

在该模块下提供了如下函数。
fnmatch.fnmatch(filename, pattern)：判断指定文件名是否匹配指定pattern。
fnmatch.fnmatchcase(filename, pattern)：该函数与上一个函数的功能大致相同,只是该函数区分大小写。
fnmatch.filter(names,pattern)：该函数对 names 列表进行过滤,返回 names 列表中匹配 pattern 的文件名组成的子集合。
fnmatch.translate(pattern)：该函数用于将一个 UNIX shell 风格的 pattern 转换为正则表达式 pattern。

如下程序示范了fnmatch()函数的用法。
"""
from pathlib import *
import fnmatch

# 遍历当前目录下所有文件和子目录
for file in Path('.').iterdir():
    # 访问所有以_test.py结尾的文件
    if fnmatch.fnmatch(file, '*_test.PY'):
        print(file)
# 上面程序先遍历当前目录下的所有文件和子目录,然后粗体字代码调用 fnmatch()函数判断所有以 test.py结尾的文件,并将该文件打印出来。
names = ['a.py', 'b.py', 'c.py', 'd.py']
# 对names列表进行过滤
sub = fnmatch.filter(names, '[ac].py')
print(sub)  # ['a.py', 'c.py']

print(fnmatch.translate('?.py'))  # (?s:.\.py)\Z
print(fnmatch.translate('[ac].py'))  # (?s:[ac]\.py)\Z
print(fnmatch.translate('[a-c].py'))  # (?s:[a-c]\.py)\Z
