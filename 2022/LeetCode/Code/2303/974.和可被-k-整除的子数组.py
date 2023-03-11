#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
# 暴力法超时，前缀和数组上

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # 同余定理
        res_dict = {0: 1}       # 考虑前缀和本来就被整除[5,5,5]的话就是 3+3, 也可以是C(n, 2)
        total, count = 0, 0
        for num in nums:
            total += num
            res = total % k
            temp = res_dict.get(res, 0)
            count += temp
            res_dict[res] = temp + 1
        return count

# @lc code=end

