from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix[0])
        col = len(matrix)
        num = []
        for i in range(row):
            for j in range(col):
                num.append(matrix[i][j])
        num.sort()
        return num[k - 1]
