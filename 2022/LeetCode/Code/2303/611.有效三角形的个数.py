#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

# @lc code=start
class Solution:
    # def triangleNumber(self, nums: List[int]) -> int:
    def triangleNumber(self, nums) -> int:
        nums.sort()
        length = len(nums)
        ans = 0
        for i in range(length):
            for j in range(i+1, length):
                left, right = j+1, length              
                while left < right:
                    mid = (left + right)//2
                    if nums[mid] < nums[i] + nums[j]:
                        left = mid + 1
                    else:
                        right = mid
                ans += left - 1 - j
            
        return ans
'''
s = Solution()
s.triangleNumber([2,2,2,2,2,2])
'''
# @lc code=end

