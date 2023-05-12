# n = len(arr)
# time: O(nlogn)
# space: O(1)
from typing import List


class Solution:
    
    def binary_search(self,
                      arr: List[int],
                      low: int,
                      high: int,
                      insert_element: int) -> int:
        if low == high:
            if arr[low] > insert_element:
                return low
            
            else:
                return low + 1
            
        elif low > high:
            return low

        middle = (low + high) // 2
        if arr[middle] < insert_element:
            return self.binary_search(arr, middle + 1, high, insert_element)
        
        elif arr[middle] > insert_element:
            return self.binary_search(arr, low, middle - 1, insert_element)
        
        else:
            return middle
    
    def insert_sort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            insert_element = arr[i]
            appropriate_index = self.binary_search(arr,
                                                   0,
                                                   i - 1,
                                                   insert_element)
            arr[:] = arr[:appropriate_index]
            + [insert_element] + arr[appropriate_index:i]
            + arr[i + 1:]
        return arr
