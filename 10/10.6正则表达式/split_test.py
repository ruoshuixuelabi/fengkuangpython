"""
1.  re.split(pattern, string,maxsplit=0,flags=0): 使用pattern对 string进行分割,该函数返回分割得到的多个子串组成的列表。
其中maxsplit参数控制最多分割几次。
2.  如下程序示范了split()函数的用法。
"""
import re

# 使用逗号对字符串进行分割
print(re.split(', ', 'fkit, fkjava, crazyit'))
# 输出：['fkit', 'fkjava', 'crazyit']
# 指定只分割1次,被切分成2个子串
print(re.split(', ', 'fkit, fkjava, crazyit', 1))
# 输出：['fkit', 'fkjava, crazyit']
# 使用a进行分割
print(re.split('a', 'fkit, fkjava, crazyit'))
# 输出：['fkit, fkj', 'va, crazyit']
# 使用x进行分割,没有匹配内容,则不会执行分割
print(re.split('x', 'fkit, fkjava, crazyit'))
# 输出：['fkit, fkjava, crazyit']


# print(re.split('\W+', ' runoob, runoob, runoob.'))
# ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
# re.split('\W+', ' runoob, runoob, runoob.', 1)
# ['', 'runoob, runoob, runoob.']
# 
# >>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言,split 不会对其作出分割
# ['hello world']
