"""
1.  如果对比findall()、finditer()和search()函数,它们的区别也很明显,search()只返回字符串中第一处匹配pattern的子串;
而findall()和 finditer()则返回字符串中所有匹配pattern的子串。
(1)re.fullmatch(pattern,string,flags=0):该函数要求整个字符串能匹配patter,
如果匹配则返回包含匹配信息的 _sre.SRE_Match 对象;否则返回None。
(2)re.sub(pattern,repl,string,count=0,flags=0): 该函数用于将 string 字符串中所有匹配 pattern 的内容替换成repl;
repl 既可是被替换的字符串,也可是一个函数。count 参数控制最多替换多少次,如果指定count为0,则表示全部替换。
"""
import re

# 返回所有匹配pattern的子串组成的列表,忽略大小写
print(re.findall('fkit', 'FkIt is very good , Fkit.org is my favorite', re.I))
# 返回所有匹配pattern的子串组成的迭代器,忽略大小写
it = re.finditer('fkit', 'FkIt is very good , Fkit.org is my favorite', re.I)
for e in it:
    print(str(e.start()) + "-->" + e.group())
