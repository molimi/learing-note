#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_sorted = sorted(nums)
        result = []
        length = len(nums)
        for i in range(length): 
            # 剪枝处理
            if nums_sorted[i] > target and nums_sorted[i] >= 0:
                break
            # 对 nums_sorted[i] 去重
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            for j in range(i+1, length):        # 比原来多一层循环
                # 二级剪枝处理
                if nums_sorted[i] + nums_sorted[j] > target and nums_sorted[i] + nums_sorted[j] >= 0:
                    break   # 这里直接 return 会出错
                # 对 nums_sorted[j] 去重
                if j > i+1 and nums_sorted[j] == nums_sorted[j-1]:
                    continue
                left = j + 1
                right = length - 1
                while left < right:
                    if nums_sorted[i] + nums_sorted[j] + nums_sorted[left] + nums_sorted[right] == target:
                        result.append([nums_sorted[i], nums_sorted[j], nums_sorted[left], nums_sorted[right]])
                        while left < right and nums_sorted[left] == nums_sorted[left+1]:
                            left += 1
                        while left < right and nums_sorted[right] == nums_sorted[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums_sorted[i] + nums_sorted[j] + nums_sorted[left] + nums_sorted[right] > target:
                        right -= 1
                    else:
                        left += 1
        return result

# @lc code=end

