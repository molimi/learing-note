#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
#

# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        '''
        # 双变量问题，先穷举一个变量，再去寻找另一个变量
        '''
        max_value = 0
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1]+num)

        for i in range(0, len(nums)-firstLen+1):
            res1 = pre_sum[i+firstLen]-pre_sum[i]
            res2 = self.sliding_window(nums[:i]+nums[i+firstLen:], secondLen)
            max_value = max(max_value, res1+res2)
        return max_value
    

    def sliding_window(self, arr, arr_len):
        if arr_len == 1: return max(arr)
        left = 0
        max_value = 0
        temp = 0
        for right, tail in enumerate(arr):
            temp += tail
            if right - left + 1 == arr_len:
                max_value = max(max_value, temp)
            if right >= arr_len-1:
                temp -= arr[left]
                left += 1
        return max_value
# @lc code=end

