# n = len(arr)
# time: O(n**2)
# space: O(1)
from typing import List


class Solution:
    def bubble_sort(self, arr: List[int]) -> List[int]:
        arr_length = len(arr)
        for i in range(arr_length):
            for j in range(arr_length - 1, i, -1):
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return arr
