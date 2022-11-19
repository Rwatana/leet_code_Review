# time: O(nlogn)
# space: O(n)
from collections import Counter


class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = Counter(s)
        for char in t:
            if not char in char_freq:
                return False
            
            else:
                char_freq[char] -= 1
                if char_freq[char] == 0:
                    del char_freq[char]
                    
        return True if not char_freq else False
