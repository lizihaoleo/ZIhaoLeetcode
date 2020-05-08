#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        d = {None: -1}
        max_depth = -1
        def dfs(node, parent = None):
            nonlocal max_depth
            if node:
                d[node] = d[parent] + 1
                max_depth = max(max_depth,d[node])
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        def helper(root): #LCA?!
            if not root or d.get(root, None) == max_depth:
                return root
            left,right = helper(root.left), helper(root.right)
            if left and right:
                return root
            return left if left else right
        return helper(root)
# @lc code=end

