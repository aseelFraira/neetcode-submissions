# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr_carry = 0
        head = dummy

        while l1 and l2:
            curr_sum = l1.val + l2.val + curr_carry
            curr_carry = int(curr_sum / 10)
            newNode = ListNode(curr_sum%10)
            dummy.next = newNode
            dummy = newNode
            l1 = l1.next
            l2 = l2.next

        while l1:
            curr_sum = (l1.val + curr_carry) 
            curr_carry = int(curr_sum / 10)
            newNode = ListNode(curr_sum%10)
            dummy.next = newNode
            dummy = newNode
            l1 = l1.next

        while l2:
            curr_sum = (l2.val + curr_carry) 
            curr_carry = int(curr_sum / 10)
            newNode = ListNode(curr_sum%10)
            dummy.next = newNode
            dummy = newNode
            l2 = l2.next
        if curr_carry:
            newNode = ListNode(curr_carry)
            dummy.next = newNode


        

        return head.next
        
            

        