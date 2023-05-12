"""
掌握了 CSV 读取器的用法之后,下面程序将会使用 Matplotlib 来展示2017年7月广州的最高气温和最低气温。
"""
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'guangzhou-2017.csv'
# 打开文件
with open(filename) as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    # 读取第一行,这行是表头数据。
    header_row = next(reader)
    print(header_row)
    # 定义读取起始日期
    start_date = datetime(2017, 6, 30)
    # 定义结束日期
    end_date = datetime(2017, 8, 1)
    # 定义3个list列表作为展示的数据
    dates, highs, lows = [], [], []
    for row in reader:
        # 将第一列的值格式化为日期
        d = datetime.strptime(row[0], '%Y-%m-%d')
        # 只展示2017年7月的数据
        if start_date < d < end_date:
            dates.append(d)
            highs.append(int(row[1]))
            lows.append(int(row[2]))

# 配置图形
fig = plt.figure(dpi=128, figsize=(12, 9))
# 绘制最高气温的折线
plt.plot(dates, highs, c='red', label='最高气温', alpha=0.5, linewidth=2.0, linestyle='-', marker='v')
# 再绘制一条折线
plt.plot(dates, lows, c='blue', label='最低气温', alpha=0.5, linewidth=3.0, linestyle='-.', marker='o')
# 为两个数据的绘图区域填充颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置标题
plt.title("广州2017年7月最高气温和最低气温")
# 为两条坐标轴设置名称
plt.xlabel("日期")
# 该方法绘制斜着的日期标签
fig.autofmt_xdate()
plt.ylabel("气温（℃）")
# 显示图例
plt.legend()
ax = plt.gca()
# 设置右边坐标轴线的颜色（设置为none表示不显示）
ax.spines['right'].set_color('none')
# 设置顶部坐标轴线的颜色（设置为none表示不显示）
ax.spines['top'].set_color('none')
plt.show()
"""
上面程序的前半部分代码用于从 CSV 文件中读取2017年7月广州的气温数据,
程序分别使用了dates、highs和 lows 三 个list列表来保存日期、最高气温、最低气温。

程序的后半部分代码绘制了两条折线来显示最高气温和最低气温,其中第一行粗体字代码用于绘制最高气温,第二行粗体字代码用于绘制最低气温;
第三行粗体字代码控制在两条折线之间填充颜色。程序也对坐标轴、图例进行了简单的设置。

运行上面程序,可以看到如图19.33所示的折线图。
"""
