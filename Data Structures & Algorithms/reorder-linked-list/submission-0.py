# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # finding the middle
        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next=None

        # reversing the list
        while second:
            temp = second.next
            second.next = prev
            prev=second
            second = temp

        # Zippering in
        first, second= head , prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next=second
            second.next=temp1
            first, second = temp1, temp2

