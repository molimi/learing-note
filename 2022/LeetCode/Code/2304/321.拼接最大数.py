#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_number(nums, k):                # 找最大          
            stack = []
            drop = len(nums)-k
            for num in nums:
                while drop and stack and stack[-1] < num:
                    drop -= 1
                    stack.pop()
                stack.append(num)
            return stack[:k]

        def merge(A, B):                        # 合并
            ans = []
            while A or B:
                bigger = A if A > B else B
                ans.append(bigger[0])
                bigger.pop(0)
            return ans
        
        return max(merge(max_number(nums1, i), max_number(nums2, k-i)) for i in range(k+1) if i <= len(nums1) and k-i <= len(nums2))

# @lc code=end

