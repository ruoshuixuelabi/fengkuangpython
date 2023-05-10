"""
服务器端的主线程依然只是建立 socket 来监听来自客户端socket 的连接请求,
但该程序增加了一些异常处理代码,可能看上去比上一节的程序稍微复杂一点。
"""
import socket, threading, CrazyitDict, CrazyitProtocol

from server_thread import server_target

SERVER_PORT = 30000
# 使用CrazyitDict来保存每个客户名字和对应socket之间的对应关系
clients = CrazyitDict.CrazyitDict()
# 创建socket对象
s = socket.socket()
try:
    # 将socket绑定到本机IP和端口
    s.bind(('192.168.1.88', SERVER_PORT))
    # 服务端开始监听来自客户端的连接
    s.listen()
    # 采用死循环来不断地接收来自客户端的请求
    while True:
        # 每当接收到客户端socket的请求时,该方法返回对应的socket和远程地址
        c, addr = s.accept()
        threading.Thread(target=server_target, args=(c, clients)).start()
# 如果抛出异常
except:
    print("服务器启动失败,是否端口%d已被占用？" % SERVER_PORT)
"""
该程序的关键代码依然只有三行,如程序中粗体字代码所示。
其依然是使用 socket 网络连接,接收来自客户端 socket 的连接请求,并为已连接的 socket 启动单独的线程。
上面程序以server_target 作为新线程的 target
"""
