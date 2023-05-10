"""
15.4.3	使用 UDP 协议实现多点广播

通过多点广播,可以将数据报以广播方式式发送到多个客户端。

若要使用多点广播,则需要将数据报发送到一个组目标地址,当数据报发出后,整个组的所有主机都能接收到该数据报。
IP 多点广播(或多点发送)实现了将单一信息发送给多个接收者的广播,其思想是设置一组特殊的网络地址作为多点广播地址,
每一个多点广播地址都被看作一个组,当客户端需要发送和接收广播信息时,加入该组即可。

IP协议为多点广播提供了特殊的 IP 地址,这些 IP 地址的范围是 224.0.0.0~239.255.255.255。多点广播示意图如图15.6所示。

从图15.6中可以看出,当 socket 把一个数据报发送到多点广播IP 地址时,该数据报将被自动广播到加入该地址的所有socket。
该 socket 既可以将数据报发送到多点广播地址,也可以接收其他主机的广播信息。

在创建了 socket 对象后,还需要将该 socket 加入指定的多点广播地址中,socket 使用 setsockopt()方法加入指定组。

如果创建仅用于发送数据报的 socket 对象,则使用默认地址、随机端口即可。但如果创建接收数据报的 socket 对象,
则需要将该 socket 对象绑定到指定端口;否则,发送方无法确定发送数据报的目标端口。

支持多点广播的socket还可设置广播信息的TTL(Time-To-Live),该 TTL 参数用于设置数据报最多可以跨过多少个网络。
当 TTL 的值为0时,指定数据报应停留在本地主机中;当 TTL 的值为1时,指定将数据报发送到本地局域网中;
当TTL 的值为32时,意味着只能将数据报发送到本站点的网络上;当TTL 的值为64时,意味着数据报应被保留在本地区;
当TTL 的值为128时, 意味着数据报应被保留在本大洲;当TTL 的值为255时,意味着数据报可被发送到所有地方;在默认情况下,TTL 的值为1。

从图15.6中可以看出,使用socket进行多点广播时所有的通信实体都是平等的,它们都将自己的数据报发送到多点广播 IP 地址,
并使用socket接收其他人发送的广播数据报。下面程序使用 socket实现了一个基于广播的多人聊天室。
程序只需要一个socket、 两个线程,其中socket既用于 发送数据,也用于接收数据;主线程负责读取用户的键盘输入内容,
并向 socket 发送数据,子线程则负责从socket中读取数据。
"""
import socket
import threading

# 定义本机IP地址
SENDERIP = '192.168.1.88'
# 定义本地端口
SENDERPORT = 30000
# 定义本程序的多点广播IP地址
MYGROUP = '230.0.0.1'
# 通过type属性指定创建基于UDP协议的socket
s = socket.socket(type=socket.SOCK_DGRAM)
# 将该socket绑定到0.0.0.0的虚拟IP
s.bind(('0.0.0.0', SENDERPORT))  # ①
# 设置广播消息的TTL（Time-To-Live）
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 64)
# 设置允许多点广播使用相同的端口
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 将socket进入广播组
s.setsockopt(socket.IPPROTO_IP,
             socket.IP_ADD_MEMBERSHIP,
             socket.inet_aton(MYGROUP) + socket.inet_aton(SENDERIP))


# 定义从socket读取数据的方法
def read_socket(sock):
    while True:
        data = sock.recv(2048)
        print("信息: ", data.decode('utf-8'))


# 以read_socket作为target启动多线程
threading.Thread(target=read_socket, args=(s,)).start()
# 采用循环不断读取键盘输入,并输出到socket中
while True:
    line = input('')
    if line is None or line == 'exit':
        break
        os._exit(0)
    # 将line输出到socket中
    s.sendto(line.encode('utf-8'), (MYGROUP, SENDERPORT))
"""
上面主程序中的第一行粗体字代码先创建了一个基于 UDP 协议的socket对象,由于需要使用该 socket对象接收数据报,
所以将该 socket 绑定到固定端口——由于只需要绑定到固定端口,因此程序中①号粗体字代码使用了 0.0.0.0 这个虚拟 IP 地址。
第三行粗体字代码将该 socket 对象添加 到指定的多点广播 IP 地址。
至于程序中使用 socket 发送和接收数据报的代码,与前面的程序并没有区别,故此处不再赘述。
"""