#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = cur = ListNode(-1)
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry,ans_val = divmod(v1+v2+carry,10)
            cur.next = ListNode(ans_val)
            cur = cur.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return dummy.next
        
# @lc code=end

