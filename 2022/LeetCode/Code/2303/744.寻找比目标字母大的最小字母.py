#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    def nextGreatestLetter(self, letters, target) -> str:
        left, right = 0, len(letters)
        while left < right:
            mid = (left+right)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if left < len(letters) and letters[left] > target:
            return letters[left]
        else:
            return letters[0]

s = Solution()
s.nextGreatestLetter(["x", "x", "y", "y", "z"], "x")


# @lc code=end

