#
# @lc app=leetcode.cn id=1574 lang=python3
#
# [1574] 删除最短的子数组使剩余数组有序
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''发现通式，两端遍历'''
        length = len(arr)
        right = length - 1
        while right and arr[right] >= arr[right - 1]:      # 找到右边的非递减序列
            right -= 1
        if right == 0:
            return 0

        ans = right
        left = 0
        while left == 0 or arr[left] >= arr[left - 1]:      # 找到左边非递减序列
            while right < length and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right-left-1)
            left += 1
        return ans
# @lc code=end

