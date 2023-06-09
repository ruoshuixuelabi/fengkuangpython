"""
下面的客户端程序也非常简单,它仅仅使用 socket 建立与指定 IP 地址和端口的连接,并从 socket 中获取服务器端发送的数据。
"""
# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()
# 连接远程主机
s.connect(('172.20.102.27', 30000))    # ①
print('--%s--' % s.recv(1024).decode('utf-8'))
s.close() 
"""
上面程序中①号粗体字代码使用 socket 建立与服务器端的连接,接下来的粗体字代码调用socket的 recv()方法来接收网络数据。

先运行服务器端程序,将看到服务器一直处于等待状态,因为服务器使用了死循环来接收来自客户端的请求;
再运行客户端程序,将看到程序输出："--您好,您收到了服务器的新年祝福!-- ",这表明客户端和服务器端通信成功。
"""