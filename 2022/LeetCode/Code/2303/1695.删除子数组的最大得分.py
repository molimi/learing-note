#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash_map = {}
        max_value = 0
        temp = 0
        start = 0
        for end, num1 in enumerate(nums):
            hash_map[num1] = hash_map.get(num1, 0) + 1
            temp += num1
            if len(hash_map) == end - start + 1:
                max_value = max(max_value, temp)
            while len(hash_map) < end-start+1:
                num2 = nums[start]
                temp -= num2
                hash_map[num2] -= 1
                if hash_map[num2] == 0:
                    del hash_map[num2]
                start += 1
        return max_value
'''
s = Solution()
print(s.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))
'''
# @lc code=end

