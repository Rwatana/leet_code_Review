# Time: O(n**2)
# Space: O(n)
from typing import List


class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return dic[digits]
        if len(digits) > 1:
            for i in dic[digits[-1]]:
                for j in self.letterCombinations(digits[:-1]):
                    res.append(j + i)
                    
        return res
