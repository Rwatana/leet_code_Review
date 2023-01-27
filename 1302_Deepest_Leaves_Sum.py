# n = node widths
# time: O(n)
# space: O(n)

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None,
        ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        while queue:
            sum_of_current_level = 0
            width = len(queue)
            for _ in range(width):
                node = queue.popleft()
                sum_of_current_level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return sum_of_current_level
