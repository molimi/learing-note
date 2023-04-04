#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res, need = 0, 0        # 分别统计需要右括号和左括号的数量
        for ch in s:
            if ch == '(':
                need += 1       # 需要左括号
            else:
                need -= 1   
            if need == -1:      # 此时需要右括号
                need = 0
                res += 1
        return res + need       # 需要右括号的数量可能并不为0
# @lc code=end

