#
# @lc app=leetcode.cn id=710 lang=python3
#
# [710] 黑名单中的随机数
#

# @lc code=start
import random
class Solution:
    '''
    将黑名单中的数字, 映射到白名单。
    这样即使 pick 到黑名单的索引, 找出对应的值, 
    还是白名单中的值
    '''
    def __init__(self, n: int, blacklist: List[int]):
        self.white = n - len(blacklist)         # 白名单长度
        self.hash_map = {}      
        for num in blacklist:                   # 将黑名单的值先添加到字典
            self.hash_map[num] = 888            # 取任何值都可以

        last = n - 1                            # 在黑名单区 要映射的指针
        for num in blacklist:
            if num >= self.white:               # 黑名单中的值 已经在 黑名单的区间, 那么可以忽略
                continue
            while last in self.hash_map:        # last对应的值已经在黑名单中
                last -= 1
            self.hash_map[num] = last
            last -= 1


    def pick(self) -> int:
        res = random.randint(0, self.white-1)   # 在白名单部分随机挑选
        if res in self.hash_map:                # 如果在黑名单中, 那么就映射为白名单的值
            return self.hash_map[res]
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

