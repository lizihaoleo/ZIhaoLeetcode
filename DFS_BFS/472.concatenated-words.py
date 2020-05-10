#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
from functools import lru_cache
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        ans = []
        @lru_cache(None)
        def dfs(word)->bool:
            for i in range(1,len(word)):
                pre, suf = word[:i], word[i:]
                if pre in words and suf in words:
                    return True
                if pre in words and dfs(suf):
                    return True
            return False
        for word in words:
            if dfs(word):
                ans.append(word)
        return ans
    
# @lc code=end

