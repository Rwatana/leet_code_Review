# T(logn)
# S(n)
from typing import List
from typing import TreeNode


class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createNode(self, s, e, nums):
            if s > e:
                return None
            
            mid = (s+e) // 2
            self.node = TreeNode(nums[mid])
            self.node.left = createNode(s, mid - 1, nums)
            self.node.right = createNode(mid + 1, e, nums)
            return node
        
        createNode(0, len(nums) - 1, nums)
