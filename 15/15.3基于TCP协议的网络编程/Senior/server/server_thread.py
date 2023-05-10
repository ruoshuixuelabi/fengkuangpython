"""
服务器端线程的 server_target 函数比上一节的程序要复杂一点,因为该函数要分别处理公聊、私聊两类聊天信息。
除此之外,还需要处理用户名是否重复的问题。服务器端线程的 server_target  函数的代码如下。
"""
import CrazyitProtocol


def server_target(s, clients):
    try:
        while True:
            # 从socket读取数据
            line = s.recv(2048).decode('utf-8')
            print(line)
            # 如果读到的行以CrazyitProtocol.USER_ROUND开始,并以其结束,则可以确定读到的是用户登录的用户名
            if line.startswith(CrazyitProtocol.USER_ROUND) and line.endswith(CrazyitProtocol.USER_ROUND):
                # 得到真实消息
                user_name = line[CrazyitProtocol.PROTOCOL_LEN: \
                                 -CrazyitProtocol.PROTOCOL_LEN]
                # 如果用户名重复
                if user_name in clients:
                    print("重复")
                    s.send(CrazyitProtocol.NAME_REP.encode('utf-8'))
                else:
                    print("成功")
                    s.send(CrazyitProtocol.LOGIN_SUCCESS.encode('utf-8'))
                    clients[user_name] = s
            # 如果读到的行以CrazyitProtocol.PRIVATE_ROUND开始,并以其结束
            # 则可以确定是私聊信息,私聊信息只向特定的socket发送
            elif line.startswith(CrazyitProtocol.PRIVATE_ROUND) and line.endswith(CrazyitProtocol.PRIVATE_ROUND):
                # 得到真实消息
                user_and_msg = line[CrazyitProtocol.PROTOCOL_LEN: \
                                    -CrazyitProtocol.PROTOCOL_LEN]
                # 以SPLIT_SIGN分割字符串,前半是私聊用户,后半是聊天信息
                user = user_and_msg.split(CrazyitProtocol.SPLIT_SIGN)[0]
                msg = user_and_msg.split(CrazyitProtocol.SPLIT_SIGN)[1]
                # 获取私聊用户对应的socket,并发送私聊信息
                clients[user].send((clients.key_from_value(s) + "悄悄地对你说：" + msg).encode('utf-8'))
            # 公聊要向每个socket发送
            else:
                # 得到真实消息
                msg = line[CrazyitProtocol.PROTOCOL_LEN: \
                           -CrazyitProtocol.PROTOCOL_LEN]
                # 遍历clients中的每个socket
                for client_socket in clients.values():
                    client_socket.send((clients.key_from_value(s) + "说：" + msg).encode('utf-8'))
    # 捕获到异常后,表明该socket对应的客户端已经出现了问题
    # 所以程序将其对应的socket从dict中删除
    except:
        clients.remove_by_value(s)
        print(len(clients))
        # 关闭网络、IO资源
        if s is not None:
            s.close()


"""
上面程序比上一节的程序除增加了异常处理代码之外,还主要增加了对读取数据的判断代码,如程序中两行粗体字代码所示。
当程序读取到客户端发送过来的内容之后,会根据该内容前后的协议字符串进行相应的处理。
"""
