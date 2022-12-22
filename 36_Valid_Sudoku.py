# Time: O(n**2)
# Space: O(n)
from typing import List
 
 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row = [set() for i in range(n)]
        column = [set() for i in range(n)]
        box = [set() for i in range(n)]
        
        for r in range(n):
            for c in range(n):
                if board[c][r] == '.':
                    continue
                
                if board[c][r] in row[r]:
                    return False
                
                row[r].add(board[c][r])
                if board[c][r] in column[c]:
                    return False
                
                column[c].add(board[c][r])
                idx = (r//3*3) + c//3
                
                if board[c][r] in box[idx]:
                    return False
                
                box[idx].add(board[c][r])
        return True
