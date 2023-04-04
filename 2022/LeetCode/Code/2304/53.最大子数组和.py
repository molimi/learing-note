#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        max_sum = float('-inf')
        for i in range(length):
            sum_sub_array = 0
            for j in range(i, length):
                sum_sub_array += nums[j]
                max_sum = max(max_sum, sum_sub_array)
        return max_sum
        '''
        # 时间复杂度：O(n),遍历了一遍
        # 空间复杂度:O(1)，用了2个变量
        cur_sum=nums[0]
        max_sum=nums[0]
        #range范围是[1，len(nums)) 左开右闭，切记切记
        for i in range(1,len(nums)):
            #若当前指针指向元素之前的和小于0，则丢弃此元素之前的数列(拖后腿的丢弃！！！)
            #当前和=当前值 与 当前值+之前最大和 的比较中较大的那个、
            #通俗易懂的理解：看当前这个值和之前数列的和，是否会拖当前这个值的后腿，如果扯后腿了说明没必要把之前的数列放到当前和，如果没有扯后腿则把最新的较大数放在当前和里面
            cur_sum=max(nums[i],cur_sum+nums[i])
            #最大和=当前和 与 最大和 的比较中较大的那个
            #通俗易懂的理解：当前和就相当于当前潜在的最大和，把原来的最大和 与当前的潜在最大和进行比较，如果当前和比较大，则更换最大和，否则不更换
            max_sum=max(cur_sum,max_sum)
        return max_sum
        '''
# @lc code=end

