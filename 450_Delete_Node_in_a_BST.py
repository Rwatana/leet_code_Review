# Time: O(logn)
# Space: O(1)
from collections import Optional
from collections import TreeNode


class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.right and root.left:
                return root.left
            
            if not root.left and root.right:
                return root.right
            
            if not root.left and not root.right:
                return None
            
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            
        else:
            root.left = self.deleteNode(root.left, key)
            
        return root
    
