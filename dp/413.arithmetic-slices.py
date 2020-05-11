#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0]*len(A)
        _sum = 0
        for i in range(2,len(A)):
            diff0 = A[i]-A[i-1]
            diff1 = A[i-1]-A[i-2]
            if diff0 == diff1:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 0
            _sum += dp[i]
        return _sum
# @lc code=end

