# Time: O(n**2)
# Space: O(1)
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = {
            'a': ".-", 
            'b': "-...",
            'c': "-.-.",
            'd': "-..",
            'e': ".",
            'f': "..-.",
            'g': "--.",
            'h': "....",
            'i': "..",
            'j': ".---",
            'k': "-.-",
            'l': ".-..",
            'm': "--",
            'n': "-.",
            'o': "---",
            'p': ".--.",
            'q': "--.-",
            'r': ".-.",
            's': "...",
            't': "-",
            'u': "..-",
            'v': "...-",
            'w': ".--",
            'x': "-..-",
            'y': "-.--",
            'z': "--..",
        }

        count = set()
        for word in words:
            s = ""
            for char in word:
                s += chars[char]
            count.add(s)

        return len(count)
