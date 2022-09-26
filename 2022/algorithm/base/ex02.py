# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/16
@version: 0.1
@description: 变位词检测，用字符串1遍历字符串2
要求：两种字符串长度相等，如果不相等这个方法就失效了，而且这个算法会每次遍历所有的s2，造成不必要的计算量
"""

def anagram_solution(s1, s2):
    copy_list = list(s2)       
    pos1 = 0
    while pos1 < len(s1):
        pos2 = 0
        while pos2 < len(s2):
            if s1[pos1] == copy_list[pos2]:
                copy_list[pos2] = None
            else:
                pos2 += 1
        pos1 += 1
    if all(item is None for item in copy_list):
        return True
    else:
        return False

def main():
    print(anagram_solution('abfsfsfhshhs', 'shshh'))
    print(anagram_solution('optyho', 'python'))


main()