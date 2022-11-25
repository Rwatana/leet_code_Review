# time complexity O(logn)
# space complexity O(1)
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or target is None:
            return False
        
        row_num = len(matrix)
        col_num = len(matrix[0])
        
        left, right = 0, row_num * col_num - 1
        
        while left <= right:
            middle = (left + right) // 2
            value = matrix[middle // col_num][middle % col_num]
            
            if value == target:
                return True
            
            elif value > target:
                right = middle - 1
                
            else:
                left = middle + 1
                
        return False
