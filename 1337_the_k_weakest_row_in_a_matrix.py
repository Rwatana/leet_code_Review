# T(n)
# S(n)
from typing import List
from typing import heapq


class Solution:
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_sum = []
        for idx, row in enumerate(mat):
            heapq.heappush(row_sum, (sum(row), idx))
        return [min[1] for min in heapq.nsmallest(k, row_sum)]
