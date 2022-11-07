# time: O(n)
# space: O(n)
from typing import ListNode
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = dummy_head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummy_head.next = list1
                list1 = list1.next
            else:
                dummy_head.next = list2
                list2 = list2.next
            dummy_head = dummy_head.next
        
        if list1:
            dummy_head.next = list1
        if list2:
            dummy_head.next = list2
        return new_head.next
