# Time: O(n)
# Space: O(n)
# n = len(code)
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        direction = 1
        if k > 0:
            direction *= 1
            extended_code = code[:k]
            shifted_code = code + extended_code
        else:
            direction *= -1
            extended_code = code[k:]
            k *= -1
            shifted_code = extended_code + code

        result = []
        sliding_window = []
        
        for i in range(k):
            sliding_window.append(shifted_code[i])
        
        result.append(sum(sliding_window))
        
        if not sliding_window:
            return [0] * len(code)
        
        for i in range(k, len(shifted_code)):
            sliding_window.pop(0)
            sliding_window.append(shifted_code[i])
            if len(sliding_window) == k:
                result.append(sum(sliding_window))
        
        if direction == 1:
            return result[1:]
        return result[:-1]
