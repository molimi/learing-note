#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.result= []
        self.traversal(root)
        return self.result
    
    def traversal(self, root: 'Node'):
        if not root: return 
        for child in root.children:
            self.traversal(child)
        self.result.append(root.val)
        
# @lc code=end

