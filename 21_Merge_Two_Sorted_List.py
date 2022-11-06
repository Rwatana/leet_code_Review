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
        new_Head = dummy_Head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummy_Head.next = list1
                list1 = list1.next
            else:
                dummy_Head.next = list2
                list2 = list2.next
            dummy_Head = dummy_Head.next
        
        if list1:
            dummy_Head.next = list1
        if list2:
            dummy_Head.next = list2
        return new_Head.next
