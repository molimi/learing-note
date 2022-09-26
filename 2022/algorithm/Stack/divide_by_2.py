# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/19
@version: 0.1
@description: 十进制转换为二进制
"""
import stack

def divide_by_2(dec_number):
    number_stack = stack.Stack()
    while dec_number:
        number_stack.push(dec_number % 2)
        dec_number = dec_number // 2
    
    output_string = ''
    while not number_stack.is_empty():
        output_string += str(number_stack.pop())
    
    return output_string

def main():
    print(divide_by_2(42))          # 101010
    print(divide_by_2(156))         # 10011100
    print(divide_by_2(463))         # 111001111

main()