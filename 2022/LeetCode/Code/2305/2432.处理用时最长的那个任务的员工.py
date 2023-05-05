#
# @lc app=leetcode.cn id=2432 lang=python3
#
# [2432] 处理用时最长的那个任务的员工
#

# @lc code=start
from typing import List
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        res = [logs[0]]
        for i, (worker, leave_time) in enumerate(logs[1:]):
            res.append([worker, leave_time-logs[i][1]])
        ans = sorted(res, key=lambda item: (item[1], -item[0]))
        return ans[-1][0]
# @lc code=end

