# time: O(logn)
# space: O(n)
class Node:
    
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    
    def connect(self, root: Node) -> Node:
        if root != None:
            narr = []
            if root.left != None:
                narr.append(root.left)
            if root.right != None:
                narr.append(root.right)

            while len(narr) != 0:
                for (i, e) in enumerate(narr):
                    if i != len(narr) - 1:
                        e.next = narr[i + 1]
                    else:
                        e.next = None
                temp = []
                for (i, e) in enumerate(narr):
                    if narr[i].left != None:
                        temp.append(narr[i].left)
                    if narr[i].right != None:
                        temp.append(narr[i].right)
                narr = temp
        return root
