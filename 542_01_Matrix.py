# Time: O(n**2)
# Space: O(1)


class Solution(object):

    def updateMatrix(self, matrix):
        row, col = len(matrix), len(matrix[0])
        dp = matrix[:]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] != 0:
                    if i == 0 and j == 0:
                        dp[i][j] = float("inf")
                    elif i == 0:
                        dp[i][j] = matrix[i][j-1] + 1
                    elif j == 0:
                        dp[i][j] = matrix[i-1][j] + 1
                    else:
                        dp[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + 1

        for x in range(row - 1, -1, -1):
            for y in range(col-1, -1, -1):
                if matrix[x][y] != 0:
                    if x == row-1 and y == col-1:
                        matrix[x][y] = dp[x][y]
                    elif x == row-1:
                        matrix[x][y] = min(dp[x][y], 1+matrix[x][y+1])
                    elif y == col-1:
                        matrix[x][y] = min(dp[x][y], 1+matrix[x+1][y])
                    else:
                        matrix[x][y] = min(dp[x][y], 1+min(matrix[x+1][y], matrix[x][y+1]))

        return matrix
