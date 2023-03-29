#
# @lc app=leetcode.cn id=1095 lang=python3
#
# [1095] 山脉数组中查找目标值
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        '''
        先使用二分法找到数组的峰值。
        在峰值左边使用二分法寻找目标值。
        如果峰值左边没有目标值，那么使用二分法在峰值右边寻找目标值。
        '''
        head, tail = 0, mountain_arr.length()-1
        while head < tail:             # 找峰值，注意越界处理
            mid = (head+tail)//2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                head = mid + 1
            else:
                tail = mid
        peak = head
        ans = self.binarySearch(mountain_arr, target, 0, peak)                                              # 在左半边搜索
        if ans != -1:
            return ans
        return self.binarySearch(mountain_arr, target, peak+1, mountain_arr.length()-1, lambda x:-x)        # 在右半边搜索
    

    def binarySearch(self, mountain, target, left, right, key=lambda x: x): 
        target = key(target)                            # 这里的key相当于把两边全部转为升序部分，也可以用target*reverse，根据reverse的正负来判断
        while left <= right:
            mid = (left + right) // 2
            curr = key(mountain.get(mid))
            if curr == target:
                return mid
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
# @lc code=end

