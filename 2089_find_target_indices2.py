from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        l ,m = 0, 0      
        for num in nums:
            if num < target:
                l += 1
            elif target == num:
                m += 1
        return list(range(l,m+l))