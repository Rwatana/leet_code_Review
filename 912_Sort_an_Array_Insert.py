# time: O(nlogn)
# space: O(1)
from typing import List


class Solution(object):
    def binary_search(self, arr: List[int], low: int, hig: int, ele: int) -> int:
        if low == hig:
            if arr[low] > ele:
                return low
            else:
                return low + 1
        elif low > hig:
            return low

        middle = (low + hig) // 2
        if arr[middle] < ele:
            return self.binary_search(arr, middle + 1, hig, ele)
        elif arr[middle] > ele:
            return self.binary_search(arr, low, middle - 1, ele)
        else:
            return middle
    
    def insert_sort_bin(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            ele = arr[i]
            appropriate_index = self.binary_search(arr, 0, i - 1, ele)
            arr[:] = arr[:appropriate_index]
            + [ele] + arr[appropriate_index:i]
            + arr[i + 1:]
        return arr
