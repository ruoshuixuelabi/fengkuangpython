"""
前面程序展示的数据都是直接通过程序给出的,但实际应用可能需要展示不同来源(比如文件、网络)、不同格式(比如CSV、JSON)的数据,
这些数据可能有部分是损坏的,因此程序需要对这些数据进行处理。

19.5.1	CSV文件格式

CSV 文件格式的本质是一种以文本存储的表格数据(使用Excel工具即可读写 CSV 文件)。
CSV 文件的每行代表一行数据,每行数据中每个单元格内的数据以逗号隔开。

Python 提供了 csv 模块来读写 CSV 文件。由于 CSV 文件的格式本身比较简单(通常第一行是表头,用于说明每列数据的含义,
接下来每行代表一行数据),因此使用csv模块读取 CSV 文件也非常简单。
① 创建 csv 模块的读取器。
② 循环调用CSV 读取器的next()方法逐行读取 CSV 文件内容即可。
next() 方法返回一个list 列表代表一行数据,list列表的每个元素代表一个单元格数据。

本节使用的是2017年广州天气数据的CSV 文件,数据来源于htp://lishi.tianqi.com/网站。

下面程序示范了使用CSV 读取器来读取CSV 文件的两行内容。
"""
import csv

filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    # 读取第一行,这行是表头数据。
    header_row = next(reader)
    print(header_row)
    # 读取第二行,这行是真正的数据。
    first_row = next(reader)
    print(first_row)
"""
上面程序中第一行粗体字代码创建了 CSV 读取器,第二行、第三行粗体字代码各读取文件的一行,
其中第一行粗体字代码会返回 CSV 文件的表头数据;第二行粗体字代码会返回真正的数据。 运行上面程序,可以看到如下输出结果。
['Date', 'Max TemperatureC', 'Min TemperatureC', 'Description', 'WindDir', 'WindForce']
['2017-1-1', '24', '13', '晴', '西南风', '1级']

从上面的输出结果可以看到,该文件的每行包含6个数据,分别是日期、最高温度、最低文档、 天气情况、风向、风力。
"""