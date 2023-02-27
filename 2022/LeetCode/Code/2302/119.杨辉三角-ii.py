#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
# 使用组合数的思想，递归应该会比较复杂吧


# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [a + b for a, b in zip([0] + res, res + [0])]
        return res


# @lc code=end
