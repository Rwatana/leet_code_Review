# T(logn)
# S(n)
from typing import List, Optional


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            queue = [root]
            res = []
            if root == None:
                return []
            while queue:
                cur = queue.pop(0)
                res.append(cur.val)
                if cur.left != None:
                    queue.insert(0, cur.left)
                if cur.right != None:
                    queue.insert(0, cur.right)
            
            return res[::-1]
