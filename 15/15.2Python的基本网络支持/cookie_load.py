"""
如果将上面程序中①号粗体字代码的注释取消,程序就会把cookie信息写入a.txt文件中。
这意味着该程序将会把服务器响应的session id等 cookie持久化保存在a.txt文件中,
后面程序可以读取该 cookie 文件信息,这样程序就可以模拟前面登录过的客户端,从而直接访问被保护页面了。

例如如下程序。
"""
from urllib.request import *
import http.cookiejar

# 以指定文件创建CookieJar对象,对象将可以把cookie保存在文件中
cookie_jar = http.cookiejar.MozillaCookieJar('a.txt')
# 直接加载a.txt中的Cookie信息
cookie_jar.load('a.txt', ignore_discard=True, ignore_expires=True)
# 遍历a.txt中保存的cookie信息
for item in cookie_jar:
    print('Name =' + item.name)
    print('Value =' + item.value)
# 创建HTTPCookieProcessor对象
cookie_processor = HTTPCookieProcessor(cookie_jar)
# 创建OpenerDirector对象
opener = build_opener(cookie_processor)
# 定义模拟Chrome浏览器的user_agent
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
             r' (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# 定义请求头
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
# -------------下面代码发送访问被保护资源的GET请求----------------
# 创建向"受保护页面"发送GET请求的Request
request = Request('http://localhost:8888/test/secret.jsp', headers=headers)
response = opener.open(request)
print(response.read().decode())
"""
该程序的前面部分同样用于创建 CookieJar、HTTPCookieProcessor、OpenerDirector对象,
但它多了第一行粗体字代码,这行代码用于从a.txt文件中读取cookie 信息。
接下来的粗体字代码只是用于显示a.txt文件中所保存的cookie信息,这些代码不影响程序本身。

该程序并未向服务器发送登录请求,但由于该CookieJar会把登录成功的session id发送给服务器,
因此服务器就会认为该程序与前面那个登录成功的程序是同一个客户端。
运行上面程序,也可以访问到Web 应用中的被保护页面,输出结果如下。

上面前两行输出内容就是 a.txt 文件中保存的 cookie 信息。从该输出结果可以看到,
该cookie 信息只是保存了服务器发送给客户端的 session id。因此,程序使用 OpenerDirector 向服务器发送请求时,
就会将该 session id 发送给服务器,这样服务器就会把程序当成前一个已经登录成功的程序。所以,该程序也可以访问到被保护页面。
"""