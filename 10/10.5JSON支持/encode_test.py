"""
10.5	JSON支持

1.  JSON 是一种轻量级、跨平台、跨语言的数据交换格式, JSON 格式被广泛应用于各种语言的数据交换中,Python 也提供了对 JSON 的支持。

10.5.1	JSON的基本知识

2.  JSON 的全称是 JavaScript Object Notation,即 JavaScript 对象符号,它是一种轻量级的数据交换格式。
JSON 的数据格式既适合人来读写,也适合计算机本身解析和生成。
最早的时候, JSON 是JavaScript语言的数据交换格式,后来慢慢发展成一种语言无关的数据交换格式,这一点非常类似于 XML。
3.  JSON 主要在类似于 C 的编程语言中广泛使用,这些语言包括C、C++、C#、Java、JavaScript、 Perl、Python等。
JSON 提供了多种语言之间完成数据交换的能力,因此, JSON 也是一种非常理想的数据交换格式。 JSON 主要有如下两种数据结构。
(1)由 key-value 对组成的数据结构。这种数据结构在不同的语言中有不同的实现。
例如,在 JavaScript 中是一个对象;在 Python 中是一种 dict 对象;在 C 语言中是一个struct;在其他语言中,
则可能是record、dictionary、hash table等。
(2)有序集合。这种数据结构在Python中对应于列表;在其他语言中,可能对应于list、vector、数组和序列等。

4.  上面两种数据结构在不同的语言中都有对应的实现,因此这种简便的数据表示方式完全可以实现跨语言。
所以, JSON 可以作为程序设计语言中通用的数据交换格式。在JavaScript中主要有两种 JSON 语法,其中一种用于创建对象;另一种用于创建数组。
1. 使用 JSON 语法创建对象
    使用 JSON 语法创建对象是一种更简单的方式。使用 JSON 语法可避免书写函数,也可避免使用 new 关键字,
而是可以直接获取一个 JavaScript对象。对于早期的 JavaScript 版本,如果要使用 JavaScript 创建一个对象,通常可能会这样写。
//定义一个函数,可以作为该类的构造器
function Person(name,gender)
{
    this.name    =  name;
    this.gender =  gender;
//创建一个Person 实例
var  p  =  new  Person('yeeku','male');
//输出Person 实例的name 属性
alert(p.name);

从 JavaScript 1.2开始,创建对象有了一种更快捷的语法,如下所示。
var  p  ={
    "name":'yeeku',
    "gender":'male'
};
alert(p);
这种语法就是一种 JSON 语法。显然,使用 JSON 语法创建对象更加简捷、方便。如图10.2所示是使用JSON 创建对象的语法示意图。

从图10.2可以看出,在创建对象object时,总以"{"开始,以"}"结束,对象的每个属性名和属性值之间以英文冒号(:)隔开,
多个属性定义之间以英文逗号(,)隔开。语法格式如下：
object = {
    propertyName1:propertyValue1,
    propertyName2:propertyValue2,
    ......
}

必须注意的是,并不是在每个属性定义的后面都有英文逗号(,),必须当后面还有属性定义时才需要有逗号(,)。因此,下面的对象定义是错误的。
var  p  ={
    "name":'yeeku',
    "gender":'male',
};
因为在 gender 属性定义的后面多出了一个英文逗号。如果在最后一个属性定义的后面直接以"}"结束了,则不应该再有英文逗号。

当然,在使用JSON 语法创建 JavaScript 对象时,属性值不仅可以是普通字符串,也可以是任何基本数据类型,
还可以是函数、数组,甚至是另外一个使用 JSON 语法创建的对象。例如：
person =
{
    name : 'yeeku',
    gender : 'male',
    //使用 JSON 语法为其指定一个属性
    son : {
        name : 'tiger',
        grade : 1
    },
    //使用JSON 语法为 person 直接分配一个方法
    info  : function()
    {
        console.log(" 姓名："+ this.name   +"性别："+ this.sex);
    }
}

2. 使用 JSON 语法创建数组
使用JSON 语法创建数组也是非常常见的情形,在早期的JavaScript语法中,我们通过如下方式来创建数组。

//创建数组对象
var a  =  new  Array();
//为数组元素赋值
a[0]='yeeku';
//为数组元素赋值
a[1]='nono';

或者,通过如下方式创建数组。
//在创建数组对象时直接赋值
var  a = new  Array('yeeku','nono');

但如果使用JSON 语法,则可以通过如下方式创建数组。

//使用JSON 语法创建数组
var  a  =['yeeku','nono'];

如图10.3所示是使用JSON 创建数组的语法示意图。
正如从图10.3中所看到的,使用JSON 语法创建数组总是以英文方括号([)开始,然后依次放入数组元素,
元素与元素之间以英文逗号(,)隔开,最后一个数组元素后面不需要英文逗号, 但以英文反方括号(])结束。使用JSON 创建数组的语法格式如下：
arr = [value1,value2 ...]
与使用JSON 语法创建对象相似的是,在数组的最后一个元素的后面不能有英文逗号(,)。

鉴于JSON 语法的简单易用,而且作为数据传输载体时,数据传输量更小,因此在跨平台的数据交换中,往往采用 JSON 作为数据交换格式。
假设需要交换一个对象person,其name 属性为yeeku, gender属性为male,age 属性为29,使用JSON 语法可以简单写成如下形式。
person  =
{
    name:'yeeku',
    gender:'male',
    age:29
}
而 Python 则提供了将符合格式的 JSON 字符串恢复成对象的函数,也提供了将对象转换成 JSON 字符串的方法。
JSON 的官方站点是 http://www.json.org ,读者可以登录该站点了解关于 JSON  的更多信息。
10.5.2  Python 的 JSON 支持

1.  json模块提供了对 JSON  的支持,它既包含了将 JSON 字符串恢复成Python 对象的函数,
也提供了将Python 对象转换成JSON 字符串的函数。
2.  当程序把 JSON 对象或 JSON 字符串转换成 Python 对象时,从 JSON 类型到 Python 类型的转换关系如表10.3所示。
表10.3 JSON 类型转换Python类型的对应关系

JSON类型	                        Python类型
对象(object)	                    字典(dict)
数组(array)	                    列表(list)
字符串(string)	                字符串(str)
整数(number(int))	        整数(int)
实数(number(real))	        浮点数(float)
true	                                True
false	                            False
null	                                None

3.  当程序把Python对象转换成 JSON 格式字符串时,从 Python 类型到 JSON 类型的转换关系如表10.4所示。
表10.4 Python类型转换JSON 类型的对应关系

Python类型	                                                                                                            JSON类型
字典(dict)	                                                                                                                对象(object)
列表(list)和元组(tuple)	                                                                                            数组(array)
字符串(str)	                                                                                                            字符串(string)
整型、浮点型,以及整型、浮点型派生的枚举(float,int-& float-derived Enums)	        数值型(number)
True	                                                                                                                        true
False	                                                                                                                    false
None	                                                                                                                    null

4.  在Python的交互式解释器中先导入json模块,然后输入json.__all__ 命令,即可看到该模块所包含的全部属性和函数。
json.__all__
['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecodeError', 'JSONEncoder']

5.  json模块中常用的函数和类的功能如下。
(1)json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw): 将 obj 对象转换成 JSON 字符串输出到fp流中, fp是一个支持write()方法的类文件对象。
(2)json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):将 obj 对象转换为 JSON 字符串,并返回该 JSON 字符串。
(3)json.load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
        从fp流读取 JSON 字符串,将其恢复成 JSON 对象,其中fp 是一个支持 write() 方法的类文件对象。
(4)json.loads(s, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw): 将 JSON 字符串s 恢复成 JSON 对象。

6.  通过上面4个功能函数就可以实现JSON 的两个主要应用场景,由于JSON 只是一种轻量级的数据交换格式,
因此JSON的主要应用场景如图10.4所示。

7.  下面程序示范了 dumps() 和 dump() 函数的 encode 操作(将 Python 对象转换成JSON 字符串)。
8.  上面程序主要是调用 dumps() 函数执行 encode 操作,程序在调用 dumps() 函数时指定了不同的选项。
上面程序最后一行代码调用 dump() 函数将通过 encode 操作得到的JSON 字符串输出到文件中。
实际上,dumps()和 dump() 函数的功能、所支持的选项基本相同,只是 dumps()函数直接返回转换得到的 JSON 字符串,
而 dump() 函数则将转换得到的JSON 字符串输出到文件中。

"""
import json

