#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#


# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sum = [0]
        reverse_sum = [0]
        length = len(nums)
        if length == 1:
            return 1 if lower <= nums[-1] <= upper else 0
        for i in range(length):
            pre_sum.append(pre_sum[-1] + nums[i])
            reverse_sum.append(reverse_sum[-1] + nums[length - i - 1])

        count = 0
        for item in pre_sum[1:]:
            if lower <= item <= upper:
                count += 1
        for item in reverse_sum[1:]:
            if lower <= item <= upper:
                count += 1
        return count


# @lc code=end
