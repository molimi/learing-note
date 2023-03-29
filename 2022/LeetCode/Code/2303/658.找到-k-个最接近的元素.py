#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
import copy
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        length = len(arr)
        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > x:
                right = mid
            else:
                left = mid + 1
        if left == 0:
            return arr[:left+k]
        elif left == length:
            return arr[length-k:length]
        else:
        '''
        # 双指针删除元素，二分法太复杂，就不看了
        length = len(arr)
        count = 0
        left, right = 0, length-1
        while count < length-k:
            count += 1
            if abs(x-arr[left]) <= abs(x-arr[right]):       # 删去距离远的
                right -= 1
            else:
                left += 1
        return arr[left:left+k]
# @lc code=end

