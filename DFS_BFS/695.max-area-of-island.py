#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        row, col = len(grid), len(grid[0])
        self.maxArea = 0
        def dfs(i,j):
            count = 1
            if 0<=i<row and 0<=j<col and grid[i][j]:
                grid[i][j] = 0
                for direction in directions:
                    count += dfs(i+direction[0],j+direction[1])
                return count
            return 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.maxArea = max(self.maxArea, dfs(i,j))
        return self.maxArea

# @lc code=end

