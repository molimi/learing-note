#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
# 哈希表，遍历的时候做一个记录，如果出现，就是有环
# 快慢指针法

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
        '''
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    
        
# @lc code=end

