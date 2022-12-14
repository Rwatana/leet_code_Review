# T(n)
# S(n)

from typing import List
from typing import heappush
from typing import heapreplace


class Solution:
     
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for c in points:
            x, y = c
            d = -(x ** 2 + y ** 2)
        if len(h) < k:
            heappush(h, (d, x, y))
        elif h[0][0] < d:
            heapreplace(h, (d, x, y))
        return [[p[1], p[2]] for p in h]
