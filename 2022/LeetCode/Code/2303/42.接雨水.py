#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            left_max = max(left_max, height[left])      # 每次记录左边最大的高度
            right_max = max(right_max, height[right])
            if height[left] < height[right]:            # 雨水减小的高度就是最矮的那一端
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
# @lc code=end

