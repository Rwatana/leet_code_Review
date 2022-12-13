# T(n)
# S(n)
from typing import List


class Solution:
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        pend = intervals[0][1]
        remove_count = 0
        
        for i in range(1, len(intervals)):
            if pend <= intervals[i][0]:
                pend = intervals[i][1]
            else:
                pend = min(pend, intervals[i][1])
                remove_count += 1
        return remove_count
