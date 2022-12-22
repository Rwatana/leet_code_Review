# TIme: O(n)
# Space: O(n)
from typing import List


class Solution:
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq, result = [0] * (len(nums)+1), []
        for num in nums:
            if freq[num] == 1:
                result.append(num)
            else:
                freq[num] = 1
        return result
