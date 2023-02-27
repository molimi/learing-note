#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
# 思路一：传统写法，就是中间的值为上一行左右两个元素相加
# 思路二：小技巧 上一行左右两边的数相加求得，左右补零就可以完美实现


# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        res = [[1]]
        for _ in range(2, numRows + 1):
            res.append([a + b for a, b in zip([0] + res[-1], res[-1] + [0])])
        return res
        '''
        res1 = []
        for i in range(numRows):
            res2 = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    res2.append(1)
                else:
                    res2.append(res1[i - 1][j - 1] + res1[i - 1][j])
            res1.append(res2)
        return res1


# @lc code=end
