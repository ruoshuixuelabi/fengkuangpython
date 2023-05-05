"""
7.3 使用raise引发异常

当程序出现错误时,系统会自动引发异常。除此之外,Python 也允许程序自行引发异常,自行引发异常使用raise语句来完成。

7.3.1 引发异常

异常是一种很"主观"的说法,以下雨为例,假设大家约好明天去爬山郊游,如果第二天下雨了,
这种情况会打破既定计划,就属于一种异常;但对于正在期盼天降甘霖的农民而言,如果第二天下雨了,他们正好随雨追肥,这就完全正常。

很多时候,系统是否要引发异常,可能需要根据应用的业务需求来决定,如果程序中的数据、执行与既定的业务需求不符,这就是一种异常。
由于与业务需求不符而产生的异常,必须由程序员来决定引发,系统无法引发这种异常。

如果需要在程序中自行引发异常,则应使用raise语句。 raise语句有如下三种常用的用法。
(1)raise：单独一个raise。 该语句引发当前上下文中捕获的异常(比如在except块中),或默认引发RuntimeError异常。
(2)raise异常类：raise后带一个异常类。该语句引发指定异常类的默认实例。
(3)raise异常对象：引发指定的异常对象。

上面三种用法最终都是要引发一个异常实例(即使指定的是异常类,实际上也是引发该类的默认实例),raise 语句每次只能引发一个异常实例。

可以利用raise语句再次改写前面五子棋游戏中处理用户输入的代码。
"""
# 定义棋盘的大小
BOARD_SIZE = 15
# 定义一个二维列表来充当棋盘
board = []


def initBoard():
    # 把每个元素赋为"╋",用于在控制台画出棋盘
    for i in range(BOARD_SIZE):
        row = ["╋"] * BOARD_SIZE
        board.append(row)


# 在控制台输出棋盘的方法
def printBoard():
    # 打印每个列表元素
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # 打印列表元素后不换行
            print(board[i][j], end="")
        # 每打印完一行列表元素后输出一个换行符
        print()


initBoard()
printBoard()
inputStr = input("请输入您下棋的坐标,应以x,y的格式：\n")
while inputStr != None:
    try:
        # 将用户输入的字符串以逗号（,）作为分隔符,分隔成2个字符串
        x_str, y_str = inputStr.split(sep=",")
        # 如果要下棋的点不为空
        if board[int(y_str) - 1][int(x_str) - 1] != "╋":
            # 引发默认的RuntimeError异常
            raise

        # 把对应的列表元素赋为"●"。
        board[int(y_str) - 1][int(x_str) - 1] = "●"
    except Exception as e:
        print(type(e))
        inputStr = input("您输入的坐标不合法,请重新输入,下棋坐标应以x,y的格式\n")
        continue
    '''
     电脑随机生成2个整数,作为电脑下棋的坐标,赋给board列表
     还涉及
        1．坐标的有效性,只能是数字,不能超出棋盘范围
        2．下的棋的点,不能重复下棋
        3．每次下棋后,需要扫描谁赢了
    '''
    printBoard()
    inputStr = input("请输入您下棋的坐标,应以x,y的格式：\n")
"""
上面程序中粗体字代码使用raise语句来自行引发异常,程序认为当用户试图向一个已有棋子的坐标点下棋时就是异常。
当 Python 解释器接收到开发者自行引发的异常时,同样会中止当前的执行流,跳到该异常对应的 except 块,由该 except 块来处理该异常。
也就是说,不管是系统自动引发的异常,还是程序员手动引发的异常,Python 解释器对异常的处理没有任何差别。
"""
