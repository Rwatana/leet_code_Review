class Solution:
    def convert(self, s: str, numrows: int) -> str:
        if numrows == 1:
            return s
        return_list = [''] * numrows  
        depth = 0
        vector = 1
        for string in s:
            return_list[depth] += string  
            if depth == 0:
                vector = 1
            elif depth == numrows - 1:
                vector = -1
            depth += vector
        return ''.join(return_list)
