#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#

# @lc code=start
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        # print(R,count)

        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            # print(R2,count2)
            if R != R2:
                continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))
            print(word)
        return ans

# @lc code=end

