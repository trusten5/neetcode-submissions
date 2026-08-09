# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while fast:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow.next

        while curr:
            temp=curr.next
            curr.next = prev
            prev=curr
            curr=temp

        first, second = head, prev
        count = 0
        while first and second:
            count=max(count, first.val+second.val)
            first=first.next
            second=second.next

        return count