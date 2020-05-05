#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1: fast and slow pointer to find the mid point
        s,f = head,head
        while f and f.next:
            f = f.next.next
            s = s.next
        # step 2: reverse last half linked list 
        pre = None
        while s:
            s.next, pre, s = pre, s, s.next
        # step 3: reconstruct two halves linked list by moving 2 pointers
        t = pre
        h = head
        while t and t.next:
            h.next, h = t, h.next
            t.next, t = h, t.next
            
        return head
# @lc code=end

