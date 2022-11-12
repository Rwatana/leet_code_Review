# time complexity O(logn)
# space complexity O(1)
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target or letters[0] > target:
            return letters[0]

        left, right = 0, len(letters) - 1
        while left <= right:
            middle = (right+left) // 2
            if letters[middle] > target:
                right = middle - 1
            elif letters[middle] <= target:
                left = middle + 1
        return letters[left]
