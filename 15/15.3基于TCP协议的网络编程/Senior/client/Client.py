"""
客户端程序增加了让用户输入用户名的代码,并且不允许用户名重复。
除此之外,还可以根据用户的键盘输入内容来判断用户是否想发送私聊信息。客户端程序的代码如下。
"""
import CrazyitProtocol
import os
import socket
import threading
import time

SERVER_PORT = 30000


# 定义一个读取键盘输入,并向网络发送的函数
def read_send(s):
    # 采用死循环不断地读取键盘输入
    while True:
        line = input('')
        if line is None or line == 'exit':
            break
        # 如果发送的信息中有冒号,且以//开头,则认为想发送私聊信息
        if ":" in line and line.startswith("//"):
            line = line[2:]
            s.send((CrazyitProtocol.PRIVATE_ROUND
                    + line.split(":")[0] + CrazyitProtocol.SPLIT_SIGN
                    + line.split(":")[1] + CrazyitProtocol.PRIVATE_ROUND).encode('utf-8'))
        else:
            s.send((CrazyitProtocol.MSG_ROUND + line
                    + CrazyitProtocol.MSG_ROUND).encode('utf-8'))


# 创建socket对象
s = socket.socket()
try:
    # 连接远程主机
    s.connect(('192.168.1.88', SERVER_PORT))
    tip = ""
    # 采用循环不断地弹出对话框要求输入用户名
    while True:
        user_name = input(tip + '输入用户名:\n')  # ①
        # 在用户输入的用户名前后增加协议字符串后发送
        s.send((CrazyitProtocol.USER_ROUND + user_name
                + CrazyitProtocol.USER_ROUND).encode('utf-8'))
        time.sleep(0.2)
        # 读取服务器端的响应
        result = s.recv(2048).decode('utf-8')
        if result is not None and result != '':
            # 如果用户名重复,则开始下次循环
            if result == CrazyitProtocol.NAME_REP:
                tip = "用户名重复！请重新"
                continue
            # 如果服务器端返回登录成功,则结束循环
            if result == CrazyitProtocol.LOGIN_SUCCESS:
                break
# 捕获到异常,关闭网络资源,并退出该程序
except:
    print("网络异常！请重新登录！")
    s.close()
    os._exit(1)


def client_target(s):
    try:
        # 不断地从socket中读取数据,并将这些数据打印输出
        while True:
            line = s.recv(2048).decode('utf-8')
            if line is not None:
                print(line)
            """
            本例仅打印了从服务器端读到的内容。实际上,此处的情况可以更复杂：如果希望客户端能看到聊天室的用户列表,
            则可以让服务器端在每次有用户登录、用户退出时,将所有的用户列表信息都向客户端发送一遍。
            为了区分服务器端发送的是聊天信息,还是用户列表,服务器端也应该在要发送的信息前、后都添加一定的协议字符串,
            客户端则根据协议字符串的不同而进行不同的处理！
            更复杂的情况：
            如果两端进行游戏,则还有可能发送游戏信息,例如两端进行五子棋游戏,
            则需要发送下棋坐标信息等,服务器端同样在这些下棋坐标信息前、后添加
            协议字符串后再发送,客户端就可以根据该信息知道对手的下棋坐标。
            """
    # 使用finally块来关闭该线程对应的socket
    finally:
        s.close()


# 启动客户端线程
threading.Thread(target=client_target, args=(s,)).start()
read_send(s)
"""
上面程序在建立连接之后,立即提示用户输入用户名,如程序中①号粗体字代码所示。
然后程序立即将用户输入的用户名发送给服务器端,服务器端会返回该用户名是否重复的提示信息,
程序又立即读取服务器端的提示信息,并根据该提示信息判断是否需要继续让用户输入用户名。

与上一节的客户端主程序相比,该程序还增加了对用户输入信息的判断代码——判断用户输入的内容是否以斜线(/)开头,并包含冒号(:)。
如果满足该特征,系统认为该用户想发送私聊信息,就会将冒号(:)之前的部分当成私聊用户名,将冒号(:)之后的部分当成聊天信息,
如read_send() 函数中的粗体字代码所示。

本程序中客户端线程的 client_target 函数没有太大的改变,程序依然只是采用死循环不断地读 取来自服务器端的信息。

虽然该线程的 client_target 函数简单,但正如程序注释中所指出的,如果服务器端可以返回更多丰富类型的数据,
则该线程类的处理将会更复杂,那么该程序可以扩展到功能非常强大。

先运行上面的Server程序,启动服务器;再多次运行Client程序,启动多个客户端,并输入不同的用户名,登录服务器后,
两个客户端的聊天界面如图15.5所示。

提示：本程序没有提供 GUI 部分,而是直接使用命令行窗口进行聊天的——因为增加 GUI 部分会让程序的代码更多,从而引起读者的畏难心理。
如果读者理解了本程序,那么相信读者一定乐意为该程序添加界面部分,因为整个程序的所有核心功能都已经实现了。
不仅如此,读者完全可以在本程序的基础上扩展成一个仿 QQ 游戏大厅的网络程序。
"""
