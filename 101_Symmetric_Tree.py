# Time: O(logn)
# Space: O(1)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root, root)

    def isSame(self, left_t, right_t):
        if not left_t and not right_t:
            return True
        elif not left_t or not right_t:
            return False

        return left_t.val == right_t.val and self.isSame(left_t.left, right_t.right) and self.isSame(left_t.right, right_t.left)
