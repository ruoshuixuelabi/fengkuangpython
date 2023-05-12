"""
程序也可以使用 Pygal 来统计2017年广州的天气汇总情况,比如统计出阴天、晴天、多云天 和雨天各占多少天。
程序会使用CSV 读取器读取2017年广州阴天、晴天、多云天和雨天共有多少 天,然后将这些数据添加到pygal.Pie对象中即可绘制饼图。
该程序的代码如下。
"""
import csv
import pygal

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
    for row in reader:
        if '阴' in row[3]:
            shades += 1
        elif '晴' in row[3]:
            sunnys += 1
        elif '云' in row[3]:
            cloudys += 1
        elif '雨' in row[3]:
            rainys += 1
        else:
            print(rows[3])
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
上面程序的前半部分代码也是用于从 CSV文件中读取2017年广州的天气数据,该程序只读取 CSV 文件的数据行的第四列数据(天气描述),
并使用shades、sunnys、cloudys、rainys  分别保存阴天、晴天、多云天和雨天的数据。

上面程序中第一行粗体字代码创建了一个 pygal.Pie 对象,该对象就表示一个饼图。
接下来的4行粗体字代码用于向 pygal.Pie 对象添加数据。运行上面程序,可以生成如图 19.34 所示的饼图。
"""