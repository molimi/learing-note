#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+2)
        for booking in bookings:
            start, end, inc = booking[0], booking[1], booking[2]
            diff[start] += inc
            diff[end+1] -= inc
        for i in range(1, n+1):
            diff[i] += diff[i-1]
        return diff[1:-1]

# @lc code=end

