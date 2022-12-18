# TIme: O()
# Space: O()
from typing import List


class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        concecutive = {}
        res = 0
        for k in nums:
            if k in concecutive:
                continue
            concecutive[k] = [k, k]
            
            if k - 1 in concecutive:
                lst = concecutive[k - 1]
                lst[1] = concecutive[k][1]
                concecutive[k] = concecutive[lst[1]] = lst
                
            if k + 1 in concecutive:
                lst = concecutive[k + 1]
                lst[0] = concecutive[k][0]
                concecutive[k] = concecutive[lst[0]] = lst
                
            left, right = concecutive[k]
            res = max(res, right - left + 1)
        return res
