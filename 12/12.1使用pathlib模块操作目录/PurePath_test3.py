"""
12.1.2	PurePath的属性和方法

PurePath 提供了不少属性和方法,这些属性和方法主要还是用于操作路径字符串。
由于 PurePath 并不真正执行底层的文件操作,也不理会路径字符串在底层是否有对应的路径,因此这些操作有点类似于字符串方法。
(1)PurePath.parts:该属性返回路径字符串中所包含的各部分。
(2)PurePath.drive:该属性返回路径字符串中的驱动器盘符。
(3)PurePath.root:该属性返回路径字符串中的根路径。
(4)PurePath.anchor:该属性返回路径字符串中的盘符和根路径。
(5)PurePath.parents:该属性返回当前路径的全部父路径。
(6)PurePath.parent:该属性返回当前路径的上一级路径,相当于parents[0]的返回值。
(7)PurePath.name:该属性返回当前路径中的文件名。
(8)PurePath.suffixes:该属性返回当前路径中的文件所有后缀名。
(9)PurePath.suffix:该属性返回当前路径中的文件后缀名。相当于suffixes属性返回的列表的最后一个元素。
(10)PurePath.stem:该属性返回当前路径中的主文件名
(11.1 Python的 GUI 库)PurePath.as posix(): 将当前路径转换成UNIX 风格的路径。
(12)PurePath.as uri(): 将当前路径转换成URI。 只有绝对路径才能转换,否则将会引发ValueError。
(13)PurePath.is_absolute(): 判断当前路径是否为绝对路径。
(14)PurePath.joinpath(*other): 将多个路径连接在一起,作用类似于前面介绍的斜杠运算符。
(15)PurePath.match(pattern): 判断当前路径是否匹配指定通配符。
(16)PurePath.relative_to(*other): 获取当前路径中去除基准路径之后的结果。
(17)PurePath.with_name(name):将当前路径中的文件名替换成新文件名。如果当前路径中没有 文件名,则会引发ValueError。
(18)PurePath.with_suffix(suffix):将当前路径中的文件后缀名替换成新的后缀名。如果当前路径中没有后缀名,则会添加新的后缀名。

下面程序大致测试了上面属性和方法的用法。
"""
from pathlib import *

# 访问drive属性
print(PureWindowsPath('c:/Program Files/').drive)  # c:
print(PureWindowsPath('/Program Files/').drive)  # ''
print(PurePosixPath('/etc').drive)  # ''

# 访问root属性
print(PureWindowsPath('c:/Program Files/').root)  # \
print(PureWindowsPath('c:Program Files/').root)  # ''
print(PurePosixPath('/etc').root)  # /

# 访问anchor属性
print(PureWindowsPath('c:/Program Files/').anchor)  # c:\
print(PureWindowsPath('c:Program Files/').anchor)  # c:
print(PurePosixPath('/etc').anchor)  # /

# 访问parents属性
pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0])  # abc\xyz\wawa
print(pp.parents[1])  # abc\xyz
print(pp.parents[2])  # abc
print(pp.parents[3])  # .
# 访问parent属性
print(pp.parent)  # abc\xyz\wawa

# 访问name属性
print(pp.name)  # haha
pp = PurePath('abc/wawa/bb.txt')
print(pp.name)  # bb.txt

pp = PurePath('abc/wawa/bb.txt.tar.zip')
# 访问suffixes属性
print(pp.suffixes[0])  # .txt
print(pp.suffixes[1])  # .tar
print(pp.suffixes[2])  # .zip
# 访问suffix属性
print(pp.suffix)  # .zip
print(pp.stem)  # bb.txt.tar

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp)  # abc\xyz\wawa\haha
# 转成Unix风格的路径
print(pp.as_posix())  # abc/xyz/wawa/haha
# 将相对路径转换成Uri引发异常
# print(pp.as_uri()) # ValueError
# 创建绝对路径
pp = PurePath('d:/', 'Python', 'Python3.6')
# 将绝对路径转换成Uri
print(pp.as_uri())  # file:///d:/Python/Python3.6

# 判断当前路径是否匹配指定模式
print(PurePath('a/b.py').match('*.py'))  # True
print(PurePath('/a/b/c.py').match('b/*.py'))  # True
print(PurePath('/a/b/c.py').match('a/*.py'))  # False

pp = PurePosixPath('c:/abc/xyz/wawa')
# 测试relative_to方法
print(pp.relative_to('c:/'))  # abc\xyz\wawa
print(pp.relative_to('c:/abc'))  # xyz\wawa
print(pp.relative_to('c:/abc/xyz'))  # wawa

# 测试with_name方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py'))  # e:\Downloads\fkit.py
p = PureWindowsPath('c:/')
# print(p.with_name('fkit.py')) # ValueError

# 测试with_suffix方法
p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))  # e:\Downloads\pathlib.tar.zip
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))  # README.txt
