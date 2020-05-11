#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = l = r = 0
        counter = defaultdict(deque)
        while r < len(s):
            tail = s[r]
            counter[tail].append(r)
            while len(counter) > k:
                head = s[l]
                # print(head,counter)
                counter[head].popleft()
                if len(counter[head]) == 0:
                    del counter[head]
                l += 1
            # print(l,r,counter)
            ans = max(ans,r-l+1)
            r += 1
        return ans
# @lc code=end

