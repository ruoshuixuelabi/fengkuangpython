"""
① 定义 Item 类。由于本项目的目标是爬取高清图片,因此其所使用的 Item 类比较简单,
只要保存图片 id 和图片下载地址即可。下面是该项目的 Item 类的代码。
"""
import scrapy


class ImageItem(scrapy.Item):
    # 保存图片id
    image_id = scrapy.Field()
    # 保存图片下载地址
    download = scrapy.Field()


"""
上面程序为 Item 类定义了两个变量,分别用于保存图片 id 和图片下载地址。
"""
