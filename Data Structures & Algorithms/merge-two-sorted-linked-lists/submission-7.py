# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        dummy = ListNode()
        ret = dummy

        while n1 and n2:
            if n1.val < n2.val:
                dummy.next = n1
                n1 = n1.next
            else:
                dummy.next = n2
                n2 = n2.next
            dummy = dummy.next
            
        if n1:
            dummy.next = n1
        elif n2:
            dummy.next = n2
        
        return ret.next