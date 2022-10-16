from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      
        left , right = 0, len(nums)-1
        
        while left <= right:
            middle = (left+right) //2
            m_mid = nums[middle]
            if middle  > 0:
                l_left = nums[middle-1]
            else:
                l_left = float('-inf')
            if middle < len(nums) -1:
                r_right = nums[middle+1]
            else:
                r_right = float('-inf')

            if l_left <  m_mid > r_right:
                return middle
            elif r_right > m_mid >l_left:
                left = middle+1
            else:
                right = middle-1
        return 0
