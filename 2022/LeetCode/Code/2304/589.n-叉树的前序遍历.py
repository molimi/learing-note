#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        # 栈的写法也一样，把每个孩子加入栈中进行遍历
        self.result = []
        self.traversal(root)
        return self.result
    
    def traversal(self, root):
        if not root: return 
        self.result.append(root.val)
        for child in root.children:
            self.traversal(child)
        
# @lc code=end

