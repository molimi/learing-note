#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start

'''
import math
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 逆向思维，去中间最小就是两边最大
        sum_sub_array, min_sum, start = 0, float('inf'), 0
        length = len(cardPoints)
        for end, tail in enumerate(cardPoints):
            sum_sub_array += tail
            if length - k == end - start + 1:
                min_sum = min(min_sum, sum_sub_array)
            if end >= len(cardPoints)-k-1:
                sum_sub_array -= cardPoints[start]
                start += 1
        return sum(cardPoints)-min_sum if min_sum != inf else sum(cardPoints)
'''

class Solution:
    # 这题相比前面的题目加了一丢丢小的变通: 题目要求首尾串最大点数，其实就是求非首尾串的连续序列的最小点数
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Step 1
        # 定义需要维护的变量，因为涉及求和所以定义sum_sub_array和min_sum
        sum_sub_array, min_sum = 0, float('inf')

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end, tail in enumerate(cardPoints):
            # Step 3
            # 更新需要维护的变量 (sum_sub_array)
            sum_sub_array += tail
            if len(cardPoints)-k == end - start + 1:
                min_sum = min(min_sum, sum_sub_array)
            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (min_sum， sum_sub_array)
            if end >= len(cardPoints) - k - 1:
                sum_sub_array -= cardPoints[start]
                start += 1
        # Step 5: 返回答案 (总点数减去非首尾串的连续序列的最小点数就可以得到首尾串的最大点数)
        return sum(cardPoints) - min_sum if min_sum != inf else sum(cardPoints)

# @lc code=end

