#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int) # val:freq
        _sum = 0
        d[0] = 1
        count = 0
        for i,val in enumerate(nums):
            _sum += val
            if _sum - k in d:
                count += d[_sum-k]
            d[_sum] += 1
        return count
# @lc code=end

