# Time colomplexity: O(mn)
# Spacole complexity: O(1)
# m = len(grid), n = len(grid[0])
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def is_valid_land(r: int, col: int) -> bool:
            return 0 <= r < len(grid) \
                and 0 <= col < len(grid[0]) \
                and grid[r][col] == 1

        def count_perimeter(row: int, col: int) -> int:
            perimeter = 4
            if is_valid_land(row - 1, col):
                perimeter -= 1
            if is_valid_land(row + 1, col):
                perimeter -= 1
            if is_valid_land(row, col - 1):
                perimeter -= 1
            if is_valid_land(row, col + 1):
                perimeter -= 1
            return perimeter

        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += count_perimeter(row, col)

        return perimeter
