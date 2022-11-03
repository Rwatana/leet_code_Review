# Time complexity O(n)
# Space complexity O(1)
from typing import List


class Solution:
    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return right

        leftvalue = binarySearchLeft(nums, target)
        rightvalue = binarySearchRight(nums, target)
        if leftvalue < rightvalue:
            return [i for i in range(leftvalue, rightvalue + 1)]

        if leftvalue == rightvalue:
            return [leftvalue]
        
        return []
