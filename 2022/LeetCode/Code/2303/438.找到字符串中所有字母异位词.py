#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
'''
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_map_p = Counter(p)     # 固定要匹配的字符串
        hash_map_s = {}
        start = 0
        ans = []
        for end, tail in enumerate(s):
            hash_map_s[tail] = hash_map_s.get(tail, 0) + 1
            if hash_map_s == hash_map_p:        # 判断字典是否相同，来判断是否是异位词
                ans.append(start)
            # 固定窗口，用 if 即可单个滑动
            if end >= len(p) - 1:
                head = s[start]
                hash_map_s[head] -= 1
                if hash_map_s[head] == 0:
                    del hash_map_s[head]
                start += 1
        return ans
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Step 1: 
        # 定义需要维护的变量
        # 本文需要对比两组字符串是否为异位词，所以用哈希表 (abc和bac是异位词是因为他们对应的哈希表相等)
        # 同时我们需要找到所有合法解，所以还需要一个ans数组
        ans, hashmap_s = [], {}

        # Step 1.1： 同时把p的哈希表也建立了 (这个哈希表不需要维护，为定值)
        hashmap_p = Counter(p)

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end, tail in enumerate(s):
            # Step 3: 更新需要维护的变量 (hashmap)， 如果hashmap == hashmap_p，代表找到了一个解，加入到ans
            hashmap_s[tail] = hashmap_s.get(tail, 0) + 1
            if hashmap_s == hashmap_p:
                ans.append(start)

            # Step 4 
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (hashmap)
            if end >= len(p) - 1:
                head = s[start]
                hashmap_s[head] -= 1
                if hashmap_s[head] == 0:
                    del hashmap_s[head]
                start += 1
        # Step 5: 返回答案
        return ans
# @lc code=end

