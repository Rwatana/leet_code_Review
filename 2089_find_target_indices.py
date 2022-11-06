# Time complexity O(nlogn)
# Space complexity O(n)
from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left, right = 0, len(nums) - 1
        answer_array = []
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] == target:
                if nums[left] < target:
                    left += 1
                elif nums[right] > target:
                    right -= 1
                if nums[left] == target and nums[right] == target:
                    answer_array.append(left)
                    left += 1
        return answer_array
