#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        '''模拟法'''
        '''
        hex = '0123456789abcdef'
        ans = ''
        if num == 0:
            return '0'
        elif num < 0:
            num = 2 ** 32 + num
        while num > 0:
            num, res = divmod(num, 16)
            ans += hex[res]
        
        return ans[::-1]
        '''
        return hex(num&0xffffffff)[2:]
# @lc code=end

