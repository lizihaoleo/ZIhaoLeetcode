#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        _sum = 0
        def dfs(node):
            nonlocal _sum
            if node:
                # print(node.val)
                if L <= node.val <= R:
                    # print("*",node.val)
                    _sum += node.val
                    dfs(node.left)
                    dfs(node.right)
                elif node.val >= R:
                    dfs(node.left)
                elif node.val <= L:
                    dfs(node.right)
        dfs(root)
        return _sum
# @lc code=end

