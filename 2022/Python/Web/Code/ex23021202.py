# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230212
# @Version: 1.0
# @Description: 实现获取网页信息内容

import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://www.baidu.com/')
print(response.data)