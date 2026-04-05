# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lengthNode = head
        length = 0
        while lengthNode:
            lengthNode = lengthNode.next
            length += 1

        index = length - n
        if index == 0:
            return head.next
        
        count = 1
        remove = head
        while remove:
            if count == index:
                remove.next = remove.next.next
                break
            count +=1
            remove = remove.next
        return head
