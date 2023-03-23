#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 用双端队列来存储数组的下标，为什么要存下标而不是存数值？
        # 因为存下标可以更方便的来确定元素是否需要移出滑动窗口
        # 判断下标是否合法来确定是否要移出
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        result, queue = [], deque()             # 使用collections内置的双端队列，加快运行速度
        for i in range(len(nums)):
            # 如果当前队列最左侧存储的下标等于 i-k 的值，代表目前队列已满。
            # 但是新元素需要进来，所以列表最左侧的下标出队列
            if queue and queue[0] == i - k:           
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:      # 对于新进入的元素，如果队列前面的数比它小，那么前面的都出队列
                queue.pop()
            queue.append(i)         # 新元素入队列
            if i >= k-1:            # 当前的大值加入到结果数组中
                result.append(nums[queue[0]])
        
        return result
# @lc code=end

