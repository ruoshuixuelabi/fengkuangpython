"""
实际上,使用 data 属性不仅可以发送 POST 请求,还可以发送PUT、PATCH、DELETE 等请求,
此时需要使用urllib.request.Request来构建请求参数。
程序使用 urlopen() 函数打开远程资源时,第一个url参数既可以是 URL 字符串,也可以使用urllib.request.Request对象。
urllib.request.Request 对象的构造器如下：
(self, url, data=None, headers={},origin_req_host=None, unverifiable=False,method=None):
从该构造器可以看出,使用 Request 可以通过 method 指定请求方法,也可以通过 data 指定请求参数,还可以通过headers指定请求头。

下面代码示范了如何通过Request对象来发送 PUT 请求。
"""
from urllib.request import *

params = 'put请求数据'.encode('utf-8')
# 创建Request对象,设置使用PUT请求
req = Request(url='http://localhost:8888/test/put', data=params, method='PUT')
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))
"""
正如从上面粗体字代码所看到的,程序在创建 Request 对象时通过 method 指定使用 PUT 请求方式,这意味着程序会发送 PUT 请求。
测试该代码,同样需要将本书配套代码中codes/15/15.2/路径下的test应用复制到Tomcat 的 webapps 目录下,并启动Tomcat 服务器。

正如刚刚所提到的,程序也可以使用Request对象来添加请求头。例如如下代码(程序清单同上)。
"""
# 创建Request对象
req = Request('http://localhost:8888/test/header.jsp')
# 添加请求头
req.add_header('Referer', 'http://www.crazyit.org/')
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))
"""
正如从上面粗体字代码所看到的,程序通过 Request 的 add_header()方法添加了一个 Referer 请求头,
服务器端的处理程序将可以读到此处添加的请求头。
"""