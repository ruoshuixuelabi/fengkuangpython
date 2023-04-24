"""
1.  从前面的示例可以看到,Python执行if语句时,会判断if条件是True还是False。
 那么if条件是不是只能使用bool类型的表达式呢?不是。 if条件可以是任意类型,当下面的值作为bool表达式时,会被解释器当作False处理。
False 、None 、0 、"" 、() 、[] 、{}
2.  从上面介绍可以看出,除了False 本身,各种代表"空"的None、 空字符串、空元组、空列表、空字典都会被当成False处理。
"""
# 定义空字符串
s = ""
if s:
    print('s不是空字符串')
else:
    print('s是空字符串')
# 定义空列表
my_list = []
if my_list:
    print('my_list不是空列表')
else:
    print('my_list是空列表')
# 定义空字典
my_dict = {}
if my_dict:
    print('my_dict不是空字典')
else:
    print('my_dict是空字典')
