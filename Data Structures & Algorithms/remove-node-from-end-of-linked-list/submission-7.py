# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sl, fa = dummy, head

        while n>0:
            fa=fa.next
            n-=1

        while fa:
            fa=fa.next
            sl=sl.next

        sl.next=sl.next.next

        return dummy.next