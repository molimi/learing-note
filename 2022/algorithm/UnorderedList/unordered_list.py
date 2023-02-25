#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/18
@version: 0.1
@description: 无序列表
"""
from node import Node

class UnOrderedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if item == current.get_data():
                found = True
            else:
                current = current.get_next()
        
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:                # current是首个节点
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


if __name__ == "__main__":
    """测试代码"""
    my_list = UnOrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    print(my_list.search(17))
    my_list.remove(17)
    print(my_list.search(17))
    