# T(logn)
# S(1)
from typing import TreeNode


class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def Difference(node, low, high):
            if not node:
                return high - low
            else:
                left = Difference(node.left, low, node.val)
                right = Difference(node.right, node.val, high)
                return min(left, right)
        return Difference(root, float('-inf'), float('inf'))
