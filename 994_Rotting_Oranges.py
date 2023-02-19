# m = len(grid)
# n = len(grid[0])
# time: O(m x n)
# space: O(m x n)
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        fresh_orange_num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))

                elif grid[i][j] == 1:
                    fresh_orange_num += 1
        
        res = 0
        while queue and fresh_orange_num > 0:
            res += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for i_adj, j_adj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if (0 <= i_adj < len(grid) and 0 <= j_adj < len(grid[0])
                            and grid[i_adj][j_adj] == 1):
                        grid[i_adj][j_adj] = 2
                        fresh_orange_num -= 1
                        queue.append((i_adj, j_adj))

        if fresh_orange_num == 0:
            return res
        
        else:
            return -1
