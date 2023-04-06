#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
from typing import List
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        results = []
        que = deque([root])
        while que:
            result = []
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.children:            # 把孩子加入队列
                    que.extend(cur.children)
            results.append(result)
        return results

# @lc code=end