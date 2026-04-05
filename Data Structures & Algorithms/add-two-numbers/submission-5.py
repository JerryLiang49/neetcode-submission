# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        curr = l1
        multiply = 1
        while curr:
            num1 += multiply * curr.val
            multiply *= 10
            curr = curr.next
            
        curr = l2
        multiply = 1
        while curr:
            num2 += multiply * curr.val
            multiply *= 10
            curr = curr.next
        
        result = num1+num2
        if result == 0:
            return ListNode(0)
            
        dummy = ListNode()
        curr = dummy
        while result > 0:
            digit = result % 10
            curr.next = ListNode(digit)
            result //= 10
            curr = curr.next
        
        return dummy.next