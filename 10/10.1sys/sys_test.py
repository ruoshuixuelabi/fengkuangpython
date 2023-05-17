"""
第 9 章介绍了 Python 模块的相关知识,读者已经掌握了如何自定义模块。但在实际开发中,Python 的很多功能都已有了成熟的第三方实现,
一般不需要开发者"重复造轮子",当开发者需要完成某种功能时,通过搜索引擎进行搜索,通常就可以找到第三方在 Python 中为该功能所扩展的模块。
实际上,Python 语言本身也内置了大量模块,对于常规的日期、时间、正则表达式、JSON 支持、容器类等,
Python 内置的模块已经非常完备,而本章就将带着读者来熟悉 Python 自带的这些模块。

需要说明的是,Python 内置的模块总是在不断的更新中,阅读本章内容只是掌握 Python 内置模块的入门之路,
关于更详细、更完备的模块介绍文档可参考 Python 库的参考手册：https://docs.python.org/3/library/index.html。

10.1	sys

sys 模块代表了 Python 解释器,主要用于获取和 Python 解释器相关的信息。

在 Python 的交互式解释器中先导入 sys 模块,然后输入[e for e in dir(sys) if not e.startswith('_')] 命令 (sys 模块没有__all__ 变量),
可以看到如下输出结果。
[e for e in dir(sys) if not e.startswith('_')]
['addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook',
'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode',
'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks',
'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding',
'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern',
'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache',
'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth',
'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names',
'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']

上面列出的程序单元就是 sys 模块所包含的全部程序单元(包括变量、函数等),读者不要被它们吓着了,以为这些全都需要记下来。
实际上完全没有必要,通常都是用到哪些模块就去查阅其对应的说明文档和参考手册。
sys 模块的参考页面为 https://docs.python.org/3/ibrary/sys.html。

需要说明的是,大部分时候用不到 sys 模块里很冷僻的功能,因此本节只介绍 sys 模块中常用的属性和函数。
(1)sys.argv:获取运行 Python 程序的命令行参数。其中 sys.argv[0] 通常就是指该Python程序,
sys.argv[1] 代表为 Python 程序提供的第一个参数,sys.argv[2] 代表为 Python 程序提供的第二个参数……依此类推。
(2)sys.byteorder：显示本地字节序的指示符。如果本地字节序是大端模式,则该属性返回big;否则返回little
(3)sys.copyright：该属性返回与 Python 解释器有关的版权信息。
(4)sys.executable：该属性返回 Python 解释器在磁盘上的存储路径。
(5)sys.exit()：通过引发 SystemExit 异常来退出程序。将其放在 try 块中不能阻止 finally 块的执行。
(6)sys.flags：该只读属性返回运行 Python 命令时指定的旗标。
(7)sys.getfilesystemencoding()：返回在当前系统中保存文件所用的字符集。
(8)sys.getrefcount(object)：返回指定对象的引用计数。前面介绍过,当 object 对象的引用计数为0时,系统会回收该对象。
(9)sys.getrecursionlimit()：返回 Python 解释器当前支持的递归深度 。 该属性可通过 setrecursionlimit()方法重新设置。
(10)sys.getswitchinterval()：返回在当前 Python 解释器中线程切换的时间间隔。该属性可通过 setswitchinterval()函数改变。
(11)sys.implementation：返回当前 Python 解释器的实现。
(12)sys.maxsize：返回 Python 整数支持的最大值。在32位平台上,该属性值为2**31- 1;在 64位平台上,该属性值为2**63- 1。
(13)sys.modules：返回模块名和载入模块对应关系的字典。
(14)sys.path：该属性指定 Python 查找模块的路径列表。程序可通过修改该属性来动态增加 Python 加载模块的路径。
(15)sys.platform：返回Python 解释器所在平台的标识符。
(16)sys.stdin：返回系统的标准输入流——一个类文件对象。
(17)sys.stdout：返回系统的标准输出流——一个类文件对象。
(18)sys.stderr：返回系统的错误输出流——一个类文件对象。
(19)sys.version：返回当前Python 解释器的版本信息。
(20)sys.winver：返回当前Python 解释器的主版本号。

下面程序示范了使用sys 模块的部分功能。
"""
import sys

# 显示本地字节序的指示符。
print(sys.byteorder)
# 显示Python解释器有关的版权信息
print(sys.copyright)
# 显示Python解释器在磁盘上的存储路径。
print(sys.executable)
# 显示当前系统上保存文件所用的字符集。
print(sys.getfilesystemencoding())
# 显示Python整数支持的最大值
print(sys.maxsize)
# 显示Python解释器所在平台
print(sys.platform)
# 显示当前Python解释器的版本信息。
print(sys.version)
# 返回当前Python解释器的主版本号。
print(sys.winver)
