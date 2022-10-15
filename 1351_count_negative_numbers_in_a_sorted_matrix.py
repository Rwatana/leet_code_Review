from typing import List


class Solution:
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        yoko = len(grid[0])
        tate = len(grid)

        i = 0
        j = yoko -1 
        count = 0
        while i < tate and j >= 0:
            if grid[i][j] < 0:
                count = count + 1

                j -= 1
                
            else:
                 j = yoko -1
                 i += 1
        return count