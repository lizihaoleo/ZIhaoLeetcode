#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left != None:
            cur = leftmost
            while cur:
                #1
                cur.left.next = cur.right
                # print(cur.left.val, '->',cur.right.val)
                #2
                cur.right.next = cur.next.left if cur.next else None
                # print(cur.right.val, '->', cur.right.next.val if cur.right.next else None)
                cur = cur.next
            leftmost = leftmost.left
        return root    
# @lc code=end

