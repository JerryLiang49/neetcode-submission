"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDict = dict()
        old = head
        while old:
            nodeDict[old] = Node(old.val)
            old = old.next

        old = head
        while old:
            newNode = nodeDict[old]
            newNode.next = nodeDict.get(old.next)
            newNode.random = nodeDict.get(old.random)
            old = old.next
        
        return nodeDict.get(head)