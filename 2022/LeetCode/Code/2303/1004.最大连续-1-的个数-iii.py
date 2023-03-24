#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, start = 0, 0
        hash_map = {}
        for end, tail in enumerate(nums):
            hash_map[tail] = hash_map.get(tail, 0) + 1
            if hash_map.get(0, 0) <= k:     # 相比较于上一题，只需要把1改成k
                max_len = max(max_len, end-start+1)
            while hash_map.get(0, 0) > k:
                head = nums[start]
                hash_map[head] -= 1
                start += 1
        return max_len
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, hashmap = 0, {}

        start =  0
        for end in range(len(nums)):
            tail = nums[end]
            hashmap[tail] = hashmap.get(tail, 0) + 1
            if hashmap.get(0, 0) <= k:
                max_len = max(max_len, end - start + 1)

            # 相比较于上一题，只需要把1改成k
            while hashmap.get(0, 0) > k:
                head = nums[start]
                hashmap[head] -= 1
                start += 1
        return max_len



# @lc code=end

