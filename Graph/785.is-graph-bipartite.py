#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [None]*n
        def dfs(i=0,c=1):
            if colors[i]!=None:
                return colors[i] == c
            colors[i] = c
            return all(dfs(nei,-c) for nei in graph[i])
        return all(dfs(i) for i in range(n) if colors[i]==None)
# @lc code=end

