"""
如果对比 findall()、finditer()和 search()函数,它们的区别也很明显,search()只返回字符串中第一处匹配 pattern 的子串;
而 findall()和 finditer()则返回字符串中所有匹配 pattern 的子串。
"""
import re

# 返回所有匹配pattern的子串组成的列表,忽略大小写
print(re.findall('fkit', 'FkIt is very good , Fkit.org is my favorite', re.I))
# 返回所有匹配pattern的子串组成的迭代器,忽略大小写
it = re.finditer('fkit', 'FkIt is very good , Fkit.org is my favorite', re.I)
for e in it:
    print(str(e.start()) + "-->" + e.group())
