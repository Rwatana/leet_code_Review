# Time: O(n)
# Space: O(n)
class Solution:
    
    def longestPalindrome(self, s: str) -> int:
        num = {}
        cnt = 0
        
        for char in s:
            num[char] = num.get(char, 0) + 1
            
        for key, val in num.items():
            if val % 2 == 1:
                cnt += 1
                
        if cnt == 0:
            return len(s)
        
        else:
            return len(s) - cnt + 1
