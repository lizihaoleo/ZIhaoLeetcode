#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        # print(root.val,root.left,root.right)
        tmp = root.right
        root.left, root.right = None, root.left
        self.flatten(root.right)
        while root.right:
            root = root.right
        root.right = tmp
        self.flatten(tmp)
        
# @lc code=end

