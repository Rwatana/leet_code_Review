# T(n)
# S(n)
from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pool = []
        for num in nums1:
            if num in nums2 and num not in pool:
                pool.append(num)
                
        return pool
