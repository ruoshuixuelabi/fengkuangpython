"""
下面程序使用codecs 模块的open()函数来打开文件,此时可以显式指定字符集。
"""
import codecs

# 指定使用utf-8字符集读取文件内容
f = codecs.open("read_test4.py", 'r', 'utf-8', buffering=True)
while True:
    # 每次读取一个字符
    ch = f.read(1)
    # 如果没有读到数据,跳出循环
    if not ch: break
    # 输出ch
    print(ch, end='')
f.close()
"""
上面程序中粗体字代码在调用open()函数时显式指定使用UTF-8 字符集,这样程序在读取文件内容时就完全没有问题了。
"""