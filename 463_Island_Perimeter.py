# Time Complexity: O(mn)
# Space Complexity: O(1)
# m = len(grid), n = len(grid[0])
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def is_valid_land(r: int, c: int) -> bool:
            return 0 <= r < len(grid) \
                and 0 <= c < len(grid[0]) \
                and grid[r][c] == 1

        def calculate_cell_perimeter(r: int, c: int) -> int:
            perimeter = 4
            if is_valid_land(r - 1, c):
                perimeter -= 1
            if is_valid_land(r + 1, c):
                perimeter -= 1
            if is_valid_land(r, c - 1):
                perimeter -= 1
            if is_valid_land(r, c + 1):
                perimeter -= 1
            return perimeter

        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    perimeter += calculate_cell_perimeter(r, c)

        return perimeter
