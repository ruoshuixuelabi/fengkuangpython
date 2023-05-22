"""
12.5.5	管道输入

从上面的示例看到,系统标准输入 sys.stdin 也是一个类文件对象,因此,Python 程序可以通过 sys.stdin 来读取键盘输入。
但在某些时候,Python 程序希望读取的输入不是来自用户,而是来自某个命令,此时就需要使用管道输入了。

管道的作用在于：将前一个命令的输出,当成下一个命令的输入。不管是 UNIX 系统(包括 Mac OS X)还是 Windows 系统,它们都支持管道输入。
管道输入的语法如下：
cmd1  |  cmd2  |  cmd3 ...

上面语法的作用是：cmd1 命令的输出,将会传给 cmd2 命令作为输入;cmd2 命令的输入,又会传给 cmd3 命令作为输出。

下面的 Python 程序用于读取 sys.stdin 的输入,并通过正则表达式识别其中包含多少个 E-mail 地址。
"""
import sys
import re

# 定义匹配Email的正则表达式
mailPattern = r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+' \
              + '[\.][a-z]{2,3}([\.][a-z]{2})?'
# 读取标准输入
text = sys.stdin.read()
# 使用正则表达式执行查找
it = re.finditer(mailPattern, text, re.I)
# 输出所有的电子邮件
for e in it:
    print(str(e.span()) + "-->" + e.group())
"""
上面程序中粗体字代码使用 sys.stdin 来读取标准输入的内容,并使用正则表达式匹配所读取字符串中的 E-mail 地址。

如果程序使用管道输入的方式,就可以把前一个命令的输出当成 pipein_test.py 这个程序的输入。例如使用如下命令。
type   ad.txt  |  python  pipein_test.py

上面的管道命令由两个命令组成。
(1)type ad.txt：该命令使用 type 读取 ad.txt 文件的内容,并将文件内容输出到控制台。
但由于使用了管道,因此该命令的输出会传给下一个命令。
(2)python pipein_test.py：该命令使用python执行 pipein_test.py程序。由于该命令前面有管道,因此它会把前一个命令的输出当成输入。

前面命令读取的ad.txt文件内容如下：
我有一台二手电脑要出售，联系者请发邮件到sun@heaven.com，尽快联系。
我要租房，联系者请发邮件到bai@crazyit.org，价格2000元左右。
谁要找工作，请将简历发送到zhu@fkit.org。
刚来广州，想交个朋友，联系者请发邮件到niu@yao.com。

运行上面的type ad.txt | python pipein_test.py 命令,pipein_test.py程序将会把 ad.xt 文件的内容作为标准输入。程序运行的结果如下：
(20, 34)-->sun@heaven.com
(54, 69)-->bai@crazyit.org
(94, 106)-->zhu@fkit.org
(127, 138)-->niu@yao.com
"""