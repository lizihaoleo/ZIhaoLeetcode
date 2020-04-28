#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        from functools import lru_cache
        @lru_cache(None)
        # from right to left
        def helper(i,j):
            # base case
            if j==-1:
                return i == -1
            if i==-1:
                if p[j]=="*" and j>=1:
                    return helper(i,j-2)
                else:
                    return False
            # same char or p[j] is '.' -> move to right
            if s[i] == p[j] or p[j] == '.':
                return helper(i-1,j-1)
            elif p[j] == '*' and j >= 1:
                pre_match = p[j-1] in {s[i],'.'}
                return helper(i,j-2) \
                    or (pre_match and helper(i-1,j)) # char match zero or more than one time

            return False
        
        return helper(m-1,n-1)
        
# @lc code=end

