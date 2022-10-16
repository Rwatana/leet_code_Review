from typing import List


class Solution:
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        i = 0
        j = col -1 
        count = 0
        while i < row and j >= 0:
            if grid[i][j] < 0:
                count += 1
                j -= 1                
            else:
                 j = col -1
                 i += 1
        return count