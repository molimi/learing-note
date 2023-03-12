#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 0, num // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > num:
                right = mid - 1 
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        return False
            
# @lc code=end

