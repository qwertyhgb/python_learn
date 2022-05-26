# 通过urllib.request模块实现发送请求并读取网页内容
import urllib.request  # 导入urllib.request模块

# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()  # 读取网页内容
print(html)  # 打印网页内容
