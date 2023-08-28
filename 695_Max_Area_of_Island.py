# n = len(grid)
# m = len(grid[0])
# time: O(n*m)
# space: O(1)
from typing import List


class Solution:
    def count_the_max_are_of_island(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        max_area = 0

        def count_the_are_of_same_island(row: int, col: int) -> int:
            if {0 <= row < len(grid)
                    and 0 <= col < len(grid[0])
                    and grid[row][col] == 1}:
                grid[row][col] = 0
                area = 1
                area += count_the_are_of_same_island(row + 1, col)
                area += count_the_are_of_same_island(row - 1, col)
                area += count_the_are_of_same_island(row, col + 1)
                area += count_the_are_of_same_island(row, col - 1)
                return area

            return 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    num_area = count_the_are_of_same_island(i, j)
                    max_area = max(max_area, num_area)
        
        return max_area
