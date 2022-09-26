"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/2
Description: 可迭代对象
"""
import time


def genrator_func1():
    a = 1
    print('定义变量a')
    yield a
    b = 2
    print('定义变量b')
    yield b


g1 = genrator_func1()
print('g1: ', g1)
print('-' * 20)
print(next(g1))
time.sleep(1)
print(next(g1))