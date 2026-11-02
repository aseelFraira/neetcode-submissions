# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListAux(head,None)

    def reverseListAux(self,head,prev):
        if head is None:
            return prev
        temp = head.next
        head.next = prev
        print(head.val)

        return self.reverseListAux(temp,head)


        

        