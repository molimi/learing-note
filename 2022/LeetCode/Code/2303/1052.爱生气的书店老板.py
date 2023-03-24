#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_sum, sum_sub_array, start, max_start = 0, 0, 0, 0
        for end, tail in enumerate(customers):
            if grumpy[end] == 1:
                sum_sub_array += tail
            if sum_sub_array > max_sum:
                max_sum = sum_sub_array
                max_start = start
            if end >= minutes - 1:
                head = customers[start]
                if grumpy[start] == 1:
                    sum_sub_array -= head
                start += 1
 
        grumpy[max_start:max_start+minutes] = [0] * minutes
        res = 0
        for customer, grum in zip(customers, grumpy):
            if grum == 0:
                res += customer
        return res
# @lc code=end

