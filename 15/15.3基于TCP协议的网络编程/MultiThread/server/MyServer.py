"""
15.3.4	加入多线程

前面的服务器端和客户端只是进行了简单的通信操作：服务器端接受客户端的连接之后,向客户端输出一个字符串,
而客户端也只是读取服务器端的字符串后就退出了。在实际应用中,客户端则可能需要和服务器端保持长时间通信,
即服务器端需要不断地读取客户端数据,并向客户端写入数据;客户端也需要不断地读取服务器端数据,并向服务器端写入数据。

由于socket的 recv()方法在成功读取到数据之前,线程会被阻塞,程序无法继续执行。
考虑到这个原因,服务器端应该为每个socket都单独启动一个线程,每个线程负责与一个客户端进行通信。

客户端读取服务器端数据的线程同样会被阻塞,所以系统应该单独启动一个线程,该线程专门负责读取服务器端数据。

现在考虑实现一个命令行界面的 C/S 聊天室应用,服务器端应该包含多个线程,每个 socket 对应一个线程,
该线程负责从socket中读取数据(从客户端发送过来的数据),并将所读取到的数据向每个socket发送一次
(将一个客户端发送过来的数据"广播"给其他客户端),因此需要在服务器端使用list来保存所有的socket。

下面是服务器端的实现代码。该服务器端代码定义了一个 server_target()函数,该函数将会作为线程执行的target,
负责处理每个socket的数据通信。
"""
import socket
import threading

# 定义保存所有socket的列表
socket_list = []
# 创建socket对象
ss = socket.socket()
# 将socket绑定到本机IP和端口
ss.bind(('192.168.1.88', 30000))
# 服务端开始监听来自客户端的连接
ss.listen()


def read_from_client(s):
    try:
        return s.recv(2048).decode('utf-8')
    # 如果捕获到异常,则表明该socket对应的客户端已经关闭
    except:
        # 删除该socket
        socket_list.remove(s);  # ①


def server_target(s):
    try:
        # 采用循环不断地从socket中读取客户端发送过来的数据
        while True:
            content = read_from_client(s)
            print(content)
            if content is None:
                break
            for client_s in socket_list:
                client_s.send(content.encode('utf-8'))
    except Exception as e:
        print(e.strerror)


while True:
    # 此行代码会阻塞,将一直等待别人的连接
    s, addr = ss.accept()
    socket_list.append(s)
    # 每当客户端连接后启动一个线程为该客户端服务
    threading.Thread(target=server_target, args=(s,)).start()

"""
上面实现的服务器端主程序只负责接收客户端 socket的连接请求,每当客户端socket连接进来之后,
程序都将对应的socket加入 socket_list 列表中保存,并为该socket启动一个线程,
该线程负责处理该socket所有的通信任务,如程序中最后3行粗体字代码所示。

代表服务器端线程执行体的 server_target()函数则不断地读取客户端数据。
程序使用 read_from_client()函数来读取客户端数据,如果在读取数据过程中捕获到异常,
则表明该socket对 应的客户端 socket 出现了问题(到底什么问题不用深究,反正不正常),
程序就将该 socket 从 socket list列表中删除,如 read_from_client()函数中的①号代码所示。

当服务器端线程读取到客户端数据之后,程序遍历 socket list列表,并将该数据向 socket_list 列表中的每个socket发送一次——
该服务器端线程把从socket中读取到的数据向socket list列表中 的每个socket转发一次,如server target()函数中的粗体字代码所示。
"""