# 将Python对象转JSON字符串(元组会当成数组)
s = json.dumps(['yeeku', {'favorite': ('coding', None, 'game', 25)}])
print(s)  # ["yeeku", {"favorite": ["coding", null, "game", 25]}]
# 简单的Python字符串转JSON
s2 = json.dumps("\"foo\bar")
print(s2)  # "\"foo\bar"
# 简单的Python字符串转JSON
s3 = json.dumps('\\')
print(s3)  # "\\"
# Python的dict对象转JSON,并对key排序
s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
print(s4)  # {"a": 0, "b": 0, "c": 0}
# 将Python列表转JSON,
# 并指定JSON分隔符：逗号和冒号之后没有空格(默认有空格)
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))
# 输出的JSON字符串中逗号和冒号之后没有空格
print(s5)  # '[1,2,3,{"4":5,"6":7}]'
# 指定indent为4,意味着转换的JSON字符串有缩进
s6 = json.dumps({'Python': 5, 'Kotlin': 7}, sort_keys=True, indent=4)
print(s6)
# 使用JSONEncoder的encode方法将Python转JSON
s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
print(s7)  # {"names": ["\u5b59\u609f\u7a7a", "\u9f50\u5929\u5927\u5723"]}
f = open('a.json', 'w')
# 使用dump()函数将转换得到JSON字符串输出到文件
json.dump(['Kotlin', {'Python': 'excellent'}], f)
