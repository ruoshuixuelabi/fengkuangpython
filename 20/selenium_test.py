from selenium import webdriver
import time

# 通过executable_path指定浏览器驱动的路径
browser = webdriver.Firefox(executable_path="WeiboSpider/geckodriver.exe")
# 等待3秒，用于等待浏览器启动完成
time.sleep(3)
# 浏览指定网页
browser.get("http://www.crazyit.org/")
# 暂停5秒
time.sleep(5)
