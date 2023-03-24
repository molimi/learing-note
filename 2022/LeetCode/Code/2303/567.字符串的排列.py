#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map_s1 = Counter(s1)
        hash_map_s2 = {}
        start = 0
        for end, tail in enumerate(s2):
            hash_map_s2[tail] = hash_map_s2.get(tail, 0) + 1
            if hash_map_s1 == hash_map_s2:
                return True
            if end >= len(s1) - 1:
                head = s2[start]
                hash_map_s2[head] -= 1
                if hash_map_s2[head] == 0:
                    del hash_map_s2[head]
                start += 1 
        return False
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Step 1
        # 定义需要维护的变量
        # 因为和排列相关 (元素相同，顺序可以不同)，使用哈希表
        hash_map_s2 = {}

        # Step 1.1: 同时建立s1的哈希表 (这个哈希表不需要维护，为定值)
        hash_map_s1 = Counter(s1)
        
        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end, tail in enumerate(s2):
            # Step 3: 更新需要维护的变量 (hash_map_s2)， 如果hash_map_s1 == hash_map_s2，代表s2包含s1的排列，直接return
            hash_map_s2[tail] = hash_map_s2.get(tail, 0) + 1
            if hash_map_s1 == hash_map_s2:
                    return True

            # Step 4: 
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (hash_map_s2)
            if end >= len(s1) - 1:
                head = s2[start]
                hash_map_s2[head] -= 1
                if hash_map_s2[head] == 0:
                    del hash_map_s2[head]
                start += 1
        # Step 5： 没有在s2中找到s1的排列，返回False
        return False
# @lc code=end

