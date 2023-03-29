#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        # 最大的后面必定是最小的，找到最大的数位置+1就是旋转次数
        left, right= 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:         # 二分查找最主要是找和谁比，那个山峰数组，就是和nums[mid]<nums[mis+1],这里是和nums[high]
                right = mid
            else:
                left = mid + 1
        return nums[left]

# @lc code=end

