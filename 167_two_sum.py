from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        indices = []
        i = 0
        while i < 1:
            sum = numbers[left] + numbers[right]
            if sum == target:
                indices.append(left + 1)
                indices.append(right + 1)
                return indices
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return 0
