# time: O(n)
# space: O(n)
from typing import List


class Solution:
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        double_list = []
        left = 0
        right = len(nums) - 1
        while left < right:
            left_double = (nums[left])**2
            right_double = (nums[right])**2
            if left_double > right_double:
                double_list.append(left_double)
                left += 1
            else:
                double_list.append(right_double)
                right -= 1
        double_list.append((nums[left])**2)
        return double_list[::-1]
