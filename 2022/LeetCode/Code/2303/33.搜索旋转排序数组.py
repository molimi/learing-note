#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:                        # 左半部分有序
                if nums[0] <= target < nums[mid]:           # target 在左半部分
                    right = mid - 1
                else:
                    left = mid + 1
            else:                                           # 右半部分有序
                if nums[mid] < target <= nums[len(nums)-1]: # target 在右半部分
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    '''
        # 先找有序的那一段
        head, length = 0, len(nums)
        while head+1 < length and nums[head] < nums[head+1]:
            head += 1
        if nums[0] <= target:
            flag = self.binarySearch(nums[:head+1], target)
            return flag if flag != -1 else -1
        else:
            flag = self.binarySearch(nums[head+1:], target)
            return head+1+flag if flag != -1 else -1
        
    def binarySearch(self, nums: List[int], target: int):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    '''

# @lc code=end

