#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask1 = 0xffffffff
        a &= mask1
        b &= mask1
        while b:
            carry = (a & b) << 1       # 将存在进位的位置置1
            a ^= b                      # 计算无进位的结果
            b = carry
        return a if a < 0x80000000 else ~(a^mask1)  # 考虑负数时的输出
# @lc code=end

