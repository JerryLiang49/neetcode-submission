# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half
        reverse = slow.next
        prev = None
        while reverse:
            temp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = temp
        
        slow.next = None
        left = head
        right = prev
        while right:
            temp1 = left.next
            temp2 = right.next
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2
        
