"""
12.5.6	使用 with 语句

在前面的程序中,我们都采用了程序主动关闭文件的方式。实际上,Python 提供了 with 语句来管理资源关闭。
比如可以把打开的文件放在with语句中,这样with语句就会帮我们自动关闭文件。

with语句的语法格式如下：
with  context_expression [as  target(s)]:
    with 代码块

在上面的语法格式中,context_expression 用于创建可自动关闭的资源。

例如,程序使用with语句来读取文件。
"""
import codecs

# 使用with语句打开文件,该语句会负责关闭文件
with codecs.open("readlines_test.py", 'r', 'utf-8', buffering=True) as f:
    for line in f:
        print(line, end='')
"""
在上面的语法格式中,context_expression 用于创建可自动关闭的资源。
"""