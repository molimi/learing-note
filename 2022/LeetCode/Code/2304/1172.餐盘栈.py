#
# @lc app=leetcode.cn id=1172 lang=python3
#
# [1172] 餐盘栈
#

# @lc code=start
from sortedcontainers import SortedSet
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.not_full = SortedSet() 

    def push(self, val: int) -> None:
        if not self.not_full:               # 全满，直接添加元素
            self.stack.append([val])
            if self.capacity > 1:
                self.not_full.add(len(self.stack)-1)
        else:
            ind = self.not_full[0]
            self.stack[ind].append(val)
            if len(self.stack[ind]) == self.capacity:   # 判断添加元素是否满了
                self.not_full.discard(ind)

    def pop(self) -> int:
        return self.popAtStack(len(self.stack)-1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index > len(self.stack) - 1 or not self.stack[index]:
            return -1
        val = self.stack[index].pop()
        if index == len(self.stack) -1 and not self.stack[-1]:      # 把后面的空栈给删除掉，若最后一个栈为空，则not_full存的元素就没有意义
            while self.stack and not self.stack[-1]:
                self.not_full.discard(len(self.stack)-1)
                self.stack.pop()
        else:
            self.not_full.add(index)
        return val
        
        

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# @lc code=end

