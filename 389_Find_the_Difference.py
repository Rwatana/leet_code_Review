# Time: O(n)
# Space: O(1)
class Solution:
    
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(min(len(s), len(t))):
            if s[i] in t:
                t = t.replace(s[i], '', 1)
        return t[0]
