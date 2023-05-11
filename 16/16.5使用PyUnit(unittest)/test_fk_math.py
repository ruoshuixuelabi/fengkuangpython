"""
在定义好上面的 fk_math.py 程序之后,该程序就相当于一个模块,接下来为该模块编写单元测试代码。

unittest要求单元测试类必须继承 unittest.TestCase,该类中的测试方法需要满足如下要求。
(1)测试方法应该没有返回值。
(2)测试方法不应该有任何参数。
(3)测试方法应以 test 开头。

下面是测试用例的代码。
"""
import unittest

from fk_math import *


class TestFkMath(unittest.TestCase):
    # 测试一元一次方程的求解
    def test_one_equation(self):
        # 断言该方程求解应该为-1.8
        self.assertEqual(one_equation(5, 9), -1.8)
        # 断言该方程求解应该为-2.5
        self.assertTrue(one_equation(4, 10) == -2.5, .00001)
        # 断言该方程求解应该为27/4
        self.assertTrue(one_equation(4, -27) == 27 / 4)
        # 断言当a == 0时的情况,断言引发ValueError
        with self.assertRaises(ValueError):
            one_equation(0, 9)

    # 测试一元二次方程的求解
    def test_two_equation(self):
        r1, r2 = two_equation(1, -3, 2)
        self.assertCountEqual((r1, r2), (1.0, 2.0), '求解出错')
        r1, r2 = two_equation(2, -7, 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        # 断言只有一个解的情形
        r = two_equation(1, -4, 4)
        self.assertEqual(r, 2.0, '求解出错')
        # 断言当a == 0时的情况,断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(0, 9, 3)
        # 断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(4, 2, 3)


if __name__ == '__main__':
    unittest.main()
"""
上面测试用例中的粗体字代码使用断言方法判断函数的实际输出结果与期望输出结果是否一致,如果一致则表明测试通过,否则表明测试失败。

在上面的测试用例中,在测试 one_equation()方法时传入了四组参数(如粗体字代码所示)。
至于此处到底需要传入几组参数进行测试,关键取决于测试者要求达到怎样的逻辑覆盖程度,随着测试要求的提高,
此处可能需要传入更多的测试参数。当然,此处只是介绍 PyUnit 的用法示例,并未刻意去达到怎样的逻辑覆盖,这一点请务必留意。

提示：在测试某个方法时,如果实际测试要求达到某种覆盖程度,那么在编写测试用例时必须传入多组参数来进行测试,
使得测试用例能达到指定的逻辑覆盖。

unittest.TestCase内置了大量 assertXxx 方法来执行断言,其中最常用的断言方法如表16.5所示。
表16.5 TestCase 中最常用的断言方法
断言方法	                            检查条件
assertEqual(a,b)	                a =b
assertNotEqual(a,b)	        a!=b
assertTrue(x)	                    bool(x) is True
assertFalse(x)	                    bool(x) is False
assertls(a,b)	                    a is h
assertlsNot(a,b)	                a is not b
assertlsNone(x)	                x is None
assertlsNotNonc(x)	        x is not None
assertIn(a,b)	                    a in b
assertNotIn(a,b)	                a not in b
assertlsInstance(a,b)	        isinstance(a,b)
assertNotlsInstance(a,b)	not isinstance(a,b)

除了上面这些断言方法,如果程序要对异常、错误、警告和日志进行断言判断,TestCase 提供了如表16.6所示的断言方法。
表16.6 TestCase 包含的与异常、错误、警告和日志相关的断言方法

断言方法	                                                                                                检查条件
assertRaises(exc, fun,*args,**kwds)	                            fun(*args,**kwds)引发exc异常
assertRaisesRegex(exc,r, fun,*args,**kwds)	                fun(*args,**kwds)引发exc异常,且异常信息匹配r正则表达式
assertWarns(wam, fun,*args,**kwds)	                        fun(*args,**kwds)引发wam警告
assertWamsRegex(warn, r,fun,*args,**kwds)	            fun(*args,**kwds)引发wam警告,且警告信息匹配r正则表达式
assertLogs(logger, level)	                                            With语句块使用日志器生成level级别的日志

TestCase还包含了如表16.7所示的断言方法用于完成某种特定检查。
表16.7 TestCase 包含的用于完成某种特定检查的断言方法

断言方法	检查条件
assertAlmostEqual(a,b)	        round(a-b,7)=0
assertNotAlmostEqual(a,b)	round(a-b,7)!=0
assertGreater(a,b)	                a>b
assertGreaterEqual(a,b)	        a>=b
assertLess(a,b)	                    a<b
assertLessEqual(a,b)	            a<=b
assertRegex(s,r)	                    r.search(s)
assertNotRegex(s,r)	            not r.search(s)
assertCountEqual(a,b)	        a、b两个序列包含的元素相同,不管元素出现的顺序如何

当测试用例使用 assertEqual()判断两个对象是否相等时,如果被判断的类型是字符串、序列、 列表、元组、集合、字典,
则程序会自动改为使用如表16.8所示的断言方法进行判断。换而言之,如表16.8所示的断言方法其实没有必要使用,unittest模块会自动应用它们。
表16.8 TestCase 包含的针对特定类型的断言方法

断言方法	                                用于比较的类型
assertMultiLineEqual(a,b)	    字符串(string)
assertSequenceEqual(a.b)	    序列(sequence)
assertListEqual(a,b)	            列表(list)
assertTupleEqual(a,b)	            元组(tuple)
assertSetEqual(a,b)	                集合(set或frozenset)
assertDictEqual(a,b)	            字典(dict)

16.5.2	运行测试

在编写完测试用例之后,可以使用如下两种方式来运行它们。
(1)通过代码调用测试用例。程序可以通过调用 unittest.main() 来运行当前源文件中的所有测试用例。例如,在上面的测试用例中增加如下代码。
if __name__ == '__main__':
    unittest.main()

在增加了上面的代码之后,如果程序直接执行该 Python 程序,程序就会调用 unittest.main(),该方法就会运行当前源文件中的所有测试用例。
(2)使用 unittest 模块运行测试用例。使用该模块的语法格式如下：
python -m unittest 测试文件

对于上面的test_fk_math.py测试文件,可以通过如下命令来运行测试用例。
py -m unittest test_fk_math.py

在使用python -m unittest 命令运行测试用例时,如果没有指定测试用例,该命令将自动查找并运行当前目录下的所有测试用例。
因此,程序也可直接使用如下命令来运行所有测试用例。
py -m unittest
采用上面任意一种方式来运行测试用例,均可以看到如下输出结果。
D:\BaiduNetdiskDownload\766841《疯狂Python讲义》PDF+源代码+习题\fengkuangpython\16\16.5使用PyUnit(unittest)>py -m unittest
F...
======================================================================
FAIL: test_one_equation (test_fk_math.TestFkMath)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:test_fk_math.py", line 20, in test_one_equation
    self.assertEqual(one_equation(5, 9), -1.8)
AssertionError: 1.8 != -1.8

----------------------------------------------------------------------
Ran 4 tests in 0.012s

FAILED (failures=1)

在上面输出结果的第一行可以看到两个点,这里的每个点都代表一个测试用例(每个以 test 开头的方法都是一个真正独立的测试用例)的结果。
由于上面测试类中包含了两个测试用例,因此此处看到两个点,其中点代表测试用例通过。此处可能出现如下字符。
(1).：代表测试通过。
(2)F：代表测试失败,F 代表failure。
(3)E：代表测试出错,E 代表error。
(4)s：代表跳过该测试,s代表skip。

在上面输出结果的横线下面看到了"Ran 2 tests in 0.000s"提示信息,这行提示信息说明本次测试运行了多少个测试用例。
如果看到下面提示OK,  则表明所有测试用例均通过。

上面的测试用例都可通过,是因为 fk_math.py程序没有错误。如果将fk_math.py 程序中的① 号代码故意修改为出错,
假如将①号代码修改为return b/a, 再次运行上面的测试用例,将会看到如下输出结果。

此时看到第一行的输出信息为F., 这表明第一个测试用例失败,第二个测试用例成功。
接下来在两条横线之间可以看到断言错误的Traceback信息,以及函数运行的实际输出结果和期望输出结果的差异,如粗体字代码所示。
这行信息提示该函数运行的实际输出结果是1.8,但期望输出结果是-1.8。
"""