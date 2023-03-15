#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
# 递归超时啊

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """滚动数组法"""
        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r
# @lc code=end

