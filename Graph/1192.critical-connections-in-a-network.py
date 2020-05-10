#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)
        for conn in connections:
            a,b = conn
            g[a].append(b)
            g[b].append(a)
        ans = []
        # print(g)
        low = [None]*n
        def dfs(cur=0,par=-1,step=0)->int:
            # return the min step it can achieve
            low[cur] = step+1
            for nei in g[cur]:
                if nei == par:
                    continue
                elif not low[nei]:
                    low[cur] = min(low[cur],dfs(nei,cur,step+1))
                else:
                    low[cur] = min(low[cur],low[nei])
            if low[cur] == step+1 and cur != 0: # cur not in a cycle
                ans.append([cur,par])
            return low[cur]
        dfs()
        return ans
# @lc code=end

