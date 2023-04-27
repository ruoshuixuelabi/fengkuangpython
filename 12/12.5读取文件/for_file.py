"""
12.5.4 文件迭代器

实际上,文件对象本身就是可遍历的(就像一个序列一样),因此,程序完全可以使用 for 循环来遍历文件内容。
例如,如下程序使用for循环读取文件内容。
"""
import codecs
# 指定使用 utf-8 字符集读取文件内容
f = codecs.open("for_file.py", 'r', 'utf-8', buffering=True)
# 使用for循环遍历文件对象
for line in f:
    print(line, end='')
f.close()
"""
如果有需要,程序也可以使用list()函数将文件转换成 list 列表,就像文件对象的 readlines() 方法的返回值一样。例如如下代码(程序清单同上)。
"""
# 将文件对象转换为list列表
print(list(codecs.open("for_file.py", 'r', 'utf-8', buffering=True)))
