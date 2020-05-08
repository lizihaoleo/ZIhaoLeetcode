#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        d = {}
        visited = set()
        def dfs(node):
            visited.add(node)
            copy = Node(node.val)
            d[node] = copy
            for nei in node.neighbors:
                if nei not in visited:
                    dfs(nei)
        dfs(node)
        for n in d.keys():
            for nei in n.neighbors:
                d[n].neighbors.append(d[nei])

        # for n in d.keys():
        #     print(n.val,[x.val for x in n.neighbors],d[n].val,[x.val for x in d[n].neighbors])
        return d[node]
# @lc code=end

