# time: O(n)
# space: O(1)
import Optional
import collections


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dictionary = collections.defaultdict(ListNode)
        while head:
            if head in dictionary:
                return head
            dictionary[head] = True
            head = head.next
        return None
