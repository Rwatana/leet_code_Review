# Time: O(n)
# Space: O(1)
# n = len(nums)
from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        sum_tmp = 0
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] < nums[i]:
                sum_tmp += nums[i]
            else:
                sum_tmp = nums[i]
            max_sum = max(max_sum, sum_tmp)
        return max_sum
