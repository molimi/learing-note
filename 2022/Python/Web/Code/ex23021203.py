# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230212
# @Version: 1.0
# @Description: 实现获取网页信息内容

import requests

url = 'https://www.baidu.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
# requests.get默认使用了127.0.0.1：8888做代理，要关闭代理
proxies = { "http": None, "https": None}
response = requests.get(url, headers=headers, proxies=proxies)
print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)