"""
在使用 from…import 语法时也可一次导入指定模块内的所有成员,例如如下程序。
"""
# 导入sys模块的所有成员
from sys import *

# 使用导入成员的语法,直接使用成员的别名访问
print(argv[0])
print(winver)
"""
上面粗体字代码一次导入了 sys 模块中的所有成员,这样程序即可通过成员名来使用该模块内的所有成员。
该程序的输出结果和前面程序的输出结果完全相同。

需要说明的是,一般不推荐使用"from 模块 import *"这种语法导入指定模块内的所有成员,因为它存在潜在的风险。
比如同时导入module1和 module2 内的所有成员,假如这两个模块内都有一个foo()函数,那么当在程序中执行如下代码时：
foo()

上面调用的这个foo()函数到底是module1模块中的还是module2模块中的?因此,这种导入指定模块内所有成员的用法是有风险的。

但如果换成如下两种导入方式：
import   module1
import   module2    as    m2
接下来要分别调用这两个模块中的foo()函数就非常清晰。

#使用模块modulel 的模块名作为前缀调用foo() 函数
modulel.foo()
使  用module2 的模块别名作为前缀调用foo() 函数
m2.foo()

或者使用from…import语句也是可以的。

#导入 module1  中的 foo 成员，并指定其别名为foo1
from module1  import    foo    as    foo1
#导入 module2 中的foo 成员，并指定其别名为foo2
from module2 import   foo   as   foo2

此时通过别名将modulel 和 module2 两个模块中的foo 函数很好地进行了区分，接下来分别调 用两个模块中foo()函数就很清晰。

fool()   # 调用 module1 中的foo() 函数
foo2()  # 调用 module2 中的foo() 函数
"""
