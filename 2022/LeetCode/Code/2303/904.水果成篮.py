#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """直接遍历会超时啊"""
        left = 0
        max_len = 0
        count_dict = {}                # 哈希表还是快啊
        for right, item in enumerate(fruits):
            count_dict[item] = count_dict.get(item, 0) + 1
            while len(count_dict) > 2:
                count_dict[fruits[left]] -= 1
                if count_dict[fruits[left]] == 0:
                    count_dict.pop(fruits[left])
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len


# @lc code=end

