# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230504
# @Version: 1.0
# @Description: Python 请求天气

import requests

rep = requests.get('http://www.weather.com.cn/weather1d/101010100.shtml', )
rep.encoding = 'utf-8'

print('返回结果：%s' % rep.text)