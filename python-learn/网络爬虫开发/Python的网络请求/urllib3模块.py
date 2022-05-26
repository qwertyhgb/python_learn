# 通过urllib3模块来爬取网页
import urllib3

# 创建PoolManager对象,用于处理与线程池以及线程安全的所有与细节
http = urllib3.PoolManager()
# 对http进行get请求
response = http.request('GET', 'http://www.baidu.com')
# 获取网页内容
print(response.data)
