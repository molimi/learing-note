#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sorted = sorted(nums)
        diff = float('inf')         # 初始化，因为找最小值，因此把初始值设置成实数的最大值
        length = len(nums)          # 排序是前提
        for i in range(length):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:    # 常见的剪枝操作
                continue
            left = i+1                                          # 双指针：指针对撞
            right = length-1 
            while left < right:
                temp = nums_sorted[left] + nums_sorted[right] + nums_sorted[i]
                if abs(temp-target) < diff:     
                    diff = abs(temp-target)
                    ans = temp
                # 不管是变小还是变大，尝试的作用是让 temp 与 target 更接近，即 temp 与 target 的绝对值之差越来越小
                if temp > target:        # 如果大了，尝试右边界收缩一格，让 temp 变小
                    right -= 1
                elif temp < target:     # 如果小了，尝试左边界收缩一格，让 target 变大
                    left += 1
                else:                   # 如果已经等于 target 的话, 肯定是最接近的，根据题目要求，返回这三个数的和
                    return target
        return ans
# @lc code=end

