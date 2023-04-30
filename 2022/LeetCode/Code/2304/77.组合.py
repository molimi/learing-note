#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(n, k, start_index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_index, n-(k-len(path))+2):     # 顺便剪枝
                path.append(i)
                backtrack(n, k, i+1)        # 递归
                path.pop()                  # 回溯
        backtrack(n, k, 1)
        return res

# @lc code=end

