#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in nums:
            return [-1, -1]
        return [self.lower_bound(nums, target), self.upper_bound(nums, target)]

    def upper_bound(self, nums: List[int], target: int):    # 寻找上边界
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid -1
        return right


    def lower_bound(self, nums: List[int], target: int):    # 寻找下边界
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left
# @lc code=end

