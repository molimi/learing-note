#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        head, tail = 0, len(height)-1
        res = 0
        while head < tail:
            if height[head] < height[tail]:
                res = max(res, height[head]*(tail-head))
                head += 1
            else:
                res = max(res, height[tail]*(tail-head))
                tail -= 1
        return res
# @lc code=end

