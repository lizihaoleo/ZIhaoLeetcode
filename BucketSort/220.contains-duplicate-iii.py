#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        size = t+1
        d = dict()
        for i,num in enumerate(nums):
            bucket_id = num // size
            if bucket_id in d:
                return True
            if bucket_id-1 in d and abs(d[bucket_id-1] - num) <= t:
                return True
            if bucket_id+1 in d and abs(d[bucket_id+1] - num) <= t:
                return True
            d[bucket_id] = num
            if len(d) > k:
                bucket_id = nums[i-k] // size
                del d[bucket_id]
        return False
# @lc code=end

