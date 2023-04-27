"""
linecache模块允许从 Python 源文件中随机读取指定行,并在内部使用缓存优化存储。
由于该模块主要被设计成读取Python 源文件,因此它会用 UTF-8 字符集来读取文本文件。
实际上,使用 linecache模块也可以读取其他文件,只要该文件使用了 UTF-8 字符集存储。

linecache模块包含以下常用函数。
(1)linecache.getline(filename,lineno,module globals=None): 读取指定模块中指定文件的指定行。
其中filename指定文件名,lineno指定行号。
(2)linecache.clearcache():清空缓存。
(3)linecache.checkcache(filename=None):检查缓存是否有效。如果没有指定 filename 参数, 则默认检查所有缓存的数据。

下面程序示范了使用linecache模块来随机读取指定行。
"""
import linecache
import random

# 读取random模块的源文件的第3行
print(linecache.getline(random.__file__, 3))
# 读取本程序的第3行
print(linecache.getline('linecache_test.py', 3))
# 读取普通文件的第2行
print(linecache.getline('utf_text.txt', 2))
