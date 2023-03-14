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
        if not head:        # 空链表直接返回
            return head
        
        length = 0          # 获取链表的长度
        node = head
        while node: 
            length += 1
            node = node.next
        
        dummy_head = ListNode(0, head)
        sub_length = 1                                # 归并的有效处理长度，最小为 1
        while sub_length < length:
            prev, curr = dummy_head, dummy_head.next  # 为了更好的实现迭代，定义 prev, curr 分别指向 dummy_head, dummy_head.next
            while curr:                               # 当 cur 不为空时
                head1 = curr                           # 定义当前链表，head1 指向 cur
                for i in range(1, sub_length):
                    '''当 i 等于 1 时, cur 不需要指向后下一个链表其余情况，
                       cur 在链表 cur 不为空的情况, 向后移动 sub_length - 1 个位置'''
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next   # 切断链表，第一部分长度为 sub_length
                curr.next = None    # 第二部分为 head 除 head1 以外的部分
                curr = head2
                for i in range(1, sub_length):  # 将 cur 在满足 cur.next 不为空的情况下， 又往后移动 sub_length 长度
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                remain = None         # 定义 remain 链表，指向 null
                if curr:              # 当移动完 sub_length 后，仍不为空，remain 等于 cur.next;
                    remain = curr.next
                    curr.next = None  # 切断链表， 这时候 head2 的长度与 head1 一致
                
                merged = self.merge(head1, head2)   # merge , 然后 prev 的 next 指针指向将 merge 后的子链表
                prev.next = merged
                while prev.next:        # 然后将 prev 指向与 merge 完成后的链表位置
                    prev = prev.next
                curr = remain           # 然后当前节点位置指向 remain 部分链表
            '''
            进入下一批次的归并排序操作，直到将相同 sub_length 的全部处理完，才会退出此处 while
            再进入到下轮 sub_length, sub_length 以 1 -> 2 -> 4 -> 8 的方法进行，符合自低向上不断迭代，
            直到找到最终答案。其实递归底层本质也是一样的，到最短的1，才开始合并，不断合并，到最终结果
            '''
            sub_length <<= 1

        
        return dummy_head.next
    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
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

