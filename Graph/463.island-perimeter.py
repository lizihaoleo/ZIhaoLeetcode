#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    count += 4
                    if j > 0 and grid[i][j - 1]:
                        count -= 2
                    if i > 0 and grid[i - 1][j]:
                        count -= 2
        return count
# @lc code=end

