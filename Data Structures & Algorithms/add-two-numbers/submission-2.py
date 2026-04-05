# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, place = 0, 1
        while l1:
            num1 += l1.val * place
            place *= 10
            l1 = l1.next

        num2, place = 0, 1
        while l2:
            num2 += l2.val * place
            place *= 10
            l2 = l2.next

        total = num1 + num2
        if total == 0:
            return ListNode(0)

        dummy = ListNode()
        curr = dummy
        while total > 0:
            digit = total % 10
            curr.next = ListNode(digit)
            total //= 10
            curr = curr.next

        return dummy.next
