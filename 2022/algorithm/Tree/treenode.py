#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/27
@version: 0.1
@description: 节点链接法实现
"""
class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_key(self, obj):
        self.key = obj

    def get_root_key(self):
        return self.key

    def pre_order(self):            # 前序遍历
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):            # 中序遍历
        if self.left_child:
            self.left_child.in_order()
        print(self.key)
        if self.right_child:
            self.right_child.in_order()
    
    def post_order(self):             # 后序遍历
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

def pre_order(tree):
    if tree:
        print(tree.key)
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())

def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.key)

def in_order(tree):
    if tree:
        in_order(tree.get_left_child())
        print(tree.key)
        in_order(tree.get_right_child())


if __name__ == "__main__":
    r = BinaryTree('a')
    r.insert_left('b')
    r.insert_right('c')
    r.get_right_child().set_root_key('hello')
    r.get_left_child().insert_right('d')
    print(r.pre_order()==pre_order(r))
    print()
    print(r.in_order()==in_order(r))
    print()
    print(r.post_order()==post_order(r))
    print()