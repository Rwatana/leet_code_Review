# time:(nlogn)
# space: (1)
from typing import List


class Solution:
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                middle = (left+right) // 2
                if numbers[middle] > new_target:
                    right = middle - 1
                elif numbers[middle] < new_target:
                    left = middle + 1
                else:
                    return [i + 1, middle + 1]
