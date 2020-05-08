#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter,defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            
        n,m = len(s1), len(s2)
        if n > m: return False
        window = Counter(s2[:n])
        counter = Counter(s1)
        if counter==window:
                return True
        for i in range(n,m):
            window[s2[i]] += 1
            removed_char = s2[i-n]
            window[removed_char] -= 1
            if window[removed_char] == 0:
                del window[removed_char]

            if counter==window:
                return True
            # print(i,counter,window)
        return False       
# @lc code=end

