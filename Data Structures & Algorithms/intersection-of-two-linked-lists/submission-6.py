# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        curr_A = headA
        curr_B = headB

        while curr_A is not curr_B:
            curr_A = curr_A.next
            curr_B = curr_B.next
            if curr_A is None and curr_B is not None:
                curr_A = headB
            if curr_B is None and curr_A is not None:
                curr_B = headA

        
        return curr_A
        