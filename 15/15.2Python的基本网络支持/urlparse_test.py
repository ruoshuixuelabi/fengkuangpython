"""
本章将主要介绍 Python 的网络通信支持,通过网络模块,Python 程序可以非常方便地访问互联网上的HTTP 服务、FTP 服务等,
并可以直接获取互联网上的远程资源,还可以向远程资源发送 GET、POST 请求。

本章先简要介绍计算机网络的基础知识,包括 IP 地址和端口等概念,这些知识是网络编程的基础。
接下来将详细介绍 Python 的 urllib 模块,这个模块是 Python 访问网络资源最常用的工具,它不仅可用于访问各种网络资源,
也可用于向Web 服务器发送GET、POST、DELETE、PUT 等各种请求,而且还能有效地管理cooke。这是一个非常实用的网络模块。

本章将重点介绍 Python 提供的 TCP 网络通信支持,包括如何利用 socket 建立 TCP 服务器端,以及如何利用 socket 建立 TCP 客户端。
实际上,Python 的网络通信非常简单,服务器端与客户端通过 socket 建立连接之后,程序就可以通过socket的send()、recv()
方法来发送和接收数据。本章将以采用逐步迭代的方式开发一个 C/S 结构的多人网络聊天工具为例,向读者介绍基于TCP 协议的网络编程。

本章还将重点介绍 Python 提供的 UDP 网络通信支持。由于 UDP 协议是非连接的,
因此基于 UDP 协议的 socket 在发送数据时要使用 sendto()方法,该方法会将数据报发送到指定地址。
本章还会讲解基于 UDP 协议实现多点广播。本章也将以开发局域网通信程序为例来介绍基于 UDP 协议的网络编程。

本章最后还会介绍利用 smtplib、poplib 来发送和接收邮件。在实际开发中邮件处理也是非常 实用的功能,因此也需要读者好好掌握。

15.1  网络编程的基础知识

时至今日,计算机网络缩短了人们之间的距离,把"地球村"变成现实,网络应用已经成为计算机领域最广泛的应用。

15.1.1	网络基础知识

所谓计算机网络,就是把分布在不同地理区域的计算机与专门的外部设备用通信线路互联成一个规模大、功能强的网络系统,
从而使众多的计算机可以方便地互相传递信息,共享硬件、软件、数据信息等资源。

计算机网络是现代通信技术与计算机技术相结合的产物,计算机网络可以提供如下一些主要功能。
(1)资源共享
(2)信息传输与集中处理
(3)均衡负荷与分布处理
(4)综合信息服务

通过计算机网络可以向全社会提供各种经济信息、科研情报和咨询服务等。其中,国际互联网 Internet 上的全球信息网
(WWW,World Wide Web)服务就是一个最典型的、最成功的例子。实际上,今天的网络承载了绝大部分大型企业的运转,
一个大型的、全球性的企业或组织的日常工作流程都是建立在互联网基础之上的。

计算机网络有很多种类型,根据不同的分类原则,可以得到不同类型的计算机网络。
通常计算机网络是按照规模大小和延伸范围来分类的,常见的类型有：局域网 (LAN)、城域网(MAN)和广域网(WAN)。
Internet 可以被视为世界上最大的广域网。

在计算机网络中实现通信必须有一些约定,这些约定被称为通信协议。通信协议负责对传输速率、传输代码、代码结构、
传输控制步骤、出错控制等制定处理标准。为了让两个节点能进行对话,必须在它们之间建立通信工具,使彼此之间能进行信息交换。

通信协议通常由三部分组成：一是语义部分,用于决定双方对话的类型;二是语法部分,用于决定双方对话的格式;
三是变换规则,用于决定通信双方的应答关系。

国际标准化组织(ISO)于1978年提出了"开放系统互连参考模型",即著名的OSI(Open System Interconnection)参考模型。
OSI 参考模型力求将网络简化,并以模块化的方式来设计网络。

OSI 参考模型把计算机网络分成物理层、数据链路层、网络层、传输层、会话层、表示层、应用层七层,
受到计算机界和通信业的极大关注。经过十多年的发展和推进,OSI 模式已成为各种计算机网络结构的参考标准。

图15.1显示了OSI 参考模型的推荐分层。

通信协议是网络通信的基础,IP 协议则是一种非常重要的通信协议。IP(Internet Protocol)又称网际协议,是支持网间互联的数据报协议。
IP 协议提供了网间连接的完善功能,包括IP 数据报规定的互联网络范围内的地址格式。

经常与 IP 协议放在一起的还有TCP(Transmission Control Protocol),即传输控制协议,它规定了一种可靠的数据信息传递服务。
虽然IP 和 TCP 这两个协议的功能不尽相同,也可以分开单独使用,但它们是在同一个时期作为一个协议来设计的,
并且在功能上是互补的,因此,在实际使用中常常把这两个协议统称为TCP/IP 协议。
TCP/IP 协议最早出现在UNIX 操作系统中,现在几乎所有的操作系统都支持TCP/IP 协议,因此,TCP/IP 协议也是Internet中最常用的基础协议。

按照TCP/IP 协议模型,网络模型通常被分为四层。OSI 参考模型和TCP/IP 分层模型的大致对应关系如图15.2所示。

15.1.2	IP地址和端口号

IP 地址用于唯一标识网络中的一个通信实体,这个通信实体既可以是一个主机,也可以是一台打印机,或者是路由器的某一个端口。
而在基于 IP 协议的网络中传输的数据包,都必须使用 IP  地址来进行标识。

就像写一封信,要标明收信人的地址和寄信人的地址,而邮政工作人员则通过该地址来决定信件的去向。
类似的过程也发生在计算机网络中,被传输的每一个数据包也要包括一个源 IP 地址和一个目的 IP 地址。
当该数据包在网络中进行传输时,这两个地址要保持不变,以确保网络设备总能根据确定的 IP 地址,
将数据包从源通信实体送往指定的目的通信实体。

IP 地址是数字型的,它是一个32位(32bit)整数。但为了便于记忆,通常把它分成4个8位的二进制数,每8位之间用圆点隔开,
每个8位整数都可以转换成一个0~255的十进制整数,因此日常看到的IP 地址常常是这种形式：202.9.128.88。

NIC(Internet Network Information Center)统一负责全球 Internet IP 地址的规划和管理,
而Inter NIC、APNIC、RIPE  三大网络信息中心则具体负责美国及其他地区的IP 地址分配。
其中APNIC 负责亚太地区的IP 地址管理,我国申请IP 地址也要通过APNIC,APNIC 的总部设在日本东京大学。

IP地址被分成A、B、C、D、E五类,每个类别的网络标识和主机标识各有规则。
A类：10.0.0.0~10.255.255.255
B类：172.16.0.0~172.31.255.255
C类：192.168.0.0~192.168.255.255

IP 地址用于唯一标识网络上的一个通信实体,但一个通信实体可以有多个通信程序同时提供网络服务,此时还需要使用端口。

端口是一个16位的整数,用于表示将数据交给哪个通信程序处理。因此,端口就是应用程序与外界交流的出入口,
它是一种抽象的软件结构,包括一些数据结构和I/O(输入/输出)缓冲区。

不同的应用程序处理不同端口上的数据,在同一台机器中不能有两个程序使用同一个端口。端口号可以为0~65535,通常将端口分为如下三类。
(1)公认端口(Well Known Port)：端口号为0~1023,它们紧密地绑定(Binding)一些特定的服务。
(2)注册端口(Registered Port)：端口号为1024~49151,它们松散地绑定一些服务。应用程序通常应该使用这个范围内的端口。
(3)动态和/或私有端口(Dynamic and/or Private Port)：端口号为49152~65535,这些端口是应用程序使用的动态端口,
应用程序一般不会主动使用这些端口。

如果把应用程序比作人,把计算机网络比作类似于邮递员的角色,把IP 地址理解为某个人所在地方的地址(包括街道和门牌号),
但仅有地址是找不到这个人的,还需要知道这个人所在的房间号才可以找到他,这个房间号就相当于端口号。
因此,当一个程序需要发送数据时,需要指定目的地的IP 地址和端口号,只有指定了正确的IP地址和端口号,
计算机网络才可以将数据发送给该 IP 地址和端口号所对应的程序。

15.2 Python的基本网络支持

Python 模块的优势在网络支持这个部分得到了极好的体现,Python 的网络模块非常丰富,
这些网络模块既提供了底层的 TCP、UDP 协议的网络通信功能,也提供了对应用层 HTTP、FTP、SMTP、POP3 协议的支持。

15.2.1 Python的网络模块概述

根据前面对网络分层模型的介绍,我们知道实际的网络模型大致分为四层,这四层各有对应的网络协议提供支持,如图15.3所示。

网络层协议主要是 IP, 它是所有互联网协议的基础,其中 ICMP(Internet Control Message Protocol)、
IGMP(Internet   Group   Manage   Protocol)、ARP(Address   Resolution   Protocol)、
RARP (Reverse Address Resolution Protocol)等协议都可认为是IP 协议族的子协议。通常来说,很少会直接基于网络层进行应用程序编程。

传输层协议主要是 TCP 和 UDP,Python 提供了 socket 等模块针对传输层协议进行编程。

应用层协议就更多了,正如图15.3所示的,FTP、HTTP、TELNET 等协议都属于应用层协议,
Python 同样为基于应用层协议的编程提供了丰富的支持。

虽然 Python 自带的标准库已经提供了很多与网络有关的模块,但如果在使用时觉得不够方便,
则不要忘记了 Python 的优势：大量的第三方模块随时可用于增强Python的功能。表15.1显示了Python标准库中的网络相关模块。

表15.1 Python标准库中的网络相关模块

模块	                                                                    描述
socket	                                                    基于传输层 TCP、UDP 协议进行网络编程的模块
asyncore	                                                socket模块的异步版,支持基于传输层协议的异步通信
asynchat	                                                asyncore的增强版
cgi	                                                        基本的CGl(Common Gateway Interface,早期开发动态网站的技术)支持
email	                                                    E-mail和MIME消息处理模块
ftplib	                                                    支持FTP协议的客户端模块
httplib、http.client	                                支持HTTP协议以及HTTP客户端的模块
imaplib	                                                支持IMAP4协议的客户端模块
mailbox	                                                操作不同格式邮箱的模块
mailcap	                                                支持Mailcap文件处理的模块
nntplib	                                                支持NTTP协议的客户端模块
smtplib	                                                支持SMTP协议(发送邮件)的客户端模块
poplib	                                                    支持POP3协议的客户端模块
telnetlib	                                                支持TELNET协议的客户端模块
urllib及其子模块	                                    支持URL处理的模块
xmlrpc、xmlrpc.server、xmlrpc.client	支持XML-RPC协议的服务器端和客户端模块

15.2.2	使用 urllib.parse 子模块

URL(Uniform Resource Locator)对象代表统一资源定位器,它是指向互联网"资源"的指针。
资源可以是简单的文件或目录,也可以是对复杂对象的引用,例如对数据库或搜索引擎的查询。
在通常情况下,URL 可以由协议名、主机、端口和资源路径组成,即满足如下格式：
protocol://host:port/path

例如如下的URL 地址：
http://www.crazyit.org/index.php

urllib模块则包含了多个用于处理URL 的子模块。
(1)urllib.request：这是最核心的子模块,它包含了打开和读取 URL 的各种函数。
(2)urllib.error：主要包含由 urllib.request 子模块所引发的各种异常。
(3)urllib.parse：用于解析URL。
(4)urllib.robotparser：主要用于解析robots.txt文件。

通过使用 urllib 模块可以打开任意 URL 所指向的资源,就像打开本地文件一样,这样程序就能完整地下载远程页面。
如果再与第10章介绍的 re 模块结合使用,那么程序完全可以提取页面中各种信息,这就是所谓的"网络爬虫"的初步原理。


提示：在 Python 2.x中,urllib 模块被分为urllib和 urllib2 两个模块,其中 urllib 主要用于简单的下载,
而 urllib2 则可实现 HTTP 验证、cookie 管理。

下面先介绍 urllib.parse 子模块中用于解析 URL 地址和查询字符串的函数。
(1)urllib.parse.urlparse(urlstring,scheme=",allow fragments=True):该函数用于解析URL 字符串。
程序返回一个 ParseResult 对象,可以获取解析出来的数据。
(2)urllib.parse.urlunparse(parts):该函数是上一个函数的反向操作,用于将解析结果反向拼接成URL 地址。
(3)urllib.parse.parse_qs(qs,keep_blank_values=False,strict_parsing=False,encoding='utf-8', errors='replace'):
该函数用于解析查询字符串(application/x-www-form-urlencoded类型的数据),并以 dict 形式返回解析结果。
(4)urllib.parse.parse_qsl(qs,keep_blank_values=False,strict parsing=False,encoding='utf-8', errors=replace'):
该函数用于解析查询字符串(application/x-www-form-urlencoded类型的数据),并以列表形式返回解析结果。
(5)urllib.parse.urlencode(query,doseq=False,safe=",encoding-None,errors=None,quote_via= quote_plus):
将字典形式或列表形式的请求参数恢复成请求字符串。该函数相当于 parse_qs()、parse_qsl()的逆函数。
(6)urllib.parse.urljoin(base,url,allow fragments=True): 该函数用于将一个base  URL和另一个资源 URL 连接成代表绝对地址的URL。

例如,如下程序使用 urlparse() 函数来解析 URL 字符串。
"""
from urllib.parse import *

