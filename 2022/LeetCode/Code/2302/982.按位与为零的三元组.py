#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#

# @lc code=start
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        cnt = Counter(i&j for i in nums for j in nums)
        ans = 0
        for k in nums:
            for mask, item in cnt.items():
                if k & mask == 0:
                    ans += item
        return ans
# @lc code=end

