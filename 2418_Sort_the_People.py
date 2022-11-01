# O(n) T(n)
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        
        heights_sorted = sorted(heights, reverse=True)
        for height in heights_sorted:
            index = heights.index(height)
            result.append(names[index])
        return result
