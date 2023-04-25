"""
6.7.2	检查类型
1.  Python 提供了如下两个函数来检查类型。
(1)issubclass(cls,class or tuple): 检查cls是否为后一个类或元组包含的多个类中任意类的子类。
(2)isinstance(obj,class or tuple):检查obj 是否为后一个类或元组包含的多个类中任意类的对象。
2.  通过使用上面两个函数,程序可以方便地先执行检查,然后才调用方法,这样可以保证程序不会出现意外情况。
3.  如下程序示范了通过这两个函数来检查类型。
4.  通过上面程序可以看出,issubclass()和 isinstance()两个函数的用法差不多,区别只是issubclass()的第一个参数是类名,
而isinstance()的第一个参数是变量,这也与两个函数的意义对应：issubclass 用于判断是否为子类,
而isinstance()用于判断是否为该类或子类的实例。
5.  issubclass()和 isinstance()两个函数的第二个参数都可使用元组。例如如下代码(程序清单同上)。
"""
# 定义一个字符串
hello = "Hello";
# "Hello"是str类的实例,输出True
print('"Hello"是否是str类的实例: ', isinstance(hello, str))
# "Hello"是object类的子类的实例,输出True
print('"Hello"是否是object类的实例: ', isinstance(hello, object))
# str是object类的子类,输出True
print('str是否是object类的子类: ', issubclass(str, object))
# "Hello"不是tuple类及其子类的实例,输出False
print('"Hello"是否是tuple类的实例: ', isinstance(hello, tuple))
# str不是tuple类的子类,输出False
print('str是否是tuple类的子类: ', issubclass(str, tuple))
# 定义一个列表
my_list = [2, 4]
# [2, 4]是list类的实例,输出True
print('[2, 4]是否是list类的实例: ', isinstance(my_list, list))
# [2, 4]是object类的子类的实例,输出True
print('[2, 4]是否是object类及其子类的实例: ', isinstance(my_list, object))
# list是object类的子类,输出True
print('list是否是object类的子类: ', issubclass(list, object))
# [2, 4]不是tuple类及其子类的实例,输出False
print('[2, 4]是否是tuple类及其子类的实例: ', isinstance([2, 4], tuple))
# list不是tuple类的子类,输出False
print('list是否是tuple类的子类: ', issubclass(list, tuple))

data = (20, 'fkit')
print('data是否为列表或元组: ', isinstance(data, (list, tuple)))  # True
# str不是list或者tuple的子类,输出False
print('str是否为list或tuple的子类: ', issubclass(str, (list, tuple)))
# str是list或tuple或object的子类,输出True
print('str是否为list或tuple或object的子类 ', issubclass(str, (list, tuple, object)))
