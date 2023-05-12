"""
除了前面介绍的各种折线图,Matplotlib 也支持其他常见的数据图。前面介绍的对数据图的管理知识,完全适用于下面将要介绍的数据图。

19.2.1	饼图

使用 Matplotlib 提供的 pie() 函数来绘制饼图。下面是TIOBE 2018年8月的编程语言指数排行
榜的前10名及其他。
下面程序将使用饼图来直观地展示这个编程语言指数排行榜。
"""
import matplotlib.pyplot as plt

# 准备数据
data = [0.16881, 0.14966, 0.07471, 0.06992, 0.04762, 0.03541, 0.02925, 0.02411, 0.02316, 0.01409, 0.36326]
# 准备标签
labels = ['Java', 'C', 'C++', 'Python', 'Visual Basic .NET', 'C#', 'PHP', 'JavaScript', 'SQL', 'Assembly langugage',
          '其他']
# 将第4个语言（Python）分离出来
explode = [0, 0, 0, 0.3, 0, 0, 0, 0, 0, 0, 0]
# 使用自定义颜色
colors = ['red', 'pink', 'magenta', 'purple', 'orange']
# 将横、纵坐标轴标准化处理,保证饼图是一个正圆,否则为椭圆
plt.axes(aspect='equal')
# 控制X轴和Y轴的范围（用于控制饼图的圆心,半径）
plt.xlim(0, 8)
plt.ylim(0, 8)

# 绘制饼图
plt.pie(x=data,  # 绘图数据
        labels=labels,  # 添加编程语言标签
        explode=explode,  # 突出显示Python
        colors=colors,  # 设置饼图的自定义填充色
        autopct='%.3f%%',  # 设置百分比的格式,此处保留3位小数
        pctdistance=0.8,  # 设置百分比标签与圆心的距离
        labeldistance=1.15,  # 设置标签与圆心的距离
        startangle=180,  # 设置饼图的初始角度
        center=(4, 4),  # 设置饼图的圆心（相当于X轴和Y轴的范围）
        radius=3.8,  # 设置饼图的半径（相当于X轴和Y轴的范围）
        counterclock=False,  # 是否逆时针,这里设置为顺时针方向
        wedgeprops={'linewidth': 1, 'edgecolor': 'green'},  # 设置饼图内外边界的属性值
        textprops={'fontsize': 12, 'color': 'black'},  # 设置文本标签的属性值
        frame=1)  # 是否显示饼图的圆圈,此处设为显示
# 不显示X轴和Y轴的刻度值
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('2018年8月的编程语言指数排行榜')
# 显示图形
plt.show()
"""
上面程序中的粗体字代码调用 pie()函数来生成饼图。创建饼图最重要的两个参数就是x和 labels,
其中x指定饼图各部分的数值, labels则指定各部分对应的标签。

运行上面程序,可以看到如图19.13所示的效果。
"""