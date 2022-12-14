# T(n)
# S(n)
from typing import List
from typing import heapq


class Solution:
    
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        cur = 0

        for p, s, e in trips:
            heapq.heappush(heap, (s, p))
            heapq.heappush(heap, (e, -p))
        while heap:
            if cur <= capacity:
                cur += heapq.heappop(heap)[1]
            else:
                return False
            
        return True
