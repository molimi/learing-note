#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        # 维持一个长度为k的集合
        hash_set = set()
        for i, num in enumerate(nums):
            if num in hash_set:
                return True
            hash_set.add(num)
            if len(hash_set) > k:
                hash_set.remove(nums[i-k])
        return False
        '''
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map and abs(i - hash_map[num]) <= k:
                return True
            else:
                hash_map[num] = i
        return False

# @lc code=end

