#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets
   
    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                item[1] = value
                return
        self.table[hash_key].append([key, value])

    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        for i, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                self.table[hash_key].pop(i)
                return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

