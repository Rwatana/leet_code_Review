# time: O(n)
# space: O(n)
from typing import List


class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from_num_to_supplement = {}
        
        for i, num in enumerate(nums):
            if target - num in from_num_to_supplement:
                return [from_num_to_supplement[target - num], i]
            
            from_num_to_supplement[num] = i
            
            return []
