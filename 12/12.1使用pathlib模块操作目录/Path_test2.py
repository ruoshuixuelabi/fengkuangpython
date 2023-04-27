"""
此外,Path 还提供了read_bytes()和 read_text(encoding=None,errors=None)方法,
分别用于读取该 Path 对应文件的字节数据(二进制数据)和文本数据;
也提供了 write_bytes(data)和 Path.write_text(data,encoding=None,errors=None)方法来输出字节数据(二进制数据)和文本数据。

下面程序示范了使用Path来读写文件。
"""
from pathlib import *

p = Path('a_test.txt')
# 以GBK字符集输出文本内容
result = p.write_text('''有一个美丽的新世界
它在远方等我
那里有天真的孩子
还有姑娘的酒窝''', encoding='GBK')
# 返回输出的字符数
print(result)

# 指定以GBK字符集读取文本内容
content = p.read_text(encoding='GBK')
# 输出读取的文本内容
print(content)

# 读取字节内容
bb = p.read_bytes()
print(bb)
"""
上面程序中第一行粗体字代码使用 GBK 字符集调用write_text()方法输出字符串内容,该方法将会返回实际输出的字符个数;
第二行粗体字代码使用 GBK 字符集读取文件的字符串内容,该方法将会返回整个文件的内容,也就是刚刚输出的内容。
"""
