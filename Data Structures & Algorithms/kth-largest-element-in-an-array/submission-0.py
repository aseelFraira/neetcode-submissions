class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        helper = []
        heapq.heapify(helper)
        for num in nums:
            if len(helper) < k:
                heapq.heappush(helper,num)
            elif helper[0] < num:
                heapq.heapreplace(helper,num)

        return helper[0]



        