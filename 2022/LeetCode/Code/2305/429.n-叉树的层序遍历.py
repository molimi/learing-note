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

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        # BFS
        if not root: return []
        results = []
        que = deque([root])
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                node = que.popleft()
                result.append(node.val)
                # cur.children 是 Node 对象组成的列表，也可能为 None
                if node.children:
                    que.extend(node.children)
            results.append(result)
        return results
        '''
        # DFS
        def dfs(root, level):
            if not root: return
            if len(res) < level:
                res.append([root.val])
            else:
                res[level-1].append(root.val)
            for child in root.children:
                dfs(child, level+1)

        res = []
        dfs(root, 1)
        return res
        
# @lc code=end

