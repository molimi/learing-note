#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        ans = []
        for i in range(n+1):
            ans.append(bin(i).count('1'))
        return ans
        '''
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = ans[i>>1] + (i&1)
        return ans
    
# @lc code=end

