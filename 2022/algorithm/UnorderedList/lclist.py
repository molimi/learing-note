#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/23
@version: 0.1
@description: 节点的实现
"""

class LCList:                   # 循环单链表类
    def __init__(self):
        self._rear = None

        def is_empty(self):
            return self._rear is None
        
        def prepend(self, elem):    # 前端插入
            p = LNode(elem)
            if self._rear is None:
                p.next = p          # 建立一个结点的环
                self._rear = p
            else:
                p.next = self._rear.next
                self.rear.next = p
        
        def append(self, elem):     # 尾插入
            self.prepend(elem)
            self._rear = self._rear.next

        def pop(self):  # 前端弹出
            if self._rear is None:
                raise LinkedListUnderflow("in pop of CLList")
            p = self._rear.next
            if self._rear is p:
                self._rear = None
            else:
                self._rear.next = p.next
            return p.elem
        
        def printall(self):     # 输出元素
            if self.is_empty():
                return
            p = self._rear.next
            while True:
                print(p.elem)
                if p is self._rear:
                    break
                p = p.next
