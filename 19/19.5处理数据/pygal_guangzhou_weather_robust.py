"""
19.5.3	数据清洗

如果仔细查看前面介绍的展示 2017 年广州天气情况的程序,不难发现最终只统计出363天天气情况
(雨天：164天;晴天：67天;阴天：24天;多云天：108天),但一年应该有365天,因此这份数据出现了问题。

当程序使用 Python 进行数据展示时,经常发现数据存在以下两种情况。
(1)数据丢失 。
(2)数据格式错误 。

对于数据丢失的情况,程序应该生成报告;对于数据格式发生错误的情况,程序应该能略过发生错误的数据,
继续处理后面的程序,并报告发生错误的数据。

下面程序对前面介绍的展示2017年广州天气情况的程序进行改进,看看到底哪些数据出现了问题 。
"""
import csv
import pygal
from datetime import datetime
from datetime import timedelta

filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    # 读取第一行,这行是表头数据。
    header_row = next(reader)
    print(header_row)

    # 准备展示的数据
    shades, sunnys, cloudys, rainys = 0, 0, 0, 0
    prev_day = datetime(2016, 12, 31)
    for row in reader:
        try:
            # 将第一列的值格式化为日期
            cur_day = datetime.strptime(row[0], '%Y-%m-%d')
            description = row[3]
        except ValueError:
            print(cur_day, '数据出现错误')
        else:
            # 计算前、后两天数据的时间差
            diff = cur_day - prev_day
            # 如果前、后两天数据的时间差不是相差一天,说明数据有问题
            if diff != timedelta(days=1):
                print('%s之前少了%d天的数据' % (cur_day, diff.days - 1))
            prev_day = cur_day
            if '阴' in description:
                shades += 1
            elif '晴' in description:
                sunnys += 1
            elif '云' in description:
                cloudys += 1
            elif '雨' in description:
                rainys += 1
            else:
                print(description)
# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
# 为饼图添加数据
pie.add("阴", shades)
pie.add("晴", sunnys)
pie.add("多云", cloudys)
pie.add("雨", rainys)
pie.title = '2017年广州天气汇总'
# 设置将图例放在底部
pie.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
pie.render_to_file('guangzhou_weather.svg')
"""
上面程序的主要改进体现在两个方面。
(1)将数据解析部分放在 try 块中完成,这样即使数据出现问题,程序的异常处理也可以跳过数据中的错误——
如果解析数据没有错误,程序将会执行else块;如果解析数据出现错误,程序将会使用except块处理错误,程序也不会中止执行。
(2)第二段粗体字代码部分,检查两条数据之间的时间差,如果数据没有错误、没有缺失,那么两条数据之间的时间差应该是一天;
否则,意味着数据错误或缺失。

运行上面程序,将可以看到在控制台生成如下输出结果。
2017-03-06 00:00:00之前少了2天的数据

从控制台中的输出结果可以看到,这份天气数据缺少了2017年3月6日前两天的数据。
打开 guangzhou-2017.csv文件,找到2017-03-06处,即可发现这份数据确实缺少了3月4日、3月5日的数据。
"""