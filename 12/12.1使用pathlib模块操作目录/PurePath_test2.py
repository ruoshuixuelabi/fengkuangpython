"""
PurePath 对象支持各种比较运算符,它们既可比较是否相等,也可比较大小------实际上就是比较它们的路径字符串。

提示：PurePath 只是代表特定平台的路径字符串,读者可以把它们看作包装后的字符串------它们的本质就是字符串

下面程序示范了PurePath对象的比较运算。
"""
from pathlib import *

# 比较两个Unix风格的路径,区分大小写
print(PurePosixPath('info') == PurePosixPath('INFO'))  # False
# 比较两个Windows风格的路径,不区分大小写
print(PureWindowsPath('info') == PureWindowsPath('INFO'))  # True
# Windows风格的路径不区分大小写
print(PureWindowsPath('INFO') in {PureWindowsPath('info')})  # True
# Unix风格的路径区分大小写,所以'D:'小于'c:'
print(PurePosixPath('D:') < PurePosixPath('c:'))  # True
# Windows风格的路径不区分大小写,所以'd:'(D:)大于'c:'
print(PureWindowsPath('D:') > PureWindowsPath('c:'))  # True

# 对于不同风格的 PurePath,它们依然可以比较是否相等(结果总是返回False),但不能比较大小,否则会引发错误。例如如下代码(程序清单同上)。
# 不同风格的路径可以判断是否相等(总不相等)
print(PureWindowsPath('crazyit') == PurePosixPath('crazyit'))  # False
# 不同风格的路径不能判断大小,否则会引发异常
# print(PureWindowsPath('info') < PurePosixPath('info')) # TypeError
"""
PurePath 对象支持斜杠(/)作为运算符,该运算符的作用是将多个路径连接起来。
不管是 UNIX 风格的路径,还是 Windows 风格的路径,都是使用斜杠作为连接运算符的(程序清单同上)。
"""
pp = PureWindowsPath('abc')
# 将多个路径拼起来(Windows风格的路径)
print(pp / 'xyz' / 'wawa')  # abc\xyz\wawa
pp = PurePosixPath('abc')
# 将多个路径拼起来(Unix风格的路径)
print(pp / 'xyz' / 'wawa')  # abc/xyz/wawa
pp2 = PurePosixPath('haha', 'hehe')
# 将pp、pp2两个路径连接起来
print(pp / pp2)  # abc/haha/hehe
"""
正如从上面程序中粗体字代码所看到的,程序将使用斜杠来连接多个 Windows 路径,连接完成后可以看到 Windows 路径的分隔符依然是反斜杠。

PurePath的本质其实就是字符串,因此程序可使用str()将它们恢复成字符串对象。
在恢复成字符串对象时会转换为对应平台风格的字符串。例如如下代码(程序清单同上)。
"""
pp = PureWindowsPath('abc', 'xyz', 'wawa')
print(str(pp))  # abc\xyz\wawa
pp = PurePosixPath('abc', 'xyz', 'wawa')
print(str(pp))  # abc/xyz/wawa
"""
上面程序在创建 PurePath 时传入的参数完全相同,但在创建 PureWindowsPath 对象后路径字符串使用反斜杠作为分隔符;
在创建 PurePosixPath 对象后路径字符串使用斜杠作为分隔符。
"""