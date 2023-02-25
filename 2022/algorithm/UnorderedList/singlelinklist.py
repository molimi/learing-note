#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/15
@version: 0.1
@description: 单链表的实现
"""

class Node:
    """单链表的结点"""
    def __init__(self, item):
        # item 存放数据元素
        self.item = item
        # next 下一个节点的标识
        self.next = None

class SingleLinkList:
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None
    
    def length(self):
        """获取链表长度"""
        cur = self._head        # cur 初始时指向头结点
        count = 0
        while cur:              # 尾结点指向None，遍历结束
            count += 1
            cur = cur.next      # 将cur后移一个节点
        return count

    def add(self, item):
        """头部添加元素"""
        node = Node(item)         # 先创建一个保存 item 值的节点
        node.next = self._head          # 将新节点的链接域 next 指向头节点，即 _head 指向的位置
        self._head = node               # 将链表的头 _head 指向新节点
    
    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next
        print("")
        

    def append(self, item):
        """向尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾结点的 next 指向新节点
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
    
    def insert(self, pos, item):
        """向链表指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
            # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        else:                   # 找到指定位置
            pre = self._head    # pre 用来指向指定位置pos前一个位置pos-1，初始从头节点开始移动到指定位置
            count = 0
            node = Node(item)
            while count < pos-1:
                pre = pre.next
                count += 1
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
    
    def remove(self, item):
        """删除元素"""
        cur = self._head
        pre = None
        while cur:
            if cur.item == item:            # 找到指定元素
                if not pre:                 # 如果第一个就是删除节点
                    self._head = cur.next   # 将头指针指向头节点的后一个节点
                else:
                    pre.next = cur.next     # 将删除位置的前一个节点的next指向删除位置的后一个节点
                break
            else:
                # 继续后移节点
                pre = cur
                cur = cur.next
    


    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    l1 = SingleLinkList()
    l1.add(1)
    l1.add(2)
    l1.append(3)
    l1.insert(2, 4)
    print("length: ", l1.length())
    l1.travel()
    print(l1.search(3))
    print(l1.search(5))
    l1.remove(1)
    print("length: ", l1.length())
    l1.travel()