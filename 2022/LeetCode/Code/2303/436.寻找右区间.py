#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#

# @lc code=start
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        ind = sorted(range(length), key=lambda i: intervals[i][0])      # 索引排序
        ans = []
        for _, end in intervals:
            left, right = 0, length
            while left < right:
                mid = (left + right) // 2
                if sorted_intervals[mid][0] < end:
                    left = mid + 1
                else:
                    right = mid
            if left >= length or sorted_intervals[left][0] < end:
                ans.append(-1)
            else:
                ans.append(ind[left])
                
        return ans
'''
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_map = {interval[0] : i for i, interval in enumerate(intervals)}       # 以区间左侧构建索引字典
        starts = [interval[0] for interval in intervals]                            # 取出区间的左侧
        res = []
        starts.sort()
        for interval in intervals:
            pos = self.higher_find(starts, interval[1])                             # 遍历每个区间的右侧，在所有区间的左侧进行二分查找
            res.append(start_map[starts[pos]] if pos != -1 else -1)
        return res
    
    def higher_find(self, nums, target):
        left, right = 0, len(nums)              # 左闭右开
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if left < len(nums) and nums[left] >= target:    # 最后判断一下，是否满足条件
            return left
        return -1

# @lc code=end

