"""
如果希望程序在该类的所有测试用例执行之前都用一个方法来初始化测试固件,
在该类的所有测试用例执行之后都用一个方法来销毁测试固件,则可通过重写setUpClass()和tearDownClass()类 方法来实现。
例如如下测试程序。
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

    @classmethod
    def setUpClass(cls):
        print('\n====执行setUpClass在类级别模拟初始化固件====')

    @classmethod
    def tearDownClass(cls):
        print('\n====调用tearDownClass在类级别模拟销毁固件====')


"""
上面程序中定义的setUpClass()和 tearDownClass()两个类方法也是用于初始化测试固件和销毁测试固件的方法,
但它们会在该类的所有测试用例执行之前和执行之后执行。

使用如下命令来运行该测试程序。
python  -m unittest -v fixture_test2.py

可以看到如下输出结果。
"""
