# time: O(logn)
# space: O(1)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        middle = 0
        left, right = 0, len(nums) - 1
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                return middle
            else:
                right = middle - 1
        return left
