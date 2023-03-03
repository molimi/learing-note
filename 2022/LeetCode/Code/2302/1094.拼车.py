#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * (1001)      # 题目中最多有1001个车站
        max_station = 0
        for trip in trips:
            inc, start, end = trip[0], trip[1], trip[2]
            diff[start] += inc
            diff[end] -= inc     # 第end站乘客已经下车，这里就不用end+1
            max_station = max(max_station, end)
        for i in range(1, max_station+1): # 进行区间求和
            diff[i] += diff[i-1]
        if max(diff[:max_station]) > capacity:
            return False
        return True

# @lc code=end

