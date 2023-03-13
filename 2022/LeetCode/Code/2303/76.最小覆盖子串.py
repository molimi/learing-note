#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
# 滑动窗口的思想就是先增加窗口找到可行解，然后缩小窗口优化可行解

# @lc code=start
from collections import defaultdict
from math import inf
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = defaultdict(int)
        for ch in t:
            need_dict[ch] += 1
        need_count = len(t)
        left = 0
        res = (0, inf)
        for right, ch in enumerate(s):
            if need_dict[ch] > 0:           # 不断增加窗口，直到包含所有元素
                need_count -= 1
            need_dict[ch] -= 1              # 这里把用不到的字母也记录下来，利于左指针的移动
            if need_count == 0:             # 此时缩小窗口
                while True:
                    if need_dict[s[left]]==0:
                        break
                    need_dict[s[left]] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                need_dict[s[left]] += 1
                left += 1
                need_count +=1
        return s[res[0]:res[1]+1] if res[1] < len(s) else ""

            
        
# @lc code=end

