# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        if len(lists) == 0:
            return
        # This only adds the tuple to the list if the node is not None
        heap = [(node.val, i) for i, node in enumerate(lists) if node is not None]

        heapq.heapify(heap)

        while len(heap):
            min_tuple = heapq.heappop(heap)
            curr.next = lists[min_tuple[1]]
            lists[min_tuple[1]] = lists[min_tuple[1]].next
            if lists[min_tuple[1]] is not None:
                heapq.heappush(heap,(lists[min_tuple[1]].val,min_tuple[1]))
            
            curr = curr.next


        return dummy.next

        