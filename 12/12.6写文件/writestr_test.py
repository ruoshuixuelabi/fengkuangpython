"""
文件对象提供的写文件的方法主要有两个。
(1)write(str 或 bytes): 输出字符串或字节串。只有以二进制模式(b 模式)打开的文件才能写入字节串。
(2)writelines(可迭代对象):输出多个字符串或多个字节串。

下面程序示范了使用write()和 writelines()输出字符串。
"""
import os

f = open('x.txt', 'w+')
# os.linesep代表当前操作系统上的换行符
f.write('我爱Python' + os.linesep)
f.writelines(('土门壁甚坚，' + os.linesep,
              '杏园度亦难。' + os.linesep,
              '势异邺城下，' + os.linesep,
              '纵死时犹宽。' + os.linesep))
"""
上面程序中第一行粗体字代码调用 write()方法输出单个字符串;第二行粗体字代码则调用 writelines()方法输出多个字符串。
"""