# 解析URL字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
# 通过属性名和索引来获取URL的各部分
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机:', result.hostname)
print('端口:', result.port)
print('资源路径:', result.path, result[2])
print('参数:', result.params, result[3])
print('查询字符串:', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())
"""
上面程序中粗体字代码使用 urlparse() 函数解析 URL 字符串,解析结果是一个 ParseResult 对象,该对象实际上是tuple的子类。
因此,程序既可通过属性名来获取 URL 的各部分,也可通过索引来获取 URL 的各部分。

表15.2显示了ParseResult各属性与元组索引的对应关系。

属性名	        元组索引	    返回值	                                默认值
scheme	    0	                返回URL的scheme	            scheme参数
netloc	        1	                网络位置部分(主机名+端口)	空字符串
path	        2	                资源路径	                            空字符串
params	    3	                资源路径的附加参数	            空字符串
query	        4	                查询字符串	                        空字符串
fragment	    5	                Fragment标识符	                空字符串
username		                用户名	                                None
password		                密码	                                    None
hostname		                主机名	                                None
port		                            端口	                                    None
上面程序使用urlparse()函数解析 URL 字符串之后,分别使用了属性名和索引来获取URL 的 各部分。运行上面程序,将看到如下输出结果。
ParseResult(scheme='http', netloc='www.crazyit.org:80', path='/index.php', params='yeeku', query='name=fkit', fragment='frag')
scheme: http http
主机和端口: www.crazyit.org:80 www.crazyit.org:80
主机: www.crazyit.org
端口: 80
资源路径: /index.php /index.php
参数: yeeku yeeku
查询字符串: name=fkit name=fkit
fragment: frag frag
http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag

如果使用 urlunparse()函数,则可以把一个 ParseResult 对象或元组恢复成 URL 字符串。例如如下代码(程序清单同上)。
"""
print('-----------------')
result = urlunparse(('http', 'www.crazyit.org:80', 'index.php', 'yeeku', 'name=fkit', 'frag'))
print('URL为:', result)
"""
运行上面程序,将看到如下输出结果。
URL为: http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag

如果被解析的 URL 以双斜线(//)开头,那么urlparse()函数可以识别出主机,只是缺少 scheme 部分。
但如果被解析的 URL 既没有scheme,也没有以双斜线 (I/) 开头,那么 urlparse()函数将会把这些URL 都当成资源路径。
例如如下代码(程序清单同上)。
"""
print('-----------------')
# 解析以//开头的URL
result = urlparse('//www.crazyit.org:80/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])
print('-----------------')
# 解析没有scheme,也没有以双斜线（//）开头的URL
# 从开头部分开始就会被当成资源路径
result = urlparse('www.crazyit.org/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])
"""
parse_qs()和 parse_qsl()(这个l代表list)两个函数都用于解析查询字符串,只不过返回值不同而已——
parse_qs()函数的返回值是list(正如该函数名所暗示的)。urlencode()则是它们的逆函数。 例如如下代码(程序清单同上)。
"""
# 解析查询字符串,返回dict
result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 解析查询字符串,返回list
result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 将列表格式的请求参数恢复成请求参数字符串
print(urlencode(result))
"""
从上面的输出结果可以看到,parse_qs()函数返回了一个dict,其中 key 是参数名,value 是参数值。
而 parse_qsl()函数返回了一个list,每个元素代表一个查询参数。

urljoin()函数负责将两个 URL  拼接在一起,返回代表绝对地址的URL。这里主要可能出现3 种情况。
(1)被拼接的 URL 只是一个相对路径path(不以斜线开头),那么该 URL 将会被拼接到base之后,
如果 base 本身包含 path 部分,则用被拼接的 URL 替换base所包含的path部分。
(2)被拼接的 URL 是一个根路径path(以单斜线开头),那么该 URL 将会被拼接到 base 的域名之后。
(3)被拼接的 URL 是一个绝对路径path(以双斜线开头),那么该 URL 将会被拼接到 base 的 scheme 之后。

例如,如下代码示范了urljoin()函数的功能和用法(程序清单同上)。
"""
# 被拼接URL不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result)  # http://www.crazyit.org/users/help.html
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result)  # http://www.crazyit.org/users/book/list.html
# 被拼接URL以斜线（代表根路径path）开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result)  # http://www.crazyit.org/help.html
# 被拼接URL以双斜线（代表绝对URL）开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result)  # http://help.html
