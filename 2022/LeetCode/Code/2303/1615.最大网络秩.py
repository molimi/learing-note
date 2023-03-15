#
# @lc app=leetcode.cn id=1615 lang=python3
#
# [1615] 最大网络秩
#

# @lc code=start
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        '''枚举法，慢一点但可以通过'''
        max_len = 0
        degree_dict = {}                                            # 统计每个结点的度数
        for i in range(n):
            degree_dict[i] = 0
            for j in range(len(roads)):
                if i in roads[j]:
                    degree_dict[i] += 1
        for i in range(n):                                          # 计算连通数
            for j in range(i+1, n):
                if [i,j] in roads or [j, i] in roads:
                    temp = degree_dict[i] + degree_dict[j] - 1
                else:
                    temp = degree_dict[i] + degree_dict[j]
                max_len = max(temp, max_len)
        return max_len
            

# @lc code=end

