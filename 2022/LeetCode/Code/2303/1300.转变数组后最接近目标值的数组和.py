#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
    # def findBestValue(self, arr, target) -> int:
        '''枚举+二分查找'''
        sorted_arr = sorted(arr)
        length = len(arr)
        pre_sum = [0]
        diff, res = target, 0
        for num in sorted_arr:
            pre_sum.append(pre_sum[-1]+num)
        max_arr = max(arr)
        for x in range(1, max_arr+1):           # 先穷举x，再查找左边界
            left, right = 0, length
            while left < right:
                mid = (left+right) // 2
                if sorted_arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            if left < length and sorted_arr[left] >= x:
                curr = pre_sum[left] + x * (length-left)
                if abs(curr - target) < diff:
                    diff = abs(curr-target)
                    res = x
        return res
'''
s = Solution()
s.findBestValue([2,9,2], 10)
'''
# @lc code=end

