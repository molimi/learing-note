# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230212
# @Version: 1.0
# @Description: 实现获取网页信息内容

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post/', data=data)
html = response.read()
print(html)