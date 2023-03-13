#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        nums_set = {n}
        while True:
            if n == 1:
                return True
            n = self.split_num(n)
            if n not in nums_set:
                nums_set.add(n)
            else:
                return False

    def split_num(self, n):
        if 0 <= n < 10:
            return n*n
        return (n%10)**2 + self.split_num(n//10)
# @lc code=end

