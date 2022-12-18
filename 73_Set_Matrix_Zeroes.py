# TIme: O(n**2)
# Space: O(1)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_list = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    num_list.append([i, j])
        
        for ind in num_list:
            for i in range(n):
                matrix[ind[0]][i] = 0
            for i in range(m):
                matrix[i][ind[1]] = 0
                
        return matrix
