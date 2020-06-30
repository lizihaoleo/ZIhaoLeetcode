#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n,m = len(board), len(board[0])
        key = '$'
        trie = dict()
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = dict()
                node = node[letter]
            node[key] = word
        def dfs(i,j,node):
            letter = board[i][j]
            cur = node[letter]
            match = cur.pop(key,False)
            if match: ans.append(match)
            board[i][j] = "#"
            dirs = [[-1,0],[1,0],[0,1],[0,-1]]
            for dx,dy in dirs:
                new_i, new_j = i+dx, j+dy
                if 0<=new_i<n and 0<=new_j<m and board[new_i][new_j] in cur:
                    dfs(new_i,new_j,cur)
            board[i][j] = letter
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not cur:
                node.pop(letter)
        ans = []
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    dfs(i,j,trie)
        return ans
# @lc code=end

