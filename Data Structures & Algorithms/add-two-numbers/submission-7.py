# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        factor = 1
        num1 = 0
        while l1:
            num1 += factor * l1.val
            factor *= 10
            l1 = l1.next

        factor = 1
        num2 = 0
        while l2:
            num2 += factor * l2.val
            factor *= 10
            l2 = l2.next
        
        result = num1 + num2
        if result == 0:
            return ListNode(0)
        dummy = ListNode()
        curr = dummy
        while result > 0:
            node = ListNode(result%10)
            result //= 10
            curr.next = node
            curr = curr.next
        
        return dummy.next
