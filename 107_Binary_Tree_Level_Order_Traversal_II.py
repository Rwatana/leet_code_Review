# Time: O(logn)
# Space: O(n)
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue_list = deque()
        queue_list.append(root)
        if not root:
            return res
        while (len(queue_list)):
            lev = []
            for i in range(len(queue_list)):
                ele = queue_list.popleft()
                if ele.left:
                    queue_list.append(ele.left)
                if ele.right:
                    queue_list.append(ele.right)
                lev.append(ele.val)
            res.append(lev)
        return res[::-1]
