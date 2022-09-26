# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/9/16
@version: 0.1
@description: 变位词检测，用字符串1遍历字符串2，设立标志位
"""
def anagram_solution(s1, s2):
    a_list = list(s2)
    still_ok = True
    pos1 = 0
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == a_list[pos2]:
                a_list[pos2] = None
                found = True
            else:
                pos2 += 1

        if found:
            pos1 += 1
        else:
            still_ok = False
    return still_ok

def main():
    print(anagram_solution('abcd', 'cadb'))
    print(anagram_solution('abababa', 'abab'))    
    print(anagram_solution('abgsgg', 'ababjjsj'))    

main()