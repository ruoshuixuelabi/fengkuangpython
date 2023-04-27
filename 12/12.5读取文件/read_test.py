"""
12.5	读取文件

Python既可使用文件对象的方法来读取文件,也可使用其他模块的函数来读取文件。

12.5.1	按字节或字符读取

文件对象提供了 read() 方法来按字节或字符读取文件内容,到底是读取字节还是字符,则取决于是否使用了 b 模式,如果使用了b 模式,
则每次读取一个字节;如果没有使用 b 模式,则每次读取一个字符。在调用该方法时可传入一个整数作为参数,用于指定最多读取多少个字节或字符。

例如,如下程序采用循环读取整个文件的内容。
"""
f = open("read_test.py", 'r', True)
try:
    while True:
        # 每次读取一个字符
        ch = f.read(1)
        # 如果没有读到数据,跳出循环
        if not ch: break
        # 输出ch
        print(ch, end='')
finally:
    f.close()
"""
上面程序采用循环依次读取每一个字符(因为程序没有使用 b 模式),每读取到一个字符,程序就输出该字符。

正如从上面程序所看到的,当程序读写完文件之后,推荐立即调用close()方法来关闭文件,这样可以避免资源泄露。

提示：如果需要更安全地关闭文件,推荐将关闭文件的 close()方法调用在 finally块中执行。例如,将上面程序改写为如下形式。

f = open("read_test.py", 'r', True)
try:
    while True:
        # 每次读取一个字符
        ch = f.read(1)
        # 如果没有读到数据,跳出循环
        if not ch: break
        # 输出ch
        print(ch, end='')
finally:
    f.close()
"""
