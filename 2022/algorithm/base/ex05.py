# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/16
@version: 0.1
@description: 变位词检测，计数法比较
"""
def count(s):
    count_list = [0] * 26
    for i in range(len(s)):
        pos = ord(s[i]) - ord('a')
        count_list[pos] += 1
    return count_list

def anagram_solution(s1, s2):
    return count(s1) == count(s2)

def main():
    print(anagram_solution('apple', 'pleap'))
    print(anagram_solution('abd', 'ggsabad'))
    print(anagram_solution('abab', 'bbaa'))
    print(anagram_solution('gsgddjkdsdgds', 'dsdgdsgsgddjk'))

main()