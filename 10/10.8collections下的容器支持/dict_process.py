"""
假如程序中包含多个 key-value 对数据,在这些 key-value 对中有些 key 是重复的,程序希望对这些 key-value 对进行整理：
key 对应一个list,该 list 中包含这组数据中该 key 对应的所有value。

下面先使用普通dict来完成这项工作。

"""
s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
d = {}
for k, v in s:
    # setdefault()方法用于获取指定key对应的value.
    # 如果该key不存在,则先将该key对应的value设置为默认值:[]
    d.setdefault(k, []).append(v)
print(list(d.items()))
"""
正如从上面粗体字代码所看到的,如果使用普通dict来处理,就需要处理 key 不存在的情况。
程序中粗体字代码使用了dict的 setdefault()方法,该方法用于获取指定 key 对应的value,但如果该 key 不存在,
setdefault()方法就会先为该 key 设置一个默认的value。
"""
