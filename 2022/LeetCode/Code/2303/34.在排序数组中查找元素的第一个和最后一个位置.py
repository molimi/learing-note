#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        elif len(nums) == 1:
            return [0,0]
        left, right = 0, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break

        for i in range(mid-1, -1, -1):
            if nums[i] != target:
                break
        for j in range(mid+1, len(nums)):
            if nums[j] != target:
                break
        if i == 0 and nums[i] == target:
            i -= 1
        if j == len(nums)-1 and nums[j] == target:
            j += 1
        return [i+1, j-1]
# @lc code=end

