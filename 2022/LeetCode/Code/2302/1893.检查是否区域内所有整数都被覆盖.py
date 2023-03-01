#
# @lc app=leetcode.cn id=1893 lang=python3
#
# [1893] 检查是否区域内所有整数都被覆盖
# 这道题目就别想利用区间的做法，直接暴力法，多重循环做一下
# 差分数组也可以做

# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        '''
        flag = [0 for _ in range(51)]
        for interval in ranges:
            start, end = interval[0], interval[1]
            for i in range(start, end+1):
                flag[i] += 1
        for j in range(left, right+1):
            if flag[j] == 0:
                return False
  
        return True
        '''
        diff = [0] * 52
        for interval in ranges:
            diff[interval[0]] += 1
            diff[interval[1]+1] -= 1

        for i in range(1, 52):
            diff[i] += diff[i-1]
        for i in range(left, right+1):
            if diff[i] == 0:
                return False
        return True
# @lc code=end

