"""
1.  如果使用defaultdict来处理则简单得多,因为程序可以直接为defaultdict中不存在的key 设置默认的value。 该处理程序如下。
2.  对比该程序中的粗体字代码和前一个程序中的粗体字代码,不难发现使用defaultdict更加方便,
原因是程序直接访问 defaultdict 中指定的 key 对应的 value, 如果该 key 不存在,
程序在创建defaultdict时传入的list函数将会为之生成默认的value。
"""
from collections import defaultdict

s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
# 创建defaultdict,设置由list()函数来生成默认值
d = defaultdict(list)
for k, v in s:
    # 直接访问defaultdict中指定key对应的value即可。
    # 如果该key不存在,defaultdict会自动为该key生成默认值
    d[k].append(v)
print(list(d.items()))
