# V = node nums
# time: O(V)
# space: O(V)
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deepestLeavesSum(self, root) -> List[int]:
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        i = 0
        while queue:
            depth_sum = 0
            i += 1
            num = len(queue)
            for i in range(num):
                node = queue.popleft()
                depth_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth_sum
