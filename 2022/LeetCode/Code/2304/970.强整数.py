#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

# @lc code=start
from math import log
from typing import List
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        '''
        # 穷举法超时
        i = 0
        res = set()
        while x ** i <= bound:
            temp = x ** i
            j = 0
            while y ** j + temp <= bound:
                res.add(y ** j + temp)
                j += 1
            i += 1
        return list(res)
        '''
        def power_bound(num, bound):
            if bound == 0: return []
            if num == 1: return [1]
            num_bound = int(log(bound, num))        # 取对数，要注意底数不能为1，bound!=0
            nums_list = [1]
            for _ in range(1, num_bound+1):
                nums_list.append(nums_list[-1]*num)
            return nums_list
        
        x_list = power_bound(x, bound)
        y_list = power_bound(y, bound)
        res = []
        for num1 in x_list:
            for num2 in y_list:
                if num1 + num2 <= bound:
                    res.append(num1+num2)
        return list(set(res))

s = Solution()
print(s.powerfulIntegers(2, 3, 10))   
# @lc code=end

