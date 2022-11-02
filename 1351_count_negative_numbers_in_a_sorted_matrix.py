# T(n) O(1)
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_set = set(arr)
        num_set_number = num_set - {0}
        if arr.count(0) > 1:
            return True

        for i in num_set:
            if 2 * i in num_set_number:
                return True

        return False
