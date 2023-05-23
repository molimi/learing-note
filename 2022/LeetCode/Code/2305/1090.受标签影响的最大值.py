#
# @lc app=leetcode.cn id=1090 lang=python3
#
# [1090] 受标签影响的最大值
#

# @lc code=start
from collections import Counter
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # 贪心算法，进行排序
        n = len(values)
        ind = sorted(range(n), key=lambda i: values[i], reverse=True)
        res = 0
        labels_dict = Counter()
        count = 0
        for j in ind:
            if count < numWanted and labels_dict[labels[j]] < useLimit:
                res += values[j]
                count += 1
                labels_dict[labels[j]]  += 1
        return res

# @lc code=end