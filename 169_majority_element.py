from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums.sort()
        length = len(nums)//2
        if length == 0:
            return nums[0]
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+length]:
                return nums[i]
