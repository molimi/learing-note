"""
@author: CarpeDiem
@date: 22/11/25
@version: 0.1
@description: 栈要考虑大小
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)