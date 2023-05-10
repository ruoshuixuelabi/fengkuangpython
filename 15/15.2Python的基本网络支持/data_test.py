"""
在使用urlopen()函数时,可以通过data属性向被请求的URL 发送数据。例如如下程序。
"""
from urllib.request import *

# 向https://localhost/cgi-bin/test.cgi发送请求数据
# with urlopen(url='https://localhost/cgi-bin/test.cgi',
with urlopen(url='http://localhost:8888/test/test',  # ①
             data='测试数据'.encode('utf-8')) as f:
    # 读取服务器全部响应
    print(f.read().decode('utf-8'))
"""
上面程序为 data 属性指定了一个bytes字节数据,该字节数据会以原始二进制流的方式提交给服务器。
上面程序需要在本地(localhost)部署一个 Web 应用,该程序对应的服务器端所使用的 CGI 代码为：
#!/usr/bin/env python
import sys
data =  sys.stdin.read()
print('Content-type:text/plain\n\nGot  Data:"%s"' % data)

提示：如果读者部署 CGI 服务器、开发应用还不熟练,那么只要将上面程序中①号代码的前一行代码注释掉,
再取消①号代码的注释,就可以改为向 http:/localhost:8888/test/test发送请求。
部署该应用就很简单了,只要将本书配套代码中codes/15/15.2/路径下的test应用复制到Tomcat 的 webapps 目录下,
并启动Tomcat 服务器即可。

运行上面程序,可以看到如下输出结果。
Got  Data:“测试数据”
如果使用urlopen()函数向服务器页面发送GET 请求参数,则无须使用data属性,直接把请求 参数附加在URL 之后即可。
例如如下代码(程序清单同上)。
"""
import urllib.parse

params = urllib.parse.urlencode({'name': 'fkit', 'password': '123888'})
# 将请求参数添加到URL的后面
url = 'http://localhost:8888/test/get.jsp?%s' % params
with urlopen(url=url) as f:
    # 读取服务器全部响应
    print(f.read().decode('utf-8'))
"""

如果想通过 urlopen() 函数发送 POST 请求参数,则同样可通过data 属性来实现。例如如下代 码(程序清单同上)
"""

import urllib.parse

params = urllib.parse.urlencode({'name': '疯狂软件', 'password': '123888'})
params = params.encode('utf-8')
# 使用data指定请求参数
with urlopen("http://localhost:8888/test/post.jsp", data=params) as f:
    print(f.read().decode('utf-8'))
"""
从上面的粗体字代码可以看到,如果要向指定地址发送 POST 请求,那么通过 data 指定请求参数即可。
测试该代码,同样需要将本书配套代码中codes/15/15.2/路径下的test应用复制到Tomcat 的 webapps 目录下,并启动Tomcat 服务器。
这段代码与前一段代码的运行结果基本相同,此处不再给出。
"""