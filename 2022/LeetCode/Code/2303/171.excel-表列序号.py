#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lt = list(columnTitle)[::-1]
        result = 0
        for i, item in enumerate(lt):
            result += (ord(item)-ord('A')+1) * (26**i)
        return result
# @lc code=end

