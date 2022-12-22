# Time: O(n)
# Space: O(n)
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = collections.defaultdict(list)
        
        for i in range(len(strs)):
            anagram[''.join(sorted(strs[i]))].append(strs[i])
            
        return list(anagram.values())
