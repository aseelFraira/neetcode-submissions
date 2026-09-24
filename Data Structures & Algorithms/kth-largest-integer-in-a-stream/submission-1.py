class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = [-1 * num for num in nums]
        heapq.heapify(heap)
        self.heap = heap
        self.order = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, (-1 * val))
        stack = []
        for _ in range(self.order):
            stack.append(heapq.heappop(self.heap))
        res = stack[-1]

        while stack:
            heapq.heappush(self.heap,stack.pop())
        return res * -1







        
