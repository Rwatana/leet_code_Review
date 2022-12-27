# Time: O(logn)
# Space: O(n)
from typing import List, Optional
from collections import deque


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        q = deque([root])
        result = []
        
        while q:
            level_size = len(q)
            current_level = []
            
            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(current_level)
        
        return result
