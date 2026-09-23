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
        if not head:
            return None
        curr = head

        while curr:
            next_to_handle = curr.next
            new_node = Node(curr.val)
            curr.next = new_node
            new_node.next = next_to_handle

            curr = curr.next.next
        
        curr = head

        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        curr = head
        new_list = head.next 

        while curr:
            listA = curr.next.next
            listB = curr.next

            listB.next = listA.next if listA else None
            curr.next = listA

            curr = listA
        return new_list
            

        
