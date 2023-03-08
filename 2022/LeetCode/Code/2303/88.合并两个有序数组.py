#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
# 逆向指针法

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1[m:] = nums2
        nums1.sort()            # 你能告诉我可以这样无脑操作，面试直接给你pass
        """
        p0, p1, p2 = m-1, n-1, m+n-1
        while p0 >= 0 or p1 >= 0:
            if p0 == -1:
                nums1[p2] = nums2[p1]
                p1 -= 1
            elif p1 == -1:
                nums1[p2] = nums1[p0]
                p0 -= 1
            elif nums1[p0] > nums2[p1]:
                nums1[p2] = nums1[p0]
                p0 -= 1
            else:
                nums1[p2] = nums2[p1]
                p1 -= 1
            p2 -= 1
# @lc code=end

