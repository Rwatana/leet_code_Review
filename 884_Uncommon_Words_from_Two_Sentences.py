# Time: O(n)
# Space: O(n)
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(' ')
        s2 = s2.split(' ')
        h1 = {}
        h2 = {}
        for i in s1:
            h1[i] = h1.get(i, 0) + 1
        for i in s2:
            h2[i] = h2.get(i, 0) + 1
        ans = []
        for i in s1:
            if i not in h2 and h1[i] == 1:
                ans.append(i)
        for i in s2:
            if i not in h1 and h2[i] == 1:
                ans.append(i)
        return ans
