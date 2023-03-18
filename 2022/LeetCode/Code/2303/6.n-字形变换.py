#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:                                # 把行为1的先剔除掉，防止除以0
            return s
        result = [[] for _ in range(numRows)]           # 初始化矩阵
        i, j, k = 0, 0, 0                               # i代表元素数，j代表列数，k代表行数
        while i < len(s):
            temp = j % (numRows-1)                      # 除法要考虑防止分母为0
            if temp == 0:
                k = 0
                while k < numRows and i < len(s):      # k 代表行，这里得注意最后一列可能并不完整
                    result[k].append(s[i])
                    k += 1
                    i += 1
            else:
                k = numRows - temp - 1
                result[k].append(s[i])                  # 添加中间的元素
                i += 1
            j += 1
        ans = ""
        for item in result:                             # 拼接字符串
            ans += ''.join(item)
        return ans

''' 
S = Solution()                  
print(S.convert("ahhsgd", 3))                           # 终端调试
'''
# @lc code=end

