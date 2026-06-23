# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        search = head
        skip = head

        while n:
            search = search.next
            n -= 1

        if not search:
            return head.next

        while search.next:
            search = search.next
            skip = skip.next
        
        skip.next = skip.next.next
        return head
        