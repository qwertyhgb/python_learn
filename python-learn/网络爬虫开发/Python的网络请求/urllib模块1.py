# 通过使用urllib.request模块的post请求实现获取网页信息的内容
import urllib.request
import urllib.parse

# 将数据使用urlencode方法进行编码处理,在使用encoding设置为utf-8
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# 打开指定需要爬取的网页
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# 获取网页的内容
html = response.read()
print(html)
