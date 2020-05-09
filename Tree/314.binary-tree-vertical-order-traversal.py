#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        min_col, max_col = float('inf'),-float('inf')
        d = collections.defaultdict(list)
        q = collections.deque()
        q.append((root,0))
        while q:
            node, col = q.popleft()
            if node:
                min_col = min(min_col,col)
                max_col = max(max_col,col)
                d[col].append(node.val)
                q.append((node.left,col-1))
                q.append((node.right,col+1))
        # print(d)
        ans = []
        for i in range(min_col,max_col+1):
            ans.append(d[i])
        return ans       
# @lc code=end

