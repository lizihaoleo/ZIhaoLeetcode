#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q=collections.deque()
        q.append((root,1))
        ans = []
        while q:
            node,num = q.popleft()
            if node:
                ans.append(num)
                q.append((node.left,2*num))
                q.append((node.right,2*num+1))
            else:
                ans.append(None)
        while ans[-1] == None:
            ans.pop()
        print(ans)
        return None not in ans   
# @lc code=end

