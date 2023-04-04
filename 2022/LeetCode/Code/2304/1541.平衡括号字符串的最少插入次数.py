#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        res, need = 0, 0
        for ch in s:
            if ch == '(':               # 一个左括号对应两个右括号
                need += 2
                if need % 2 == 1:       # 右括号为奇数，此事要增加一个左括号
                    res += 1
                    need -= 1
            if ch == ')':               # 右括号多了
                need -= 1
                if need == -1:
                    need = 1            # 对右括号的需求变为 1
                    res += 1            # 增加一个左括号
        return res + need
# @lc code=end

