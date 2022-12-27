# time: (n)
# space: (n)
from typing import List
import deque


class Solution:
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue_list = deque()
        if root:
            queue_list.append(root)
        lst = []
        even_lvl = False
        
        while queue_list:
            level_lst = []
            for i in range(len(queue_list)):
                curr = queue_list.popleft()
                level_lst.append(curr.val)
                
                if curr.left:
                    queue_list.append(curr.left)
                    
                if curr.right:
                    queue_list.append(curr.right)
                    
            if even_lvl:
                lst.append(level_lst[::-1])
                
            else:
                lst.append(level_lst)
            even_lvl = not even_lvl
            
        return lst
