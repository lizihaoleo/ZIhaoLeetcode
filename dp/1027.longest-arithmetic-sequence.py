#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        max_length = 0
        for i in range(n):
            for j in range(0,i):
                diff = A[i] - A[j]
                dp[(diff,i)] = dp.get((diff,j),1)+1
                max_length = max(max_length,dp[(diff,i)])
        # print(dp)
        return max_length
# @lc code=end

