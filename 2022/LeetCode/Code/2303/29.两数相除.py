#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """利用减法的思想肯定会超时"""
        flag = True
        abs_divisor = abs(divisor)
        abs_dividend = abs(dividend)
        if abs_divisor == divisor and abs_dividend != dividend:
            flag = False
        if abs_divisor != divisor and abs_dividend == dividend:
            flag = False
        res, count = abs_dividend, 0
        while res >= abs_divisor:
            res -= abs_divisor
            count += 1
        if not flag:
            count = -count
        if count > (2**31-1):
            return (2**31-1)
        elif count < (-2**31):
            return (-2**31)
        return count
        
# @lc code=end

