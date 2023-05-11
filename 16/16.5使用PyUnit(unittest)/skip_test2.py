"""
此外,程序也可以使用 TestCase 的 skipTest()方法跳过测试用例。例如,如下程序示范了使用 skipTest()方法来跳过测试用例。
"""
import unittest

from hello import *


class TestHello(unittest.TestCase):
    # 测试say_hello函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello World.")

    # 测试add函数
    def test_add(self):
        self.skipTest('临时跳过test_add')
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-3, 0), -3)


"""
上面的粗体字代码使用 self.skipTest()方法跳过了测试方法(test add())。使用如下命令来运行 该测试程序。
python  -m unittest -v skip_test2.py

上面命令使用了-v 选项来生成更详细的测试报告。运行上面命令,可以看到如下输出结果。

从上面的输出结果可以看到,unittest 测试跳过了 test_add()方法,并显示了跳过的原因：
'临时跳过test_add'(如果不使用-v 选项,将不会输出该原因)。
"""
