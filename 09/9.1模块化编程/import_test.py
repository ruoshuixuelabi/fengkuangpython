"""
前面第7章在介绍异常时已经用到了系统提供的sys、os、traceback这三个模块,可能已有读者对模块这个"神秘"的东西感到很好奇：
Python 每次导入模块之后,Python 似乎就增加了某种特别的功能,模块怎么这么厉害呢?这些模块到底是从哪里来的?

本章将会带着大家去真正了解模块这个强大的工具。实际上,Python 语言之所以能被广泛应用于各行各业,
在很大程度上得益于它的模块化系统。在 Python 的标准安装中包含了一组自带的模块,这些模块被称为"标准库"。
Python  3 的标准库请参考 https://docs.python.org/3/library/index.html。

更重要的是,开发者完全可以根据自己的需要不断地为Python增加扩展库。各行各业的 Python 用户贡献了大量的扩展库,
这些扩展库极大地丰富了Python 的功能,这些扩展库从某种程度上也形成了Python 的"生态圈"。

9.1 模块化编程

对于一个真实的 Python 程序,我们不可能自己完成所有的工作,通常都需要借助于第三方类库。
此外,也不可能在一个源文件中编写整个程序的源代码,这些都需要以模块化的方式来组织项目的源代码。

9.1.1 导入模块的语法

在前面章节中已经看到使用 import 导入模块的语法,但实际上 import 还有更多详细的用法。

import语句主要有两种用法。
(1)import  模块名1[as 别名1],模块名2[as 别名2], … :导入整个模块。
(2)from 模块名 import 成员名1[as 别名1],成员名2[as 别名2],… :导入模块中指定成员。

上面两种import语句的区别主要有三点。
(1)第一种import语句导入整个模块内的所有成员(包括变量、函数、类等);
第二种import语句只导入模块内的指定成员(除非使用form 模块名 import *,但通常不推荐使用这种语法)。
(2)当使用第一种 import 语句导入模块中的成员时,必须添加模块名或模块别名前缀;
当使用第二种 import 语句导入模块中的成员时,无须使用任何前缀,直接使用成员名或成员别名即可。

下面程序使用导入整个模块的最简单语法来导入指定模块。
"""
# 导入sys整个模块
import sys

# 使用sys模块名作为前缀来访问模块中的成员
print(sys.argv[0])
"""
上面粗体字代码使用最简单的方式导入了 sys 模块,因此在程序中使用 sys 模块内的成员时,必须添加模块名作为前缀。

运行上面程序,可以看到如下输出结果(sys 模块下的argv变量用于获取运行Python 程序的命令行参数,
其中argv[0]用于获取该Python程序的程序名)。
"""