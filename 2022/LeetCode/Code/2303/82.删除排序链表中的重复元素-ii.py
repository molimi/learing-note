#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''双指针记录pre 用cur记录相同的数，加虚头节点'''
        dummy = ListNode(-1, head)
        prev, curr = dummy, dummy.next
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.val
                 # 如果有奇数个相同的值，就删不完，所以必须用 while 循环
                while curr and curr.next and curr.next.val == temp:
                    curr = curr.next        # //找到最后一个相等的数
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next



# @lc code=end

