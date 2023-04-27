"""
如果在调用read()方法时不传入参数,该方法默认会读取全部文件内容。例如如下程序。

通过上面两个程序,读者可能已经发现了一个问题：当使用open()函数打开文本文件时,
程序使用的是哪种字符集呢?总是使用当前操作系统的字符集,比如 Windows 平台,open()函数总是使用 GBK 字符集。
因此,上面程序读取的test.txt也必须使用 GBK  字符集保存;否则,程序就会出现 UnicodeDecodeError 错误。
"""
f = open("test.txt", 'r', True)
# 直接读取全部文件
print(f.read())
f.close()
