# T(n)
# S(n)
from typing import List
from typing import heapq
from typing import heappop


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * num)
        return (heappop(heap)*-1-1) * (heappop(heap)*-1-1)