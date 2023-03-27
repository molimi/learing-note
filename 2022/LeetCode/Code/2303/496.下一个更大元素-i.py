#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 暴力穷举法
        result = []
        length = len(nums2)
        for num in nums1:
            try:
                flag = True
                for i in range(nums2.index(num)+1, length):
                    if nums > num:
                        flag = False
                        result.append(nums)
                        break
                if flag or nums2.index(num)== length-1:
                    result.append(-1)
            except:
                result.append(-1)
        return result
        '''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}                       # 字典存储结果
        stack = []                          # 列表模拟栈，单调栈
        for nums in nums2:    # 遍历每个字符
            if not stack:                   # 如果当前栈为空，则直接入栈
                stack.append(nums)
            else:
                if nums < stack[-1]:        # 当前值小于栈顶元素，则入栈
                    stack.append(nums)
                elif nums > stack[-1]:      # 当前值大于栈顶元素，不停出栈，把所有栈顶key值的value赋值为当前值
                    while stack and stack[-1] < nums:
                        hash_map[stack[-1]] = nums
                        stack.pop()
                    stack.append(nums)  # 当前值入队列
        while stack:                        # 如果栈中还有元素，则全部赋值为-1，表示右边没有更大值
            hash_map[stack[-1]] = -1
            stack.pop()
        result = []
        for nums in nums1:                     # 返回每个key值对应的value
            result.append(hash_map[nums])
        return result
# @lc code=end

