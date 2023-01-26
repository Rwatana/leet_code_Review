# Time: O(nlogn)
# Space: O(1)
from typing import List, Optional


class TreeNode:
    
    def init(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create_node(start: int, end: int, nums: List[int]) -> Optional[TreeNode]:
            if start > end:
                return None

            mid = (start+end) // 2
            node = TreeNode(nums[mid])
            node.left = create_node(start, mid - 1, nums)
            node.right = create_node(mid + 1, end, nums)
            return node
        
        create_node(0, len(nums) - 1, nums)
