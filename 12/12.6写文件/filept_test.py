"""
如果以 r+、w、w+、a、a+ 模式打开文件,则都可以写入。需要指出的是,当以r+、w、w+模式打开文件时,文件指针位于文件开头处;
当以a、a+模式打开文件时,文件指针位于文件结尾处。

另外,需要说明的是,当以 w 或 w+模式打开文件时,程序会立即清空文件的内容。

12.6.1文件指针的概念

文件指针用于标明文件读写的位置。假如把文件看成一个水流,文件中每个数据(以 b 模式打开,每个数据就是一个字节;
以普通模式打开,每个数据就是一个字符)就相当于一个水滴,而文件指针就标明了文件将要读写哪个位置。

图12.3简单示意了文件指针的概念。

文件对象提供了以下方法来操作文件指针。
(1)seek(offset[,whence]):该方法把文件指针移动到指定位置。当 whence 为0时(这是默认值),表明从文件开头开始计算,
比如将offset设为3,就是将文件指针移动到第3处;当 whence  为 1 时,表明从指针当前位置开始计算,比如文件指针当前在第5处,
将offset设为3,就是将文件指针移动到第8处;当 whence 为2时,表明从文件结尾开始计算,比如将offset 设为-3,
表明将文件指针移动到文件结尾倒数第3处。
(2)tell(): 判断文件指针的位置。

此外,当程序使用文件对象读写数据时,文件指针会自动向后移动：读写了多少个数据,文件指针就自动向后移动多少个位置。

下面程序示范了文件指针操作。
"""
f = open('filept_test.py', 'rb')
# 判断文件指针的位置
print(f.tell())  # 0
# 将文件指针移动到3处
f.seek(3)
print(f.tell())  # 3
# 读取一个字节,文件指针自动后移1个数据
print(f.read(1))  # o
print(f.tell())  # 4
# 将文件指针移动到5处
f.seek(5)
print(f.tell())  # 5
# 将文件指针向后移动5个数据
f.seek(5, 1)
print(f.tell())  # 10
# 将文件指针移动到倒数第10处
f.seek(-10, 2)
print(f.tell())
print(f.read(1))  # d
"""
上面程序中粗体字代码示范了使用 seek()方法来移动文件指针,包括从文件开头、指针当前位置、文件结尾处开始计算。
运行上面程序,结合程序输出结果可以体会文件指针移动的效果。

当文件指针位于哪里时,程序就会读取哪个位置的数据;当程序读取多少个数据时,文件指针就会自动向后移动多少个位置。
"""
