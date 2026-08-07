# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        low, fast = head, head

        while fast and fast.next:
            low=low.next
            fast=fast.next.next
            if low==fast:
                return True

        return False