"""
15.2.4	管理cookie
从上面的介绍可以发现,使用 urlopen() 既可发送 GET 请求,也可发送POST、PUT、DELETE、  PATCH  等请求。
因此,在绝大部分时候,完全可以使用 urllib.request 模块代替 http.client 模块。

有时候,用户可能需要访问 Web 应用中的被保护页面,如果使用浏览器则十分简单,
通过系统提供的登录页面登录系统,浏览器会负责维护与服务器之间的session,如果用户登录的用户名、密码符合要求,就可以访问被保护资源了。

如果使用 urllib.request 模块来访问被保护页面,则同样需要维护与服务器之间的 session,此时就需要借助于 cookie 管理器来实现。

提示：HTTP 是一种"请求-响应"式协议：客户端向服务器发送请求,服务器向客户端生成响应数据。
这就涉及一个问题：服务器如何辨别两次请求的客户端是同一个客户端呢?答案是 session id。
当客户端第一次向服务器发送请求时,服务器会为该客户端分配一个 session id 作为其标识,服务器在生成响应数据时,
也会把该 session id作为响应数据发送给客户端。当客户端第二次向服务器发送请求时,如果客户端把自己的session id 也发送给服务器,
且服务器端的session id还未过期,服务器就知道该客户端与前一：次发送请求的客户端是同一个。

如果程序直接使用 urlopen()发送请求,并且并未管理与服务器之间的 session,那么服务器就无法识别两次请求是否是同一个客户端发出的。
为了有效地管理 session,程序可引入 http.cookiejar 模块。

此外,程序还需要使用 OpenerDirector 对象来发送请求。

为了使用 urllib.request 模块通过 cookie 来管理 session,可按如下步骤进行操作。
①创建 http.cookiejar.CookieJar 对象或其子类的对象。
②以 CookieJar 对象为参数,创建 urllib.request.HTTPCookieProcessor 对象,该对象负责调用 CookieJar来管理cookie。
③以 HTTPCookieProcessor 对象为参数,调用 urllib.request.build_opener() 函数创建 OpenerDirector 对象。
④使用 OpenerDirector 对象来发送请求,该对象将会通过 HTTPCookieProcessor 调用 CookieJar 来管理 cookie。

下面程序示范了先登录 Web 应用,然后访问Web 应用中的被保护页面。
"""

from urllib.request import *
import http.cookiejar, urllib.parse

# 以指定文件创建CookieJar对象,对象将可以把cookie保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 创建HTTPCookieProcessor对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建OpenerDirector对象
opener = build_opener(cookie_processor)

# 定义模拟Chrome浏览器的user_agent
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

# -------------下面代码发送登录的POST请求----------------
# 定义登录系统的请求参数
params = {'name': 'crazyit.org', 'pass': 'leegang'}
postdata = urllib.parse.urlencode(params).encode()
# 创建向登录页面发送POST请求的Request
request = Request('http://localhost:8888/test/login.jsp', data=postdata, headers=headers)
# 使用OpenerDirector发送POST请求
response = opener.open(request)
print(response.read().decode('utf-8'))

# 将cookie信息写入磁盘文件
cookie_jar.save(ignore_discard=True, ignore_expires=True)  # ①

# -------------下面代码发送访问被保护资源的GET请求----------------
# 创建向"受保护页面"发送GET请求的Request
request = Request('http://localhost:8888/test/secret.jsp', headers=headers)
response = opener.open(request)
print(response.read().decode())
"""
上面程序中第一行粗体字代码先创建了一个CookieJar对象,此处使用它的子类：MozillaCookieJar,该对象负责把 cookie 信息保存在文件中。
第二行粗体字代码负责创建 HTTPCookieProcessor 对象;第三行粗体字代码调用 build_opener()函数创建 OpenerDirector 对象
——接下来程序就会通过该对象来发送请求,而底层的CookieJar对象就负责处理cookie。

程序发送 POST 请求和 GET 请求的代码与前面的示例代码并没有太大的区别,只不过此处额外设置了一个User-Agent请求头,
该请求头用于模拟 Chrome 浏览器。

正如从上面代码所看到的,该程序同样需要访问test应用下的login.jsp和 secret.jsp页面,
因此,测试该代码同样需要将本书配套代码中 codes/15/15.2/路径下的 test 应用复制到 Tomcat 的 webapps 目录下,并启动Tomcat 服务器。

运行上面程序,可以看到如下输出结果。

上面第一行输出信息就是发送POST 登录请求的响应数据,这行响应数据提示"登录成功"。
后面的输出信息则显示该程序成功访问了"安全资源"——这份资源要求用户必须登录才能访问,
如果没有登录,直接访问secret.jsp页面是看不到该输出信息的。
"""