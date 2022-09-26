"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/2
Description: 正则表达式
"""
import re

pattern = re.compile(r'mr_\w+', re.I)  # 模式字符串，不区分大小写
string1 = 'MR_SHOP mr_shop'  # 要匹配的字符串
m1 = pattern.match(string1)
print(m1)
string2 = '项目名称 MR_SHOP mr_shop'
m2 = pattern.match(string2)
print(m2)

print('匹配值的起始位置：', m1.start())
print('匹配值的结束位置：', m1.end())
print('匹配位置的元组：', m1.span())
print('要匹配的字符串：', m1.string)
print('匹配数据：', m1.group())

match = pattern.findall(string1)
print(match)
match = pattern.findall(string2)
print(match)

import re
pattern = re.compile(r'(黑客)|(抓包)|(监听)|(Trojan)')
string = "我是一名程序员，我喜欢看黑客方面的书，想研究一下Trojan。\n"
sub = pattern.sub('@_@', string)
print(sub)

pattern1 = re.compile(r'[?|&]')
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = pattern1.split(url)
print(result)