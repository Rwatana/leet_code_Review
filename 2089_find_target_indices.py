# n = len(nums)
# Time complexity O(nlogn)
# Space complexity O(n)
from typing import List


class Solution:
    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        target_indices = []        
        while 1 < right - left:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        while right < len(nums) and nums[right] == target:
            target_indices.append(right)
            right += 1
            
        return target_indices
