"""
基于 Scrapy 项目开发爬虫大致需要如下几个步骤。
① 定义 Item 类。该类仅仅用于定义项目需要爬取的 N 个属性。比如该项目需要爬取工作名称、工资、招聘公司等信息,
则可以在items.py中增加如下类定义。
"""
import scrapy


class ZhipinspiderItem(scrapy.Item):
    # 工作名称
    title = scrapy.Field()
    # 工资
    salary = scrapy.Field()
    # 招聘公司
    company = scrapy.Field()
    # 工作详细链接
    url = scrapy.Field()
    # 工作地点
    work_addr = scrapy.Field()
    # 行业
    industry = scrapy.Field()
    # 公司规模
    company_size = scrapy.Field()
    # 招聘人
    recruiter = scrapy.Field()
    # 发布时间
    publish_date = scrapy.Field()


"""
上面程序中的一行粗体字代码表明所有的 Item 类都需要继承scrapy.Item 类,
接下来就为所有需要爬取的信息定义对应的属性,每个属性都是一个scrapy.Field对象。

该 Item 类只是一个作为数据传输对象(DTO)的类,因此定义该类非常简单。
"""
