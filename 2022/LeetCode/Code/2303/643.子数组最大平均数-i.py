#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        temp = max_value = sum(nums[:k])
        for i in range(k, len(nums)):
            temp = temp + nums[i] - nums[i-k]
            max_value = max(max_value, temp)
            
        return max_value/k
        
        # Step 1
        # 定义需要维护的变量
        # 本题求最大平均值 (其实就是求最大和)，所以需要定义sum_sub_array, 同时定义一个max_value (初始值为负无穷)
        sum_sub_array, max_value = 0, float('-inf')

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end, num in enumerate(nums):
            # Step 3: 更新需要维护的变量 (sum_sub_array, max_value), 不断把当前值积累到sum_sub_array上
            sum_sub_array += num
            if end - start + 1 == k:
                max_value = max(max_value, sum_sub_array)

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口首指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_sub_array)
            if end >= k - 1:
                sum_sub_array -= nums[start]
                start += 1
        # Step 5: 返回答案
        return max_value/k
        '''
        # 前缀和
        pre_sum = [0]
        max_value = float('-inf')
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1]+nums[i])
        for i in range(len(nums)-k+1):
            max_value = max(max_value, pre_sum[i+k]-pre_sum[i])
        return max_value/k
# @lc code=end

