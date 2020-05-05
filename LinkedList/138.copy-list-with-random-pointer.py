#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = dict()
        d[None] = None
        cur = head
        while cur:
            cur_copy = Node(cur.val)
            d[cur] = cur_copy
            cur = cur.next
        cur = head
        while cur:
            d[cur].next = d[cur.next]
            d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
# @lc code=end

