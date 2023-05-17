import re
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h3>'))

m1 = re.fullmatch('www', 'www')  # 开始位置可以匹配
print(m1)
print(re.fullmatch(r'\u0041\\', 'A\\'))  # 匹配A\
print(re.fullmatch(r'\u0061\t', 'a\t'))  # 匹配a < 制表符 >
print(re.fullmatch(r'\?\[', '?['))  # // 匹配?[
print(re.fullmatch(r'c\wt', 'cat'))  # c\wt可以匹配cat、cbt、cct、cOt、c9t等一批字符串
print(re.fullmatch(r'c\wt', 'c9t'))  # c\wt可以匹配cat、cbt、cct、cOt、c9t等一批字符串
# 匹配如000-000-0000形式的电话号码
print(re.fullmatch(r'\d\d\d-\d\d\d-\d\d\d\d', '123-456-8888'))
print(re.search(r'Windows (95|98|NT|2000)[\w ]+\1', 'Windows 98 published in 98'))
print(re.search(r'Windows (95|98|NT|2000)[\w ]+\1', 'Windows 98 published in 95'))
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h3>'))
print(re.search(r'Windows (?:95|98|NT|2000)[a-z ]+', 'Windows 98 published in 98'))
print(re.search(r'(?<=<h1>).+?(?=</h1>)', 'help! <h1>fkit.org</h1>!technology'))
print(re.search(r'(?<=<h1>).+?(?=</h1>)', 'help! <h1><div>fkit</div></h1>!technology'))
print(re.search(r'[a-zA-Z0-9_]{3,}(?#username)@fkit\.org', 'sun@fkit.org'))
print(re.search(r'(?i)[a-z0-9_]{3,}(?#username)@fkit\.org', 'Sun@FKIT.ORG'))
print(re.search(r'(?i:[a-z0-9_]){3,}(?#username)@fkit\.org', 'Sun@fkit.org'))
print(re.search(r'(?-i:[a-z0-9_]){3,}@fkit\.org', 'sun@Fkit.org', re.I))
print(re.search(r'@.+\.', 'sun@fkit.com.cn'))
print(re.search(r'@.+?\.', 'sun@fkit.com.cn'))
