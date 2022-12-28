# Time: O(n)
# Space: O(n)
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_heap = []
        from_num_to_count = {}
        
        for num in nums:
            if num in from_num_to_count:
                from_num_to_count[num] += 1
            else:
                from_num_to_count[num] = 1
                
        for key, val in from_num_to_count.items():
            heapq.heappush(count_heap, (val, key))
            if len(count_heap) > k:
                heapq.heappop(count_heap)
                
        return [element[1] for element in count_heap]
