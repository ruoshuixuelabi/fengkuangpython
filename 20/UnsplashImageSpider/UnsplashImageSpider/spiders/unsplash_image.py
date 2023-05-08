"""
② 开发 Spider。开发 Spider 就是指定 Scrapy 发送请求的 URL,并实现 parse(self,response) 方法来解析服务器响应数据。
下面是该项目的 Spider 程序。
"""
import scrapy, json
from UnsplashImageSpider.items import ImageItem


class UnsplashImageSpider(scrapy.Spider):
    # 定义Spider的名称
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']
    # 定义起始页面
    start_urls = ['https://unsplash.com/napi/photos?page=1&per_page=12&order_by=latest']

    def __init__(self):
        self.page_index = 1

    def parse(self, response):
        # 解析服务器响应的JSON字符串
        photo_list = json.loads(response.text)  # ①
        # 遍历每张图片
        for photo in photo_list:
            item = ImageItem()
            item['image_id'] = photo['id']
            item['download'] = photo['links']['download']
            yield item

        self.page_index += 1
        # 获取下一页的链接
        next_link = 'https://unsplash.com/napi/photos?page=' + str(self.page_index) + '&per_page=12&order_by=latest'
        # 继续获取下一页的图片
        yield scrapy.Request(next_link, callback=self.parse)


"""
上面程序中第一行粗体字代码指定的 URL 是本项目爬取的第一个页面,由于该页面的响应是一个 JSON 数据,
因此程序无须使用 XPath 或 CSS 选择器来"提取"数据,而是直接使用 json 模块的 loads() 函数来加载该响应数据即可。

在获取 JSON 响应数据之后,程序同样将 JSON 数据封装成 Item 对象后返回给 Scrapy 引擎。 

提示：Spider 到底应该使用 XPath 或 CSS 选择器来提取响应数据,还是使用JSON,
完全取决于目标网站的响应内容,怎么方便怎么来!总之,提取到数据之后,将数据封装成 Item 对象后返回给 Scrapy 引擎就对了。

上面程序中最后一行粗体字代码定义了加载下一页数据的 URL,接下来使用 scrapy.Request 向该 URL 发送请求,
并指定使用 self.parse 方法来处理服务器响应内容,这样程序就可以不断地请求下一页的图片数据。
"""
