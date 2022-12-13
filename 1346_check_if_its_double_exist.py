# hash map
# n = len(arr)
# time: O(n)
# space: O(n)
from typing import List


class Solution:
    
    def checkIfExist(self, arr: List[int]) -> bool:
        nums_in_arr = set()
        for num in arr:
            if num * 2 in nums_in_arr or num / 2 in nums_in_arr:
                return True
            
            nums_in_arr.add(num)
        return False
