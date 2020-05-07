#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        k = 10**9+7
        @lru_cache(None)
        def helper(N,i,j):
            if i == m or j == n or i <0 or j < 0:
                return 1
            if N == 0:
                return 0
            
            ans = helper(N-1,i-1,j) % k \
                + helper(N-1,i+1,j) % k \
                + helper(N-1,i,j+1) % k \
                + helper(N-1,i,j-1) % k
            return ans%k
        return helper(N,i,j)     
# @lc code=end

