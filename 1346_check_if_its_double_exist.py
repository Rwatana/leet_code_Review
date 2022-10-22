from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        s = set(arr)        
        SS = s - {0}
        if arr.count(0) > 1:
            return True

        for i in s:
            if 2 * i in SS:
                return True

        return False
