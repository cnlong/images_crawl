import os
import requests
from bs4 import BeautifulSoup


url = "http://www.mzitu.com/26685"
# 设置headers，网站会根据这个判断是否是浏览器或者爬虫。没有这个信息会被拒绝
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
}
html = requests.get(url, headers=header)
# 打印结果 .text是打印出文本信息即源码
print(html.text)
# 将获取的源码转换成BeautifulSoup对象，便于搜索，如果用re搜索，正则很难写
soup = BeautifulSoup(html.text, 'html.parser')
