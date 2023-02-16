# n = len(mat)
# m = len(mat[0])
# Time: O(n*m)
from typing import List


# dynamic programming
# class Solution(object):

#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
#         row, col = len(matrix), len(matrix[0])
#         dp = matrix[:]
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] != 0:
#                     if i == 0 and j == 0:
#                         dp[i][j] = float("inf")
#                     elif i == 0:
#                         dp[i][j] = matrix[i][j-1] + 1
#                     elif j == 0:
#                         dp[i][j] = matrix[i-1][j] + 1
#                     else:
#                         dp[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + 1

#         for x in range(row - 1, -1, -1):
#             for y in range(col-1, -1, -1):
#                 if matrix[x][y] != 0:
#                     if x == row-1 and y == col-1:
#                         matrix[x][y] = dp[x][y]
#                     elif x == row-1:
#                         matrix[x][y] = min(dp[x][y], 1+matrix[x][y+1])
#                     elif y == col-1:
#                         matrix[x][y] = min(dp[x][y], 1+matrix[x+1][y])
#                     else:
#                         matrix[x][y] = min(dp[x][y], 1+min(matrix[x+1][y],
#                                                            matrix[x][y+1]))

#         return matrix

# BFS
# n = len(mat)
# m = len(mat[0])
# Time: O(n*m)
# Space: O(1)
class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_num, colum_num = len(mat), len(mat[0])
        queue = []
        directions = [[0, +1], [0, -1], [1, 0], [-1, 0]]
        for i in range(row_num):
            for j in range(colum_num):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = "*"
            for r, c in queue:
                for row_direction, colum_direction in directions:
                    row = r + row_direction
                    col = c + colum_direction
                    if 0 <= row < row_num
                        and 0 <= col < Col
                            and mat[row][col] == "*":
                        mat[row][col] = mat[r][c] + 1
                        queue.append((row, col))
        return mat
