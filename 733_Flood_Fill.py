# BFS
# m, n = len(image), len(image[0])
# time: O(m * n)
# space: O(m * n) 
from collections import deque
from typing import List


class Solution:

    def floodFill(
        self,
        image: List[List[int]],
        start_row: int,
        start_colum: int,
        color: int
        ) -> List[List[int]]:
        """Function to perform a "flood fill" on the image starting from the
        pixel 'image[sr][sc]'.
        To perform a "flood fill", consider the starting pixel, plus any pixels
        connected 4-directionally to the starting pixel of the same color as the
        starting pixel. plus any pixels connected 4-directionally to those pixels
        (also with the same color), and so on. Replace the color of all of the
        aforementioned pixels with `color`.
        Args:
            image (List[List[int]]): m x n integer grid
            sr (int): Row index of starting pixel
            sc (int): Column index of starting pixel
            color (int): Replacement color

        Returns:
            List[List[int]]: 'image' after replaced with `color`
        """
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        queue = deque()
        queue.append((start_row, start_colum))
        visited = set()
        oldColor = image[start_row][start_colum]

        while queue:
            start_row, start_colum = queue.popleft()
            image[start_row][start_colum] = color
            for direction in directions:
                new_start_row, new_start_colum = start_row + direction[0], start_colum + direction[1]
                if (new_start_row >= 0) and (new_start_row < len(image))
                    and (newSc >= 0) and (newSc < len(image[0]))
                        and ((newSr, newSc) not in visited)
                            and (image[newSr][newSc] == oldColor):
                    queue.append((new_start_row, new_start_colum))
                    visited.add((new_start_row, new_start_colum))
        return image
