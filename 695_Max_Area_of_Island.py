# n = len(grid)
# m = len(grid[0])
# time: O(n*m)
# space: O(1)
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_area = 0

        def check(row: int, col: int) -> int:
            if 0 <= row < len(grid)
                    and 0 <= col < len(grid[0]) 
                    and grid[row][col] == 1:
                grid[row][col] = 0
                area = 1
                area += check(row + 1, col)
                area += check(row - 1, col)
                area += check(row, col + 1)
                area += check(row, col - 1)
                return area

            return 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num_area = check(i, j)
                    max_area = max(max_area, num_area)
        
        return max_area
