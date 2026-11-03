# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #add dummy node in case the n is the first node
        dummy = ListNode(0)
        dummy.next = head
        curr = head

        while n:
            curr = curr.next
            n -= 1
        slow = dummy
        while curr:
            curr = curr.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

        
            
        