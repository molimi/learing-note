#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len, start = 0, 0
        sum_cost = 0
        for end, tail in enumerate(s):
            sum_cost += abs(ord(tail)-ord(t[end]))
            if sum_cost <= maxCost:
                max_len = max(max_len, end-start+1)
            while sum_cost > maxCost:
                head = s[start]
                sum_cost -= abs(ord(head)-ord(t[start]))
                start += 1
        return max_len
# @lc code=end

