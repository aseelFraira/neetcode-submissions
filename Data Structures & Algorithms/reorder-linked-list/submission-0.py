# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the tail half of list

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        slow = temp
        #flip the tail

        prev = None

        while slow:
            next_to_handle = slow.next
            slow.next = prev
            prev = slow
            slow = next_to_handle
        
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1

            curr1 = temp1
            curr2 = temp2

        

        