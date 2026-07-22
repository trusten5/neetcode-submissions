# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen={}

        watch = head

        while watch:
            if watch in seen:
                return True
            else:
                seen[watch]=1
            watch=watch.next
        
        return False
        


