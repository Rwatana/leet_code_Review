# T(3n)
# S(n)
from typing import heapq


class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        searched = set()
        searched.add(1)

        for _ in range(1, n):
            x = heapq.heappop(heap)
            for num in [2, 3, 5]:
                nx = x * num
                if nx in searched:
                    continue
                heapq.heappush(heap, nx)
                searched.add(nx)

        return heap[0]
