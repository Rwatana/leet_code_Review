# Time: O(n)
# Space: O(n)
from typing import List
import heapq


class Solution:
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        cur = 0

        for passenger, start, end in trips:
            heapq.heappush(heap, (start, passenger))
            heapq.heappush(heap, (end, -passenger))
        while heap:
            if cur <= capacity:
                cur += heapq.heappop(heap)[1]
            else:
                return False
            
        return True
