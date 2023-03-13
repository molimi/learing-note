#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
# 貌似哈希表会超时啊，有去重步骤，采用排序和双指针，双指针可以降低复杂度

# @lc code=start
from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums_dict = defaultdict(list)
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                nums_dict[nums[i]+nums[j]].append([nums[i],nums[j]])
        for key, value in nums_dict.items():
            if -key in set(nums):
                ind = [num for num in nums if num == -key]
                for ind1 in ind:
                    for v in value:
                        if v.count(ind1) < nums.count(ind1):
                            temp = sorted(v + [ind1])
                            if temp not in result: 
                                result.append(temp)
        return result
        '''
        nums_sorted = sorted(nums)
        result = []
        for i in range(len(nums_sorted)):
            if nums_sorted[i] > 0:                              # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
                return result
            '''
            # 错误去重a方法，将会漏掉-1,-1,2 这种情况
            if (nums[i] == nums[i + 1]) {
                continue;
            }
            '''
            if i>0 and nums_sorted[i] == nums_sorted[i-1]:      # 第一个数大于 0，后面的数都比它大，肯定不成立了
                continue
            left = i+1
            right = len(nums_sorted)-1
            while left < right:
                '''
                # 去重复逻辑如果放在这里，0，0，0 的情况，可能直接导致 right<=left 了，从而漏掉了 0,0,0 这种三元组
                while (right > left && nums[right] == nums[right - 1]) right--;
                while (right > left && nums[left] == nums[left + 1]) left++;
                '''
                if nums_sorted[i]+nums_sorted[left]+nums_sorted[right] == 0:
                    result.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    # 在要增加 left，减小 right，但是不能重复，比如: [-2, -1, -1, -1, 3, 3, 3], 
                    # i = 0, left = 1, right = 6, [-2, -1, 3] 的答案加入后，需要排除重复的 -1 和 3
                    while left < right and nums_sorted[left] == nums_sorted[left+1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right-1]:
                        right -= 1
                    # 找到答案时双指针同时收缩
                    left += 1
                    right -= 1
                elif nums_sorted[i]+nums_sorted[left]+nums_sorted[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result
# @lc code=end

