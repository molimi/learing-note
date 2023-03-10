#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
# 二分法

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            if left - right == 1:
                return left
# @lc code=end

