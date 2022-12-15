# Time: O(n)
# Space: O(n)
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_list = []
        exist_dict = {}
        
        for num in nums:
            if num in exist_dict:
                exist_dict[num] += 1
            else:
                exist_dict[num] = 1
                
        for key, val in exist_dict.items():
            heapq.heappush(heap_list, (val, key))
            if len(heap_list) > k:
                heapq.heappop(heap_list)
                
        return [element[1] for element in heap_list]
