# Time: O(n)
# Space: O(n)
from collections import deque
from typing import List


class Solution(object):

    def floodFill(self, image, sr, sc, color) -> List[List[int]]:
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        queue = deque()
        queue.append((sr, sc))
        visited = set()
        oldColor = image[sr][sc]

        while queue:
            sr, sc = queue.popleft()
            image[sr][sc] = color
            for direction in directions:
                newSr, newSc = sr + direction[0], sc + direction[1]
                if (newSr >= 0) and (newSr < len(image)) and (newSc >= 0) and (newSc < len(image[0])) and ((newSr, newSc) not in visited) and (image[newSr][newSc] == oldColor):
                    queue.append((newSr, newSc))
                    visited.add((newSr, newSc))

        return image
