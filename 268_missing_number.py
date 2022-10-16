from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        num= len(nums)
        lost = 0
        for i in range (0,num,1):
            if nums[i]  == nums[0]+i:
                continue
            else:
                lost = nums[0]+i
                return lost
        