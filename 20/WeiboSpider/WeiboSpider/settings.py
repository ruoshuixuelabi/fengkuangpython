"""
接下来依然需要对 settings.py 文件进行修改——增加一些自定义请求头(用于模拟浏览器), 设置启用指定的Pipeline。 下面是本项目修改后的settings.py文件。
"""
# -*- coding: utf-8 -*-

# Scrapy settings for WeiboSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeiboSpider'

SPIDER_MODULES = ['WeiboSpider.spiders']
NEWSPIDER_MODULE = 'WeiboSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'WeiboSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 配置默认的请求头
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'WeiboSpider.middlewares.WeibospiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'WeiboSpider.middlewares.WeibospiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 配置使用Pipeline
ITEM_PIPELINES = {
    'WeiboSpider.pipelines.WeibospiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
"""
留心上面的 ROBOTSTXT_OBEY 配置,这行配置代码指定该爬虫程序不遵守该站点下的robot.txt规则文件
(Scrapy 默认遵守robot.txt规则文件),强行爬取该站点的内容。

经过上面配置,接下来在WeiboSpider 目录下执行如下命令来启动爬虫。
scrapy  crawl weibo post

运行该爬虫程序,即可看到它会自动启动 Firefox 来登录weibo.com, 并可以在命令行窗口中看到如图20.16所示的输出信息。

从该爬虫程序的运行过程来看,整合 Selenium 之后 Scrapy 的运行速度明显慢了很多。
因此, Scrapy 通常只使用Selenium 控制浏览器执行登录,不会使用 Selenium 控制浏览器执行普通下载,
普通下载使用Scrapy 自己的下载中间件即可(效率更高)。

一句话：只要技术到位,网络上没有爬取不到的数据。当然,如果有些网站的数据属于机密数据,
并且这些网站也已经采取种种措施来阻止非法访问,但是你非要越过层层限制去访问这些数据, 这就涉嫌触犯法律了。因此,爬虫也要适可而止。

"""
