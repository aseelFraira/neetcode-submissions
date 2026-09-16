class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] -= 1
        
        h = [(freq,number) for number,freq in freqs.items()]
        heapq.heapify(h)
        res = []

        for _ in range(k):
            frequency, num = heapq.heappop(h)
            res.append(num)

        return res

        

      
        


        