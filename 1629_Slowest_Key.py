# Time: O(n)
# Space: O(1)
# n = len(releaseTimes)
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxTime = releaseTimes[0]
        maxKey = keysPressed[0]

        for i in range(1, len(releaseTimes)):
            diffTime = releaseTimes[i] - releaseTimes[i - 1]
            if diffTime > maxTime or (diffTime == maxTime and keysPressed[i] > maxKey):
                maxTime = diffTime
                maxKey = keysPressed[i]
        return maxKey
