from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if target == num:
                return True
        return False
