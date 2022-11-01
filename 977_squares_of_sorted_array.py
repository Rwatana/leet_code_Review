from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s_nums = []
        for i in range(len(nums)):
            s_nums.append(nums[i] * nums[i])
        s_nums.sort()
        return s_nums
