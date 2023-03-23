#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        '''
        result = []
        for bt in bin(num)[2:]:
            if bt == '0':
                result.append('1')
            else:
                result.append('0')
        return int(''.join(result), 2)
        
        num_copy = num
        num_1 = 1
        while num_copy:
            num_1 <<= 1 
            num_copy >>= 1
        return num ^ (num_1-1)
        '''
        i, ans = 0, 0
        while num:
            if not (num & 1):
                ans |= (1 << i)
            num >>= 1
            i += 1
        return ans

# @lc code=end

