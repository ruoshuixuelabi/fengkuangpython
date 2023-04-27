"""
1.  I/O(输入/输出)是比较乏味的事情,因为看不到明显的运行效果;但I/O是所有程序都必需的部分——
使用输入机制,允许程序读取外部数据(包括来自磁盘、光盘等存储设备的数据),用户输入数据;
使用输出机制,允许程序记录运行状态,将程序数据输出到磁盘、光盘等存储设备中。

2.  Python提供了非常丰富的I/O支持,它既提供了 pathlib 和 os.path 来操作各种路径,也提供了全局的open()函数来打开文件——
在打开文件之后,程序既可读取文件的内容,也可向文件输出内容。而且 Python 提供了多种方式来读取文件内容,因此非常简单、灵活。
此外,在 Python 的 os 模块下也包含了大量进行文件I/O 的函数,使用这些函数来读取、写入文件也很方便,
因此读者可以根据需要选择不同的方式来读写文件。

3.  Python还提供了 tempfile 模块来创建临时文件和临时目录,tempfile模块下的高级API 会自动管理临时文件的创建和删除：
当程序不再使用临时文件和临时目录时,程序会自动删除临时文件和临时目录。

12.1	使用pathlib模块操作目录

4.  pathlib 模块提供了一组面向对象的类,这些类可代表各种操作系统上的路径,程序可通过这些类操作路径。 pathlib模块下的类如图12.1所示。
(1)PurePath:代表并不访问实际文件系统的"纯路径"。简单来说,PurePath 只是负责对路径字符串执行操作,
至于该字符串是否对应实际的路径,它并不关心。PurePath 有两个子类, 即 PurePosixPath 和 PureWindowsPath,
分别代表UNIX 风格的路径(包括Mac OS  X)和 Windows 风格的路径。
(2)Path:代表访问实际文件系统的"真正路径"。Path对象可用于判断对应的文件是否存在、是否为文件、是否为目录等。
Path同样有两个子类,即 PosixPath 和 WindowsPath。

提示：UNIX 风格的路径和 Windows 风格的路径的主要区别在于根路径和路径分隔符：
UNIX 风格的路径的根路径是斜杠(/),而Windows 风格的路径的根路径是盘符(c:);
UNIX 风格的路径的分隔符是斜杠(/),而Windows 风格的路径的分隔符是反斜杠(\)。

12.1.1  PurePath 的基本功能

程序可使用 PurePath 或它的两个子类来创建 PurePath 对象,如果在 UNIX 或 Mac OS X 系统上使用PurePath创建对象,
程序实际返回 PurePosixPath 对象;如果在 Windows 系统上使用 PurePath 创建对象,程序实际返回 PureWindowsPath 对象。

如果程序明确希望创建 PurePosixPath 或 PureWindowsPath 对象,则应该直接使用 PurePath 的子类。

程序在创建 PurePath和 Path 时,既可传入单个路径字符串,也可传入多个路径字符串,PurePath 会将它们拼接成一个字符串。例如如下程序。

"""
from pathlib import *

# 创建PurePath,实际上使用PureWindowsPath
pp = PurePath('setup.py')
print(type(pp))  # <class 'pathlib.PureWindowsPath'>
pp = PurePath('crazyit', 'some/path', 'info')
# 看到输出Windows风格的路径
print(pp)  # 'crazyit\some\path\info'
pp = PurePath(Path('crazyit'), Path('info'))
# 看到输出Windows风格的路径
print(pp)  # 'crazyit\info'
# 明确指定创建PurePosixPath
pp = PurePosixPath('crazyit', 'some/path', 'info')
# 看到输出Unix风格的路径
print(pp)  # crazyit/some/path/info
"""
如果在创建PurePath时不传入任何参数,系统默认创建代表当前路径的 PurePath,相当于传入点号(代表当前路径)作为参数。
"""
# 如果不传入参数,默认使用当前路径
pp = PurePath()
print(pp)  # .

# 如果传入参数包含多个根路径,则只有最后一个根路径及后面子路径生效
pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp)  # /usr/lib64
pp = PureWindowsPath('c:/Windows', 'd:info')
print(pp)  # d:info
# 需要说明的是,在 Windows 风格的路径中,只有盘符才能算根路径,仅有斜杠是不算的。例如如下代码(程序清单同上)。
# 在Windows风格路径中,只有盘符才算根路径
pp = PureWindowsPath('c:/Windows', '/Program Files')
print(pp)  # c:\Program Files
"""
 如果在创建 PurePath 时传入的路径字符串中包含多余的斜杠和点号,系统会直接忽略它们。
 但不会忽略两点,因为两点在路径中有实际意义(两点代表上一级路径)。例如如下代码(程序清单同上)。
"""
# 路径字符串中多出来的斜杠和点号(代表当前路径)都会被忽略
pp = PurePath('crazyit//info')
print(pp)  # crazyit\info
pp = PurePath('crazyit/./info')
print(pp)  # crazyit\info
pp = PurePath('crazyit/../info')
print(pp)  # crazyit\..\info,相当于找和crazyit同一级的info路径
