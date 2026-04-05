# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        head = l1
        l1sum = 0
        while head:
            l1sum += head.val * multiplier
            multiplier *= 10
            head = head.next
        
        multiplier = 1
        head = l2
        l2sum = 0
        while head:
            l2sum += head.val * multiplier
            multiplier *= 10
            head = head.next

        dummy = ListNode()
        curr = dummy
        currSum = l1sum + l2sum
        if currSum == 0:
            return ListNode(0)

        while currSum > 0:
            digit = currSum % 10
            currSum //= 10
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next
