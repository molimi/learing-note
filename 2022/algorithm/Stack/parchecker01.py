# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/20
@version: 0.1
@description: 左右括号匹配的问题，此时变成{[()]}
"""
import stack

def par_checker(symbol_string):
    par_stack = stack.Stack()
    for item in symbol_string:
        if item in '([{':
            par_stack.push(item)
        elif item in ')]}':
            if par_stack.is_empty():
                return False
            else:
                close = par_stack.pop()
                if not matches(close, item):
                    return False
    return par_stack.is_empty()

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

def main():
    print(par_checker('{{([][])}()}'))                      # True
    print(par_checker('[ [ { { ( ( ) ) } } ] ]'))           # True
    print(par_checker('[ ] [ ] [ ] ( ) { }'))               # True
    print(par_checker('( [ ) ]'))                           # False
    print(par_checker('( ( ( ) ] ) )'))                     # False
    print(par_checker('[ { ( ) ]'))                         # False
    print(par_checker('[{()]'))                             # False

main()