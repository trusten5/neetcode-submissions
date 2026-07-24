# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = {}
        
        while curr:
            if curr in seen:
                return True
            else:
                seen[curr]=1
            curr = curr.next

        return False