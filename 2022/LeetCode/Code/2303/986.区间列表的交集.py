#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#


# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        '''双指针大法就是好用'''
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:  # 此时说明有交集
                result.append([start, end])
            if firstList[i][1] > secondList[j][1]:  # 谁的区间小，就更新谁
                j += 1
            else:
                i += 1
        return result


# @lc code=end
