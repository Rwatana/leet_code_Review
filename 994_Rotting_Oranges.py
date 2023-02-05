# Time: O(n**2)
# Space: O(1)


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        visited = set()
        rotted_group = []
        ans = -1

        for row_num in range(row):
            for col_num in range(col):
                if grid[row_num][col_num] == 2:
                    rotted_group.append((row_num, col_num))

        while rotted_group:
            for x in range(len(rotted_group)):
                row_num, col_num = rotted_group.pop(0)
                if (row_num, col_num) in visited:
                    continue
                visited.add((row_num, col_num))

                if row_num + 1 < row and grid[row_num+1][col_num] == 1:
                    grid[row_num+1][col_num] = 2
                    rotted_group.append((row_num + 1, col_num))
                if row_num - 1 >= 0 and grid[row_num - 1][col_num] == 1:
                    grid[row_num-1][col_num] = 2
                    rotted_group.append((row_num-1, col_num))
                if col_num + 1 < col and grid[row_num][col_num + 1] == 1:
                    grid[row_num][col_num+1] = 2
                    rotted_group.append((row_num, col_num + 1))
                if col_num - 1 >= 0 and grid[row_num][col_num - 1] == 1:
                    grid[row_num][col_num - 1] = 2
                    rotted_group.append((row_num, col_num - 1))
            ans += 1
        for row_num in range(row):
            for col_num in range(col):
                if grid[row_num][col_num] == 1:
                    return -1

        if ans == -1:
            return 0
        return ans
