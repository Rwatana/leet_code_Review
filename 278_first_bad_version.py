# time cpmplexity O(n)
# space complexityO(1)
from typing import List
from typing import isBadversion
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        up, down = 1, n
        while up < down:
            middle = (up + down) // 2
            if isBadVersion(middle):
                down = middle
            else:
                up = middle + 1
        return up
