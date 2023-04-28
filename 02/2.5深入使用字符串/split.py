"""
2.5.7 分割、连接方法

Python 还为 str 提供了分割和连接方法。
(1)split()：将字符串按指定分割符分割成多个短语。
(2)join()：将多个短语连接成字符串。

下面代码示范了上面两个方法的用法
"""
s = 'crazyit.org is a good site'
# 使用空白对字符串进行分割
print(s.split())  # 输出 ['crazyit.org', 'is', 'a', 'good', 'site']
# 使用空白对字符串进行分割,最多只分割前2个单词
print(s.split(None, 2))  # 输出 ['crazyit.org', 'is', 'a good site']
# 使用点进行分割
print(s.split('.'))  # 输出 ['crazyit', 'org is a good site']
mylist = s.split()
# 使用'/'为分割符，将mylist连接成字符串
print('/'.join(mylist))  # 输出 crazyit.org/is/a/good/site
# 使用','为分割符，将mylist连接成字符串
print(','.join(mylist))  # 输出 crazyit.org,is,a,good,site
