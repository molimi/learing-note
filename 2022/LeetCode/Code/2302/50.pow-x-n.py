#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
# 使用递归实现

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            return x
        p = self.myPow(x, n // 2)
        if n % 2 == 0:
            return p * p
        else:
            return x * p * p
# @lc code=end

