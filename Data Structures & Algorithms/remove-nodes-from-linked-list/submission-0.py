# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reverse the list

        new_head = self.reverseList(head)
        curr_head = new_head
        curr_max = curr_head.val
        prev = None


        while curr_head:
            if curr_max > curr_head.val:
                prev.next = curr_head.next
    
            else:
                curr_max = curr_head.val
                prev = curr_head
            curr_head = curr_head.next
        return self.reverseList(new_head)



        
        