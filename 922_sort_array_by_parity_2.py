# time: O(n)
# space: O(1)
from typing import List


class Solution:
    
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd, nums_length = 0, 1, len(nums) - 1
        while odd <= nums_length:
            if nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
                even += 2
        return nums