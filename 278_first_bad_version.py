from typing import List


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        up , down = 1, n
        middle = 0
        while up < down:
            middle = (up+down)//2
            if  isBadVersion(middle) == True:
                down = middle
            else:
                up = middle+1                
        return up