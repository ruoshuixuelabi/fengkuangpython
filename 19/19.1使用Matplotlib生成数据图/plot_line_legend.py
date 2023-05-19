"""
19.1.3 管理图例

对于复式折线图来说,应该为每条折线都添加图例,此时可以通过 legend() 函数来实现。
对于该函数可传入两个 list 参数,其中第一个list参数(handles 参数)用于引用折线图上的每条折线;
第二个list参数(labels)代表为每条折线所添加的图例。

下面程序示范了为两条折线添加图例。
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# 定义2个列表分别作为两条折线的Y轴数据
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# 指定折线的颜色、线宽和样式
ln1, = plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
ln2, = plt.plot(x_data, y_data2, color='blue', linewidth=3.0, linestyle='-.')
# 使用Matplotlib的字体管理器加载中文字体
# my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
my_font = fm.FontProperties(fname="C:\Windows\Fonts\STSONG.TTF")
# 调用legend函数设置图例
# plt.legend(handles=[ln2, ln1], labels=['疯狂Android讲义年销量', '疯狂Java讲义年销量'], loc='lower right', prop=my_font)
# plt.legend(handles=[ln2, ln1], labels=['疯狂Android讲义年销量', '疯狂Java讲义年销量'], loc='lower right')
plt.legend(labels=['疯狂Java讲义年销量', '疯狂Android讲义年销量'], loc='lower right', prop=my_font)
# 调用show()函数显示图形
plt.show()
"""
上面程序在调用 plot() 函数绘制折线图时,获取了该函数的返回值。
由于该函数的返回值是一个列表,而此处只需要获取它返回的列表的第一个元素(第一个元素才代表该函数所绘制的折线图),
因此程序利用返回值的序列解包来获取。

上面程序中的粗体字代码用于为 In2、In1 所代表的折线添加图例(按传入该函数的两个列表的元素顺序一一对应),
其中loc 参数指定图例的添加位置,该参数支持如下参数值。
(1)'best': 自动选择最佳位置。
(2)'upper right': 将图例放在右上角。
(3)'upper left':将图例放在左上角。
(4)'lowerleft': 将图例放在左下角。
(5)'lower right': 将图例放在右下角。
(6)'right': 将图例放在右边。
(7)'center left': 将图例放在左边居中的位置。
(8)'center right': 将图例放在右边居中的位置。
(9)'lower  center':将图例放在底部居中的位置。
(10)'upper center': 将图例放在顶部居中的位置。
(11.1 Python的 GUI 库)'center': 将图例放在中心。

运行上面程序,将会发现该程序并没有绘制图例,这是因为Matplotlib默认不支持中文字体。
如果希望在程序中修改Matplotlib 的默认字体,则可按如下步骤进行。
①使用matplotlib.font_manager 子模块下的 FontProperties  类加载中文字体。
②在调用legend() 函数时通过prop 属性指定使用中文字体。
将上面程序中的粗体字代码改为如下几行代码。
# 使用Matplotlib的字体管理器加载中文字体
# my_font = fm.FontProperties(fname="C:\Windows\Fonts\msyh.ttf")
plt.legend(handles=[ln2, ln1], labels=['疯狂Android讲义年销量', '疯狂Java讲义年销量'], loc='lower right', prop=my_font)

上面程序使用FontProperties类来加载 C:\Windows\Fonts\msyh.ttf 文件所对应的中文字体,因此
需要保证系统能找到该路径下的中文字体。

再次运行上面程序,将看到如图19.7所示的效果。

在使用legend()函数时可以不指定 handles 参数,只传入 labels 参数,这样该 labels 参数将按顺序为折线图中的多条折线添加图例。
因此,可以将上面的粗体字代码改为如下形式。
plt.legend(labels=['疯狂Java讲义年销量', '疯狂Android讲义年销量'], loc='lower right', prop=my_font)

上面代码只指定了 labels 参数,该参数传入的列表包含两个字符串,其中第一个字符串将作为第一条折线(虚线)的图例,
第二个字符串将作为第二条折线(短线、点相间的虚线)的图例。
"""