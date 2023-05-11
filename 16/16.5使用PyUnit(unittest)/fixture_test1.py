"""
16.5.4	测试固件之setUp和tearDown

到目前为止,针对 unittest 已经介绍了测试用例类(TestCase 的子类)、测试包(TestSuite)和测试运行器(TestRunner)。
此外,unittest 还有测试固件(Test Fixture)的概念。

(1)测试用例类：测试用例类就是单个的测试单元,其负责检查特定输入和对应的输出是否匹配。
unittest提供了一个TestCase基类用于创建测试用例类。
(2)测试包：用于组合多个测试用例,测试包也可以嵌套测试包。
(3)测试运行器：负责组织、运行测试用例,并向用户呈现测试结果。
(3)测试固件：代表执行一个或多个测试用例所需的准备工作,以及相关联的准备操作,准备工作可能包括创建临时数据库、
创建目录、开启服务器进程等。

unittest.TestCase包含了setUp()和tearDown()两个方法,其中setUp()方法用于初始化测试固件：
而 tearDown()方法用于销毁测试固件。程序会在运行每个测试用例(以test 开头的方法)之前自动执行
setUp(方法来初始化测试固件,并在每个测试用例(以test 开头的方法)运行完成之后自动 执行 tearDown()方法来销毁测试固件。

由此可见,如果希望程序为测试用例初始化、销毁测试固件,那么只要重写TestCase的 setUp() 和tearDown()方法即可。例如如下测试程序。
"""
import unittest

from hello import *


class TestHello(unittest.TestCase):
    # 测试say_hello函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello World.")

    # 测试add函数
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-3, 0), -3)

    def setUp(self):
        print('\n====执行setUp模拟初始化固件====')

    def tearDown(self):
        print('\n====调用tearDown模拟销毁固件====')


"""
使用如下命令来运行该测试程序。

python      -m      unittest      -v      fixture_test1.py

为该命令添加了 -v 选项,该选项用于告诉unittest生成更详细的输出信息。此时可以看到如下 输出结果。

从上面的输出结果可以看出, unittest在运行每个测试用例(以test 开头的方法)之前都执行了 setUp()方法,
在每个测试用例(以test 开头的方法)运行完成之后都执行了tearDown()方法。
"""
