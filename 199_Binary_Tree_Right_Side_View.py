# T(logn)
# S(n)
from typing import List
import deque


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root:

            q = deque()
            q.append(root) 

            while (q):
                level_size = len(q)
                
                for i in range(level_size):
                    node = q.popleft()

                    if i + 1 == level_size:
                        res.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return res
