# n = len(arr)
# time: O(n**2)
# space: O(1)
from typing import List


class Solution:
    
    def sortArray(self, arr: List[int]) -> List[int]:
        for ind, ele in enumerate(arr):
            min_ind = min(range(ind, len(arr)), key=lambda x: arr[x])
            arr[ind], arr[min_ind] = arr[min_ind], ele
        return arr
