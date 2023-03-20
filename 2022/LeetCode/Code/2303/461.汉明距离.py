#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
        '''
        z = x ^ y
        count = 0
        while z:
            count += 1
            z = z & (z-1)
        return count
        
        z = bin(x ^ y)[2:]
        count = 0
        for bt in z:
            if bt == '1':
                count += 1
        return count
        '''
# @lc code=end

