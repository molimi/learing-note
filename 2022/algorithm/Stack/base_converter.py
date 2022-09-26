# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/20
@version: 0.1
@description: 任意进制转换
"""
import stack

def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    number_stack = stack.Stack()
    while dec_number:
        number_stack.push(dec_number % base)
        dec_number = dec_number // base

    output_string = ''
    while not number_stack.is_empty():
        output_string += digits[number_stack.pop()]

    return output_string

def main():
    print(base_converter(152, 2))       # 10011000
    print(base_converter(152, 8))       # 230
    print(base_converter(152, 16))      # 98

main()