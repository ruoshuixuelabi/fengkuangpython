"""
每个客户端都应该包含两个线程,其中一个负责读取用户的键盘输入内容,并将用户输入的数据输出到 socket 中;
另一个负责读取 socket 中的数据(从服务器端发送过来的数据),并将这些数据打印输出。
由程序的主线程负责读取用户的键盘输入内容,由新线程负责读取 socket 数据。
"""
import socket
import threading

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('192.168.1.88', 30000))


def read_from_server(s):
    while True:
        print(s.recv(2048).decode('utf-8'))


# 客户端启动线程不断地读取来自服务器的数据
threading.Thread(target=read_from_server, args=(s,)).start()  # ①
while True:
    line = input('')
    if line is None or line == 'exit':
        break
    # 将用户的键盘输入内容写入socket
    s.send(line.encode('utf-8'))
"""
上面程序中的主线程读取到用户的键盘输入内容后,将该内容发送到 socket 中(实际上就是把数据发送给服务器端)。

此外,当主线程的 socket 连接到服务器端之后,以 read_from_server()函数为target启动了新线程来处理socket通信,
如程序中①号粗体字代码所示。read_from_server()函数使用死循环读取 socket 中的数据(就是来自服务器端的数据),
并将这些内容在控制台打印出来,如 read_from_server()函数中的粗体字代码所示。

先运行上面的 MyServer 程序,该程序运行后只是作为服务器,看不到任何输出信息。
再运行多个 MyClient 程序——相当于启动多个聊天室客户端登录该服务器,接下来可以在任何一个客户端通过键盘输入一些内容,
然后按回车键,即可在所有客户端(包括自己)的控制台中收到刚刚输 入的内容,这就粗略地实现了一个 C/S 结构的聊天室应用。
"""