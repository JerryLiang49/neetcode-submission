# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        removeIndex = length - n
        if removeIndex == 0:
            return head.next
        
        curr = head
        for i in range(length - 1):
            if i + 1 == removeIndex:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
