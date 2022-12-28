# Time: O(nlogn)
# Space: O(1)
from typing import List, Optional


class TreeNode:
    
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create＿Node(start, end, nums) -> Optional[TreeNode]:
            if start > end:
                return None
            
            mid = (start+end) // 2
            node = TreeNode(nums[mid])
            node.left = create＿Node(start, mid - 1, nums)
            node.right = create＿Node(mid + 1, end, nums)
            return node
        
        create＿Node(0, len(nums) - 1, nums)
