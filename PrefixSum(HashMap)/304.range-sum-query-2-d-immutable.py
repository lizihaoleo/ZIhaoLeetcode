#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.p_matrix = matrix
            return
        n,m = len(matrix), len(matrix[0])
        self.p_matrix = [[0]*(m+1) for _ in range(n)]
        for row_id,row in enumerate(matrix):
            for i in range(1,m+1):
                self.p_matrix[row_id][i] = self.p_matrix[row_id][i-1] + matrix[row_id][i-1]
        # print(self.p_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row_id in range(row1,row2+1):
            tmp = self.rowSum(row_id,col1,row_id,col2)
            ans += tmp
            # print(row_id,tmp)
        return ans
    def rowSum(self,row1,col1,row2,col2):
        # print('*',row1,col1,row2,col2)
        return self.p_matrix[row1][col2+1] - self.p_matrix[row2][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

