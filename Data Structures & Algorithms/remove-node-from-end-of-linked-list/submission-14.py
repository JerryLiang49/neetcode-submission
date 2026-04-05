# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        count = length - n
        if count == 0:
            return head.next
        
        dummy = head
        while dummy:
            count -= 1
            if count == 0:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return head
            
