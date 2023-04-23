"""
2.5.4 大小写相关方法
1. Python字符串由内建的str类代表，那么str类包含哪些方法呢?
Python 非常方便，它甚至不需要用户查询文档，Python 是“自带文档”的。此处需要读者简单掌握两个帮助函数。
(1)dir():列出指定类或模块包含的全部内容(包括函数、方法、类、变量等)。
(2)help():查看某个函数或方法的帮助文档。
"""
a = 'our domain is crazyit.org'
# 每个单词首字母大写
print(a.title())
# 每个单词首字母小写
print(a.lower())
# 每个单词首字母大写
print(a.upper())

