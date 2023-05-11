"""
16.5.5	跳过测试用例

在默认情况下,unittest 会自动测试每一个测试用例(以test 开头的方法),但如果希望临时跳过某个测试用例,则可以通过如下两种方式来实现。
(1)使用skipXxx装饰器来跳过测试用例。unittest一共提供了3个装饰器,分别是@unittest.skip(reason)、
@unittest.skiplf(condition, reason)和 @unittest.skipUnless(condition, reason)。
其中skip代表无条件跳过,skiplf代表当condition为 True 时跳过;skipUnless代表当condition为 False 时跳过。
(2)使用TestCase的 skipTest()方法来跳过测试用例。

下面程序示范了使用@unittest.skip装饰器来跳过测试用例。
"""
import unittest

from hello import *


class TestHello(unittest.TestCase):
    # 测试say_hello函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello World.")

    # 测试add函数
    @unittest.skip('临时跳过test_add')
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-3, 0), -3)


"""
上面的粗体字代码使用 @unittest.skip 装饰器跳过了 test_add()测试方法。使用如下命令来运行 该测试程序。
python  -m unittest skip_test1.py

可以看到如下输出结果。

在上面输出结果的第一行可以看到s., 这表明程序运行了两个测试用例,s 代表跳过了第一个测试用例,点(.)代表第二个测试用例通过。
"""
