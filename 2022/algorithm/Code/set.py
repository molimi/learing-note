"""
@author: CarpeDiem
@date: 23/2/20
@version: 0.1
@description: 集合的实现
"""
import copy

class Set:
    """集合类"""
    MaxSize = 100                           # 集合中最多元素个数
    def __init__(self):
        self.data = [None] * Set.MaxSize    # data 存放集合
        self.size = 0                       # data 为集合长度

    def get_size(self):
        '''返回集合长度'''
        return self.size

    def get(self, i):                       # 返回集合的第i个元素
        assert i >=0 and i < self.size
        return self.data[i]

    def is_in(self, e):                     # 判断 e 是否在集合中
        for i in range(self.size):
            if self.data[i] == e:
                return True
        return False

    def add(self, e):                       # 将元素e添加到集合中
        if not self.is_in(e):
            self.data[self.size] = e
            self.size += 1

    def delete(self, e):                    # 从集合中删除元素e
        i = 0
        while i < self.size and self.data[i] != e:
            i += 1
        if i >= self.size:                  # 为找到元素直接返回
            return
        for j in range(i, self.size-1):     # 找到元素e后通过移动实现删除
            self.data[j] = self.data[j+1]   # 考虑越界问题      
        self.size -= 1

    def copy(self):                         # 返回当前集合的复制集合
        s1 = Set()
        s1.data = copy.deepcopy(self.data)
        s1.size = self.size  
        return s1                

    def display(self):                      # 输出集合中的元素
        for i in range(self.size):
            print(self.data[i], end= ' ')
        print()

    def union(self, s2):                    # 求 s3 = s1 ∪ s2 s1 为当前集合
        s3 = self.copy()
        for i in range(s2.get_size()):
            e = s2.get(i)
            if not self.is_in(e):
                s3.add(e)
        return s3

    def inter(self, s2):                    # s3 = s1 ∩ s2
        s3 = Set()
        for i in range(self.size):
            e = self.data[i]
            if s2.is_in(e):
                s3.add(e)
        return s3

    def diff(self, s2):                     # 求 s3 = s1 -s2
        s3 = Set()
        for i in range(self.size):
            e = self.data[i]
            if not s2.is_in(e):
                s3.add(e)
        return s3
    
if __name__ == '__main__':
    """对Set集合类进行测试"""
    s1 = Set()
    s1.add(1)
    s1.add(4)
    s1.add(2)
    s1.add(6)
    s1.add(8)
    print('s1的长度为 {}'.format(s1.get_size()))
    print('s1的第2个元素为 {}'.format(s1.get(1)))
    print('集合s1是: ', end=' '), s1.display()
    s2 = Set()
    s2.add(2)
    s2.add(5)
    s2.add(3)
    s2.add(6)
    print('集合s2: ', end= ' '), s2.display()
    print("集合s1和集合s2的并集->s3")
    s3 = s1.union(s2)
    print("集合s3: ", end=' '), s3.display()
    print("集合s1和集合s2的交集->s4")
    s4 = s1.inter(s2)
    print("集合s4: ", end=' '), s4.display()
    print("集合s1和集合s2的差集->s5")
    s5 = s1.diff(s2)
    print("集合s5: ", end=' '), s5.display()