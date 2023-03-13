#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ch in s:
            if not st:
                st.append(ch)
            else:
                if st[-1] == ch:
                    st.pop()
                else:
                    st.append(ch)
        return ''.join(st)
# @lc code=end

