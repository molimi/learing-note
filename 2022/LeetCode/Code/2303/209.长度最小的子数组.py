#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
# 滑动窗口

# @lc code=start
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if min(nums) > target or sum(nums) < target:
            return 0
        min_len = inf
        head, tail = 0, 0
        total = 0
        while tail < len(nums):
            total += nums[tail]
            while total >= target:
                min_len = min(min_len, tail - head + 1)
                total -= nums[head]
                head += 1
            tail += 1

        return min_len
        '''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Step 1: 定义需要维护的变量, 本题求最小长度，所以需要定义min_len, 本题又涉及求和，因此还需要一个sum变量
        min_len, sum_sub_array = math.inf, 0

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end, num in enumerate(nums):
            # Step 3: 更新需要维护的变量 (min_len, sum_sub_array)
            sum_sub_array += num

            # 这一段可以删除，因为下面的while已经handle了这一块儿逻辑，不过写在这也没影响
            if sum_sub_array >= target:
                min_len = min(min_len, end - start + 1)

            # Step 4
            # 这一题这里稍微有一点特别: sum_sub_array >= target其实是合法的，但由于我们要求的是最小长度，
            # 所以当sum_sub_array已经大于target的时候继续移动右指针没有意义，因此还是需要移动左指针慢慢逼近答案
            # 由于左指针的移动可能影响min_len和sum_sub_array的值，因此需要在移动前将它们更新
            while sum_sub_array >= target:
                min_len = min(min_len, end - start + 1)
                sum_sub_array -= nums[start]
                start += 1
        # Step 5：返回答案 (最小长度)
        if min_len == math.inf:
            return 0
        return min_len
# @lc code=end

