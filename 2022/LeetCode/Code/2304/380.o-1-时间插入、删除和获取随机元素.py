#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:
    '''
    元素存储使用数组，索引使用字典
    想在 O(1) 的时间删除数组中的某一个元素 val，
    可以先把这个元素交换到数组的尾部，然后再 pop 掉
    '''
    def __init__(self):
        self.nums = []                  # 存储元素值
        self.val_to_index = {}          # 记录每个元素对应在 nums 中的索引

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:    # 若val已存在，不用再插入
            return False
        self.val_to_index[val] = len(self.nums) # 若val不存在，插入到 nums 尾部
        self.nums.append(val)
        return True                     # 并记录val对应的索引值

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:            # 若val不存在，不再用删除
            return False
        index = self.val_to_index[val]              # 先拿到 val 的索引
        self.val_to_index[self.nums[-1]] = index    # 将最后一个元素对应的索引修改为 index
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]   # 交换 val 和最后一个元素
        self.nums.pop()                             # 在数组中删除元素 val
        del self.val_to_index[val]                  # 删除元素 val 对应的索引
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)     # 随机获取 nums 中的一个元素


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

