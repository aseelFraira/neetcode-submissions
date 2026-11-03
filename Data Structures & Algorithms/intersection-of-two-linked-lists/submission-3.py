# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_A = 0
        length_B = 0

        curr_A = headA
        curr_B = headB

        while curr_A:
            curr_A = curr_A.next
            length_A += 1
        
        while curr_B:
            curr_B = curr_B.next
            length_B += 1
        
        while length_A > length_B:
            headA = headA.next
            length_A -= 1
        while length_B > length_A:
            headB = headB.next
            length_B -= 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
        