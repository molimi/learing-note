# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/16
@version: 0.1
@description: 左右括号匹配的问题
"""
import stack

def par_checker(symbol_string):
    new_stack = stack.Stack()
    for item in symbol_string:
        if item == "(":
            new_stack.push(item)
        elif item == ")":
            if new_stack.is_empty():
                return False
            new_stack.pop()
    return new_stack.is_empty()

def main():
    print(par_checker('((()))'))
    print(par_checker('((())'))
    print(par_checker('(()))'))
    print(par_checker('())'))


if __name__ == "__main__":
    main()