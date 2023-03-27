#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

# @lc code=start
class Solution:
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        length = len(nums1)
        idx = sorted(range(length), key=lambda i: nums2[i], reverse=True)   # 按索引逆序排列
        left, right = 0, length-1
        res = [0] * length
        for i in idx:                           # 遍历次序
            if nums2[i] < nums1[right]:         # 如果大就直接比赛
                res[i] = nums1[right]
                right -= 1
            else:                               # 如果小，就换个最小的
                res[i] = nums1[left]
                left += 1
        return res
# @lc code=end

