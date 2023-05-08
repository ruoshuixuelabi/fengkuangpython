"""
通过分析得到以上内容之后,接下来可以在 Spider 类中额外定义一个方法来使用 Selenium 调用 Firefox登 录weibo.com。
该 Spider 类的代码如下。
"""
import scrapy
from selenium import webdriver
import time


class WeiboPostSpider(scrapy.Spider):
    name = 'weibo_post'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']

    def __init__(self):
        # 定义保存登录成功之后的cookie的变量
        self.login_cookies = []

    # 定义发送请求的请求头
    headers = {
        "Referer": "https://weibo.com/login/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }

    def get_cookies(self):
        '''使用Selenium模拟浏览器登录并获取cookies'''
        cookies = []
        browser = webdriver.Firefox(executable_path="geckodriver.exe")
        # 等待3秒,用于等待浏览器启动完成,否则可能报错
        time.sleep(3)
        browser.get("https://weibo.com/login/")  # ①
        # 获取输入用户名的文本框
        elem_user = browser.find_element_by_xpath('//input[@id="loginname"]')
        # 模拟输入用户名
        elem_user.send_keys('xxxxxx@sina.com')  # ②
        # 获取输入密码的文本框
        elem_pwd = browser.find_element_by_xpath('//input[@type="password"]')
        # 模拟输入密码
        elem_pwd.send_keys('yyyyyy')  # ③
        # 获取提交按钮
        commit = browser.find_element_by_xpath('//a[@node-type="submitBtn"]')
        # 模拟单击提交按钮
        commit.click()  # ④
        # 暂停10秒,等待浏览器登录完成
        time.sleep(10)
        # 登录成功后获取cookie
        if "微博-随时随地发现新鲜事" in browser.title:
            self.login_cookies = browser.get_cookies()
        else:
            print("登录失败！")

    # start_requests方法会在parse方法之前执行,该方法可用于处理登录逻辑。
    def start_requests(self):
        self.get_cookies()
        print('=====================', self.login_cookies)
        # 开始访问登录后的内容
        return [scrapy.Request('https://weibo.com/lgjava/home',
                               headers=self.headers,
                               cookies=self.login_cookies,
                               callback=self.parse)]

    # 解析服务器相应的内容
    def parse(self, response):
        print('~~~~~~~parse~~~~~')
        print("是否解析成功:", '疯狂软件李刚' in response.text)


"""
上面程序中①号粗体字代码控制 Firefox 打开 weibo.com 的登录页面：htps:/weibo.com/login/:  
②号粗体字代码控制 Firefox 在登录页面的用户名文本框中输入用户名;③号粗体字代码控制  Firefox在登录页面的密码文本框中输入密码;
④号粗体字代码模拟用户单击登录页面中的"登录"按钮。

上面Spider程序重写了两个方法：start_requests(sell)和 parse(self,response),
其中 start_requests(self)方法会在 Scrapy 发送请求之前执行,该方法中的粗体字代码调用self.get cookies()方法来登录 weibo.com,
并保存登录之后的 Cookie 数据,这样该爬虫程序即可成功访问登录之后的 https://weibo.com/lgjava/home页面
(这是我的weibo 主页,读者在测试时应换成登录账户对应的主页)。

本项目的parse(self,response)方法并未yield item,只是简单地判断了response中是否包含登录 账号信息——
因为本项目只是示范在Scrapy 项目中如何整合Selenium 进行登录,至于登录之后如何提取信息,
前面两个项目已多次介绍,故本项目不再重复讲解。
"""
