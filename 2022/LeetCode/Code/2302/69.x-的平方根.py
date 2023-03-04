#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
# 二分查找或者牛顿迭代法

# @lc code=start
import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans+1) ** 2 <= x else ans
# @lc code=end

