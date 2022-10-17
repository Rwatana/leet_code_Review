from typing import List


class Solution:

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index = []
        for i, num in enumerate(nums):
            if num == target:
                index.append(i)                
        return index