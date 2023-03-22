#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    BIG = 2**30
    def isPowerOfTwo(self, n: int) -> bool:
        # return True if n>=0 and bin(n).count('1') == 1 else False
        # return True if bin(n&0xffffffff).count('1') == 1 else False
        # return n>0 and n&(-n)==n
        return n>0 and Solution.BIG % n == 0        # 看是不是最大数的约数
# @lc code=end

