"""
1.  Python将会根据PYTHONPATH环境变量的值来确定到哪里去加载模块。 PYTHONPATH环境变量的值是多个路径的集合,
这样Python 就会依次搜索PYTHONPATH环境变量所指定的多个路径,试图从中找到程序想要加载的模块。
2.  当程序重复导入同一个模块时, Python 只会导入一次。道理很简单,因为这些变量、函数、 类等程序单元都只需要定义一次即可,何必导入多次呢?
3.  相反,如果 Python 允许导入多次,反而可能会导致严重的后果。比如程序定义了 foo 和 bar 两个模块,
假如foo 模块导入了bar 模块,而bar 模块又导入了foo 模块——这似乎形成了无限循 环导入,但由于Python 只会导入一次,
所以这个无限循环导入的问题完全可以避免。
"""
# 两次导入module1,并指定其别名为md
import module1 as md
import module1 as md
print(md.my_book)
md.say_hi('Charlie')
user = md.User('孙悟空')
print(user)
user.walk()