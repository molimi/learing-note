#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/25
@version: 0.1
@description: 单向循环链表的实现
"""
class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkedList(object):
    """单向循环链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None
    
    def length(self):
        """返回链表的长度"""
        if self.is_empty():     # 如果链表长度为空，返回长度0
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)
        print()

    def add(self, item):
        """头部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head      # 添加的节点指向_head 
            cur = self._head            # 移到链表尾部，将尾部的节点的 next指向node
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            # _head 指向添加的node
            self._head = node

    def append(self, item):
        """尾部添加节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head        # 移到链表尾部
            while cur.next != self._head:
                cur = cur.next
            cur.next = node         # 将尾结点指向node
            node.next = self._head  # 将node指向头节点_head

    def insert(self, pos, item):
        """在指定位置添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():     # 若链表为空直接返回
            return
        cur = self._head        # 将cur指向头节点
        pre = None
        if cur.item == item:    # 若头结点的元素就是要查找的元素item
            if cur.next != self._head:  
                while cur.next != self._head:   # 先找到尾结点，将尾结点的next指向第二个节点
                    cur = cur.next      
                cur.next = self._head.next      # cur指向了尾结点
                self._head = self._head.next
            else:
                self._head = None               # 链表只有一个节点
        else:
            pre = self._head
            while cur.next != self._head:        # 第一个节点不是要删除的
                if cur.item == item:             # 找到了要删除的元素
                    pre.next = cur.next          # 删除
                    return 
                else:
                    pre = cur
                    cur = cur.next
            if cur.item == item:                # cur 指向尾结点
                pre.next = cur.next             # 尾部删除

    def search(self, item):
        """检查节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False
        
if __name__ == '__main__':
    l1 = SinCycLinkedList()
    l1.add(1)
    l1.add(2)
    l1.append(3)
    l1.insert(2, 4)
    l1.insert(4, 5)
    l1.insert(0, 6)
    print("length: ", l1.length())      # 6
    l1.travel()                         # 5 3 4 1 2 6
    print(l1.search(3))                 # True
    print(l1.search(7))                 # False
    l1.remove(1)
    print("length: ", l1.length())      # 5
    l1.travel()                         # 5 3 4 2 6