# Time: O(logn)
# Space: O(n)
from typing import List


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createNode(start, end, nums):
            if start > end:
                return None
            
            mid = (start+end) // 2
            node = TreeNode(nums[mid])
            node.left = createNode(start, mid - 1, nums)
            node.right = createNode(mid + 1, end, nums)
            return node
        
        createNode(0, len(nums) - 1, nums)
