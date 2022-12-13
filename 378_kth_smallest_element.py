# n = matrix.length (= matrix[i].length)
# m = matrix[-1][-1] - (matrix[0][0] - 1)
# time: n*logn*logm
# space: O(1)
import bisect
from typing import List


class Solution:
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            raise ValueError("matrix should not be empty.")
        
        if k is None:
            raise ValueError("k should not be empty.")
        
        for row in matrix:
            if len(matrix) != len(row):
                raise ValueError("The number of rows and columns should be the same.")
            
        left = matrix[0][0] - 1
        right = matrix[-1][-1]
        while right - left > 1:
            mid = (left+right) // 2
            if sum(bisect.bisect(row, mid) for row in matrix) < k:
                left = mid
            else:
                right = mid
        return right
