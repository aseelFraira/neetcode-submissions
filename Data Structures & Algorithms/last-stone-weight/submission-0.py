class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * w for w in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap,min(stone1,stone2) - max(stone1,stone2))
        
        return -1 * heap[0] if len(heap) else 0

        