# time complexity O(logn)
# space complexity O(n)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            middle = (left + right) // 2
            value = matrix[middle // col][middle % col]
            if value == target:
                return True
            elif value > target:
                right = middle - 1
            else:
                left = middle + 1
        return False
