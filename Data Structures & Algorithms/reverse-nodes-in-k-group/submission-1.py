# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dummyPrev = dummy

        while True:
            kth = self.kth(dummyPrev, k)
            if not kth:
                break
            nextGroup = kth.next
        
            prev = kth.next
            curr = dummyPrev.next
            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = dummyPrev.next
            dummyPrev.next = kth
            dummyPrev = tmp

        return dummy.next
    
    def kth(self, curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr