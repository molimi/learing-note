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
        if not root: return None        # 这里空树，直接返回None
        que = deque([root])
        while que:
            n = len(que)
            for i in range(n):
                cur = que.popleft()
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
                if i == n-1: break          # 遍历到最右边，结束本行循环
                cur.next = que[0]           # 指向同一行的右边节点
        return root
# @lc code=end

