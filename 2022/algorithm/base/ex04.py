# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/16
@version: 0.1
@description: 变位词检测，排序法比较
"""
def anagram_solution(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)
    a_list1.sort()
    a_list2.sort()
    return (a_list1 == a_list2)

def main():
    print(anagram_solution('abcde', 'edcba'))
    print(anagram_solution('abcd', 'edcba'))
    print(anagram_solution('abababab', 'abab'))

main()