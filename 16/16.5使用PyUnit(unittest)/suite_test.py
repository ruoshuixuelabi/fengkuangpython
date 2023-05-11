"""
我们可以看到在codes\16\16.5\目录下包含了test fk math.py和 test hello.py文件,
此时程序就可以通过TestSuite将它们组织在一起,然后使用TestRunner来运行该测试包。
"""
import unittest
from test_fk_math import TestFkMath
from test_hello import TestHello

test_cases = (TestHello, TestFkMath)


def whole_suite():
    # 创建测试加载器
    loader = unittest.TestLoader()
    # 创建测试包
    suite = unittest.TestSuite()
    # 遍历所有测试类
    for test_class in test_cases:
        # 从测试类中加载测试用例
        tests = loader.loadTestsFromTestCase(test_class)
        # 将测试用例添加到测试包中
        suite.addTests(tests)
    return suite


if __name__ == '__main__':
    #    # 创建测试运行器（TestRunner）
    #    runner = unittest.TextTestRunner(verbosity=2)
    #    runner.run(whole_suite())
    with open('fk_test_report.txt', 'a') as f:
        # 创建测试运行器（TestRunner）,将测试报告输出到文件中
        runner = unittest.TextTestRunner(verbosity=2, stream=f)
        runner.run(whole_suite())
"""
上面程序中的粗体字代码调用TestSuite的 addTests()方法来添加测试用例,这样就实现了使用 TestSuite来组织多个测试用例。

上面程序还使用TestLoader来加载测试用例,该对象提供了一个loadTestsFromTestCase()方法,从指定类加载测试用例。

上面程序中的①号代码创建了TextTestRunner,它是一个测试运行器,专门用于运行测试用例和测试包。
其实前面使用的unittest.main()函数,同样也是通过TextTestRunner来运行测试用例的。

程序中的①号代码在创建TextTestRunner时还指定了verbosity=2,这样可以生成更详细的测试信息。
提示：在调用unittest.main()函数时同样可指定verbosity=2,用来生成更详细的测试信息。

运行上面程序,可以看到生成如下测试报告。

从上面的运行结果可以看到,测试报告通过更详细的信息来提示每个测试用例的运行结果,此时同样可以看到test one equation()测试失败。
如果不希望仅能在控制台中看到测试报告,而是希望直接生成文件格式的测试报告,则可以在①
号代码创建TextTestRunner  对象时指定stream 属性,该属性是一个打开的类文件对象,这样程序 就会把测试报告输出到该类文件对象中。
例如,将上面的 __main__ 部分改为如下形式。

再次运行该程序,此时在控制台中将看不到任何信息,测试报告将会被输出到 fk_test_report.txt 文件中。
"""