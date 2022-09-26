"""
Version: 0.1
Author: CarpeDiem
Date: 2022/4/29
Description: 读写文件
"""
f = None
try:
    f = open('myfile.txt', 'r', encoding='utf-8')
    print(f.read())
    with open('myfile.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('无法打开指定的文件！')
except LookupError:
    print('指定了未知编码！')
except UnicodeDecodeError:
    print('读取文件时解码错误！')
finally:
    if f:
        f.close()

import json
mydict = {
    'name':
    '骆昊',
    'age':
    38,
    'qq':
    957658,
    'friends': ['王大锤', '白元芳'],
    'cars': [{
        'brand': 'BYD',
        'max_speed': 180
    }, {
        'brand': 'Audi',
        'max_speed': 280
    }, {
        'brand': 'Benz',
        'max_speed': 320
    }]
}
try:
    with open('data.json', 'w', encoding='utf-8') as fs:
        json.dump(mydict, fs)
except IOError as e:
    print(e)
print('保存数据完成!')

import pickle

tup1 = ('Python', {1, 2, 3}, None)
p1 = pickle.dumps(tup1)  # 序列化成二进制对象
t2 = pickle.loads(p1)  # 发序列化成Python对象
with open("a.txt", 'wb') as f:  # 打开文件
    pickle.dump(tup1, f)  # 用 dump 函数将 Python 对象转成二进制对象文件
with open("a.txt", 'rb') as f:  # 打开文件
    t3 = pickle.load(f)  # 将二进制文件对象转换成 Python 对象

import fileinput
# 使用for循环遍历fileinput对象
for line in fileinput.input(file=('myfile.txt', 'file.txt')):
    print(line)  # 输出读取到的内容
fileinput.close()  # 关闭文件流

import linecache
import string

print(linecache.getline(string.__file__, 3))  # 读取string模块中的第三行数据

print(linecache.getline('myfile.txt', 2))  # 读取普通文件的第二行
