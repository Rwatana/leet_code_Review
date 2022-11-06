# time: O(1)
# space: O(1)
from typing import List


class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])
