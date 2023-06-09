"""
本章将会介绍 Python 内置的三种常用数据结构：列表(list)、元组(tuple)和字典(dict),
这三种数据结构都可用于保存多个数据项,这对于编程而言是非常重要的----因为程序不仅需要使用单个变量来保存数据,
还需要使用多种数据结构来保存大量数据,而列表、元组和字典就可满足保存大量数据的需求。

列表和元组比较相似,它们都按顺序保存元素,每个元素都有自己的索引,因此列表和元组都可通过索引访问元素。
二者的区别在于元组是不可修改的,但列表是可修改的。字典则以key-value 的形式保存数据。
这三种数据结构各有特色,它们都是Python 编程中必不可少的内容。

3.1 序列简介

所谓序列,指的是一种包含多项数据的数据结构,序列包含的多个数据项(也叫成员)按顺序排列,可通过索引来访问成员。

3.1.1 Python 的序列

Python 的常见序列类型包括字符串、列表和元组等。前一章介绍过的字符串,其实就是一种常见的序列,
通过索引访问字符串内的字符程序就是序列的示范程序。

本章介绍的序列主要是指序列和元组,这两种类型看起来非常相似,最主要的区别在于：元组是不可变的,元组一旦构建出来,
程序就不能修改元组所包含的成员(就像字符串也是不可变的,程序无法修改字符串所包含的字符序列);
但序列是可变的,程序可以修改序列所包含的元素。

在具体的编程过程中,如果只是固定地保存多个数据项,则不需要修改它们,此时就应该使用元组：反之,就应该使用序列。
此外,在某些时候,程序需要使用不可变的对象,比如Python 要求字典的 key 必须是不可变的,此时程序就只能使用元组。

序列和元组的关系就是可变和不可变的关系。

3.1.2 创建列表和元组

创建列表和元组的语法也有点相似,区别只是创建列表使用方括号,创建元组使用圆括号,并在括号中列出元组的元素,元素之间以英文逗号隔开。

创建列表的语法格式如下：[ele1,ele2,ele3,..]

创建元组的语法格式如下：(ele1,ele2,ele3,...)

下面代码示范了在程序中定义列表和元组。
"""
# 使用方括号定义列表
my_list = ['crazyit', 20, 'Python']
print(my_list)
# 使用圆括号定义元组
my_tuple = ('crazyit', 20, 'Python')
print(my_tuple)
