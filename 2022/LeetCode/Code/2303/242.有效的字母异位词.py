#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''return Counter(s) == Counter(t)'''
        '''
        if len(s) != len(t) or set(s) != set(t):
            return False
        s1, t1 = [0]*26, [0]*26
        for ch1, ch2 in zip(s, t):
            s1[ord(ch1)-ord('a')] += 1
            t1[ord(ch2)-ord('a')] += 1
        return s1 == t1
        '''
        if len(s) != len(t) or set(s) != set(t):
            return False
        s_dict, t_dict = {}, {}
        for ch1, ch2 in zip(s, t):
            s_dict[ch1] = s_dict.get(ch1, 0) + 1
            t_dict[ch2] = t_dict.get(ch2, 0) + 1
        return s_dict == t_dict
# @lc code=end

