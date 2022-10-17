from typing import List


class Solution:
    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index_matrix = []
        for i, num in enumerate(nums):
            if num == target:
                index_matrix.append(i)                
        return index_matrix