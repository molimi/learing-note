#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
class MedianFinder:
    # heapq默认是最小堆，所以在最大堆添加时传入负值
    def __init__(self):
        self.small_heap = []        # 最大堆
        self.large_heap = []        # 最小堆

    def addNum(self, num: int) -> None:
        if len(self.small_heap) < len(self.large_heap):                 # 加到small堆中
            # 先将num加到large中，再将large中的最小值弹出加入到small
            small_num = heapq.heappushpop(self.large_heap, num)     
            heapq.heappush(self.small_heap, -small_num)
        else:
            # 先将num加到small中，再将small中的最小值弹出加入到large
            large_num = -heapq.heappushpop(self.small_heap, -num)
            heapq.heappush(self.large_heap, large_num)

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            small = - self.small_heap[0]
            large = self.large_heap[0]
            return (large+small)/2
        else:
            mid = self.large_heap[0]
            return mid


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

