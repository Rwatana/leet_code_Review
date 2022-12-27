# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
    
        def backtrack(cur):
            if (cur > n):
                return
            ans.append(cur)
            backtrack(cur * 10)
            if cur % 10 != 9:
                backtrack(cur + 1)
                
        backtrack(1)
        return ans
