#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for num in nums:            # 异或运算，目的是找到两个落单数值的不同，便于后面分类
            mask ^= num
        mask  &= (-mask)            # 找到二者某一位的不同，将这一位定为分类依据
        type1, type2 = 0, 0         
        for num in nums:            # 把数组分为两部分，每部分再分别异或
            if mask & num:          # 对于 num，如果 mask 为1，分类为 type1，对这个 type1 进行异或，可以找到落单的数值
                type1 ^= num
            else:                   # 如果 num 的 mask 对应的是0，那么异或找到另一个落单的数值
                type2 ^= num
        return [type1, type2] 
# @lc code=end

