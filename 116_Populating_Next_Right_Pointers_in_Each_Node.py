# Time: O(logn)
# Space: O(n)
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        root.next = None
        q = deque([root])
        
        while len(q) != 0:
            u = q.popleft()
            if u.left != None:
                q.append(u.left)
                u.left.next = u.right

                q.append(u.right)
                if u.next != None:
                    u.right.next = u.next.left
                else:
                    u.right.next = None

        return root
