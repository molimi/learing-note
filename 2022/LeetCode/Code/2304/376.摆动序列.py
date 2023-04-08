#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        j = 0
        while j < len(nums) and nums[j] - nums[0]==0:       # 一开始的值相等
            j += 1
        if j < len(nums):       
            if nums[j] - nums[0] > 0:
                k = 1 
            elif nums[j] - nums[0] < 0:
                k = -1
        else:               # 全不值都相等，直接k=0
            return 1

        count = 1           # 初识第一个默认为峰值
        for i in range(j, len(nums)):
            if (nums[i] - nums[i-1])*k > 0:         # 只要是峰值就满足条件，进行统计
                count += 1
                k *= -1
        return count
            
# @lc code=end

