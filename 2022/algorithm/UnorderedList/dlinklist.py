#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/25
@version: 0.1
@description: 双向链表的实现
"""
class Node(object):
    """双向链表节点"""
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    """双向链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None
    
    def length(self):
        """返回链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    
    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print()

    def add(self, item):
        """头部插入元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node           # 如果是空链表，将_head指向node
        else:
            node.next = self._head      # 将node的next指向_head的头节点
            self._head.prev = node      # 将_head的头节点的prev指向node
            self._head = node           # 将_head 指向node

    def append(self, item):
        """尾部插入元素"""
        node = Node(item)
        if self.is_empty():
            self._head = node       # 如果是空链表，将_head指向node
        else:
            cur = self._head        # 移动到链表尾部
            while cur.next:
                cur = cur.next
            cur.next = node         # 将尾节点cur的next指向node
            node.prev = cur         # 将node的prev指向cur

    def search(self, item):
        """查找元素是否存在"""
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    
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
            while count < (pos-1):      # 移动到指定位置的前一个位置
                count += 1
                cur = cur.next
            node.prev = cur             # 将node的prev指向cur
            node.next = cur.next        # 将node的next指向cur的下一个节点
            cur.next.prev = node        # 将cur的下一个节点的prev指向node
            cur.next = node             # 将cur的next指向node

    def remove(self, item):
        """删除元素"""
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:            # 如果首节点的元素即是要删除的元素
                    self._head = None           # 如果链表只有这一个节点
                else:
                    cur.next.prev = None        # 将第二个节点的prev设置为None
                    self._head = cur.next       # 将_head指向第二个节点
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.next.prev = cur.prev    # 将cur的后一个节点的prev指向cur的前一个节点
                    break
                cur = cur.next


if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print("length:", ll.length())   # 6 
    ll.travel()                     # 5 -> 3 -> 4 -> 1 -> 2 -> 6
    print(ll.search(3))             # True
    print(ll.search(4))             # True
    ll.remove(1)
    print("length:", ll.length())   # 5
    ll.travel()                     # 5 -> 3 -> 4 -> 2 -> 6