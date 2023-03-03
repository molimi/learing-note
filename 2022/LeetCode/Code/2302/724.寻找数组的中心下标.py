#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
# 利用前缀和数组求解会更快一点

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
        for i in range(1, len(pre_sum)):
            if pre_sum[i-1] == pre_sum[-1] - pre_sum[i]:
                return i-1
        return -1
# @lc code=end

