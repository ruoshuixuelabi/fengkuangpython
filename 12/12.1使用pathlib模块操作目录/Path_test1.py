"""
12.1.3	Path的 功 能 和 用 法

Path 是 PurePath 的子类,它除支持 PurePath 的各种操作、属性和方法之外,还会真正访问底层的文件系统,
包括判断Path对应的路径是否存在,获取Path对应路径的各种属性(如是否只读、是文件还是文件夹等),甚至可以对文件进行读写。

提示：PurePath 和 Path 最根本的区别在于：PurePath的本质依然是字符串,
而 Path 则会真正访问底层的文件路径,因此它提供了属性和方法来访问底层的文件系统。

关于 Path 的大量属性和方法本章不再详细列出,读者可参考 https://docs.python.org/3/library/pathlib.html 进行查阅。

Path同样提供了两个子类：PosixPath 和 WindowsPath, 其中前者代表 UNIX  风格的路径；后者代表 Windows 风格的路径。

Path对象包含了大量 is_xxx() 方法,用于判断该 Path 对应的路径是否为xxx。Path 包含一个 exists()方法,用于判断该Path对应的目录是否存在。

Path 还包含一个很常用的iterdir()方法,该方法可返回 Path 对应目录下的所有子目录和文件。
此外,Path还包含一个glob()方法,用于获取Path对应目录及其子目录下匹配指定模式的所有文件。
借助于glob()方法,可以非常方便地查找指定文件。

下面程序示范了Path 的简单用法。
"""
from pathlib import *

# 获取当前目录
p = Path('.')
# 遍历当前目录下所有文件和子目录
for x in p.iterdir():
    print(x)

# 获取上一级目录
p = Path('../')
# 获取上级目录及其所有子目录下的的py文件
for x in p.glob('**/*.py'):
    print(x)

# 获取g:/publish/codes对应的目录
p = Path('g:/publish/codes')
# 获取上级目录及其所有子目录下的的py文件
for x in p.glob('**/Path_test1.py'):
    print(x)

"""
上面程序中第一行粗体字代码调用了Path的 iterdir()方法,该方法将会返回当前目录下的所有文件和子目录;
第二行粗体字代码调用了 glob()方法,获取上一级目录及其所有子目录下的 *.py 文件;
第三行粗体字代码用于获取g:/publish/codes目录及其所有子目录下的 Path_test1.py文件。

从上面的输出结果来看,不管是遍历当前目录下的文件和子目录,还是搜索指定目录及其子目录, Path对象都能用一个方法搞定------
对于不少语言来说, Path 的 glob()方法所实现的功能,其他语言往往要通过递归才能实现,这可能就是 Python 的魅力所在。
"""