# n = len(arr)
# time: O(n**2)
# space: O(1)
from typing import List


class Solution:
    
    def select_sort(self, arr: List[int]) -> List[int]:
        for each_index, each_element in enumerate(arr):
            min_ind = min(range(each_index, len(arr)), key=lambda x: arr[x])
            arr[each_index], arr[min_ind] = arr[min_ind], each_element
        return arr
