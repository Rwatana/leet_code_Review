# Time: O(nlogn)
# Space: O(1)
from typing import List
from collections import heapq


class Solution:
     
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_list = []
        
        for point in points:
            element1, element2 = point
            sum = -(element1 ** 2 + element2 ** 2)
        if len(heap_list) < k:
            heapq.heappush(heap_list, (sum, element1, element2))
            
        elif heap_list[0][0] < sum:
            heapq.heapreplace(heap_list, (sum, element1, element2))
            
        return [[heap_element[1], heap_element[2]] for heap_element in heap_list]
