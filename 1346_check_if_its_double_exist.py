# time cpmplexity O(n)
# space complexityO(1)
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        set_list = set(arr)
        new_list = set_list - {0}
        if arr.count(0) > 1:
            return True

        for i in set_list:
            if 2 * i in new_list:
                return True

        return False
