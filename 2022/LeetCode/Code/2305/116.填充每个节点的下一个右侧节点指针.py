#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
                if i == size-1: break
                cur.next = que[0]
        return root
# @lc code=end

