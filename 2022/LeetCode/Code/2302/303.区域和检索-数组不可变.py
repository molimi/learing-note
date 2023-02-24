#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
# 思路一：直接每次求和，返回结果
# 思路二：利用前缀和，存储数据的求和结果。利用索引直接遍历，提升效率

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_array = [0]        # 便于计算累加和
        for num in nums:
            self.nums_array.append(self.nums_array[-1] + num) # 计算nums累加和

    def sumRange(self, left: int, right: int) -> int:
        nums_array = self.nums_array
        return nums_array[right+1] - nums_array[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

