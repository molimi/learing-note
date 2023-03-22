#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        count = 0
        while n:
            n &= (n-1)
            count += 1
        return count
        '''
        return bin(n).count('1')
# @lc code=end

