#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        hash_map, res, stack = {}, [], []
        for index, temperature in enumerate(temperatures):
            if not stack:
                stack.append(index)          # 这里的哈希表同时存储索引，也可以直接放元素的索引
            else:
                if temperature <= temperatures[stack[-1]]:             # 单调栈，温度是单调递增的
                    stack.append(index)
                else:
                    while stack and temperatures[stack[-1]] < temperature:
                        hash_map[stack[-1]] = index - stack[-1]
                        stack.pop()
                    stack.append(index)
        for index in stack:
            hash_map[index] = 0
        for index in range(len(temperatures)):
            res.append(hash_map[index])
        return res
        '''
        res, stack = [0]*len(temperatures), []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                res[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return res
# @lc code=end

