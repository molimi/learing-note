#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.split_list(head) 
    
    def split_list(self, head: ListNode):   
        '''处理归并排序的边界问题,下面两种场景都不需要进行分合操作'''
        if not head or not head.next:
            return head
        prev, slow, fast = head, head, head
        while fast and fast.next:   # 找中点,偶数找的后面那个中点的位置，奇数找到中点
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left, right = head, slow     # 将链表分割成两个子链表
        return self.merge_sort(self.split_list(left), self.split_list(right))    # 分割完后，进行合并部分操作

    def merge_sort(self, head1: ListNode, head2: ListNode) -> ListNode:
        '''归并环节'''
        dummy_head = ListNode(0)            # 构建虚拟头结点
        temp, temp1, temp2 = dummy_head, head1, head2
        while temp1 and temp2:              # 开始合并操作
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:                #  如 temp1, temp2 还存在不为空的链表，将剩余部分赋值给 temp.next
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return dummy_head.next
# @lc code=end

