#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res, stack = [-1]*length, []        # 存在重复元素，单调栈存放元素索引
        for i in range(length*2):           # 这里对环形数组求余数，变为原来的两倍，从而实现闭环
            while stack and nums[stack[-1]] < nums[i%length]:
                res[stack[-1]] = nums[i%length]
                stack.pop()
            stack.append(i%length)
        return res
# @lc code=end

