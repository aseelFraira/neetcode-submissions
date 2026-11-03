# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #firs naive approch is to copy the list reverse it and pass on both of them and check one by one
        #second naive appraoch is turn the list vals into number and check if it is a poli
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        headB = slow
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        headB = prev
        print(headB.val)
        while head and headB:
            if head.val != headB.val:
                return False
            head = head.next
            headB = headB.next
        return True

            
        