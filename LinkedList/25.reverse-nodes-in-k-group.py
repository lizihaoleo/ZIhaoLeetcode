#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,start,end) -> ListNode:
        pre = None
        while start != end:
            start.next, pre, start,  = pre, start, start.next
        return pre
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        start = end = head
        for _ in range(k):
            if not end:
                return start
            end = end.next
        new_head = self.reverse(start,end)
        start.next = self.reverseKGroup(end,k)
        return new_head
# @lc code=end

